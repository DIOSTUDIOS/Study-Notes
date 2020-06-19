---
title: 如何使用 CadSoft Eagle 制作 Gerber 文件
tags: [CadSoft Eagle, gerber, PCB, Eagle]
date: 2020-06-19 10:59:21
---

**CadSoft Eagle** 是一款简单实用的电路图绘制软件，在开源项目中使用非常广泛。但是，目前在国内还没有成为主流软件之一，所以各大制作 PCB 的厂商都不支持 **CadSoft Eagle** 文件格式的原理图及电路图。

即使你能在淘宝中找到一两家可以使用 **CadSoft Eagle** 电路图制作 PCB 板的店铺，价格往往也是非常贵。所以，本文记录一下如何将 **CadSoft Eagle** 的电路图转为 **Gerber** 文件，从而发送给各大 PCB 制造商制作电路板。

# 钻孔尺寸

![1.jpg](https://i.loli.net/2020/06/19/lg8TRIwyG4XEfJm.jpg)

如图所示，点击 **ULP** 工具，

![2.jpg](https://i.loli.net/2020/06/19/uAxTOyvjXKe2hla.jpg)

选择 **drilcfg.ulp** 文件，导出钻孔尺寸配置文件，

![3.jpg](https://i.loli.net/2020/06/19/zpcbXxsZWk4PVr7.jpg)

选择 inch（英制尺寸），然后点击 **确定** 即可，

![4.jpg](https://i.loli.net/2020/06/19/VdnORpKlfjsLwkI.jpg)

点击 **确定** 即可，将生成的 *drl* 文件保存到你指定的位置

# 生成 Gerber 文件

![5.jpg](https://i.loli.net/2020/06/19/37QD2fiCZVbjdUE.jpg)

点击 **CAM处理器** 图标，打开如图所示的 CAM 处理器界面，

![6.jpg](https://i.loli.net/2020/06/19/AlNypQPfue7E6rC.jpg)

依次点击 **文件** —— **打开** —— **作业**，选择 CAM 处理文件，

![7.jpg](https://i.loli.net/2020/06/19/SRbGYdpqDgrkBQo.jpg)

选择如图所示的文件即可，

![8.jpg](https://i.loli.net/2020/06/19/UFL9N2SyHdBKzrW.jpg)

上图展示的即为将要生成的 **Gerber** 文件，可以在箭头所指的地方设置每层需要生成的内容（如果没有特殊需求，一般不需要修改，我已经使用此配置做了很多次板子了）

![9.jpg](https://i.loli.net/2020/06/19/J4PUCVbjXgQ1B6h.jpg)

如果没有问题，点击 **处理作业** 即可，一般会很快即可生成 Gerber 文件（一般不会显示进度条，我这里使用丝印包含的多边形太多，所以生成文件比较慢）

![10.jpg](https://i.loli.net/2020/06/19/lwBPQWn1ZND9yap.jpg)

文件夹内就是生成好的 **Gerber** 文件

# 查看 Gerber 文件工具推荐

一般查看 **Gerber** 文件的工具，打击肯定都知道主流的就是 **CAM350** 软件，但是因为本人不太喜欢它的界面，所以选择了 **GerbView** 用来查看 **Gerber** 文件。如下图所示，

![11.jpg](https://i.loli.net/2020/06/19/GWPZ9cuRNs8CHSD.jpg)



> 如果需要相关文件的同学可以联系我获取