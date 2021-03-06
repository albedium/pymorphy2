#!/usr/bin/env python
from setuptools import setup
# from Cython.Build import cythonize


def get_version():
    with open("pymorphy2/version.py", "rt") as f:
        return f.readline().split("=")[1].strip(' "\n')

setup(
    name = 'pymorphy2',
    version = get_version(),
    author = 'Mikhail Korobov',
    author_email = 'kmike84@gmail.com',
    url = 'https://github.com/kmike/pymorphy2/',

    description = 'Morphological analyzer (POS tagger + inflection engine) for Russian language.',
    long_description = open('README.rst').read(),

    license = 'MIT license',
    packages = [
        'pymorphy2',
        'pymorphy2.units',
        'pymorphy2.lang',
        'pymorphy2.lang.ru',
        'pymorphy2.lang.uk',
        'pymorphy2.opencorpora_dict',
    ],
    entry_points={
        'console_scripts': ['pymorphy = pymorphy2.cli:main']
    },
    requires=[
        'dawg_python (>= 0.7.1)',
        'pymorphy2_dicts_ru (>=2.4, <3.0)',
        'docopt (>= 0.6)',
    ],
    install_requires=[
        'dawg-python >= 0.7.1',
        'pymorphy2-dicts-ru >=2.4, <3.0',
        'docopt >= 0.6',
    ],
    extras_require = {
        'fast':  ["DAWG >= 0.7.7"],
    },
    zip_safe=False,

#    cmdclass = {'build_ext': build_ext},
#    ext_modules = [Extension("pymorphy2.analyzer", ["pymorphy2/analyzer.py"])],
    # ext_modules=cythonize([
    #     'pymorphy2/*.py',
    #     'pymorphy2/units/*.py',
    #     'pymorphy2/opencorpora_dict/*.py',
    # ], annotate=True, profile=True),

    classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: Russian',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Text Processing :: Linguistic',
    ],
)
