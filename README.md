# Delta compression algorithm for python

> > This is a python wrapper of the original C implementation. (Source code from Fossil-2.6)

Fossil achieves efficient storage and low-bandwidth synchronization through the
use of delta-compression. Instead of storing or transmitting the complete
content of an artifact, fossil stores or transmits only the changes relative to
a related artifact.

- [Format](http://www.fossil-scm.org/index.html/doc/tip/www/delta_format.wiki)
- [Algorithm](http://www.fossil-scm.org/index.html/doc/tip/www/delta_encoder_algorithm.wiki)
- [Original implementation](http://www.fossil-scm.org/index.html/artifact/f3002e96cc35f37b)

Other implementations:

- [JavaScript](https://github.com/dchest/fossil-delta-js) ([Online demo](https://dchest.github.io/fossil-delta-js/))
- [C#](https://github.com/endel/FossilDelta/blob/master/README.md)

## Install

```
pip install python-fossil-delta
```

## Example

```python
import fossil_delta


def main():
    delta = fossil_delta.create_delta('abc', 'abcdef')
    out = fossil_delta.apply_delta('abc', delta)
    print out  # --> abcdef
```
