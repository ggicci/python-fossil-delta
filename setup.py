from setuptools import setup

setup(
    name='python-fossil-delta',
    version='18.6.0',
    description='Delta compression algorithm from fossil SCM',
    long_description=open('README.md', 'rt').read(),
    url='https://github.com/ggicci/fossil-delta',
    author='Ggicci',
    author_email='ggicci@163.com',
    license='MIT',
    keywords='fossil-delta compression algorithm',
    setup_requires=['cffi>=1.11.5'],
    package_dir={'': 'src'},
    packages=['fossil_delta'],
    cffi_modules=[
        'fossil_delta_build.py:ffibuilder',
    ],
    install_requires=['cffi>=1.0.0'],
    platforms='any',
)
