import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aflr_python_client",
    version="0.0.12",
    author="Antonio Tripiana",
    author_email="antonio@aflorithmic.ai",
    description="Python library for the Aflorithmic API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aflorithmic/aflr_python_client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)