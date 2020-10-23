import unittest
import io
import textwrap

from core import get_allies, is_ally, _load_from, _rotate_left


class TameOfThronesTestCase(unittest.TestCase):
    def test_no_data(self):
        data = []
        self.assertEqual(get_allies(data), [])

    def test_success(self):
        data = [
                ("air", "rozo"),
                ("land", "faijwjsoofamau"),
                ("ice", "sthststvsasos"),
        ]
        for kingdom, msg in data:
            self.assertTrue(is_ally(kingdom, msg))

    def test_can_rule(self):
        data = [
                ("air", "rozo"),
                ("land", "faijwjsoofamau"),
                ("ice", "sthststvsasos"),
        ]
        self.assertEqual(get_allies(data), ["air", "land", "ice"])

    def test_cannot_rule(self):
        data = [
            ("air", "owlaowlbowlc"),
            ("land", "ofbbmufdiccso"),
            ("ice", "vtbtbhtbbbobas"),
            ("water", "summer is coming"),
        ]
        self.assertFalse(len(get_allies(data)) >= 3)


    def test_load_from_stream(self):
        stream = io.StringIO(textwrap.dedent("""
            air owlaowlbowlc
            land ofbbmufdiccso
            ice vtbtbhtbbbobas
            water summer is coming
        """))
        expected = [
            ("air", "owlaowlbowlc"),
            ("land", "ofbbmufdiccso"),
            ("ice", "vtbtbhtbbbobas"),
            ("water", "summer is coming"),
        ]

        data = _load_from(stream)
        self.assertEqual(data, expected)


    def test_rotate_left(self):
        expected_string = 'bca'
        params = [
            ('abc', 1, 'bca'),
            ('abcdef', 3, 'defabc'),
            ('abcdef', 3, 'defabc'),
            ('abcdefghijklmnopqrstuvwxyz', 13, 'nopqrstuvwxyzabcdefghijklm'),
        ]
        for (string, count, expected_string) in params:
            with self.subTest(string=string, count=count, expected_string=expected_string):
                rotated_string = _rotate_left(string, count)
                self.assertEqual(rotated_string, expected_string)

