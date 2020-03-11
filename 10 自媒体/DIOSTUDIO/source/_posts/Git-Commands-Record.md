---
title: Git常用命令记录
date: 2016-08-12 20:09:26
tags: [git]
---

通过这段时间对Git的学习与使用，将常用的命令记录如下，以供以后参考

# git status #

查看库的状态，如做了哪些修改，还有哪些修改没有提交到版本库

# git log --oneline #

以一行的形式查看版本日志

# git push [origin] [master] #

将本地版本库推送到远程仓库

# git fetch [origin] [master] #

将远程仓库中与本地仓库存在的差异下载下来，通常代表远程仓库的版本比较新

# git merge [origin] [master] #

将从远程仓库下载下来的差异合并到本地仓库，与上一条命令配合使用

# git remote -v #

查看所有已关联的远程的仓库

# git remote add [repo] [git@git.coding.net:DIOSTUDIO/Coder.git] #

将本地仓库关联到新的远程仓库，例如本地仓库以关联到GitHub，通过这个命令可以再关联到Coding

# git remote rm [repo] #

删除远程库的关联关系

# git branch #

查看所有分支

# git checkout [develop] #

创建develop分支

# git branch [develop] #

切换到develop分支

# git branch -m [master] [develop] #

将master分支重命名为develop


