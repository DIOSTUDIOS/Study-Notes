---
title: Python 3 学习笔记：面向对象编程
tags: [Python, 面向对象, 属性, 方法]
date: 2019-08-08 16:25:00
---

> 人生苦短，我用 Python

# 概述

面向对象编程（Object Oriented Programming，即 OOP），是一种程序设计思想，比面向过程编程更加灵活，更易扩展。

Python 在设计的时候就是按照面向对象编程的思想设计的，像我们前面学过的各种数据类型，如字符串、列表、字典等都是一个个对象，它们都具有各自的属性和行为。

面向对象编程就是将客观存在的事物，总结提炼出它们各自的属性与行为，然后通过编程的方法形成一个模版（即类），我们就可以根据这个模版创建出一个个实际的、可使用的对象（即类的实例）。

# 特性

## 封装

封装是面向对象编程的核心思想，即将对象具有的，且是我们需要的属性和行为封装起来，编写成一个模版（即类），而在使用的时候只需要事先根据定义好的模版创建出其实例即可，使用过程中无需知道其属性和行为是如何实现的，只需要知道它们能够完成哪些功能即可。

## 继承

举个例子，我们创建一个四边形的类，它具有四条边，四个角这两个特性，计算周长、面积这两个行为；当我们基于这个四边形的类，再创建一个平行四边形的类，则该平行四边形也将自动具有四条边、四个角的特性和计算周长、面积的行为。

继承就是实现重复利用的重要手段，子类可以继承父类的属性和行为。

## 多态

子类继承于父类，那么子类也就拥有了父类的特性和行为，但是因为子类相对于父类而言是一个全新的类，所以它也拥有自己独特的特性和行为，这就是多态。例如，平行四边形继承于四边形，同样拥有四条边和四个角同时，它也有自己的特性，如对边相等，对角相等。

# 类和实例

面向对象编程的思想就是用代码描述客观世界中的物体，但是不可能将每个物体都用代码描述一遍，这不现实，所以引入了类。类就是一系列具有相同特性和行为的物体的集合，描述物体的模版。当我们需要一个该物体的具体实例时，只需要按照这个模版就能创建一个新的物体实例，然后对其进行操作。

## 如何定义类

在 Python 编程中，使用关键字 class 定义类，

```python
class Triangle:
    pass
```

Triangle（三角形）是类的名字。

## 创建类的实例

定义好一个类，并不能供我们直接使用，而是需要创建一个它的实例之后，才可以使用其内部的属性和行为。

就像国家发行钞票，会制作的一个钞票模版，然后根据这个模版印刷出一张张的纸币，这些纸币就是该钞票模版的实例，市场上流通的也是这些纸币，不会是这个钞票模版。所以，当我们要使用这个类的时候，就需要将其实例化，创建一个它的实例，

```python
class Triangle:
    pass

if __name__ == "__main__":
	triangle = Triangle()
```

triangle 就是类 Triangle的实例，也是这个实例的名称。

## \_\_init\_\_() 方法

在 Python 中，如果在定义一个类的时候，不自定义该方法，则编译器会自动帮我们指定一个。但是如果想在创建类的实例的时候，为它的属性赋予一些参数，就需要自定义一个 \_\_init\_\_() 方法。

该方法用于在创建类的实例时，传入必要的属性。它的第一个参数必须是 self ，代表实例本身，

```python
class Triangle:
    def __init__(self, base, height)
    	self.base = base
        self.height = height
        
if __name__ == "__main__":
    triangle = Triangle(4, 5)
```

这样就给 Triangle 这个类定义了一个 \_\_init\_\_() 方法，在创建其实例的时候，必须传入除 self 以外的所有参数。

# 属性

属性指类中的变量，包括类的属性和实例属性，它们定义的位置不同。

## 类的属性

类的属性定义在类中（实例方法之外），所有类的实例都可以访问类的属性。

```python
class Triangle:
	triangle_amount = 0

	def __init__(self, base, height):
		self.base = base
		self.height = height

		Triangle.triangle_amount += 1

if __name__ == "__main__":
	triangle_1 = Triangle(4, 5)
	triangle_2 = Triangle(12, 5)

	print(Triangle.triangle_amount)
	print(triangle_1.triangle_amount)
```

类的属性可以通过类名直接访问，也可以通过类的实例访问。

类的属性不仅仅只能在定义类的时候定义，也可以在类的定义之外动态添加，

```python
class Triangle:
	triangle_amount = 0

	def __init__(self, base, height):
		self.base = base
		self.height = height

		Triangle.triangle_amount += 1

if __name__ == "__main__":
	triangle_1 = Triangle(4, 5)
	triangle_2 = Triangle(12, 5)

	Triangle.triangle_number = "001"

	print(triangle_1.triangle_number)
	print(triangle_2.triangle_number)
```

## 实例属性

实例属性是指在类的方法中定义的属性（变量），只能被类的实例使用。而且，改变一个实例的属性并不会影响其他实例，

```python
class Triangle:
	def __init__(self, base, height):
		self.base = base
		self.height = height

	def print_base(self):
		print(self.base)

	def print_height(self):
		print(self.height)


if __name__ == "__main__":
	triangle_1 = Triangle(12, 5)
	triangle_2 = Triangle(19, 7)

	triangle_1.print_base()
	triangle_1.print_height()

	triangle_1.base = 20
	triangle_1.height = 10

	triangle_1.print_base()
	triangle_1.print_height()

	triangle_2.print_base()
	triangle_2.print_height()
```

在 \_\_init\_\_() 方法中，base 和 height 就是实例属性，当创建 triangle_1 和 triangle_2 两个三角形的时候分别给它们的 base 和 height 属性赋了值。当改变 triangle_1 的属性后，并没有影响 triangle_2 的属性值。

# 方法

每个对象都有其独有的行为，在面向对象编程中把这些行为称为方法，也就是面向过程编程中的函数，但是有些微差别。

方法需要在定义类的时候一起定义，这样类的实例就可以使用这些方法。定义方法和定义函数相似，不过方法必须包含一个 self 参数，且必须放在第一位，

```python
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def compute_area(self)
    	area = self.base * self.height / 2
```

函数用于实现某个独立的功能，而实例方法是实现类（类的实例）的一个特性行为，只有类的实例可以使用它。

# 访问限制

可以在类的外部访问创建类的时候定义的属性和方法，如果我们不想某些属性或方法在类的外部被直接访问（使用），可以给它们加上限制。不受限制的代码如下：

```python
class Triangle:
	description = "我是这个类最原始的描述"

	def __init__(self):
		pass

	def print_base_height(self):
		print("我是这个三角形的底和高")


if __name__ == "__main__":
	print(Triangle.description)

	triangle = Triangle()
	triangle.print_base_height()
```

## 受保护的

以单下划线开头的属性和方法是受保护的（protected）

```python
class Triangle:
	_description = "我是这个类最原始的描述"
	_number = 0

	def __init__(self):
		self._base = "我是底"
		print(self._base)

		pass

	def _print_base_height(self):
		print("我是这个三角形的底和高")


if __name__ == "__main__":
	print(Triangle._description)

	triangle = Triangle()
	triangle._print_base_height()

	print(triangle._base)

	print(str(Triangle._number))
	Triangle._number += 99
	print(str(Triangle._number))
```

## 私有的

以双下划线开头的属性和方法是私有的（private），

```python
class Triangle:
	__description = "我是这个类最原始的描述"
	__number = 0

	def __init__(self):
		self.__base = "我是底"
		print(self.__base)

		pass

	def __print_base_height(self):
		print("我是这个三角形的底和高")

	def modify_description(self):
		print(Triangle.__description)

		Triangle.__description = "我是在类定义之内修改的描述"
		print(Triangle.__description)


if __name__ == "__main__":
	triangle = Triangle()
	triangle.modify_description()

	print(triangle._Triangle__description)
	triangle._Triangle__print_base_height()

	print(str(triangle._Triangle__number))
	triangle._Triangle__number += 99
	print(str(triangle._Triangle__number))
```

通过上面的代码可以看出，通过 ***类的实例名._类名__xxx*** 的方式依然可以访问私有的属性和方法。

所以，在 Python 编程中，访问限制并不能真正的限制你，总是可以通过别的某种方法突破限制，全凭自觉吧。

# @property

通过 @property（装饰器）可以将一个方法转换为一个用于计算的特殊属性，可以通过方法名（无需在方法名后面加上小括号）直接访问该方法，

```python
class Triangle:
	def __init__(self, base, height):
		self.base = base
		self.height = height

	@property
	def compute_area(self):
		return self.base * self.height / 2


if __name__ == "__main__":
	triangle = Triangle(12, 5)
	print(triangle.compute_area)
```

# 继承

继承是面向对象编程的一个重要特性，被继承的类称为父类（或基类），继承父类的类称为子类（或派生类），子类具有父类除了私有属性和方法以外的所有属性和方法。继承使得子类不再需要重新定义父类中已有的属性和方法，只要拿过来直接用就可以了。

```python
class Triangle:
	def __init__(self, base, height):
		self.base = base
		self.height = height

	@property
	def compute_area(self):
		return self.base * self.height / 2

class IsoscelesTriangle(Triangle):
	pass


if __name__ == "__main__":
	isosceless_triangle = IsoscelesTriangle(12, 5)
	print(isosceless_triangle.compute_area)
```

# 多态

如果是仅仅只能继承父类的一切，那和父类还有什么两样？所以，子类除了可以继承父类，还可以根据自己的特点增加自己的特性，修改从父类集成的特性，也就是面向对象编程的多态。

```python
class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	@property
	def area(self):
		return self.length * self.width
	
	@property
	def perimeter(self):
		return (self.length + self.width) * 2

class Square(Rectangle):
	def __init__(self, length, width=0):
		self.length = length
		self.width = width

	@property
	def area(self):
		return self.length ** 2

	@property
	def perimeter(self):
		return self.length * 4
	

if __name__ == "__main__":
	rectangle = Rectangle(12, 5)
	print(str(rectangle.area))
	print(str(rectangle.perimeter))

	square = Square(12)
	print(str(square.area))
	print(str(square.perimeter))
```





------

<script type="text/javascript" src="http://tajs.qq.com/stats?sId=59765948" charset="UTF-8"></script>