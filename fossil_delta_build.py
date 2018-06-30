"""
CFFI builder wraps C source of fossil-delta implementation to python.
"""
import os
from cffi import FFI

ffibuilder = FFI()
MODULE_NAME = 'fossil_delta._delta'
CUR_DIR = os.path.dirname(__file__)

with open(os.path.join(CUR_DIR, 'src/fossil_delta/delta.h'), 'rt') as f:
    ffibuilder.cdef(f.read())

with open(os.path.join(CUR_DIR, 'src/fossil_delta/delta.c'), 'rt') as f:
    ffibuilder.set_source(
        MODULE_NAME,
        f.read(),
        source_extension='.c',
        extra_compile_args=[
            '-I' + os.path.join(CUR_DIR, 'src/fossil_delta'),
        ],
    )

ffibuilder.compile(verbose=True)

if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
