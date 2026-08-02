#!/usr/bin/env python3
"""Static prose QA harness for 《팔대신병록》.

This tool does not judge literary quality. It finds measurable risk signals:
short-sentence chains, repetitive phrasing, banned legacy canon, naming density,
paragraph rhythm, and continuity ledger mismatches.

Usage:
  python tools/prose_harness.py manuscripts/EP001.md
  python tools/prose_harness.py manuscripts --recursive --report reports/prose-qa.md
  python tools/prose_harness.py manuscripts/EP001.md --strict-canon
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence

SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?。！？]|[다요죠네까])(?:[\"'’”)]*)\s+")
WORD_RE = re.compile(r"[가-힣A-Za-z0-9]+")
DIALOGUE_RE = re.compile(r"^[\s>]*[\"“‘']")
HEADING_RE = re.compile(r"^#{1,6}\s")


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    line: int
    message: str
    excerpt: str = ""


@dataclass
class FileReport:
    path: Path
    findings: list[Finding] = field(default_factory=list)
    sentence_lengths: list[int] = field(default_factory=list)
    paragraph_sentence_counts: list[int] = field(default_factory=list)
    metrics: dict[str, float | int] = field(default_factory=dict)

    @property
    def blockers(self) -> int:
        return sum(1 for item in self.findings if item.severity == "P0")

    @property
    def warnings(self) -> int:
        return sum(1 for item in self.findings if item.severity in {"P1", "P2"})


class HarnessConfig:
    def __init__(self, raw: dict) -> None:
        self.short_sentence_words = int(raw.get("short_sentence_words", 7))
        self.short_chain_limit = int(raw.get("short_chain_limit", 4))
        self.one_sentence_paragraph_ratio_warn = float(
            raw.get("one_sentence_paragraph_ratio_warn", 0.55)
        )
        self.new_name_limit = int(raw.get("new_name_limit", 3))
        self.repeated_opening_limit = int(raw.get("repeated_opening_limit", 3))
        self.repeated_phrase_limit = int(raw.get("repeated_phrase_limit", 3))
        self.legacy_terms = list(raw.get("legacy_terms", []))
        self.watch_terms = dict(raw.get("watch_terms", {}))
        self.canon_names = list(raw.get("canon_names", []))
        self.known_terms = set(raw.get("known_terms", [])) | set(self.canon_names)
        self.landscape_terms = list(raw.get("landscape_terms", []))
        self.combat_terms = list(raw.get("combat_terms", []))
        self.continuity = dict(raw.get("continuity", {}))
        self.naming_exemptions = set(raw.get("naming_exemptions", []))

    @classmethod
    def load(cls, path: Path) -> "HarnessConfig":
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError as exc:
            raise SystemExit(f"설정 파일을 찾을 수 없습니다: {path}") from exc
        except json.JSONDecodeError as exc:
            raise SystemExit(f"설정 JSON 오류: {path}: {exc}") from exc
        return cls(raw)


def iter_input_files(paths: Sequence[Path], recursive: bool) -> Iterable[Path]:
    allowed = {".md", ".txt"}
    seen: set[Path] = set()
    for input_path in paths:
        if input_path.is_file() and input_path.suffix.lower() in allowed:
            resolved = input_path.resolve()
            if resolved not in seen:
                seen.add(resolved)
                yield input_path
            continue
        if input_path.is_dir():
            pattern = "**/*" if recursive else "*"
            for child in sorted(input_path.glob(pattern)):
                if child.is_file() and child.suffix.lower() in allowed:
                    resolved = child.resolve()
                    if resolved not in seen:
                        seen.add(resolved)
                        yield child


def strip_markdown_noise(line: str) -> str:
    line = re.sub(r"`[^`]+`", "", line)
    line = re.sub(r"!\[[^]]*]\([^)]*\)", "", line)
    line = re.sub(r"\[[^]]+]\([^)]*\)", "", line)
    return line.strip()


def split_sentences(text: str) -> list[str]:
    normalized = re.sub(r"\s+", " ", text.strip())
    if not normalized:
        return []
    chunks = SENTENCE_SPLIT_RE.split(normalized)
    return [chunk.strip() for chunk in chunks if chunk.strip()]


def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))


def sentence_opening(sentence: str, width: int = 2) -> str:
    words = WORD_RE.findall(sentence)
    return " ".join(words[:width])


def ngrams(words: Sequence[str], size: int) -> Iterable[str]:
    for index in range(len(words) - size + 1):
        yield " ".join(words[index : index + size])


def line_number_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def add_term_findings(
    report: FileReport,
    text: str,
    terms: Sequence[str],
    severity: str,
    code: str,
    message_prefix: str,
) -> None:
    for term in terms:
        for match in re.finditer(re.escape(term), text):
            line = line_number_for_offset(text, match.start())
            report.findings.append(
                Finding(severity, code, line, f"{message_prefix}: {term}", term)
            )


def detect_short_sentence_chains(
    report: FileReport, indexed_sentences: list[tuple[int, str]], config: HarnessConfig
) -> None:
    chain: list[tuple[int, str]] = []
    for line, sentence in indexed_sentences:
        length = word_count(sentence)
        report.sentence_lengths.append(length)
        if 0 < length <= config.short_sentence_words:
            chain.append((line, sentence))
            continue
        if len(chain) >= config.short_chain_limit:
            excerpt = " / ".join(sentence for _, sentence in chain[:4])
            report.findings.append(
                Finding(
                    "P2",
                    "RHYTHM_SHORT_CHAIN",
                    chain[0][0],
                    f"짧은 문장 {len(chain)}개가 연속됩니다. 충격·결정 장면이 아니라면 중문으로 연결하세요.",
                    excerpt,
                )
            )
        chain = []
    if len(chain) >= config.short_chain_limit:
        report.findings.append(
            Finding(
                "P2",
                "RHYTHM_SHORT_CHAIN",
                chain[0][0],
                f"짧은 문장 {len(chain)}개가 연속됩니다.",
                " / ".join(sentence for _, sentence in chain[:4]),
            )
        )


def detect_paragraph_rhythm(report: FileReport, paragraphs: list[tuple[int, str]], config: HarnessConfig) -> None:
    prose_paragraphs = 0
    one_sentence = 0
    for line, paragraph in paragraphs:
        sentences = split_sentences(paragraph)
        if not sentences:
            continue
        prose_paragraphs += 1
        report.paragraph_sentence_counts.append(len(sentences))
        if len(sentences) == 1:
            one_sentence += 1
        if word_count(paragraph) >= 100:
            report.findings.append(
                Finding(
                    "P2",
                    "RHYTHM_LONG_PARAGRAPH",
                    line,
                    "모바일 가독성을 해칠 수 있는 긴 문단입니다. 이미지·행동·판단 단위로 나눌지 검토하세요.",
                    paragraph[:120],
                )
            )
    ratio = one_sentence / prose_paragraphs if prose_paragraphs else 0.0
    report.metrics["one_sentence_paragraph_ratio"] = round(ratio, 3)
    if prose_paragraphs >= 6 and ratio > config.one_sentence_paragraph_ratio_warn:
        report.findings.append(
            Finding(
                "P2",
                "RHYTHM_ONE_SENTENCE_PARAGRAPHS",
                1,
                f"한 문장 문단 비율이 {ratio:.0%}입니다. 단문 모바일 호흡이 기계적으로 반복되는지 확인하세요.",
            )
        )


def detect_repeated_openings(report: FileReport, indexed_sentences: list[tuple[int, str]], config: HarnessConfig) -> None:
    openings: list[tuple[int, str]] = []
    for line, sentence in indexed_sentences:
        opening = sentence_opening(sentence)
        if opening:
            openings.append((line, opening))
    for index in range(len(openings) - config.repeated_opening_limit + 1):
        window = openings[index : index + config.repeated_opening_limit]
        values = [value for _, value in window]
        if len(set(values)) == 1:
            report.findings.append(
                Finding(
                    "P2",
                    "STYLE_REPEATED_OPENING",
                    window[0][0],
                    f"문장 첫머리 '{values[0]}'가 {len(window)}회 연속됩니다.",
                )
            )


def detect_repeated_phrases(report: FileReport, text: str, config: HarnessConfig) -> None:
    words = WORD_RE.findall(text)
    counts = Counter(ngrams(words, 3))
    ignored = {phrase for phrase in counts if len(phrase) < 5}
    candidates = [
        (phrase, count)
        for phrase, count in counts.items()
        if count >= config.repeated_phrase_limit and phrase not in ignored
    ]
    for phrase, count in sorted(candidates, key=lambda item: (-item[1], item[0]))[:15]:
        first = text.find(phrase)
        report.findings.append(
            Finding(
                "P2",
                "STYLE_REPEATED_PHRASE",
                line_number_for_offset(text, max(first, 0)),
                f"동일한 3어절 표현이 {count}회 반복됩니다: {phrase}",
                phrase,
            )
        )


def detect_watch_terms(report: FileReport, text: str, config: HarnessConfig) -> None:
    for term, limit in config.watch_terms.items():
        count = text.count(term)
        if count > int(limit):
            first = text.find(term)
            report.findings.append(
                Finding(
                    "P2",
                    "STYLE_WATCH_TERM",
                    line_number_for_offset(text, max(first, 0)),
                    f"주의 표현 '{term}'이 {count}회 사용됐습니다. 권장 상한은 {limit}회입니다.",
                    term,
                )
            )


def detect_name_density(report: FileReport, text: str, config: HarnessConfig) -> None:
    # Conservative heuristic: Korean 2-4 syllable tokens beginning with an uppercase-like
    # narrative role cannot be recognized reliably. We therefore count configured canon and
    # known terms, then separately flag unknown terms wrapped in backticks or bold markers.
    used = [name for name in config.canon_names if name in text]
    report.metrics["configured_name_count"] = len(set(used))
    marked = set(re.findall(r"(?:\*\*|`)([가-힣]{2,8})(?:\*\*|`)", text))
    unknown = sorted(marked - config.known_terms - config.naming_exemptions)
    if len(unknown) > config.new_name_limit:
        report.findings.append(
            Finding(
                "P2",
                "NAMING_DENSITY",
                1,
                f"표시된 신규 고유명 후보가 {len(unknown)}개입니다: {', '.join(unknown[:8])}",
            )
        )


def detect_scene_texture(report: FileReport, text: str, config: HarnessConfig) -> None:
    landscape_hits = sum(text.count(term) for term in config.landscape_terms)
    combat_hits = sum(text.count(term) for term in config.combat_terms)
    report.metrics["landscape_signal_count"] = landscape_hits
    report.metrics["combat_signal_count"] = combat_hits
    if word_count(text) >= 1200 and landscape_hits == 0:
        report.findings.append(
            Finding(
                "P2",
                "SCENE_NO_LANDSCAPE_SIGNAL",
                1,
                "장편 회차인데 바닥·냄새·소리·날씨·거리 등 공간 감각 신호가 없습니다. 기능적 풍경 묘사를 검토하세요.",
            )
        )
    if combat_hits >= 5:
        spatial = sum(text.count(term) for term in ("거리", "발", "왼쪽", "오른쪽", "뒤", "앞", "퇴로"))
        if spatial < 3:
            report.findings.append(
                Finding(
                    "P1",
                    "COMBAT_SPATIAL_CLARITY",
                    1,
                    "전투 신호는 많지만 거리·발자리·방향·퇴로 정보가 부족합니다.",
                )
            )


def detect_continuity(report: FileReport, text: str, config: HarnessConfig) -> None:
    required = config.continuity.get("required_when_present", {})
    for trigger, companions in required.items():
        if trigger not in text:
            continue
        missing = [term for term in companions if term not in text]
        if missing:
            report.findings.append(
                Finding(
                    "P2",
                    "CONTINUITY_CONTEXT_MISSING",
                    1,
                    f"'{trigger}' 등장 시 함께 확인할 연속성 신호가 없습니다: {', '.join(missing)}",
                )
            )


def build_paragraphs(lines: list[str]) -> list[tuple[int, str]]:
    paragraphs: list[tuple[int, str]] = []
    buffer: list[str] = []
    start = 1
    in_fence = False
    for number, raw in enumerate(lines, 1):
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or HEADING_RE.match(stripped):
            continue
        if not stripped:
            if buffer:
                paragraphs.append((start, " ".join(buffer)))
                buffer = []
            continue
        cleaned = strip_markdown_noise(raw)
        if not cleaned:
            continue
        if not buffer:
            start = number
        buffer.append(cleaned)
    if buffer:
        paragraphs.append((start, " ".join(buffer)))
    return paragraphs


def analyze_file(path: Path, config: HarnessConfig) -> FileReport:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    report = FileReport(path=path)
    paragraphs = build_paragraphs(lines)
    indexed_sentences: list[tuple[int, str]] = []
    for line, paragraph in paragraphs:
        indexed_sentences.extend((line, sentence) for sentence in split_sentences(paragraph))

    add_term_findings(report, text, config.legacy_terms, "P0", "CANON_LEGACY_TERM", "폐기 정본 발견")
    detect_short_sentence_chains(report, indexed_sentences, config)
    detect_paragraph_rhythm(report, paragraphs, config)
    detect_repeated_openings(report, indexed_sentences, config)
    detect_repeated_phrases(report, text, config)
    detect_watch_terms(report, text, config)
    detect_name_density(report, text, config)
    detect_scene_texture(report, text, config)
    detect_continuity(report, text, config)

    sentence_total = len(report.sentence_lengths)
    short_total = sum(1 for length in report.sentence_lengths if 0 < length <= config.short_sentence_words)
    report.metrics.update(
        {
            "words": word_count(text),
            "sentences": sentence_total,
            "paragraphs": len(paragraphs),
            "short_sentence_ratio": round(short_total / sentence_total, 3) if sentence_total else 0,
            "dialogue_line_ratio": round(
                sum(1 for line in lines if DIALOGUE_RE.match(line)) / max(len(lines), 1), 3
            ),
        }
    )
    report.findings.sort(key=lambda item: (item.line, item.severity, item.code))
    return report


def render_markdown(reports: Sequence[FileReport]) -> str:
    output = ["# Prose QA Report", ""]
    blockers = sum(report.blockers for report in reports)
    warnings = sum(report.warnings for report in reports)
    output.extend(
        [
            f"- Files: {len(reports)}",
            f"- P0 blockers: {blockers}",
            f"- P1/P2 warnings: {warnings}",
            "",
        ]
    )
    for report in reports:
        verdict = "BLOCK" if report.blockers else ("REVIEW" if report.warnings else "PASS")
        output.extend([f"## {report.path}", "", f"판정: **{verdict}**", "", "### Metrics", ""])
        for key, value in sorted(report.metrics.items()):
            output.append(f"- {key}: {value}")
        output.extend(["", "### Findings", ""])
        if not report.findings:
            output.append("- 없음")
        for item in report.findings:
            detail = f" — `{item.excerpt}`" if item.excerpt else ""
            output.append(
                f"- **{item.severity} {item.code}** (L{item.line}): {item.message}{detail}"
            )
        output.append("")
    return "\n".join(output)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="팔대신병록 정적 문체 QA 하네스")
    parser.add_argument("paths", nargs="+", type=Path, help="검사할 .md/.txt 파일 또는 디렉터리")
    parser.add_argument(
        "--config", type=Path, default=Path("config/prose_harness.json"), help="하네스 설정 JSON"
    )
    parser.add_argument("--recursive", action="store_true", help="디렉터리를 재귀 검사")
    parser.add_argument("--report", type=Path, help="Markdown 리포트 출력 경로")
    parser.add_argument(
        "--strict-canon",
        action="store_true",
        help="P0 정본 위반이 있으면 종료 코드 2 반환",
    )
    parser.add_argument(
        "--fail-on-warning",
        action="store_true",
        help="P1/P2 경고가 있으면 종료 코드 1 반환",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    config = HarnessConfig.load(args.config)
    files = list(iter_input_files(args.paths, args.recursive))
    if not files:
        print("검사할 .md/.txt 파일이 없습니다.", file=sys.stderr)
        return 2
    reports = [analyze_file(path, config) for path in files]
    rendered = render_markdown(reports)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered)
    blockers = sum(report.blockers for report in reports)
    warnings = sum(report.warnings for report in reports)
    if args.strict_canon and blockers:
        return 2
    if args.fail_on_warning and warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
