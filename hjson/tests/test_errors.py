# -*- coding: utf-8 -*-
import pickle
import sys
from unittest import TestCase

import hjson as json
from hjson.compat import b, u


class TestErrors(TestCase):
    def test_string_keys_error(self):
        data = [{"a": "A", "b": (2, 4), "c": 3.0, ("d",): "D tuple"}]
        self.assertRaises(TypeError, json.dumpsJSON, data)

    def test_decode_error(self):
        err = None
        try:
            json.loads("{}\na\nb")
        except json.HjsonDecodeError:
            err = sys.exc_info()[1]
        else:
            self.fail("Expected HjsonDecodeError")
        self.assertEqual(err.lineno, 2)
        self.assertEqual(err.colno, 1)
        self.assertEqual(err.endlineno, 3)
        self.assertEqual(err.endcolno, 2)

    def test_scan_error(self):
        err = None
        for t in (u, b):
            try:
                json.loads(t('{"asdf": "'))
            except json.HjsonDecodeError:
                err = sys.exc_info()[1]
            else:
                self.fail("Expected HjsonDecodeError")
            self.assertEqual(err.lineno, 1)
            self.assertEqual(err.colno, 10)

    def test_error_is_pickable(self):
        err = None
        try:
            json.loads("{}\na\nb")
        except json.HjsonDecodeError:
            err = sys.exc_info()[1]
        else:
            self.fail("Expected HjsonDecodeError")
        s = pickle.dumps(err)
        e = pickle.loads(s)

        self.assertEqual(err.msg, e.msg)
        self.assertEqual(err.doc, e.doc)
        self.assertEqual(err.pos, e.pos)
        self.assertEqual(err.end, e.end)
