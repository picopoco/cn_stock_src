from setuptools import setup
import io
import os
import cn_stock_src

__author__ = 'Cedric Zhuang'


def here(filename=None):
    ret = os.path.abspath(os.path.dirname(__file__))
    if filename is not None:
        ret = os.path.join(ret, filename)
    return ret


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n\n')
    buf = []
    for filename in filenames:
        with io.open(here(filename), encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


setup(
    name="cn_stock_src",
    version=cn_stock_src.__version__,
    author="Cedric Zhuang",
    author_email="cedric.zhuang@gmail.com",
    description="Utility for int date like 20150312.",
    license="BSD",
    keywords="Stock data retriever for China stock market.",
    url="http://github.com/jealous/cn_stock_src",
    packages=['cn_stock_src'],
    platforms=['any'],
    long_description=read('README.md'),
    classifiers=[
        "Programming Language :: Python",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    tests_require=['pytest', 'pyhamcrest']
)