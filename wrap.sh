#!/bin/bash

Color_Off='\033[0m'       # Text Reset
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan

echo -e "${Purple}# Cleaning old build...${Color_Off}"
rm -r dist/ > /dev/null 2>&1

echo -e "${Purple}# Creating new build...${Color_Off}"
# python3 setup.py sdist bdist_wheel
python3 -m build > /dev/null 2>&1

echo -e "${Purple}# Uploading to PyPi...${Color_Off}"
twine upload dist/*

# echo -e "${Purple}# Commit and push to repo? (y/n)${Color_Off}"
# read answer
# if [ "$answer" != "${answer#[Yy]}" ] ;then
#     echo -e "${Purple}# Publishing to Git${Color_Off}"
#     git add .
#     git status
#     git commit -m 'wrapping version'
#     git push origin master
# else
#     echo -e "${Purple}# Skipping...${Color_Off}"
# fi

echo -e "${Purple}# Done${Color_Off}"
