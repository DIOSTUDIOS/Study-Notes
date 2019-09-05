---
title: Python 3 学习笔记：目录&文件处理
tags: [python, os, os.path, shutil, zipfile]
date: 2019-08-09 20:34:48
---

> 人生苦短，我用 Python

# 路径

路径，用于定位目录或文件的字符串。

## 相对路径

相对路径依赖于当前工作目录（即当前文件所在的目录），可以使用如下函数获取当前工作目录，

```python
os.getcwd()
```

在当前工作目录中，可以使用相对路径访问这个目录中的所有子目录和其中的文件，而无需使用完整路径。

## 绝对路径

指一个目录或文件的实际路径，如 D:\Code\Python-Study-Notes\exercise\try_except_demo.py，这就是一个绝对路径，无论当前在哪个目录中，只要使用这个路径，就会访问 try_except_demo.py 文件。

可以使用如下函数获取目录或文件的绝对路径，

```python
os.path.abspath(path)
```

其中，参数 path 是一个相对路径，可以是目录，也可以是文件。

## 路径处理

1. 判断指定的目录或文件是否存在

```python
os.path.exists(path)
```

存在则返回 True，反之则返回 False。

2. 拼接目录与目录或文件的名字

```python
os.path.join(path, name)
```

3. 分离文件名和其扩展名

```python
os.path.splitext(fileName)
```

4. 从一个路径中提取最后的目录名或文件名

```python
os.path.basename(path)
```

5. 从一个路径中提取最后一个目录或文件所在的目录

```python
os.path.dirname(path)
```

6. 判断是否为有效路径

```python
os.path.isdir(path)
```

# 目录基本操作

目录，即文件夹，可以存放目录及文件。

1. 获取当前系统类型

```python
os.name
```

其中，nt 表示 Windows；posix 表示 Linux 或 Unix 或 MacOS。

2. 获取当前系统的换行符

```python
os.linesep
```

3. 获取当前系统的路径分隔符

```python
os.sep
```

4. 获取当前的工作目录的路径

```pythin
os.getcwd()
```

6. 已列表的形式返回指定路径下的目录和文件

```python
os.listdir(path)
```

7. 在指定路径下新建一个目录

```python
os.mkdir(path, mode)
```

path 为路径，mode 表示目录的权限（在非 Unix 系统上无效）。

8. 在指定路径下创建多级目录

```python
os.makedirs(path, mode)
```

创建多级目录，即创建它本身及它的子目录和子目录的子目录，mode 表示目录的权限（在非 Unix 系统上无效）。

9. 删除文件

```python
os.remove(path)
```

或者，

```python
os.unlink(path)
```

该函数可以删除指定路径下的文件。

10. 删除一个非空的目录

```python
os.rmdir(path)
```

使用 rmdir() 删除一个目录时，该目录下不能有任何子目录和文件。

11. 删除多级空目录

```python
os.removedirs(path)
```

删除它本身及其中的子目录和子目录中的子目录，但是这些目录中不能有任何文件，即这些目录必须是空的。

12. 把 path 设置为当前的工作目录

```python
os.chdir(path)
```

13. 遍历指定路径下的所有目录和文件

```python\
os.walk(path, topdown=True, onerror, followlinks=False)
```

该函数只在 Unix 和 Windows 系统中有效。

path 表示要遍历的目录；topdown 如果为 True 则自上而下遍历，反之则自下而上；onerror 用于指定错误处理函数；followlinks 用于指定在支持的系统上访问由符号链接指向的目录。

该函数返回一个元组生成器对象，其中包含三个元素：当前遍历的路径，是一个字符串；该路径下包含的目录，是一个列表；当前路径下包含的文件，是一个列表。示例如下：

```python
import os

root = r"D:\Code\YunYiCangQiong\00 原文稿"

for path, dirs, files in os.walk(root,followlinks=True):
	for name in dirs:
		print("○", os.path.join(root, name))
	for name in files:
		print("●", os.path.join(root, name))
```

14. 列出目录下的所有内容（子目录和文件）

```python
os.listdir(path)
```

该函数会列出指定路径的目录下所有内容，包含子目录、文件、隐藏文件等。

# 文件基本操作

在 Python 中，内置了文件（File）对象，在操作文件之间，需要使用 open() 函数打开或创建一个文件，

```python
file = open(fileName, mode, buffering)
```

file 表示被创建的文件对象；fileName 表示要打开或创建的文件名；mode 表示文件的打开模式；buffering 表示读写文件的缓存模式。

其中，mode 的参数如下：

![mode 模式.png](https://i.loli.net/2019/08/09/bzF4cjnpk6gOSwJ.png)

打开文件并对其操作完毕后，要及时关闭该文件，以免造成不必要的损坏。可以使用 close() 函数将文件关闭，

```python
file.close()
```

为了避免忘记关闭文件而对文件造成不必要的损坏，可以使用 with 关键字，该语句可以实现在处理文件时，无论是否出现错误，都保证 with 语句结束后关闭文件。

```python
with expression as target:
    pass
```

expression 是一个表达式，例如使用 open() 函数打开一个文件；target 用于存放 expression 的结果。

当需要向打开的文件中写入内容时，可以使用 write() 函数，

```python
file.write()
```

当使用 write() 函数向文件中写入内容后，只有在使用 close() 函数关闭文件时，才会将写入的内容保存；如果不想立即关闭文件，可以使用 flush() 函数保存写入的内容，

```python
file.flush()
```

如果要读取文件的内容，可以使用 read() 函数，

```python
file.read(size)
```

size 表示要读取的字符的个数，省略则表示读取全部字符。

read() 函数是从头开始读的，如果想要从指定位置开始，则可以使用 seek() 函数移动光标到指定位置，

```python
file.seek(offset, whence)
```

其中，offset 表示光标移动的字符个数；whence 指定字符个数从哪个位置开始计算：0 表示从头开始；1 表示从当前位置开始；2 表示从结尾开始，默认为 0。

可以使用 readline() 函数一行行读取，

```python
file.readline()
```

也可以使用 readlines() 函数读取全部行，

```python
file.readlines()
```

该函数返回一个字符串列表，每个元素为文件的一行内容。

# 高级操作

## shutil 模块

shutil 模块可以复制、移动、重命名和删除目录或文件。

```python
shutil.copy(source, destination)
```

该函数可以将 source 路径下的文件，复制到 destination 路径的目录下，如果目标目录中已存在同名文件，则直接替换；如果 destination 路径中包含文件名，则将被复制的文件重命名为此名称。

如果想要将目录及其中的子目录和文件，全部复制到一个新的目录中，可以使用

```python
shutil.copytree(source, destination)
```

注意，destination 路径下不能包含和 source 路径中目标文件夹的同名目录，否则系统会抛出异常。

如果需要移动目录（包括其中的子目录和文件）或文件，可以使用

```python
shutil.move(source, destination)
```

如果目标文件夹中已经包含同名目录或者文件，则会抛出异常。

os 模块中的 rmdir() 和 removedirs() 都只能删除一个非空的目录，如果想删除一个目录及其中的子目录和文件，可以使用，

```python
shutil.rmtree(path)
```

该函数可以删除指定的目录及其中所有内容（子目录及文件）。

## send2trash 模块

使用 shutil 模块中的函数删除目录即文件是不可恢复的，为了保险起见，可以使用第三方库 send2trash 中的函数做删除动作，它不会完全删除目录或文件，而是将它们放入回收站中，以供反悔。因为它是一个第三方模块，所以使用之前需要使用 pip 工具安装它，并使用 import 语句导入。

```python
send2trash.send2trash(path)
```

## zipfile 模块

### 读取 .zip 文件

该模块可以将多个目录或文件做成一个 ZIP 压缩包，当然也可以解压压缩包。

和 File 文件对象一样，要读取 ZIP 文件的内容，首先需要创建一个 ZipFile 对象，

```python
zipfile.ZipFile(path)
```

该函数返回一个 ZipFile 对象；path 表示一个 .zip 格式的压缩包。

然后，可以使用 namelist() 函数获取压缩包中的文件列表，

```python
ZipFile.namelist()
```

该函数返回一个以压缩包中的文件名作为元素的列表。

可以使用 getinfo() 函数获取文件列表中文件的信息，

```python
ZipFile.getinfo(ZipFile.namelist()[index])
```

该函数需要一个压缩包中的文件作为参数，返回一个 ZipInfo 对象，该对象具有许多可以获取文件信息的属性，如 filename、date_time、file_size 等。

### 解压 .zip 文件

通过 ZipFile 对象的 extractall() 方法可以对压缩包进行解压，

```python
ZipFile.extractall(path)
```

path 可选参数，用于指定解压后的存放路径；如果不指定，则解压中当前路径下。

### 创建 .zip 压缩包

创建压缩包，首先需要使用 ZipFile() 方法新建一个空的压缩包，然后使用 write() 方法将文件添加到压缩包中，

```python
zipfile.ZipFile(name, mode).write(fileName, compress_type=zipfile.ZIP_DEFLATED)
```

name 用于指定压缩包的名称；mode 用于指定压缩包的打开模式；fileName 用于指定要放入压缩包中的文件；compress_type 用于指定压缩算法，一般都是 ZIP_DEFLATED，该算法都大部分类型的文件都有效。

其中，mode 的值可以参考文件基本操作中的值。



------

<div align="center">
    ![自媒平台.jpg](https://i.loli.net/2019/07/29/5d3ea08e5052e51593.jpg)
</div>

