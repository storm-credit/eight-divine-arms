from __future__ import annotations

from pathlib import Path

import tools.generate_episode_function_maps as base


def validate(blocks: list[base.Block], outputs: dict[Path, str]) -> list[str]:
    problems: list[str] = []
    expected = list(range(111, 961))
    actual: list[int] = []
    for block in blocks:
        actual.extend(range(block.start, block.end + 1))

    if actual != expected:
        missing = sorted(set(expected) - set(actual))
        duplicates = sorted({episode for episode in actual if actual.count(episode) > 1})
        problems.append(
            f"episode coverage mismatch: missing={missing[:20]} duplicates={duplicates[:20]}"
        )

    if len(blocks) != 87:
        problems.append(f"expected 87 ACT2~8 blocks, found {len(blocks)}")

    for path, content in outputs.items():
        if path.name.startswith("ACT"):
            if "[진입]" not in content or "[결산]" not in content:
                problems.append(f"phase markers missing: {path}")
            if "서유휘" not in content:
                problems.append(f"protagonist choice missing: {path}")

    return problems


base.validate = validate


if __name__ == "__main__":
    base.main()
