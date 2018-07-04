import os
import unittest
import fossil_delta

SAMPLE_DIR = os.path.join(os.path.dirname(__file__), 'samples')


def sample_file(filename):
    return os.path.join(SAMPLE_DIR, filename)


class TestFossilDelta(unittest.TestCase):
    def test_delta_apply(self):
        delta = fossil_delta.create_delta('abc', 'abcdef')
        out = fossil_delta.apply_delta('abc', delta)
        self.assertEqual(out, 'abcdef')

    def test_delta_apply_complex_samples(self):
        num_cases = max([int(x.split('.')[1])
                         for x in os.listdir(SAMPLE_DIR)]) + 1
        for i in range(0, num_cases):
            with open(sample_file('src.{0}'.format(i))) as f_src, \
                 open(sample_file('dst.{0}'.format(i))) as f_dst, \
                 open(sample_file('out.{0}'.format(i))) as f_out:
                src = f_src.read().decode('hex')
                dst = f_dst.read().decode('hex')
                out = f_out.read().decode('hex')
                out_check = fossil_delta.apply_delta(src, dst)
                self.assertEqual(out, out_check)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
