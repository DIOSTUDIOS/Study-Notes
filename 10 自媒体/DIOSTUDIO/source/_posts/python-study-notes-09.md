---
title: Python 3 学习笔记：函数
tags: [Python, 函数, 变量, 可变参数]
date: 2019-08-02 19:18:21
---

> 人生苦短，我用 Python

函数可以理解成实现某一功能的一系列代码的集合，这样做有一个最明显的好处就是，如果我们需要反复使用某个功能，使用函数只需要写一遍这些语句，然后就可以在程序中调用这个函数，而不再需要重新写一遍这些语句。

# 创建 & 调用

## 创建函数

创建函数使用 def 关键字实现，

```python
def function_name(parameters):
    do some things
```

function_name 是函数的名称（标识符），调用函数时使用；parameters 是该函数的参数（如果有多个，则使用逗号分隔），如果被指定，则调用函数是也需要传入对应的实际数据；如果该参数不需要参数，则此处为空，调用时也无需传入数据。

## 调用函数

调用函数很简单，只需要在调用的位置写上函数的名称，传入其需要的参数即可，

```python
function_name(parameters)
```

# 参数

函数主要就是用来接收数据，然后利用函数内的代码将数据加工成我们需要的内容，那如何将数据传入函数内部供其使用呢？这就是参数的功能，参数用来接收需要传入函数的数据，然后对这些参数加工处理。

## 形参 & 实参

形参，在函数被定义时指定；实参，在函数被使用时指定。

函数是我们自己编写的，所以我们明确的知道这个函数可以做什么，实现功能时需要哪些数据，所以在定义函数时写在小括号内的参数就是形参，用于指定该函数可以接收、处理哪些数据。当我们使用这个函数的时候，就需要按照它的要求传入它需要的数据，这个数据就是实参。

```python
def summation(x, y):
    z = x + y
    print(str(x) + "+" + str(y) + "=" + str(z))
    
summation(2, 5)
```

在上面这个函数中，x 和 y 就是形参，而 2 和 5 就是实参。

## 位置参数

位置参数也被称为必备参数，其必须按照正确的顺序传递到函数内，即调用时的数量和位置必须和定义时一样。

1. **数量**必须和定义时一致
2. **位置**必须和定义时一致

```python
def computeBMI(person, height, weight):
	bmi = weight / ((height / 100) ** 2)

	print(person + "的身高为：" + str(height) + "厘米")
	print(person + "的体重为：" + str(weight) + "千克")
	print(person + "的指数为：" + str(bmi)    + "kg/m2")

# 正常调用
computeBMI("小明", 183, 74)
# 错误调用
computeBMI(183, "小明", 74)
```

## 关键字参数

该参数形式是指使用形参的标识符来确定输入的参数值，通过该方法指定实参的时候不再需要与形参的位置完全一致，只要将参数名写正确即可。这样可以避免需要牢记参数位置的麻烦，使得函数的调用和参数传递更加灵活。

```python
def computeBMI(person, height, weight):
	bmi = weight / ((height / 100) ** 2)

	print(person + "的身高为：" + str(height) + "厘米")
	print(person + "的体重为：" + str(weight) + "千克")
	print(person + "的指数为：" + str(bmi)    + "kg/m2")

computeBMI(height=183, person="小明", weight=74)
```

## 默认值参数

在调用函数时，如果没有为其中的参数赋值将会抛出异常，为了解决此类问题，可以为参数设置默认值，即在定义函数时，给形参指定一个默认值。这样，即使调用时没有传入该参数的实际值，也不会报错，程序会自动使用定义时设置的默认值。

为形参设置默认值时，该值必须是一个不可变对象，如数字、字符串、元祖等。

```python
def function(parameter=defaultvalue):
    pass
```

示例，

```python
def computeBMI(height, weight, person="路人"):
	bmi = weight / ((height / 100) ** 2)

	print(person + "的身高为：" + str(height) + "厘米")
	print(person + "的体重为：" + str(weight) + "千克")
	print(person + "的指数为：" + str(bmi)    + "kg/m2")

computeBMI(height=183, person="小明", weight=74)
print()
computeBMI(174, 64)
```

给形参设置默认值时，该形参必须放在最后，否则会抛出异常。

在 Python 中，可以使用函数的 \_\_defaults\_\_ 查看该函数参数的默认值。

## 可变参数

可变参数也被称为不定长参数，即传入函数中的实际参数可以是任意个。定义可变参数时，主要有两种形式： *parameter 和 **parameter 。

1. *parameter

该形式表示接收任意多个实参，然后将它们放入一个元组中，

```python
def computeBMI(*persons):
	for person in persons:
		for item in person:
			person = item[0]
			height = item[1]
			weight = item[2]

			bmi = weight / ((height / 100) ** 2)

			print("{:s} 的身高为：{:d} 厘米".format(person, height))
			print("{:s} 的体重为：{:d} 千克".format(person, weight))
			print("{:s} 的指数为：{:f} kg/m2".format(person, bmi))

			print()

persons = [("小明", 183, 74), ("小红", 167, 55), ("小刚", 174, 69)]
computeBMI(persons)
```

2. **parameter

该形式表示接收任意多个类似关键字参数一样显式赋值的实际参数，并将其放入一个字典中，

```python
def show_constellaiton(**persons):
	for person, constellation in persons.items():
		print("{:s} 的星座是： {:s}".format(person, constellation))

persons = {"小明":"射手座", "小红":"水瓶座", "小刚":"天蝎座"}
show_constellaiton(**persons)
```

使用这两种可变参数形式时，如果将一个已经存在的列表（或元组）、字典作为可变参数传入函数，都需要在其前方加上一个或者两个星号（*），否则会抛出异常。

# 返回值

函数最重要的功能就是将输入的参数经过其内容代码处理后，得出一个结果用于展示，或者作为参数再传入其他函数进行处理，那我们怎么才能获得函数的处理结果呢？返回值就是用来满足这个需求的。

在 Python 中，使用 return 关键字返回函数的处理结果，即返回值。返回值可以是任何 Python 支持的数据类型，而且无论 return 语句出现在函数的什么位置，只要被运行就会直接结束该函数，无论其后还有多少代码没有被执行。

```python
def function(parameters):
    return values
```

# lambda（匿名函数）

我们知道定义一个函数，需要给它一个标识符，以便可以在需要的地方调用它。而匿名函数就是一种没有名字（标识符）的函数，此类函数只能在定义它的地方使用一次，而不能在其他地方被调用。其语法格式如下，

```python
value = lambda parameters : expression
```

parameters 为匿名函数的参数，可以是多个，之间用逗号分隔；expression 是处理参数的表达式，只能进行简单的计算，如算数运算、逻辑运算等，不能使用流程控制语句，如 if、for、while等；value 用于接函数处理的结果，即接收函数的返回值。

示例：

```python
import math

circle_area = lambda r : math.pi * r * r
print(circle_area(10))

rect_area = lambda a, b : a * b
print(rect_area(10, 23))
```

# 变量及其作用域

变量，可以理解为实际数据的名字，或者标签。将实际数据赋值给一个变量，这样就可以在需要的时候通过变量调用它，而不用每次使用时都将这个实际数据写一遍。例如，当说到《兰亭集序》时，我们就知道是一篇王羲之写的行书作品，而不用将其全文内容都说出来之后，才会知道你说的是《兰亭集序》。“兰亭集序”这个四个字就可以理解为“永和九年，岁在癸丑，暮春之初……”。

在 Python 中，无需事先声明变量的数据类型，直接赋值即可创建各种类型的变量，变量的名称需要遵循 Python 中标识符的明明规范。

变量的作用域是指其在程序中可被使用的范围，如果超出该变量的可使用范围，则会出现错误。

## 局部变量

局部变量是指在函数内部定义、使用的变量，只能在定义它的函数内部使用。局部变量只会在函数运行时被创建、使用，函数运行之前或者之后，该变量就不再存在了。

## 全局变量

全局变量是能够在函数内外均可使用的变量，全局变量主要有以下两种情况：

1. 一个变量在函数外定义
2. 在函数中使用 global 关键字定义

------

<script type="text/javascript" src="http://tajs.qq.com/stats?sId=59765948" charset="UTF-8"></script>