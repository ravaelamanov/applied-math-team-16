# If you want to contribute
## Getting Started
Just clone the repository using Git CLI: 
```
$ git clone https://github.com/ravaelamanov/primat_SEM4.git
```
## Before you edit code locally
Pull the changes before you start editing the code. In your local repo:
```
$ git checkout master
$ git pull
```
If want to sync your branch with master
```
$ git checkout <your_branch>
$ git merge master 
```
## Branch naming conventions
There is only one strict rule for the branch names. Any created branch must be associated with the lab by prefixing branch name.
Example:
```
lab1/implement_fibonacci
lab1/fix_fibonacci_precision_issue
```

## Editing code
Whenever you want to edit anything **create a branch** for your change:
```
$ git checkout -b <meaningful branch name>
```
and **push** it to the remote repo:
```
$ git push --set-upstream origin <meaningful branch name>
```
Now feel free to make your changes. To upload your changes to remote repo make sure you checked out your branch:
```
$ git checkout <meaningful branch name>
```
**Stage your changes:**
```
$ git add <files_you_want_to_commit>
```
**Commit the changes:**
```
$ git commit -m "<meaningful commit description>"
```
**Push them to remote repo:**
```
$ git push origin <meaningful branch name>
```
## Pull Request
When you consider your branch to be completed create a pull request and mark other contirbutors as code reviewers.
