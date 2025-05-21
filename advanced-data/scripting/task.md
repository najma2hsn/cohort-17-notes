# Task

Create a function that:

1. Checks and retrieves a local git repo for any changes on Github

2. If there are outstanding files in the local git repo that need to be committed, commit them with a custom message entered by the user, then push the files to github

3. If no outstanding files, do nothing

HINTS:

`git_status=$(git status)`
` if [[ "$git_status" != *"nothing to commit"* ]]; then`