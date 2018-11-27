import os
import sys
import unittest
import fossil_delta

SAMPLE_DIR = os.path.join(os.path.dirname(__file__), 'samples')


def sample_file(filename):
    return os.path.join(SAMPLE_DIR, filename)


def to_bytes(s):
    if sys.version_info[0] < 3:
        return s.decode('hex')
    return bytes.fromhex(s)

class TestFossilDelta(unittest.TestCase):
    def test_delta_apply(self):
        delta = fossil_delta.create_delta(b'abc', b'abcdef')
        out = fossil_delta.apply_delta(b'abc', delta)
        self.assertEqual(out, b'abcdef')

    def test_delta_apply_complex_samples(self):
        num_cases = max([int(x.split('.')[1])
                         for x in os.listdir(SAMPLE_DIR)]) + 1
        for i in range(0, num_cases):
            with open(sample_file('src.{0}'.format(i))) as f_src, \
                 open(sample_file('dst.{0}'.format(i))) as f_dst, \
                 open(sample_file('out.{0}'.format(i))) as f_out:
                src = to_bytes(f_src.read())
                dst = to_bytes(f_dst.read())
                out = to_bytes(f_out.read())
                out_check = fossil_delta.apply_delta(src, dst)
                self.assertEqual(out, out_check)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
