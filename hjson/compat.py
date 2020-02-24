# -*- coding: utf-8 -*-
"""Python 3 compatibility shims
"""
import sys

if sys.version_info[0] < 3:
    PY3 = False

    def b(s):
        return s

    def u(s):
        return unicode(s, "unicode_escape")  # noqa: F821

    import cStringIO as StringIO

    StringIO = BytesIO = StringIO.StringIO
    text_type = unicode  # noqa: F821
    binary_type = str
    string_types = (basestring,)  # noqa: F821
    integer_types = (int, long)  # noqa: F821
    unichr = unichr  # noqa: F821
    reload_module = reload  # noqa: F821

    def fromhex(s):
        return s.decode("hex")


else:
    PY3 = True
    if sys.version_info[:2] >= (3, 4):
        from importlib import reload as reload_module  # noqa: F401
    else:
        from imp import reload as reload_module  # noqa: F401
    import codecs

    def b(s):
        return codecs.latin_1_encode(s)[0]

    def u(s):
        return s

    import io

    StringIO = io.StringIO
    BytesIO = io.BytesIO
    text_type = str
    binary_type = bytes
    string_types = (str,)
    integer_types = (int,)

    def unichr(s):
        return u(chr(s))

    def fromhex(s):
        return bytes.fromhex(s)


long_type = integer_types[-1]
