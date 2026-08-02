from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.prose_harness import HarnessConfig, analyze_file


class ProseHarnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        config = {
            "short_sentence_words": 3,
            "short_chain_limit": 4,
            "one_sentence_paragraph_ratio_warn": 0.5,
            "new_name_limit": 3,
            "repeated_opening_limit": 3,
            "repeated_phrase_limit": 3,
            "legacy_terms": ["소겸", "여성 서유휘"],
            "watch_terms": {"그 순간": 1},
            "canon_names": ["서유휘", "소연후"],
            "known_terms": ["반보문"],
            "landscape_terms": ["바닥", "비", "냄새"],
            "combat_terms": ["검", "베었다", "막았다"],
            "continuity": {"required_when_present": {"왼쪽 어깨": ["통증"]}},
        }
        config_path = self.root / "config.json"
        config_path.write_text(json.dumps(config, ensure_ascii=False), encoding="utf-8")
        self.config = HarnessConfig.load(config_path)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write(self, name: str, text: str) -> Path:
        path = self.root / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_legacy_term_is_p0(self) -> None:
        report = analyze_file(self.write("legacy.md", "소겸이 문을 열었다."), self.config)
        self.assertTrue(any(item.code == "CANON_LEGACY_TERM" and item.severity == "P0" for item in report.findings))

    def test_short_sentence_chain_is_warning(self) -> None:
        text = "멈췄다. 돌았다. 베었다. 피했다. 쓰러졌다."
        report = analyze_file(self.write("short.md", text), self.config)
        self.assertTrue(any(item.code == "RHYTHM_SHORT_CHAIN" for item in report.findings))

    def test_watch_term_limit(self) -> None:
        text = "그 순간 문이 열렸다. 그 순간 다시 닫혔다."
        report = analyze_file(self.write("watch.md", text), self.config)
        self.assertTrue(any(item.code == "STYLE_WATCH_TERM" for item in report.findings))

    def test_combat_without_space_is_p1(self) -> None:
        text = "검을 베었다. 다시 검을 막았다. 검이 부딪쳤다. 그는 베었다. 상대가 막았다."
        report = analyze_file(self.write("combat.md", text), self.config)
        self.assertTrue(any(item.code == "COMBAT_SPATIAL_CLARITY" and item.severity == "P1" for item in report.findings))

    def test_continuity_companion_signal(self) -> None:
        text = "서유휘는 왼쪽 어깨를 눌렀다."
        report = analyze_file(self.write("continuity.md", text), self.config)
        self.assertTrue(any(item.code == "CONTINUITY_CONTEXT_MISSING" for item in report.findings))

    def test_clean_excerpt_has_no_p0(self) -> None:
        text = (
            "비에 젖은 비무대 바닥은 발바닥을 반 치씩 밀어냈다. "
            "서유휘는 검을 뽑지 않고 상대의 오른발이 물웅덩이를 피하는 순간을 기다렸다.\n\n"
            "상대가 거리를 좁히자 그는 왼쪽으로 반 걸음 비켜 서며 칼등을 흘렸다. "
            "충격은 손목에서 어깨까지 번졌고, 숨을 한 번 고른 뒤에야 다음 발을 놓을 수 있었다."
        )
        report = analyze_file(self.write("clean.md", text), self.config)
        self.assertEqual(report.blockers, 0)


if __name__ == "__main__":
    unittest.main()
