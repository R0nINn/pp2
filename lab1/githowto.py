# git config --global user.name "Your Name"
# git config --global user.email "your_email@whatever.com"

# git config --global core.autocrlf input
# git config --global core.safecrlf warn

# git config --global core.autocrlf true
# git config --global core.safecrlf warn

# git config --global core.quotepath off

# mkdir hello
# cd hello
# touch hello.html

# Hello, World

# git init

# $ git init
# Initialized empty Git repository in /Users/alex/Documents/Presentations/githowto/auto/hello/.git/

# git add hello.html
# git commit -m "First Commit"

# $ git add hello.html
# $ git commit -m "First Commit"
# [master (root-commit) 911e8c9] First Commit
#  1 files changed, 1 insertions(+), 0 deletions(-)
#  create mode 100644 hello.html

# $ git status
# On branch master
# nothing to commit (working directory clean)

# $ git status
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#   modified:   hello.html
#
# no changes added to commit (use "git add" and/or "git commit -a")

# git add a.html
# git add b.html
# git commit -m "Changes for a and b"

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   modified:   hello.html

# git commit
# Waiting for Emacs...
# [master 569aa96] Added h1 tag
#  1 files changed, 1 insertions(+), 1 deletions(-)

# $ git status
# # On branch master
# nothing to commit (working directory clean)

# <html>
#   <head>
#   </head>
#   <body>
#     <h1>Hello, World!</h1>
#   </body>
# </html>

#$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   modified:   hello.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#   modified:   hello.html

# git commit -m "Added standard HTML page tags"
# git status

# $ git commit -m "Added standard HTML page tags"
# [master 8c32287] Added standard HTML page tags
#  1 files changed, 3 insertions(+), 1 deletions(-)
# $ git status
# # On branch master
# # Changes not staged for commit:
# #   (use "git add <file>..." to update what will be committed)
# #   (use "git checkout -- <file>..." to discard changes in working directory)
# #
# #   modified:   hello.html
# #
# no changes added to commit (use "git add" and/or "git commit -a")

#git add .
#$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   modified:   hello.html
#

# $ git log
# commit fa3c1411aa09441695a9e645d4371e8d749da1dc
# Author: Alexander Shvets <alex@githowto.com>
# Date:   Wed Mar 9 10:27:54 2011 -0500

#     Added HTML header

# commit 8c3228730ed03116815a5cc682e8105e7d981928
# Author: Alexander Shvets <alex@githowto.com>
# Date:   Wed Mar 9 10:27:54 2011 -0500

#     Added standard HTML page tags

# commit 43628f779cb333dd30d78186499f93638107f70b
# Author: Alexander Shvets <alex@githowto.com>
# Date:   Wed Mar 9 10:27:54 2011 -0500

#     Added h1 tag

# commit 911e8c91caeab8d30ad16d56746cbd6eef72dc4c
# Author: Alexander Shvets <alex@githowto.com>
# Date:   Wed Mar 9 10:27:54 2011 -0500

#     First Commit

# git log --pretty=oneline --max-count=2
# git log --pretty=oneline --since='5 minutes ago'
# git log --pretty=oneline --until='5 minutes ago'
# git log --pretty=oneline --author=<your name>
# git log --pretty=oneline --all

# git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short

# $ git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short
# * fa3c141 2011-03-09 | Added HTML header (HEAD, master) [Alexander Shvets]
# * 8c32287 2011-03-09 | Added standard HTML page tags [Alexander Shvets]
# * 43628f7 2011-03-09 | Added h1 tag [Alexander Shvets]
# * 911e8c9 2011-03-09 | First Commit [Alexander Shvets]

# --pretty="..." — определяет формат вывода.
# %h — укороченный хэш коммита
# %d — дополнения коммита («головы» веток или теги)
# %ad — дата коммита
# %s — комментарий
# %an — имя автора
# --graph — отображает дерево коммитов в виде ASCII-графика
# --date=short — сохраняет формат даты коротким и симпатичным

# git config --global alias.co checkout
# git config --global alias.ci commit
# git config --global alias.st status
# git config --global alias.br branch
# git config --global alias.hist "log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short"
# git config --global alias.type 'cat-file -t'
# git config --global alias.dump 'cat-file -p'

# [alias]
#   co = checkout
#   ci = commit
#   st = status
#   br = branch
#   hist = log --pretty=format:\"%h %ad | %s%d [%an]\" --graph --date=short
#   type = cat-file -t
#   dump = cat-file -p

# $ git hist
# * fa3c141 2011-03-09 | Added HTML header (HEAD, master) [Alexander Shvets]
# * 8c32287 2011-03-09 | Added standard HTML page tags [Alexander Shvets]
# * 43628f7 2011-03-09 | Added h1 tag [Alexander Shvets]
# * 911e8c9 2011-03-09 | First Commit [Alexander Shvets]

# $ git checkout 911e8c9
# Note: checking out '911e8c9'.

# You are in 'detached HEAD' state. You can look around, make experimental
# changes and commit them, and you can discard any commits you make in this
# state without impacting any branches by performing another checkout.

# If you want to create a new branch to retain commits you create, you may
# do so (now or later) by using -b with the checkout command again. Example:

#   git checkout -b new_branch_name

# HEAD is now at 911e8c9... First Commit
# $ cat hello.html
# Hello, World

# $ git checkout 911e8c9
# Note: checking out '911e8c9'.

# You are in 'detached HEAD' state. You can look around, make experimental
# changes and commit them, and you can discard any commits you make in this
# state without impacting any branches by performing another checkout.

# If you want to create a new branch to retain commits you create, you may
# do so (now or later) by using -b with the checkout command again. Example:

#   git checkout -b new_branch_name

# HEAD is now at 911e8c9... First Commit
# $ cat hello.html
# Hello, World

# git checkout master
# cat hello.html

# $ git checkout master
# Previous HEAD position was 911e8c9... First Commit
# Switched to branch 'master'
# $ cat hello.html
# <html>
#   <head>
#   </head>
#   <body>
#     <h1>Hello, World!</h1>
#   </body>
# </html>

# git checkout v1^
# cat hello.html
# РЕЗУЛЬТАТ:
# $ git checkout v1^
# Note: checking out 'v1^'.

# You are in 'detached HEAD' state. You can look around, make experimental
# changes and commit them, and you can discard any commits you make in this
# state without impacting any branches by performing another checkout.

# If you want to create a new branch to retain commits you create, you may
# do so (now or later) by using -b with the checkout command again. Example:

#   git checkout -b new_branch_name

# HEAD is now at 8c32287... Added standard HTML page tags
# $ cat hello.html
# <html>
#   <body>
#     <h1>Hello, World!</h1>
#   </body>
# </html>


# git tag
# РЕЗУЛЬТАТ:
# $ git tag
# v1
# v1-beta

# git hist master --all

# $ git hist master --all
# * fa3c141 2011-03-09 | Added HTML header (v1, master) [Alexander Shvets]
# * 8c32287 2011-03-09 | Added standard HTML page tags (HEAD, v1-beta) [Alexander Shvets]
# * 43628f7 2011-03-09 | Added h1 tag [Alexander Shvets]
# * 911e8c9 2011-03-09 | First Commit [Alexander Shvets]

print('helloworld')