#!/bin/bash

Color_Off='\033[0m'       # Text Reset
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan

echo -e "${Purple}# Cleaning old build${Color_Off}"
rm -r dist/ > /dev/null 2>&1
echo "..."

echo -e "${Purple}# Creating new build${Color_Off}"
# python3 setup.py sdist bdist_wheel
# twine upload --verbose dist/*

echo -e "${Purple}# Repo: ${Cyan}$(git remote -v | grep origin | head -n 1)${Color_Off}"
echo -n -e "${Purple}Confirm? (y/n) ${Color_Off}"
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
    echo -e "${Purple}# Publishing to Git${Color_Off}"
    git add .
    git status
    # git commit -m 'wrapping version'
    # git push origin master
else
    echo -e "${Purple}# Skipping...${Color_Off}"
fi
echo -e "${Purple}# Done${Color_Off}"
