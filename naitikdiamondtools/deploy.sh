#!/bin/bash

# repos=(
#   "/diamond-tools-website/"
# )
#
# echo ""
# echo "Getting latest for" ${#repos[@]} "repositories using pull --rebase"
#
# for repo in "${repos[@]}"
# do
#   echo ""
#   echo "****** Getting latest for" ${repo} "******"
#   cd "${repo}"
#   git pull origin master
#   echo "******************************************"
# done

# Get servers list
set -f
string=$PROD_DEPLOY_SERVER
array=(${string//,/ })

# Iterate servers for deploy and pull last commit:
for i in "${!array[@]}"; do
  echo "Deploy project on server ${array[i]}"
  ssh ec2-user@${array[i]} "cd diamond-tools-website && git pull origin master && sudo systemctl restart nginx"
done
