---
title: Processing 编程：时钟
tags: [Processing,时钟效果,编程]
date: 2020-04-07 07:55:58
---

使用 Processing 语言编写的一个时钟，效果及代码如下，

# 效果

![2020-04-07_08-07-34.gif](https://i.loli.net/2020/04/07/2Kt8gIqVdQ4ZsLG.gif)

# 代码

```processing
import ddf.minim.*;
import ddf.minim.analysis.*;
import ddf.minim.effects.*;
import ddf.minim.signals.*;
import ddf.minim.spi.*;
import ddf.minim.ugens.*;

AudioPlayer player;
Minim minim;

float angle = radians(0);
float speed = 0.009;
int direction = 1;

String hour;
String minute;
String second;

PFont font;

void setup()
{
  size(960, 540);
  background(0);

  smooth();
  
  stroke(255);
  strokeWeight(2);
  
  minim = new Minim(this);
  player = minim.loadFile("sound.mp3", 1024);
  
  font = createFont("Raleway-Bold.ttf", 32);
  textFont(font);
  textAlign(CENTER);
  textSize(64);
}

void draw()
{
  background(0);
  
  hour   = transform(hour());
  minute = transform(minute());
  second = transform(second());
  
  text(hour + ":" + minute + ":" + second, width/2, height/4);
  
  translate(width/2, 200);
  rotate(angle);
  ellipse(0, 300, 50, 50);
  line(0, 0, 0, 300);
  
  angle += speed * direction;
  
  if(angle >= radians(25) || angle <= radians(-25))
  {
    direction = -direction;
    player.rewind();
    player.play();
  }
}

String transform(int number)
{
  String value = "";
  
  if(number < 10)
  {
    value = "0" + number;
  }
  else
  {
    value = str(number);
  }
  
  return value;
}
```

# 资源

程序用到的资源在百度网盘中，可自行下载

链   接: https://pan.baidu.com/s/1rbjVPhUPRCCvG9D98Fh0hg

提取码: tbpc

