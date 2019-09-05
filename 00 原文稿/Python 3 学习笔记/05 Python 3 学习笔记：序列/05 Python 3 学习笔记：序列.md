> 人生苦短，我用 Python

# 序列

## 索引

序列是一块用于放置多个值得连续存储空间，并且按特定顺序排列，每个值（称为元素）都分配一个整数（由左至右则从 0 开始；由右至左则从 -1 开始），称为索引（index）或位置，如下所示：

![2019-07-31_07-33-36.jpg](https://i.loli.net/2019/07/31/5d40d4850226f48654.jpg)

可以根据索引获取每个元素实际的值

``` python
string = "飞流直下三千尺，疑是银河落九天。"
print(string[5])
```

则上面的语句的运行结果为“千”。

## 切片

切片是访问序列中元素的另一种方法，该方法可以访问一定范围内的元素。

``` python
sequence[startIndex : endIndex : step]
```

如果 startIndex 未指定，则默认从 0 开始；如果 endIndex 未指定，则默认一直到最后才结束切片；如果 step 未指定，则默认为 1，且其前面的冒号可以省略。

## 序列相加

在 Python 中支持将多个相同类型的序列相加（或者说拼接更准确），该操作只是单纯的将序列拼接在一起，而不进行其他附加的任何运算。

``` python
seq_1 = "飞流直下三千尺，"
seq_2 = "疑是银河落九天。"
print(seq_1 + seq_2)
```

当然，拼接之后实际上就是得到了一个新的序列，其索引将会重新排序。

## 序列相乘

数学意义上的乘法就是将一个数重复相加若干次之后得到一个结果，序列的乘法同样如此，也是将一个序列重复拼接若干次之后得到一个新的序列。

``` python
sequence = "Hello, Python !"
print(sequence * 3)
```

## in

in 关键字用于检查某个元素是否在被检测的序列中，

``` python
element in sequence
```

在 in 的前面加上 not 关键字，则表示检查某个元素是否不在被检测的序列中，

``` python
element not in sequence
```

如果满足以上两种操作，则返回 True，否则返回 False。

##  len()

len() 方法用于计算序列的长度，即序列中元素的个数，

``` python
len(sequence)
```

## max()

max() 方法用于计算序列中元素的最大值

``` python
max(sequence)
```

我们知道数字可以比较大小，那么序列（如字符串、列表等）是如何比较大小的呢？序列在比较大小的时候，会先将元素按照 ASCII 码表转换成数字，然后再进行比较，这样就可以得出最大值或者最小值了，如：

``` python
seq = "Hello, Python!"
print(max(seq))
```

得到的结果是小写字母 y 。

max() 函数会先将 seq 的所有元素（每个字母、标点）转换成 ASCII码值，然后取出码值最大的元素打印出来。我们常用的字符，如数字、字母等，在 ASCII 码表中的码值大小依次是 **数字<大写字母<小写字母**。当然，ASCII 码表中不只包含数字、字母，其中还有许多标点符号、特殊符号（具体码表请自行查找）。

当然，如果我们想验证 max() 函数得到的结果是否正确，可以使用 ord() 函数获取 seq 中每个元素的 ASCII 码值，

``` python
seq = "Hello, Python!"
lst = []

for n in range(len(seq)):
	lst.append(ord(seq[n]))

print(lst)
```

得到的结果是 [72, 101, 108, 108, 111, 44, 32, 80, 121, 116, 104, 111, 110, 33]，从中可以看出最大值是 121，然后我们再用 chr() 函数看看 ASCII 码值 121 对应的字符是什么，

``` python
print(chr(121))
```

得到的结果也是小写字母 y 。

## min()

min() 函数用于计算序列中元素的最小值，原理同 max() 函数一样。

# 字符串

字符串就是连续的字符序列，可以是计算机能够表示的所有字符的集合。

字符串不可变，在 Python 编程中，因为没有设置字符（char）类型，所以字符串通常使用引号（包括单引号、双引号、三引号）括起来，这三种引号没有本质上的差别，只是单引号、双引号中的内容必须在同一行，而三引号可以在连续的多行上。

## 常用操作

### 拼接字符串

使用 “+” 运算符可以将多个字符串拼接在一起，从而生成一个字符串。

### 重复字符串

使用 ”*“ 运算符可以重复字符串，类似数字的乘法。

### 计算字符串的长度

使用 len() 函数可以获取字符串中字符的个数，

``` python
len(string)
```

其中，string 表示要统计长度的字符串。

en() 函数在计算字符串长度时，不区分符号、数字、英文和汉字，所有字符均按一个字符进行计算。

但是，根据编码方式的不同，字符所占的字节数也不同（这里主要针对汉字，如采用 GBK/GB2312 编码，汉字占 2 个字节；而如果采用 UTF-8/unicode 编码，则汉字占 3 或 4 个字节。在 Python 编程中，数字、英文、符号、下划线和空格均占一个字节）。所以，如果需要取得字符串实际所占的字节数，就需要通过 encode() 方法指定编码格式，例如：

``` python
print(len("提放有度，自在为人；保持前进，以致更好！".encode("utf-8")))

print(len("提放有度，自在为人；保持前进，以致更好！".encode("gbk")))
```

根据运行结果可以看出，同一句话，采用 UTF-8 编码方式每个汉字字符占 3 个字节，而如果采用 GBK 编码方式则每个汉字字符占 2 个字节。

### 截取字符串

截取字符串采用切片的方式实现，

``` python
string[startIndex : endIndex : step]
```

### 分割 & 合并字符串

1. 分割字符串

把字符串按照指定的分隔符分成字符串列表，该列表中的元素不包含分隔符，

``` python
string.split(symbol, maxsplit)
```

其中，symbol 表示分隔符；maxsplit 表示分割次数，如果不指定则不限制次数。

``` python
print("提放有度，自在为人，保持前进，以致更好".split("，"))
```

2. 合并字符串

合并字符串正好与分割相反，是将多个字符串采用固定的分隔符连接在一起，

``` python
string = symbol.join(sequence)
```

例如，

``` python
list = ["小明", "小红", "小刚"]
string = "@".join(list)
print(string)
```

### 检索字符串

在 Python 中提供多种语句查找指定字符串的方法。

1. count()

该方法用于检索指定字符串在另一个字符串中出现的次数，如果不存在则返回 0，否则返回出现的次数，

``` python
string.count(substring, startIndex, endIndex)
```

string 表示被被查找的字符串；substring 表示查找的子串；startIndex 表示起始位置的索引，默认为零；endIndex 表示结束位置的索引，默认为最后一个字符的索引。

``` python
print(["小明", "小红", "小刚"].count("小红"))
```

2. find()

该方法用于检测是否包含指定的子字符串，如果不存在则返回 -1，否则返回首次出现该子字符串的索引，

``` python
string.find(substring, startIndex, endIndex)
```

例如，

``` python
print("小明和小刚一起去小红家里做客".find("小红"))
```

3. in

该关键字用于判断子字符串是否在目标字符串中存在，是则返回 True，否则返回 False，

``` python
substring in string
```

例如，

``` python
if "小红" in ["小明", "小红", "小刚"]:
	print("TRUE")
else:
	print("FALSE")
```

4. index()

index() 和 find() 方法类似，也是用于检测目标字符串是否包含指定的子字符串，但是使用 index() 方法检测时，如果不存在则会抛出异常，

``` python
string.index(substring, startIndex, endIndex)
```

例如，

``` python
print(["小明", "小红", "小刚"].index("小红"))
```

5. startswith()

该方法检测目标字符串是否以指定的子字符串开头，如果是则返回 True，否则返回 False，

``` python
string.startswith(substring, startIndex, endIndex)
```

例如，

``` python
print("小红邀请小明和小刚来家里做客".startswith("小红"))
```

6. endswith()

该方法检测目标字符串是否以指定的子字符串结尾，如果是则返回 True，否则返回 False,

``` python
string.endswith(substring, startIndex, endIndex)
```

### 字母大小写转换

1. lower()

该方法用于将字符串中的大写字母转换为小写字母。

```python
string.lower()
```

2. upper()

该方法用于将字符串中的小写字母转换为大写字母。

``` python
string.upper()
```

### 去除空格 & 特殊字符

1. strip()

该方法用于去除字符串左、右两侧的空格（包括空格、制表符、回车符、换行符等）和特殊字符,

``` python
string.strip(symbol)
```

2. lstrip()

该方法用于去掉字符串左侧的空格和特殊字符

```python
string.lstrip(symbol)
```

3. rstrip()

该方法用于去掉字符串右侧的空格和特殊字符

``` python
string.rstrip(symbol)
```

###　格式化字符串

格式化字符串是指先制定一个模版，在这个模版中预留几个空位，然后再根据需要填上相应的内容。这些空位需要通过指定的符号标记（即占位符），而这些符号还不会显示出来。

1. 使用 % 操作符

``` python
"%[-][+][0][m][.n][symbol]" % strTuple
```

这种方式是 Python 早期提供的方法，自从 Python 2.6 开始，字符串提供了 format() 方法对字符串进行格式化（目前比较推荐这种方式进行格式化字符串），所以这里就不过多学习了。

2. format() 方法

基本语法如下，

``` python
stringTemplate.format(args)
```

stringTemplate 用于指定字符串的显示样式，即模版；args 用于指定替换模版中占位符的实际内容，多个项之间使用逗号分隔。

创建模版时，需要使用大括号和冒号指定占位符，语法如下，

``` python
{index:[fill][align][sign][#][width][.precsion][type]}
```

![format占位符.jpg](https://i.loli.net/2019/08/02/5d443331e9d1967066.jpg)

其中，type 的类型如下：

![format占位符类型.jpg](https://i.loli.net/2019/08/02/5d4433839908172355.jpg)

# 列表

由一系列按特定顺序排列的元素组成，这些元素的类型可以是 Python 中的任何数据类型。列表是 Python 中内置的可变序列，在形式上，是将其所有元素放在中括号（[]）中，两个相邻的元素使用逗号（,）分隔。列表中的元素可以是不同的数据类型，元素与元素之间互相独立，互不干扰。

## 创建列表

只需要给列表指定一个标识符，然后将其元素放入其中即可：

``` python
list = ["hello", "python", 2019, 7, 31]
```

当然，在实际编程过程中，我们也可以先创建一个空列表，然后再需要的时候，在其中放入元素，

``` python
list = []
```

##　删除列表

当我们不在需要某个列表的时候，只需要使用 del 语句即可删除：

``` python
del list
```

## 访问列表元素

因为列表也是序列的一种，所以也可以使用索引、切片的方式获取列表中的元素。

## 操作列表元素

### 添加元素

可以使用 append() 方法向列表的结尾处追加一个元素，

``` python
list.append(element)
```

该方法只能向列表的结尾处追加元素，如果想要向列表的中间插入一个元素，可以使用如下方法，

``` python
list.insert(index, element)
```

insert() 方法会向指定的索引处插入一个元素，原位置的元素及其以后的元素会自动向后退一位，即其原索引加一。

上面的两种方法都是想列表中添加一个单一的元素，如果想要向一个列表中添加另一个列表，则可以使用如下方法，

``` python
list.extend(sequence)
```

该方法会将 sequence 中的元素按原顺序依次追加到 list 的结尾处。

示例代码：

``` python
list = ["hello", "python"]
# append() 方法
list.append(2019)
print(list)
# insert() 方法
list.insert(2, "world")
print(list)
# extend() 方法
sequ = ["天下", "兴亡"]
list.extend(sequ)
print(list)
```

### 修改元素

通过索引定位到要修改的元素，然后直接给其赋值即可，

``` python
list[index] = newValue
```

### 删除元素

1. 通过索引删除

和修改元素相似，定位要删除的元素的索引，然后使用 del 关键字删除即可，

``` python
del list[index]
```

2. 根据元素的值删除

使用列表的 remove() 方法实现，

``` python
list.remove(elementValue)
```

### 对列表进行统计与计算

1. 获取某个元素出现的次数

使用列表的 count() 方法可以获取列表中某个元素的个数，

``` python
list.count(element)
```

2. 获取某个元素首次出现的索引

通过列表的 index() 方法可以获取指定元素在该列表中第一次出现的索引，

``` python
list.index(element)
```

3. 求纯数字列表中元素的和

如果一个列表的元素全部是数字，则可以使用列表的 sum() 方法求其全部元素的和，

``` python
sum(list, addend)
```

其中，addend 为可选参数，默认值 0，如果指定则在列表元素之和的基础上再加上 addend ，如：

``` python
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sum(list))
print(sum(list, 3))
```

### 列表元素排序

1. sort() 方法

该方法用于将列表中的元素按指定方式排序，排序后元素的索引将会改变，

``` python
list.sort(key=None, reverse=False)
```

key 用于指定从每个元素中提取一个用于比较的键；reverse 默认为 False，表示升序排列，如果为 True 则降序排列。

sort() 方法没有返回值，所以只能对列表排序后，输出该列表，

``` python
list = ["hello", "Python", "world", "Welcome", "list"]

list.sort()
print(list)
```

对全部元素均为数字的列表排序很简单，如果是对字符串元素进行排序，则先对大写字母排序，然后再对小写字母进行排序。如果想不区分大小写排序，需要指定 key 参数的值，如 key=str.lower 。

而且，需要注意如果一个列表中的元素既有数字，又有字符串，则无法使用 sort() 方法进行排序。

2. sorted() 函数

在 Python 中，提供了一个内置的 sorted() 函数，用于对列表进行排序，该方法返回一个排序后的列表，而原列表保持不变，

``` python
new_list = sorted(old_list, key=None, reverse=False)
```

其中，参数 key 和 reverse 的作用和 sort() 方法的参数一样，例如：

``` python
old_list = ["hello", "Python", "world", "Welcome", "list"]

new_list = sorted(old_list, key=str.lower, reverse=True)
print(new_list)
```

### 反转列表元素

可以使用列表的方法 reverse() 将列表中的元素反转，

``` python
list.reverse()
```

此方法没有返回值，使用后列表中的元素就会反转调换。

# 元组

元组与列表相似，也是有一系列按特定顺序排列的元素（可以是 Python 中的任意数据类型）组成，但元组是不可变序列，即不能向元组中追加、删除元素。在形式上，元组的所有元素被放入一对小括号中，两个相邻的元素使用逗号分隔，元素之间没有任何关系。由于元组的不可变特性，所以元组一般用于保存程序中不可修改的内容。

## 创建元组

只需要给元组指定一个标识符，然后在其中填充元素即可，

``` python
tuple = ("hello", "python", 2019, 7, 31)
```

我们也可以创建一个空元组，

``` python
tuple = ()
```

在 Python 中，元组也不是一定就会使用小括号括起来，只要将一组元素使用逗号分隔开来，Python 就可以视其为元组，

``` python
tuple = "hello", "python", 2019, 7, 31
```

当我们使用 print() 函数打印该元组时，这些元素将会被小括号括起来。

如果创建一个只有一个元素的元组，则需要在元素后面加一个逗号，否则该元组将会被视为一个字符串，或者其他数据类型。

## 删除元组

因为元组已经创建就不可再改变，所有只能删除元组，而不能删除其中的元素，

``` python
del tuple
```

## 访问元组元素

元素也是一种序列，所以也可以使用索引、切片的方式访问其中的元素。

# 元组与列表的区别

1. 列表属于可变序列，其元素可以被修改或删除；而元组不能，只能整体替换
2. 元组比列表的访问和处理速度快
3. 元组可以作为字典的键，而列表不可以

# 字典

在 Python 中，字典也是可变序列，但是字典没有索引，而是以 **键-值** 对的形式存储数据。字典具有一下特征;

1. 通过 **键** 而不是索引来读取
2. 字典是任意对象的无需集合
3. 字典是可变的，并且可以任意嵌套
4. 字典的 **键** 必须是唯一的
5. 字典的 **键** 必须不可变

## 创建字典

定义字典时，每个元素都包含两个部分 **键** 和 **值** ，它们之间使用冒号分隔，组成一个元素，元素和元素之间使用逗号分隔，

``` python
dictionary = {key_1:value_1, key_2:value_2, ..., key_n:value_n}
```

元组中每个元素的 **键** 必须是唯一的、不可变的，可以是数字、字符串或者元组。元素的 **值** 可以是 Python 中的任何数据类型，且可以不是唯一的。

除了直接创建字典，也可以通过 dict() 和 zip() 函数将列表、元组组合成一个字典，

``` python
dictionary = dict(zip(tuple, list))
```

如果 tuple 和 list 的长度不同，则以短的为基准创建相同长度的字典。

## 删除字典

删除字典同样可以使用 del 关键字，

``` python
del dictionary
```

如果不想删除字典，而只是想删除其中的全部元素，则可以使用 clear() 方法，

``` python
dictionary.clear()
```

## 访问字典元素

因为字典不像列表、元组一样具有索引，所以不能通过索引、切片的方式访问其元素。字典只能通过 **键** 访问其对应的 **值**。

## 操作字典元素

### 添加元素

字典同列表一样是可变序列，所以可以向其中添加元素，只需要指定元素的键和值即可，

``` python
dictionary[key] = value
```

只要新加入的 key 在字典中已存在的**键**中不存在即可。

### 修改元素

修改字典的元素其实就是变相的添加元素，只需要 key 值在字典中已存在，就会将其对应的 value 替换成新的值。

### 删除元素

删除字典中的元素同样可以使用 del 关键字，

``` python
del dictionary[key]
```

将字典元素的 key 删除，其对应的 value 也会被删除，则这个元素在字典中就不存在了。

# 集合

Python 中的集合和数学中的集合相似，也是用于保存不重复元素的，有可变集合和不可变集合两种。在形式上，集合中的元素之间用逗号分隔，所有元素被放在大括号中。集合最好的应用就是去除重复元素，因为集合中的每个元素都是唯一的。

## 创建集合

直接将所有元素放入括号中，然后给定一个标识符即可，

``` python
set = {element_1, element_2, ..., element_n}
```

如果创建集合的时候，不小心输入了若干个重复的元素，Python 会自动只保留一个。

我们也可以使用 set() 函数将列表、元组转换成集合，

``` python
set = set(list/tuple)
```

如果我们想创建一个空集合，也只能使用 set() 方法，而不使用空的大括号（因为空的大括号表示一个空字典）。

## 删除集合

集合同样可以使用 del 关键字删除，

``` python
del set
```

## 操作结合

### 添加元素

可以使用 add() 方法向集合中添加元素，

``` python
set.add(element)
```

### 删除元素

可以使用 pop() 或 remove() 方法删除集合中的元素，或者使用 clear() 方法清空集合中的元素，

``` python
set.pop()
```

pop() 方法会按顺序删除集合中的第一个元素。

``` python
set.remove(element)
```

remove() 方法需要指定要删除的元素，如果该元素不存在，则抛出异常。

``` python
set.clear()
```

clear() 方法会删除集合中的所有元素，使其变为一个空集合。

## 集合运算

### 交集

在 Python 中，求集合的交集使用 & 符号进行运算。

### 并集

在 Python 中，求集合的并集使用 | 符号进行运算。

### 差集

在 Python 中，求集合的差集使用 - 符号进行运算。

### 对称差集

在 Python 中，求集合的对称差集使用 ^ 符号进行运算。

例如，

``` python
set_1 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
set_2 = {1, 2, 3, 4, 5,  6,  7,  8,  9, 10}

print(set_1 & set_2)
print(set_1 | set_2)
print(set_1 - set_2)
print(set_1 ^ set_2)
```

