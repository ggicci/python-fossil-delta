"""
This module encapsulates the C API of fossil delta compression algorithm to
simplify its use in Python.
"""

from _delta import ffi, lib


def create_delta(src, dst):
    """
    Create a new delta.

    Parameters
    ----------
    src : bytes
        The source or pattern content
    dst : bytes
        The target content

    Returns
    -------
    bytes:
        The delta
    """
    assert isinstance(src, bytes), 'src must be type of bytes'
    assert isinstance(dst, bytes), 'dst must be type of bytes'

    # The delta is written into a preallocated buffer, zDelta, which
    # should be at least 60 bytes longer than the target file, zOut.
    out = ffi.new('char[]', len(dst) + 60)
    n = lib.delta_create(
        src,
        ffi.cast('unsigned int', len(src)),
        dst,
        ffi.cast('unsigned int', len(dst)),
        out,
    )

    if n < 0:
        raise Exception('lib.delta_create failed, return code: %d' % n)

    return bytes(ffi.unpack(out, n))


def apply_delta(src, delta):
    """
    Apply a delta.

    Parameters
    ----------
    src : bytes
        The source or pattern content
    delta : bytes
        Delta to apply to the pattern

    Returns
    -------
    bytes:
        The patched result
    """
    assert isinstance(src, bytes), 'src must be type of bytes'
    assert isinstance(delta, bytes), 'delta must be type of bytes'

    out_size = lib.delta_output_size(delta, len(delta))
    if out_size < 0:
        raise Exception(
            'lib.delta_output_size failed, return code: %d' % out_size)

    out = ffi.new('char[]', out_size + 1)
    n = lib.delta_apply(
        src,
        ffi.cast('int', len(src)),
        delta,
        ffi.cast('int', len(delta)),
        out,
    )

    if n < 0:
        raise Exception('lib.delta_apply failed, return code: %d' % n)

    return bytes(ffi.unpack(out, n))
