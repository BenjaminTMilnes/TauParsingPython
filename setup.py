import setuptools 

with open("README.md", "r") as fo:
    long_description = fo.read()

setuptools.setup(
    name="tauparsing",
    version="1.0.0",
    author="B. T. Milnes",
    description="Some simple classes to help make human-readable parsers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenjaminTMilnes/TauParsing",
    packages=["tauparsing"]
)