from pathlib import Path

import yaml

from unittest import TestCase

from altercase import (
    split_string,
    camel_case,
    hazard_case,
    kebab_case,
    pascal_case,
    snake_case,
    train_case,
)


class AltercaseTestCase(TestCase):
    def test(self) -> None:
        path = Path(__file__).parent.parent / "test-cases.yaml"
        text = path.read_text(encoding="utf-8", errors="ignore")
        cases = yaml.safe_load(text)
        for case in cases:
            # noinspection PyShadowingBuiltins
            input = case["input"]
            expected = case["expected"]
            expected_split = expected["split"]
            expected_camel = expected["camel"]
            expected_pascal = expected["pascal"]
            expected_kebab = expected["kebab"]
            expected_snake = expected["snake"]
            self.assertEqual(expected_split, split_string(input))
            self.assertEqual(expected_camel, camel_case(input))
            self.assertEqual(expected_pascal, pascal_case(input))
            self.assertEqual(expected_kebab, kebab_case(input))
            self.assertEqual(expected_kebab.upper(), train_case(input))
            self.assertEqual(expected_snake, snake_case(input))
            self.assertEqual(expected_snake.upper(), hazard_case(input))
            print(
                f"{input}:\n"
                f"\tsplit: {expected_split}\n"
                f"\tcamel: {expected_camel}\n"
                f"\tpascal: {expected_pascal}\n"
                f"\tkebab: {expected_kebab}\n"
                f"\ttrain: {expected_kebab.upper()}\n"
                f"\tsnake: {expected_snake}\n"
                f"\thazard: {expected_snake.upper()}\n"
            )
