> 人生苦短，我用 Python

# 什么是异常

程序运行过程中，产生的错误统称为异常（bug）。这些异常有的可能是语法错误，如关键字输入错误、调用错误等，这一类的异常都是显式的，很好发现；还有一种就是隐式的错误，只用在使用时才会被发现，和使用者的操作有关。

下面介绍一下 Python 常见的异常提示：

![异常类型.jpg](https://i.loli.net/2019/08/04/L5j3dq4Cwf8UgJX.jpg)

# 异常处理语句

1. try ... except ...

在使用时，将可能产生异常的代码放在 try 语句中，把处理结果放在 except 语句中，这样，当 try 后面的代码发生错误时就会执行 except 中的代码。如果 try 后的代码没有异常，则不会执行 except 后的代码。

``` python
try:
    do some things
except exceptionName:
    do some things
```

exceptionName 用于指定可能出现的异常的名称。如果不指定异常的名称，则表示捕获全部可能发生的异常。

示例代码：

``` python
def division():
	print("====== 开始分苹果 ======")

	apple = int(input("一共有几个大苹果："))
	child = int(input("一共有几个小朋友："))

	result = apple // child
	remain = apple % child

	if remain > 0:
		print("一共 {:d} 个大苹果平均分给 {:d} 个小朋友，每人 {:d} 个，剩余 {:d} 个。".format(apple, child, result, remain))
	else:
		print("一共 {:d} 个大苹果平均分给 {:d} 个小朋友，每人 {:d} 个。".format(apple, child, result))


if __name__ == "__main__":
	try:
		division()
	except ZeroDivisionError:
		print("苹果不能被 0 个小朋友平分！！！")
```

在捕获异常的时候，可以同时捕获多个异常，如：

``` python
try:
    do some things
except(ValueError, ZeroDivisionError) as e:
    do some things
```

2. try ... except ... else

该语句在 except 之后加了一个 else 语句，用于指定当 try 语句没有发现异常时需要执行的代码，如果 try 语句中发现了异常，则不再执行 else 之后的代码。

``` python
try:
    do some things
except exceptionName:
    do some things
else:
    do some things
```

示例代码：

``` python
def division():
	print("====== 开始分苹果 ======")

	apple = int(input("一共有几个大苹果："))
	child = int(input("一共有几个小朋友："))

	result = apple // child
	remain = apple % child

	if remain > 0:
		print("一共 {:d} 个大苹果平均分给 {:d} 个小朋友，每人 {:d} 个，剩余 {:d} 个。".format(apple, child, result, remain))
	else:
		print("一共 {:d} 个大苹果平均分给 {:d} 个小朋友，每人 {:d} 个。".format(apple, child, result))


if __name__ == "__main__":
	try:
		division()
	except ZeroDivisionError:
		print("苹果不能被 0 个小朋友平分！！！")
	except ValueError as e:
		print("输入错误！！！", e)
	else:
		print("苹果分配成功。。。")
```

3. try ... except ... finally

无论 try 语句中是否发生异常，都会执行 finally 之后的代码。

``` python
try:
    do some things
except exceptionName:
    do some things
finally:
    do some things
```

示例代码：

``` python
def division():
	print("====== 开始分苹果 ======")

	apple = int(input("一共有几个大苹果："))
	child = int(input("一共有几个小朋友："))

	result = apple // child
	remain = apple % child

	if remain > 0:
		print("一共 {:d} 个大苹果平均分给 {:d} 个小朋友，每人 {:d} 个，剩余 {:d} 个。".format(apple, child, result, remain))
	else:
		print("一共 {:d} 个大苹果平均分给 {:d} 个小朋友，每人 {:d} 个。".format(apple, child, result))


if __name__ == "__main__":
	try:
		division()
	except ZeroDivisionError:
		print("苹果不能被 0 个小朋友平分！！！")
	except ValueError as e:
		print("输入错误！！！", e)
	else:
		print("苹果分配成功。。。")
	finally:
		print("分配了一次苹果。")
```

4. raise

如果某个函数可能会产生异常，但是不想在当前函数中处理该异常，则可以使用 raise 语句在函数中抛出异常，

``` python
raise [exceptionName[(reason)]]
```

其中，exceptionName[(reason)] 为可选参数，用于指定抛出的异常名称及异常信息的描述，如果省略则把异常原样抛出。

示例代码：

``` python
def division():
	print("====== 开始分苹果 ======")

	apple = int(input("一共有几个大苹果："))
	child = int(input("一共有几个小朋友："))

	if apple < child:
		raise ValueError("苹果太少了不够分！")

	result = apple // child
	remain = apple % child

	if remain > 0:
		print("一共 {:d} 个大苹果平均分给 {:d} 个小朋友，每人 {:d} 个，剩余 {:d} 个。".format(apple, child, result, remain))
	else:
		print("一共 {:d} 个大苹果平均分给 {:d} 个小朋友，每人 {:d} 个。".format(apple, child, result))


if __name__ == "__main__":
	try:
		division()
	except ZeroDivisionError:
		print("苹果不能被 0 个小朋友平分！！！")
	except ValueError as e:
		print("输入错误！！！", e)
	else:
		print("苹果分配成功。。。")
	finally:
		print("分配了一次苹果。")
```

# 程序测试

## 使用 IDE 调试

基本上所有的 IDE 都具有代码调试功能，如 Python 自带的 IDLE 和 PyCharm 等等。一般都是在出现异常的地方设置断点，然后在此处查看数据的值是否正确。具体的内容我也在学习过程中，没有可以调试的代码，以后如果有资料了在进行补充。

## 使用 assert 语句调试

该语句一般用于对程序在某个时刻必须满足的条件进行验证，

``` python
assert expression [reason]
```

其中，expression 是一个条件表达式，如果为假则抛出 AssertError 异常，反之则什么都不做。reason 为可选参数，用于描述前面的 expression 为了更好的知道哪里出现了错误。

示例代码：

``` python
def division():
	print("====== 开始分苹果 ======")

	apple = int(input("一共有几个大苹果："))
	child = int(input("一共有几个小朋友："))

	assert apple > child, "苹果不够分。"

	result = apple // child
	remain = apple % child

	if remain > 0:
		print("一共 {:d} 个大苹果平均分给 {:d} 个小朋友，每人 {:d} 个，剩余 {:d} 个。".format(apple, child, result, remain))
	else:
		print("一共 {:d} 个大苹果平均分给 {:d} 个小朋友，每人 {:d} 个。".format(apple, child, result))


if __name__ == "__main__":
	try:
		division()
	except ZeroDivisionError:
		print("苹果不能被 0 个小朋友平分！！！")
	except ValueError as e:
		print("输入错误！！！", e)
	else:
		print("苹果分配成功。。。")
	finally:
		print("分配了一次苹果。")
```

