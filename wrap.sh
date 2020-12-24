#!/bin/bash

echo "Cleaning old build" &&
rm -vr dist/ &&

echo "Creating new build" &&
python3 setup.py sdist bdist_wheel &&
twine upload --verbose dist/*

echo "Publishing to Git"
git add .
git status
git commit -m 'wrapping version'
git push origin master
