import io
import re
import setuptools


with io.open('datass/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string!")

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

run_requirements = [
    'numpy',
    'nltk',
    'pandas',
    'seaborn',
    'matplotlib',
    'plotly'
]

setuptools.setup(
    name='datass',
    version=version,
    author='Henrique Brandão',
    author_email='hbrandao@protonmail.com',
    license='MIT',
    zip_safe=False,
    install_requirements=run_requirements,
    description='Data Science Shortcuts (DataSS): Package for lazy, or overwhelmed, data scientists',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/htbrandao/datass',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
    ],
    python_requires='>=3.8',
)
