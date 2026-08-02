from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "outline" / "960EP-COLLECTION-REWARD-MAP-v1.md"
OUT_DIR = ROOT / "production" / "episode-function-maps"
QA_PATH = ROOT / "audit" / "960EP-EPISODE-FUNCTION-MAP-QA.md"
LEDGER_PATH = ROOT / "outline" / "FORESHADOW-PAYOFF-LEDGER-v2.md"

ACT_SUBPLOTS: dict[int, list[str]] = {
    2: ["임강현의 현장 주도권", "백여울의 기록권", "서유휘의 어깨 손상", "천공팔기 장인 계보", "수맥 영수와 최종 수로 구역"],
    3: ["진서하의 독립 잠입", "곽하진의 거래와 배신", "가짜의 실제 가치", "강호기보록 누락 칸", "독물·해독 비용"],
    4: ["백여울의 회수자 정체성", "소연후와의 승부", "두 공동체의 생존권", "분기 제작 계보", "거리 선점 무공"],
    5: ["소연후의 문파 책임", "빈 검집과 부러진 검편", "젊은 제자의 전승 선택", "장인 후손 추적", "연계 절단 무공"],
    6: ["장인 인연망", "석주안·임강현의 영구 비용", "실패작의 유효성", "심법 충돌 조율", "신수 서식지 계약"],
    7: ["연무진과의 방식 충돌", "만류귀일보 한 점 집중", "백여울·소연후의 독립 선택", "영약 뒤 남는 감각 비용", "팔대신병 8/8 정보 완성"],
    8: ["팔대신병 최종 처분", "연무진의 책임", "소연후·진서하의 독립 결산", "백여울과 기록권 분리", "개로무극·팔방개로 완성"],
}

ACT_TITLES: dict[int, str] = {
    2: "장강과 첫 완전 신병",
    3: "암시장과 진위 전쟁",
    4: "두 진품과 거리 지배",
    5: "문파 비고와 검진",
    6: "장인 연합과 재련",
    7: "사부의 완성 목록",
    8: "집결과 자기 무공",
}

PHASES = [
    ("진입", "{block}의 현장에 들어가 첫 불일치를 확인한다.", "서유휘는 안전한 관망보다 직접 확인을 택한다.", "{subplot}을 현재 사건과 연결한다.", "{next_hook}"),
    ("대면", "‘{block}’을 둘러싼 당사자들의 이해관계를 대조한다.", "가장 강한 세력보다 가장 약한 피해자의 말을 먼저 듣는다.", "{subplot}에 첫 관계 충돌을 남긴다.", "공식 설명과 현장 증언의 시각이 어긋난다."),
    ("시험", "‘{block}’의 기능이나 진위를 작은 실험·대련·감정으로 검증한다.", "완전한 성공보다 실패 원인을 얻는 쪽을 택한다.", "후반 회수에 쓸 물리 법칙이나 절차 단서를 심는다.", "성공했지만 다른 조건에서만 작동한다."),
    ("압력", "시간·부상·제도 압력이 동시에 커진다.", "한 가지 이득을 포기해 피해 확산을 막는다.", "{subplot}의 비용을 실제 손실로 바꾼다.", "포기한 목표가 상대의 손에 들어간다."),
    ("부분 회수", "앞서 심은 단서 하나의 현재 의미를 밝힌다.", "확실한 사실과 아직 모르는 사실을 분리한다.", "{subplot}을 설치에서 증폭 단계로 올린다.", "{next_hook}"),
    ("전환", "처음 세운 목표가 충분하지 않았음을 깨닫는다.", "소유·승리보다 사용·책임을 새 목표로 삼는다.", "{subplot}의 의미를 변환한다.", "새 목표를 막는 얼굴 있는 반대자가 등장한다."),
    ("협상", "동료·적대자·사용자와 권리와 책임을 협상한다.", "자신에게 유리한 독점 조항을 지우고 상대의 독립 목적을 인정한다.", "{subplot}의 관계 상태를 비가역적으로 바꾼다.", "합의 밖의 제3 권리자가 나타난다."),
    ("실전", "앞선 단서를 추격·대련·구조·탈취의 동선에 적용한다.", "가장 빠른 승리보다 퇴로와 후속 선택을 남기는 승리를 택한다.", "{subplot}을 행동과 물리 결과로 증명한다.", "승리한 방식이 다음 문제의 원인이 된다."),
    ("결산전", "블록의 핵심 선택을 실행하고 대립자의 마지막 수를 받는다.", "완전한 승리보다 이후 책임 구조가 남는 선택을 한다.", "맥거핀을 증폭하거나 처음 의미를 뒤집는다.", "결산 직전 다른 해석을 뒷받침하는 증거가 나온다."),
    ("결산", "‘{block}’의 보상과 후유증을 장부에 남긴다.", "소유·사용·기록·처분 권리를 필요한 만큼 분리한다.", "{subplot}을 다음 블록으로 이월하고 질문 하나를 부분 회수한다.", "{next_hook}"),
]

GLOBAL_PAYOFFS = [
    ("이름", "참가하지 않은 명단", "타인의 추천과 반보문 자격", "이름 도용이 피해이자 강호 진입의 문", "직함이 아닌 선택과 전적으로 서유휘의 이름을 공인"),
    ("부러진 검편", "비무 상품", "장인 계보와 신병 재료 단서", "완성검 파편이 아닌 분기 제작의 증거", "팔대신병이 단일 왕권 병기가 아닌 기능 분리 체계임을 입증"),
    ("반보문", "술김에 만든 가짜 문파", "피해 보상과 책임 계약", "가짜 소속이 실제 책임망으로 변화", "거대 문파가 아닌 느슨한 길 보증망으로 정착"),
    ("연무진의 추천", "죽은 사부의 생존 단서", "여러 사건의 박자와 기록", "흑막이 아니라 선택을 선점한 효율주의자", "다른 방식이 실제로 작동함을 보여 책임을 묻는 결말"),
    ("백여울의 기록", "검편 공개 기록 요구", "소유권 충돌과 결별", "기록 공개도 권력이 될 수 있음", "소유·사용·기록권을 분리하고 다음 기물을 함께 추적"),
    ("만류귀일보", "여러 무공의 발자리 원리", "한 점 집중형 절정", "연무진의 독점 방식과 닮았음을 자각", "개로무극·팔방개로로 공격로와 퇴로를 동시에 개방"),
]


@dataclass(frozen=True)
class Block:
    act: int
    start: int
    end: int
    summary: str


def parse_blocks(text: str) -> list[Block]:
    act = 0
    blocks: list[Block] = []
    for raw in text.splitlines():
        line = raw.strip()
        m_act = re.match(r"## ACT\s+(\d+)\s+—", line)
        if m_act:
            act = int(m_act.group(1))
            continue
        m = re.match(r"-\s+(\d+)~(\d+):\s+(.+)", line)
        if m and 2 <= act <= 8:
            blocks.append(Block(act, int(m.group(1)), int(m.group(2)), m.group(3).strip()))
    return blocks


def clean_block_name(summary: str) -> str:
    first = summary.split(".", 1)[0].strip()
    return first.rstrip(". ")


def phase_for(index: int, count: int) -> tuple[str, str, str, str, str]:
    if count == 1:
        return PHASES[-1]
    if count < 10:
        mapped = round(index * 9 / max(1, count - 1))
        return PHASES[mapped]
    return PHASES[min(index, 9)]


def next_hook(blocks: list[Block], idx: int) -> str:
    if idx + 1 < len(blocks) and blocks[idx + 1].act == blocks[idx].act:
        return f"다음 구간 ‘{clean_block_name(blocks[idx + 1].summary)}’의 징후가 현재 결과에서 드러난다."
    if blocks[idx].act < 8:
        return f"ACT {blocks[idx].act + 1}의 첫 사건으로 이어지는 인물·물건·기록이 모습을 드러낸다."
    return "남겨 둔 미확인 기물이 다음 여정을 연다."


def render_act(act: int, blocks: list[Block]) -> str:
    title = ACT_TITLES[act]
    act_blocks = [b for b in blocks if b.act == act]
    lines = [
        f"# 《팔대신병록》 ACT {act} 화별 기능표 — {title}",
        "",
        "상태: `episode-function-map / canon-aligned / manuscript-locked`",
        f"범위: EP{act_blocks[0].start}~EP{act_blocks[-1].end}",
        "",
        "각 화 표기: `목표 / 서유휘의 선택 / 서브플롯·복선 / 화말 훅`",
        "",
    ]
    subplots = ACT_SUBPLOTS[act]
    all_index = {id(b): i for i, b in enumerate(blocks)}
    for block_index, block in enumerate(act_blocks):
        block_name = clean_block_name(block.summary)
        subplot = subplots[block_index % len(subplots)]
        hook = next_hook(blocks, all_index[id(block)])
        count = block.end - block.start + 1
        lines += [f"## EP{block.start}~EP{block.end} — {block_name}", "", f"블록 정본: {block.summary}", ""]
        for local, ep in enumerate(range(block.start, block.end + 1)):
            phase, goal, choice, thread, end_hook = phase_for(local, count)
            values = {
                "block": block_name,
                "subplot": subplot,
                "next_hook": hook,
            }
            lines.append(
                f"- **EP{ep} [{phase}]** 목표: {goal.format(**values)} / "
                f"선택: {choice.format(**values)} / "
                f"서브·복선: {thread.format(**values)} / "
                f"**훅:** {end_hook.format(**values)}"
            )
        lines.append("")
    lines += [
        "## ACT 완료 Gate",
        "- 모든 화에 서유휘의 선택 또는 그 선택의 직접 비용이 존재한다.",
        "- 각 블록은 기존 질문을 하나 이상 부분 회수하고 새 질문은 최대 두 개만 연다.",
        "- 추적·거래·감정·전투·구조·복원 중심 동사를 한 액트 안에서 교차한다.",
        "- 장기 맥거핀은 설치·증폭·변환·회수 중 한 단계에 연결한다.",
        "- 가까운 30화만 상세 비트로, 가까운 10화만 장면표로 확장한다.",
        "",
    ]
    return "\n".join(lines)


def render_ledger(blocks: list[Block]) -> str:
    lines = [
        "# 《팔대신병록》 복선·맥거핀·결말 회수 장부 v2",
        "",
        "상태: `generated-ledger / canon-aligned / manuscript-locked`",
        "",
        "## 대서사 회수축",
        "",
        "| 축 | 설치 | 증폭 | 변환 | 최종 회수 |",
        "|---|---|---|---|---|",
    ]
    for row in GLOBAL_PAYOFFS:
        lines.append("| " + " | ".join(row) + " |")
    lines += ["", "## ACT 2~8 블록별 회수 운용", ""]
    for act in range(2, 9):
        lines.append(f"### ACT {act} — {ACT_TITLES[act]}")
        lines.append("")
        lines.append("| 범위 | 설치·증폭 대상 | 부분 회수 기준 | 다음 이월 |")
        lines.append("|---|---|---|---|")
        act_blocks = [b for b in blocks if b.act == act]
        for i, block in enumerate(act_blocks):
            subplot = ACT_SUBPLOTS[act][i % len(ACT_SUBPLOTS[act])]
            follow = clean_block_name(act_blocks[i + 1].summary) if i + 1 < len(act_blocks) else (f"ACT {act + 1}" if act < 8 else "에필로그 이후 미확인 기물")
            lines.append(f"| EP{block.start}~{block.end} | {subplot}: {clean_block_name(block.summary)} | 블록 중간과 결산화에서 의미를 한 번씩 갱신 | {follow} |")
        lines.append("")
    lines += [
        "## 방치 방지 Gate",
        "- 3~5화 장치는 10화 안에 1차 회수한다.",
        "- 소액트 질문은 같은 중액트 안에서 부분 답변한다.",
        "- 대액트 질문은 다음 두 액트 안에 재등장시킨다.",
        "- 대서사 회수축은 ACT 7 이전 최소 세 차례 의미를 증폭한다.",
        "- 회수는 설명문이 아니라 선택·전투·소유·관계 변화로 발생시킨다.",
        "",
    ]
    return "\n".join(lines)


def validate(blocks: list[Block], outputs: dict[Path, str]) -> list[str]:
    problems: list[str] = []
    expected = list(range(111, 961))
    actual: list[int] = []
    for b in blocks:
        actual.extend(range(b.start, b.end + 1))
    if actual != expected:
        missing = sorted(set(expected) - set(actual))
        duplicates = sorted({ep for ep in actual if actual.count(ep) > 1})
        problems.append(f"episode coverage mismatch: missing={missing[:20]} duplicates={duplicates[:20]}")
    if len(blocks) != 85:
        problems.append(f"expected 85 ACT2~8 blocks, found {len(blocks)}")
    for path, content in outputs.items():
        if "[진입]" not in content or "[결산]" not in content:
            problems.append(f"phase markers missing: {path}")
        if "서유휘" not in content:
            problems.append(f"protagonist choice missing: {path}")
    return problems


def qa_report(blocks: list[Block], outputs: dict[Path, str], problems: list[str]) -> str:
    episode_count = sum(b.end - b.start + 1 for b in blocks)
    digest = hashlib.sha256("".join(outputs.values()).encode("utf-8")).hexdigest()[:16]
    lines = [
        "# 960화 화별 기능표 자동 QA",
        "",
        "상태: `PASS`" if not problems else "상태: `BLOCK`",
        "",
        f"- ACT 2~8 블록 수: {len(blocks)}",
        f"- 생성 화수: {episode_count}",
        "- 목표 범위: EP111~EP960 (850화)",
        f"- 생성물 해시: `{digest}`",
        "- 원고 상태: 잠금 유지",
        "",
        "## 검사 결과",
        "",
    ]
    if problems:
        lines.extend(f"- P0: {item}" for item in problems)
    else:
        lines += [
            "- 연속 화수 누락·중복: 없음.",
            "- ACT 2~8 범위: 모두 생성.",
            "- 화별 목표·선택·서브플롯·훅 필드: 존재.",
            "- 블록별 부분 회수와 다음 이월: 존재.",
            "- 대서사 회수 장부: 생성.",
        ]
    lines += [
        "",
        "## 해석 제한",
        "",
        "- 자동 생성 문서는 전편 화별 기능을 고정하는 제작 뼈대다.",
        "- 실제 집필 직전 30화는 상세 비트, 10화는 장면표로 재작성한다.",
        "- 자동 QA는 재미·감정·전투 박진감을 대신 판정하지 않는다.",
        "- 반복되는 기능 문장은 가까운 30화 상세화 과정에서 사건 고유 행동으로 교체한다.",
        "",
    ]
    return "\n".join(lines)


def build_outputs() -> tuple[list[Block], dict[Path, str]]:
    text = SOURCE.read_text(encoding="utf-8")
    blocks = parse_blocks(text)
    outputs: dict[Path, str] = {}
    for act in range(2, 9):
        act_blocks = [b for b in blocks if b.act == act]
        filename = f"ACT{act}-EP{act_blocks[0].start}-{act_blocks[-1].end}-EPISODE-FUNCTION-MAP-v1.md"
        outputs[OUT_DIR / filename] = render_act(act, blocks)
    outputs[LEDGER_PATH] = render_ledger(blocks)
    problems = validate(blocks, outputs)
    outputs[QA_PATH] = qa_report(blocks, outputs, problems)
    if problems:
        raise SystemExit("\n".join(problems))
    return blocks, outputs


def write_outputs(outputs: dict[Path, str]) -> None:
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content + "\n", encoding="utf-8")


def check_outputs(outputs: dict[Path, str]) -> None:
    stale: list[str] = []
    for path, content in outputs.items():
        expected = content + "\n"
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            stale.append(str(path.relative_to(ROOT)))
    if stale:
        raise SystemExit("generated episode maps are missing or stale:\n- " + "\n- ".join(stale))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate ACT2~8 episode function maps and payoff ledger.")
    parser.add_argument("--check", action="store_true", help="Fail when committed generated files are missing or stale.")
    args = parser.parse_args()
    _, outputs = build_outputs()
    if args.check:
        check_outputs(outputs)
    else:
        write_outputs(outputs)
        print(f"generated {len(outputs)} files")


if __name__ == "__main__":
    main()
