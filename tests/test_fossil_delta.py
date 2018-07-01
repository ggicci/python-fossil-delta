import unittest
import fossil_delta as fossil


class TestFossilDelta(unittest.TestCase):
    def test_delta_apply(self):
        delta = fossil.create_delta('abc', 'abcdef')
        out = fossil.apply_delta('abc', delta)
        self.assertEqual(out, 'abcdef')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
