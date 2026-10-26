# Copyright 2026 Microsoft Corporation
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
import unittest


class PatchScopeTest(unittest.TestCase):
    def test_backport_contains_only_go_and_documentation_changes(self):
        patch = Path(__file__).parents[1] / "patches/0001-luciusctl-transport-policy.patch"
        paths = [
            line.split(" b/", 1)[1]
            for line in patch.read_text().splitlines()
            if line.startswith("diff --git ")
        ]
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path):
                self.assertTrue(path.endswith((".go", ".md")), path)
