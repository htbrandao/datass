import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datass",
    version="0.0.1",
    author="Henrique Brandão",
    author_email="hbrandao@protonmail.com",
    description="Package functions made with repeated data analysis for loops",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/hbrandao/data-science-shortcuts",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)