from __future__ import annotations

import unittest
from pathlib import Path

import tools.generate_episode_function_maps as base
import tools.generate_episode_function_maps_v2 as corrected


ROOT = Path(__file__).resolve().parents[1]


class EpisodeFunctionGeneratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        source = ROOT / "outline" / "960EP-COLLECTION-REWARD-MAP-v1.md"
        cls.blocks = base.parse_blocks(source.read_text(encoding="utf-8"))

    def test_block_count(self) -> None:
        self.assertEqual(len(self.blocks), 87)

    def test_episode_coverage(self) -> None:
        episodes: list[int] = []
        for block in self.blocks:
            episodes.extend(range(block.start, block.end + 1))
        self.assertEqual(episodes, list(range(111, 961)))

    def test_act_boundaries(self) -> None:
        boundaries = {
            2: (111, 225),
            3: (226, 345),
            4: (346, 465),
            5: (466, 590),
            6: (591, 715),
            7: (716, 840),
            8: (841, 960),
        }
        for act, expected in boundaries.items():
            act_blocks = [block for block in self.blocks if block.act == act]
            self.assertEqual((act_blocks[0].start, act_blocks[-1].end), expected)

    def test_rendered_maps_have_required_fields(self) -> None:
        for act in range(2, 9):
            rendered = base.render_act(act, self.blocks)
            self.assertIn("목표:", rendered)
            self.assertIn("선택:", rendered)
            self.assertIn("서브·복선:", rendered)
            self.assertIn("**훅:**", rendered)
            self.assertIn("서유휘", rendered)

    def test_corrected_validation_passes(self) -> None:
        outputs = {
            Path(f"ACT{act}.md"): base.render_act(act, self.blocks)
            for act in range(2, 9)
        }
        self.assertEqual(corrected.validate(self.blocks, outputs), [])

    def test_payoff_ledger_contains_all_global_axes(self) -> None:
        ledger = base.render_ledger(self.blocks)
        for axis in ["이름", "부러진 검편", "반보문", "연무진의 추천", "백여울의 기록", "만류귀일보"]:
            self.assertIn(axis, ledger)


if __name__ == "__main__":
    unittest.main()
