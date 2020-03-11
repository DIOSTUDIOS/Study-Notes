---
title: Python 3 学习笔记：操作 MongoDB
tags: [Python, MongoDB, find(), update(), delete()]
date: 2019-08-30 11:30:06
---

> 人生苦短，我用 Python

# MongoDB

在 Python 编程中，需要通过一个第三方库——PyMongo 来连接 MongoDB 数据库，使用 pip 工具安装，然后在 Python 程序中导入即可使用。

```python
import pymongo
```

在使用 MongoDB 数据库之前，需要创建一个连接，

```python
mg_linker = pymongo.MongoClient(host='localhost', port=27017)
```

其中，host 参数表示安装 MongoDB 的主机名或 IP 地址，port 是 MongoDB 数据库服务使用的端口号，默认值为 27017（如果是默认值可以省略）

## 创建/连接数据库

创建了连接之后，就可以通过这个连接创建一个新的数据库或者连接已有的数据库了，

```python
mg_databs = mg_linker['student_information']
```

student_information 就是要连接的数据库，如果没有则会创建一个同名的数据库。

## 创建/打开数据表

连接数据库之后，就可以打开一个数据表了，

```python
mg_gather = mg_databs['report']
```

report 是数据库中的一张表，如果不存在则会创建一张同名的数据表。

***注意：在插入实际的数据之前，新建的数据库及表只是理论上的，即只有在插入数据之后，数据库和表才会被创建***

## 操作数据

MongoDB 是非关系型数据库，它不需要事先定义表结构，然后才能插入数据。其中的数据是以  key-value 的形式存储的，就像 json 格式的数据或 Python 中的字典的形式。如果将其以关系型数据库中表的形式展现，则同一个 key 被当做同一列，每个 value 就是行数据。

### 插入

1. insert_one()

使用 insert_one() 方法可以插入一条数据，

```python
datum = {"name": "Amos", "Chinese": 97, "Math": 100, "English": 95}

mg_gather.insert_one(datum)
```

2. insert_many()

如果需要插入多条数据，可以先构建一个字典的列表，然后使用 insert_many() 方法，

```python
data = [
	{"name": "Lucy",   "Chinese": 99, "Math": 95,  "English": 90},
	{"name": "Lily",   "Chinese": 87, "Math": 58,  "English": 59},
	{"name": "James",  "Chinese": 58, "Math": 20,  "English": 26},
	{"name": "Jack",   "Chinese": 60, "Math": 78,  "English": 32},
	{"name": "Thomas", "Chinese": 42, "Math": 100, "English": 99},
]

mg_gather.insert_many(data)
```

通过 MongoDB 的可视化工具 MongoDB Compass Community 以列表的形式查看数据时，可以看出相同的 key 可以被视为一个列名，

![MongoDB列表形式展示数据.jpg](https://i.loli.net/2019/08/29/ehoL7nvXuNG9cki.jpg)

插入数据时 MongoDB 会给每个数据自动创建一个 _id 作为主键，我们也可以在插入数据的时候自己指定，只要确保 _id 的值是唯一的即可。

### 删除

1. delete_one()

使用 delete_one() 方法可以删除第一条符合条件的数据，

```python
mg_gather.delete_one({"name": "Amos"})
```

该方法每次只能删除第一条符合条件的数据.

以 Oracle 为例，其可以等价于以下 PL/SQL 语句，

```plsql
DELETE FORM report WHERE name='Amos' and ROWID=(SELECT MIN(ROWID) FROM report)
```

2. delete_many()

通过 delete_many() 方法可以删除所有符合条件的数据，

```python
mg_gather.delete_many({"name": "Amos"})
```

其可以等价于以下 PL/SQL 语句，

```plsql
DELETE FORM report WHERE name='Amos'
```

如果不传入参数，则会删除表中所有数据。

3. drop()

drop() 方法用于删除表，

```python
mg_gather.drop()
```

### 查找

1. find_one()

该方法返回第一条符合条件的数据，

```python
mg_gather.find_one({"name": "Amos"})
```

如果不加条件，则会返回表中的第一条数据。

2. find()

该函数可以返回一个所有符合条件的数据的集合，

```python
mg_gather.find({"name": "Amos"})
```

可以使用 for 循环读取每条数据。如果不加条件，则返回所有数据的集合，

```python
mg_gather.find({})
```

如果没有查询条件，其中的大括号可以省略。

如果只需要查询某几个字段，则可以在条件后入输入需要显示的 key，并将其设置为 True；如果不想显示某些 key，则将其设置为 False（注意：该条件中不能同时出现 True 和 False，即只需要将需要显示的设置为 True，或者不需要显示的设置为 False 即可），

```python
mg_gather.find({},{"_id": False, "Math": True})
```

从上面的代码中可以看到，将 _id 设置成了 False，而 Math 却是 True，这样是被允许的，而且也只有这种设置是被允许的，即只有 _id 可以被设置为与其他对象相反的值。

find() 方法中除了可以使用类似 SQL 中 *where field=condition* 语句的之外，也可以使用大于、小于等语句，如：

```python
# 大于
mg_gather.find({"Math": {"$gt": 90}})
# 小于
mg_gather.find({"Math": {"$lt": 90}})
```

其他比较符号如下所示：

![比较符号.jpg](https://i.loli.net/2019/08/30/tYSw4MBh75rK8eX.jpg)

SQL 中的 like 语句可以使用正则表达式实现，

```python
mg_gather.find({"name": {"$regex": "os$"}})
```

上面的语句就是查询 name 字段中以 **os** 结尾的值。

3. limit()

该方法配合 find() 使用，用于返回指定数量的数据，

```python
mg_gather.find().limit(3)
```

此方法只有一个数字参数，用于指定返回的数据的数量。

4. count()

该方法可以返回符合条件的数据的数量，

```python
mg_gather.find().count()
```

### 修改

1. update_one()

该方法可以修改符合条件的第一条数据的值，

```python
mg_gather.update_one({"name": "Amos"}, {"$set": {"Math": 60}})
```

上面的语句将 name=Amos 的第一条数据的 Math 修改成了 60。

2. update_many()

该方法用于将所有符合条件的数据修改成目标数据，

```python
mg_gather.update_many({"name": "Amos"}, {"$set": {"Math": 0}})
```

### 排序

sort() 方法用于按需要排序，需要两个参数，第一个参数用于指定排序的字段，第二个参数用于指定升序还是降序，

```python
result = mg_gather.find().sort("name", -1)
```

其中，第二个参数为 1 时表示升序，-1 表示降序，默认值为 1。





------

<script type="text/javascript" src="http://tajs.qq.com/stats?sId=59765948" charset="UTF-8"></script>