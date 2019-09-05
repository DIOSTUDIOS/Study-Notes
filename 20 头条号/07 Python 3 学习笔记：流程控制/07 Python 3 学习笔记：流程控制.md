> 人生苦短，我用 Python

# 程序结构

计算机在解决某个具体问题时，主要有三种形式，分别是顺序控制执行所有语句、选择执行部分语句和循环执行部分语句。根据以上三种解决问题的形式，程序设计过程中，也有三种基本结构，分别为顺序结构、选择结构和循环结构。

# 顺序控制

顺序结构很好理解，就是计算机按照程序语句的顺序由上到下依次执，每一条语句都会被忠实的执行，这样就有很大的局限性。如果一个问题可能有多种情况发生，而实际只会发生一种，顺序结构就不能做这一类的选择。

# 选择控制

满足条件即执行，不满足则跳过。

## if ...

if 这个英文单词的中文意思是“如果”，在程序编写中，也就是如果...就...，

```pytho
if expression:
	do some things
```

expression 是一个表达式，这个表达式的结果为真（True），则执行 do somthing；如果为假（False），则跳过 do something 语句块。

## if ... else ...

if 语句给出了满足条件之后应该做什么，而没有给出不满足条件应该做什么。所以，有衍生出了 else 语句，

```python
if expression:
    do some things
else:
    do some things
```

if ... else ... 语句给出了如果 expression 表达式的结果为假（False）时，程序应该做什么事。

## if ... elif ... else...

如果一个问题有多种可能的结果供选择，就需要使用 elif 语句，

```python
if expression 1:
    do some things
elif expression 2:
    do some things
...
else:
    do some things
```

该语句用于从众多可能的选项中挑选一个，也就是如果第一个表达式满足条件，其后的语句就会被执行，然后跳出整个结构，无论 elif 的表达式是否为真（即使以后的 elif 的表达式都为真，其后的语句也不会被执行）。只有在前面所有的表达式都为假时，才会执行 else 后的语句。

# 循环控制

如果满足条件则进入循环体，循环体执行完毕后，再次判断条件是否满足，如果满足则再次进入循环体，反之则执行循环体之后的语句。

## while

while 循环通过一个条件来控制是否要反复执行循环体，

```python
while expression:
    do some things
```

expression 首次为真时，执行循环体，执行完毕之后再次计算 expression ，如果还为真则再次执行循环体；如果为假，则执行循环体之后的语句。

## for

for 循环是一个依次从复执行的循环，通常用于枚举或遍历序列，以及迭代对象中的元素，

```python
for iteration in objects:
    do some things
```

iteration 是一个个从 objects 中取出的可迭代变量，即只要 iteration 存在于 objects 中，则执行循环体。

例如，我们要计算 1 到 100 的累加和，就可以使用 for 循环，

```python
result = 0

for number in range(1, 101):
	result += number

print(result)
```

其中，range() 函数可在一定范围内生成一系列连续的整数，

```python
range(start, end, step)
```

start 用于指定起始值，默认值为 0；end 用于指定结束的值；step 用于指定步长，即连续两个数之间的间隔（它们的差的绝对值），默认值为 1 。

**在 Python 编程中，像 range() 这一类有起始值和结束值得函数，其取值范围都是 *起始值 <= x < 结束值***

当然了，上面的语句我们也可以使用 while 语句实现，

```python
result = 0
number = 1

while number < 101:
	result += number
	number += 1

print(result)
```

for 语句还可以来遍历序列，

```python
list = ["hello", "python", 2019, 8, 1]

for item in list:
	print(item, end="\t")
```

# 嵌套

在一个选择（循环）控制语句中，还有若干个选择（循环）控制语句，被称为选择（循环）嵌套语句，理论上是可以无限嵌套的。

```python
for i in range(1, 10):
	for j in range(1, i+1):
		print(str(j) + "x" + str(i) + "=" + str(j * i) + "\t", end="")
	print()
```

# 跳转语句

## break

break 语句可以终止当前的循环，一般结合 if 语句搭配使用，即在满足特定条件时跳出当前循环，继续执行循环之后的语句。

```python
while expression:
    do some things
    
    if condition:
        break
```

或者，

```python
for iteration in objects:
    do some things
    
    if condition:
        break
```

## continue

continue 语句无法结束循环，只能跳出本次循环，提前执行下一次循环，

```python
while expression:
    do some things
    
    if  condition:
        continue
```

或者，

```python
for iteration in objects:
    do some things
    
    if  condition:
        continue
```

# pass 语句

pass 语句没有实际作用，只起到占位的作用。例如，在 if 结构中，如果满足条件时就执行某系语句，而当还没有想好这些语句如何编写时，可以先使用 pass 占位，保证程序可以正常向下运行，待想好后在替换 pass 即可。



------

因头条号文章修改次数有限，而本文一直在持续修改充实的路上，故请各位看官移步个人博客，谢谢！

点击下方 **了解更多** 即可传送到博客。

