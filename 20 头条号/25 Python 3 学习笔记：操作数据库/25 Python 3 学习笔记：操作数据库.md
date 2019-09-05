> 人生苦短，我用 Python

获取数据之后，可以存放在文件中，如 excel 文件和文本文档等，但是对于大量数据还是存放在数据库中比较稳妥，以后查找操作也更稳妥。

使用 Python 操作数据库，有一个通用的模式，

![数据库操作基本步骤.png](https://i.loli.net/2019/08/16/DWFYeBikJIGcyLp.png)

其中，操作数据也就是日常使用的增删查改等操作，高级一些就是创建视图、触发器等等，再高级我觉得还是使用 DBMS 直接操作数据库比较好。

# SQLite

SQLite 属于一种文件型的数据库，非常小巧，可以嵌入各种程序中。Python 内置了 SQLite，无需安装其他模块即可使用。

## 创建连接

首先，需要导入 sqlite 模块，

```python
import sqlite3
```

然后，使用 connect() 方法连接一个数据库，如果该数据库不存在，将会被创建，

```python
db_link = sqlite3.connect('dbName.db')
```

这里创建了一个名为 dbName.db 的数据库。

## 创建游标

游标对象，代表数据库中的游标，用于指示抓取数据操作的上下文，主要提供执行 SQL 语句、调用存储过程、获取查询结果等方法，

```python
db_csor = db_link.cursor()
```

创建了游标对象之后，就可以使用 SQL 语句操作数据库了。

## 操作数据

操作数据库使用 SQL 语言，通过 execute() 方法提交，

```python
db_csor.execute('SQL statement')
```

## 提交操作

当使用 execute() 方法操作数据库后，如果数据出现了变化，如增加、修改、删除等，需要使用 commit() 方法提交，否则此类操作不会生效，

```python
db_link.commit()
```

## 回滚操作

如果我们不知道写的语句是否正确，可以使用 try ... except 语句进行调试，我们同样可以使用异常调试语句对数据库进行回滚操作，以免程序出错时影响数据库中的数据，

```python
try:
    db_link.commit()
except:
    db_link.rollback()
```

## 断开连接

断开连接分为两步：第一步是断开游标的连接，

```python
db_csor.close()
```

第二步是断开数据库的连接，

```python
db_link.close()
```

这两步均使用 close() 方法。

及时断开连接是非常有必要的，一方面是及时释放数据库资源，减少负荷；另一方面是避免造成对数据库的错误操作，影响数据的正确性。

# MySQL

MySQL 是一款开源的、免费的关系型数据库系统，也是目前市场上使用人数最多的一款数据库。在 Python 编程中，需要通过第三方模块才能操作 MySQL 数据库。

## 安装 PyMySQL

PyMySQL 是一款第三方库，需要使用 pip 工具进行安装，

```python
pip install PyMySQL
```

该模块同样是按照 Python Database API 2.0 规范进行设计编写的，所以它操作 MySQL 数据库的方法和 SQLite 类似。

## 创建连接

PyMySQL 模块中同样有一个 connect() 方法用于连接数据库，但是因为 MySQL 是一款通过网络进行访问的数据库系统，所以有几个必须的参数，

```python
db_link = pymysql.connect(host, username, password, database)
```

host 表示装有 MySQL 数据库服务的服务器名或 IP 地址；username 表示用户名；password 表示密码；database 表示数据库的名称。

## 创建游标

PyMySQL 模块中同样有一个 cursor() 方法用于创建游标，

```python
db_csor = db_link.cursor()
```

## 操作数据

在 PyMySQL 中同样有一个 execute() 方法用于提交 SQL，

```python
db_csor.execute()
```

该方法与 SQLite 中的一样，对于不会修改数据的语句直接使用即可，无需提交。

## 提交数据

如果编写的 SQL 对数据库中的数据进行了修改，这是就需要一个提交的动作，

```python
db_link.commit()
```

## 回滚操作

同样可以使用模块中的 rollback() 方法进行数据回滚，

```python
db_link.rollback()
```

## 断开连接

同样，为了数据的安全，执行完操作之后，需要断开连接，

```python
db_csor.close()
db_link.close()
```

虽然，PyMySQL 是一个第三方模块，但是因为它也是按照 Python Database API 规范编写的，所以很多方法和 Python 中操作 SQLite 的方法一样。



------

因头条号文章修改次数有限，而本文一直在持续修改充实的路上，故请各位看官移步个人博客，谢谢！

点击下方 **了解更多** 即可传送到博客。

