import unittest
import fossil_delta as fossil


class TestFossilDelta(unittest.TestCase):
    def test_delta_apply(self):
        delta = fossil.create_delta('abcdef', 'defghi')
        out = fossil.apply_delta('ab', delta)
        self.assertEqual(out, 'defghi')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
