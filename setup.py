import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

run_requirements = [
    'numpy',
    'nltk',
    'pandas',
    'seaborn',
    'matplotlib',
]

setuptools.setup(
    name="datass",
    version="0.0.1",
    author="Henrique Brandão",
    author_email="hbrandao@protonmail.com",
    license="MIT",
    zip_safe=False,
    install_requirements=run_requirements,
    description="Package functions made with repeated data analysis for loops",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/hbrandao/data-science-shortcuts",
    download_url="https://gitlab.com/hbrandao/data-science-shortcuts/-/archive/0.0.1/data-science-shortcuts-0.0.1.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
