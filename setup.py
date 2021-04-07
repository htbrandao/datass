import io
import re

from setuptools import find_packages, setup


# with open('datass/__init__.py', 'r') as version:
#     version = re.search('(\d\.\d\.[\d\w\.]+)', version.readline()).group()

with io.open('./nia_madruguinha_classificador/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

unit_test_requirements = [
    'pytest',
]

integration_test_requirements = [
    'pytest',
]

run_requirements = [
    'numpy',
    'nltk',
    'pandas',
    'seaborn',
    'matplotlib',
    'plotly'
]

setup(
    name='datass',
    version=version,
    author='Henrique Brandão',
    author_email='brandao.t.henrique@gmail.com',
    license='MIT',
    zip_safe=False,
    install_requirements=run_requirements,
    description='Data Science Shortcuts. Package for lazy, or overwhelmed, data scientists',
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
