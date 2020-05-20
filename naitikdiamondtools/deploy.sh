#!/bin/bash

repos=(
  "/diamond-tools-website/"
)

echo ""
echo "Getting latest for" ${#repos[@]} "repositories using pull --rebase"

for repo in "${repos[@]}"
do
  echo ""
  echo "****** Getting latest for" ${repo} "******"
  cd "${repo}"
  git pull origin master
  echo "******************************************"
done
