import os
import re
from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r"""sdk_version = ['"]([0-9.]+)['"]""")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def get_version():
    init = open(os.path.join(ROOT, "apiaudio", "__init__.py")).read()
    return VERSION_RE.search(init).group(1)


setup(
    name="apiaudio",
    version=get_version(),
    author="Aflorithmic",
    author_email="linda@aflorithmic.ai",
    description="Python SDK for api.audio API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aflorithmic/apiaudio-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests >= 2.20; python_version >= "3.0"'],
    python_requires=">=3.6",
)
