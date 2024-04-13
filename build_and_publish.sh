#!/bin/bash
set -euo pipefail

is_repo_clean=`git status --porcelain`

if [[ $is_repo_clean ]]; then
  echo Repo is not clean
  exit 1
else
  :
fi

read -p "Tag: " newtag

git push
git tag $newtag
git push --tags

rm -rf dist
python3 -m pip install --upgrade build
python3 -m build
python3 -m twine upload dist/*

echo "Succesfully uploaded the package in version ${newtag}"