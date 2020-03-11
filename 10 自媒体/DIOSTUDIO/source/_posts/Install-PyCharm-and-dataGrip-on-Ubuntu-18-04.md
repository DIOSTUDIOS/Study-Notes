---
title: 在Ubuntu 18.04中安装PyCharm与DataGrip
date: 2018-12-14 20:02:30
tags: [Ubuntu,PyCharm,DataGrip]
---
# 安装环境 #

- Ubuntu 18.04

# 安装步骤 #

## 下载软件 ##

去官网下载两款软件适用于Linux系统的压缩包文件：

PyCharm 官网：[https://www.jetbrains.com/pycharm/download/#section=linux](https://www.jetbrains.com/pycharm/download/#section=linux)

DataGrip 官网：[https://www.jetbrains.com/datagrip/download/#section=linux](https://www.jetbrains.com/datagrip/download/#section=linux)

Ubuntu系统默认下载到当前用户主目录中的【下载】（Download）目录中，将压缩包解压到当前目录中，然后使用 ***mv*** 命令将两个软件的目录移动到 opt 目录中，

	mv /home/amos/下载/pycharm-community-2018.3.1 /opt
	mv /home/amos/下载/datagrip-2018.3 /opt

## 配置快捷启动 ##

### 配置PyCharm快捷启动 ###

使用 ***cd*** 命令进入 /usr/share/applications 目录中，

	cd /usr/share/applications

使用 ***touch*** 命令创建一个名为 pycharm.desktop 的文件，

	touch pycharm.desktop

使用 ***gedit*** 打开这个文件，

	gedit pycharm.desktop

添加如下内容:

	[Desktop Entry]
	Version=1.0
	Type=Application
	Name=PyCharm
	Icon=/opt/pycharm-community-2018.3.1/bin/pycharm.png
	Exec=sh /opt/pycharm-community-2018.3.1/bin/pycharm.sh
	MimeType=application/x-py;
	Name[en_US]=pycharm

### 配置DataGrip快捷启动 ###

使用 ***cd*** 命令进入 /usr/share/applications 目录中，

	cd /usr/share/applications

使用 ***touch*** 命令创建一个名为 datagrip.desktop 的文件，

	touch datagrip.desktop

使用 ***gedit*** 打开这个文件，

	gedit datagrip.desktop

添加如下内容:

	[Desktop Entry]
	Version=1.0
	Type=Application
	Name=DataGrip
	Icon=/opt/DataGrip-2018.3/bin/datagrip.png
	Exec=sh /opt/DataGrip-2018.3/bin/datagrip.sh
	MimeType=application/x-py;
	Name[en_US]=datagrip

# 参考文章 #

[https://blog.csdn.net/qq_15192373/article/details/81091278](https://blog.csdn.net/qq_15192373/article/details/81091278)