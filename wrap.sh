#!/bin/bash

git add .

git status

git commit -m 'wrapping version'

git push origin master

python3 setup.py sdist bdist_wheel

twine upload --verbose dist/*
