# Прикладная математика
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
## Editing code
Whenever you want to edit anything create a branch for your change:
```
git checkout -b <meaningful branch name>
```
and push it to the remote repo:
```
git push -u origin <meaningful branch name>
```
Now feel free to make your changes. To upload your changes to remote repo make sure you checked out your branch:
```
git checkout <meaningful branch name>
```
Stage your changes:
```
git add <files_you_want_to_commit>
```
Commit the changes:
```
git commit -m "<meaningful commit description>"
```
Push them to remote repo:
```
git push origin <meaningful branch name>
```
## Pull Request
When you consider your branch to be completed create a pull request and mark other contirbutors as code reviewers.
