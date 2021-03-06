# -*- coding: utf-8 -*-
from operator import itemgetter
from unittest import TestCase

import hjson as json


class TestItemSortKey(TestCase):
    def test_simple_first(self):
        a = {
            "a": 1,
            "c": 5,
            "jack": "jill",
            "pick": "axe",
            "array": [1, 5, 6, 9],
            "tuple": (83, 12, 3),
            "crate": "dog",
            "zeak": "oh",
        }
        self.assertEqual(
            '{"a": 1, "c": 5, "crate": "dog", "jack": "jill", "pick": "axe", "zeak": "oh", "array": [1, 5, 6, 9], "tuple": [83, 12, 3]}',  # noqa: B950
            json.dumpsJSON(a, item_sort_key=json.simple_first),
        )

    def test_case(self):
        a = {
            "a": 1,
            "c": 5,
            "Jack": "jill",
            "pick": "axe",
            "Array": [1, 5, 6, 9],
            "tuple": (83, 12, 3),
            "crate": "dog",
            "zeak": "oh",
        }
        self.assertEqual(
            '{"Array": [1, 5, 6, 9], "Jack": "jill", "a": 1, "c": 5, "crate": "dog", "pick": "axe", "tuple": [83, 12, 3], "zeak": "oh"}',  # noqa: B950
            json.dumpsJSON(a, item_sort_key=itemgetter(0)),
        )
        self.assertEqual(
            '{"a": 1, "Array": [1, 5, 6, 9], "c": 5, "crate": "dog", "Jack": "jill", "pick": "axe", "tuple": [83, 12, 3], "zeak": "oh"}',  # noqa: B950
            json.dumpsJSON(a, item_sort_key=lambda kv: kv[0].lower()),
        )
