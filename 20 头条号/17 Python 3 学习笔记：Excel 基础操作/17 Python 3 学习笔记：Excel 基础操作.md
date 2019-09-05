> 人生苦短，我用 Python

# 安装模块

OpenPyXL 模块是一个第三方模块，所以需要使用 pip 工具安装，

```python
pip install openpyxl
```

# 文件结构

首先，我们需要了解一下 Excel 文件的基本结构，一个 Excel 文件被称为一个工作薄，工作薄中可以包含多个工作表（sheet），每个 sheet 由列和行组成，列与行的交叉点被称为单元格，实际数据就是存放在单元格中的。单元格中的数据可以是数字、文本、时间或者公式等等。

# 基本操作

## 创建工作薄

首先，需要从 OpenPyXL 引入 Workbook 类，

```python
from openpyxl import Workbook
```

使用该类可以创建一个 Excel 文件，

```python
workBookObject = Workbook()
```

workBookObject 就是 Workbook 类的实例的名称，也就是一个 Excel 工作薄。

通过 sheetnames 属性获取当前工作薄中的工作表，

```python
workBookobject.sheetnames
```

还可以通过 active 属性获取当前正在操作的工作表，

```python
workBookobject.active
```

## 保存工作薄

创建 Workbook 类的实例之后，其实并没有创建一个真正的 Excel 文件，从一点就可以看出，我们在创建 Workbook 对象时，并没有给它一个实际的文件名，这时候可以通过 save() 方法将工作薄保存成一个实际的 Excel 文件，

```python
workBookobject.save(filename="example.xlsx")
```

该方法会将文件保存到当前目录下。

如果需要将文件保存至指定位置，filename 参数也可以是一个路径，如：

```python
workBookobject.save(filename=r"D:\桌面\example.xlsx")
```

使用 save() 方法保存文件时，要注意如果目录下已经存同名文件，该方法不会做出提示，而是会直接覆盖保存。

## 创建工作表

创建工作薄之后，会默认自动创建一个工作表，我们也可以自己创建一个新的工作表，

```python
workBookobject.create_sheet(sheetName)
```

sheetName 表示新工作表的名称。如果需要将工作表重新命名，可以修改工作表的 title 属性，

```python
workBookobject["oldSheetName"].title = "newSheetName"
```

oldSheetName 即该工作表之前的名字，newSheetName 表示重命名之后的名字。而且可以看出，工作薄可以通过类似索引的方式访问它的工作表，只不过这个“索引”是工作表的名字。

## 复制工作表

如果想创建某个工作表的副本，可以使用下面的方法，

```python
workBookobject.copy_worksheet(sheetName)
```

sheetName 表示该工作薄中一个已经存在的工作表的名字。

## 删除工作表

如果某个工作表不再需要，则可以通过 remove() 方法将其删除，

```python
workBookobject.remove(workBookobject["sheetName"])
```

# 赋值与取值

## 赋值

上面的操作都是针对工作薄及工作表的，但是我们知道在 Excel 文件中，真正的数据都是储存在单元格中的。

在 Excel 文件中，列使用字母表示，行使用数字表示，如果将其视为一个坐标系，则列的值就是 X 轴坐标值，行的值就是 Y 轴坐标值，单元格是列与行的交叉点，所以单元格表示成 A1、F5 等。

给单元格赋值同样可以采用类似索引的方式，首先取得工作表，然后再给其中某个单元格赋值即可，

```python
workBookobject["sheetName"]["cellName"] = value
```

其中，cellName 就是单元格的名称，如 A1、F5 等。

还可以使用 cell() 方法对单元格进行赋值，

```python
workBookobject["sheetName"].cell(column=colNo, row=rowNo, value=value)
```

该方法需要三个参数，即列、行和值。

其中，列比较特殊，虽然在 Excel 文件中，列是由字母表示的，但是在 cell() 方法中，列和行一样都是使用整数表示，从 1 开始。例如，E3 这个单元格的列是 E，但是在 cell() 方法中需要将其赋值为整数 5，如：

```python
workBookobject["sheetName"].cell(column=5, row=3, value="python")
```

## 取值

取值很简单，直接使用单元格的编号即可取出其中的数据，

```python
workBookobject["sheetName"]["cellName"].value
```

cellName 表示单元格的名字，即它的列和行的坐标点，如 A9。单元格除了 value 这个属性，还有 column（列）和 row（行）两个属性，用法同 value 一样。

上面是取一个单元格的值，如果想要取一行中若干个单元格的值，只要在起始的单元格和结束的单元格之间使用冒号（:）分隔即可，

```python
workBookobject["sheetName"]["startCellName":"endCellName"]
```

或者，

```python
workBookobject["sheetName"]["startCellName:endCellName"]
```

得到的结果是一个元组的元组，即二维元组，里层元组的元素是 Cell 类型，如下所示：

```python
(
(<Cell 'Sheet'.A1>,),
(<Cell 'Sheet'.A2>,),
(<Cell 'Sheet'.A3>,),
(<Cell 'Sheet'.A4>,),
(<Cell 'Sheet'.A5>,),
(<Cell 'Sheet'.A6>,),
(<Cell 'Sheet'.A7>,),
(<Cell 'Sheet'.A8>,),
(<Cell 'Sheet'.A9>,)
)
```

所以，访问其中 A3 的值就是，

```python
workBookobject["sheetName"]["A1:A9"][3][0].value
```

同理，如果是多列多行的单元格，同样是一个二维元组，

```python
(
(<Cell 'Sheet'.A1>, <Cell 'Sheet'.B1>, <Cell 'Sheet'.C1>),
(<Cell 'Sheet'.A2>, <Cell 'Sheet'.B2>, <Cell 'Sheet'.C2>),
(<Cell 'Sheet'.A3>, <Cell 'Sheet'.B3>, <Cell 'Sheet'.C3>),
(<Cell 'Sheet'.A4>, <Cell 'Sheet'.B4>, <Cell 'Sheet'.C4>),
(<Cell 'Sheet'.A5>, <Cell 'Sheet'.B5>, <Cell 'Sheet'.C5>),
(<Cell 'Sheet'.A6>, <Cell 'Sheet'.B6>, <Cell 'Sheet'.C6>),
(<Cell 'Sheet'.A7>, <Cell 'Sheet'.B7>, <Cell 'Sheet'.C7>),
(<Cell 'Sheet'.A8>, <Cell 'Sheet'.B8>, <Cell 'Sheet'.C8>),
(<Cell 'Sheet'.A9>, <Cell 'Sheet'.B9>, <Cell 'Sheet'.C9>)
)
```

只不过这里是以列为基准，抛开外层元组不看，里层每个元组的元素都是同一列的单元格。

# 使用公式

在单元格使用公式与在 Office Excel 中操作文件一样，如设置一个 SUM 公式，

```python
workBookobject["sheetName"]["A10"].value = "=SUM(A1:A9)"
```

则单元格 A10 的值就是 A1 到 A9 的和，前提是其中的数据是可以计算的。

但是，openpyxl 不会检查写的 Excel 公式名称及语法是否正确，如果错误不会给出任何提示，但是可以使用 openpyxl.utils 中的 FORMULAE 检查公式名称是否正确，例如，

```python
from openpyxl.utils import FORMULAE


print("SUM" in FORMULAE)
```

如果公式名称返回 True，否则返回 False。

# 加载已有文件

如果需要打开一个已经存在的 Excel 文件，可以先加载该文件，

```python
from openpyxl import load_workbook


workBookobject = load_workbook("example.xlsx")
```

同样可以使用上面的方法对数据进行操作。





------

因头条号文章修改次数有限，而本文一直在持续修改充实的路上，故请各位看官移步个人博客，谢谢！

点击下方 **了解更多** 即可传送到博客。

