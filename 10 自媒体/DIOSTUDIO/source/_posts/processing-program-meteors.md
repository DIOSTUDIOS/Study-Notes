---
title: Processing 编程：飞星
tags: [Processing,飞星,编程]
date: 2020-04-12 13:45:50
---

使用 Processing 语言编写的一个飞星，效果及代码如下：

# 效果

![JCIA8215.GIF](https://i.loli.net/2020/04/12/1zYUAnKuf7PrBJk.gif)

# 代码

```processing
class Meteor
{
  //定义飞星的初始位置，移动速度，颜色
  PVector location;
  PVector speed;
  color   colour;
  //构造函数
  Meteor(PVector site)
  {
    //设置初始位置
    location = site;
    //设置颜色
    int colorSeed = (int)random(0, 5);
    
    if (colorSeed==0) colour = color(#05CDE5);
    if (colorSeed==1) colour = color(#FFB803);
    if (colorSeed==2) colour = color(#FF035B);
    if (colorSeed==3) colour = color(#3D3E3E);
    if (colorSeed==4) colour = color(#D60FFF);
    //设置移动速度
    float speedX = random(-0.01, 0.01);
    float speedY = random(-0.01, 0.01);
    
    speed = new PVector(speedX, speedY);
  }
  //显示飞星
  void display()
  {
    fill(colour);
    noStroke();
    ellipse(location.x, location.y, 2, 2);
  }
  //判断飞星是否移动到边界，是则反向移动
  void sweep(float route)
  {
    if (dist(location.x, location.y, 0, 0) > route)
    {
      speed.mult(-1);
      location.add(speed);
    }
    else
    {
      location.add(speed);
    }
  }
}

//飞星数组
ArrayList meteors  = new ArrayList();
//设置飞星间的连线距离
float distance = 60;
//随机设置飞星的个数
int meteorsNumber = (int)random(240, 480);
//设置边界距离
float route = 551;

void setup()
{
  size(960, 540);
  smooth();
  //生成飞星数组，个数位meteorsNumber
  for(int i=0; i<meteorsNumber; i++)
  {
    PVector PD = new PVector(random(-480, 480), random(-480, 480));
    Meteor meteor = new Meteor(PD);
    meteors.add(meteor);
  }
  
  background(0);
}

void draw()
{
  background(0);

  translate(width/2, height/2);
  //陆续显示飞星，并且判断两两之间的距离，如果小于等于distance，则绘制一个三角形并填充颜色
  for(int i=0;i<meteors.size();i++)
  {
    Meteor meteor1 = (Meteor) meteors.get(i);
    meteor1.display();
    meteor1.sweep(route);
    
    for(int j=i+1; j<meteors.size(); j++)
    {
      Meteor meteor2 = (Meteor) meteors.get(j);
      meteor2.sweep(route);
      //判断飞星1和飞星2之间的距离
      if(dist(meteor1.location.x, meteor1.location.y, meteor2.location.x, meteor2.location.y) <= distance)
      {
        for(int k=j+1; k<meteors.size(); k++)
        {
          Meteor meteor3 = (Meteor) meteors.get(k);
          meteor3.sweep(route);
          
          fill(meteor3.colour, 50);
          noStroke();
          //判断飞星2和飞星3之间的距离，绘制三角形并填充颜色
          if(dist(meteor3.location.x, meteor3.location.y, meteor2.location.x, meteor2.location.y) <= distance)
          {
            beginShape();
            vertex(meteor3.location.x, meteor3.location.y);
            vertex(meteor2.location.x, meteor2.location.y);
            vertex(meteor1.location.x, meteor1.location.y);
            endShape();
          }
        }
      }
    }
  }
}
```

