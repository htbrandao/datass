import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

run_requirements = [
    'numpy==1.18.5',
    'nltk==3.5',
    'pandas==1.1.5',
    'seaborn==0.11.0',
    'matplotlib==3.3.2',
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
    download_url="https://gitlab.com/hbrandao/data-science-shortcuts/dist/datass-0.0.1.tar.gz"
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Data Science",
        "Natural Language :: English"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.8',
)
