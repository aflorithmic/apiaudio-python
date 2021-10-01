import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apiaudio",
    version="0.11.1",
    author="Antonio Tripiana",
    author_email="antonio@aflorithmic.ai",
    description="Python SDK for api.audio API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aflorithmic/aflr_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests >= 2.20; python_version >= "3.0"'],
    python_requires=">=3.6",
)
