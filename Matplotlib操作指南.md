Matplotlib操作指南

```
-- matplotlib.pyplot模块
>> import matplotlib.pyplot as plt
-- %matplotlib具体作用
是当你调用matplotlib.pyplot的绘图函数plot()进行绘图的时候，或者生成一个figure画布的时候，可以直接在你的python console里面生成图像。

作者：hplllrhp
链接：https://www.jianshu.com/p/2dda5bb8ce7d
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
-- 图形绘制流程：
1.创建画布 -- plt.figure()
>> plt.figure(figsize=(), dpi=)
    figsize:指定图的长宽
    dpi:图像的清晰度
    返回fig对象
2.绘制图像 -- plt.plot(x, y)
3.显示图像 -- plt.show()

-- 中文显示问题解决
下载中文字体（黑体，看准系统版本）
步骤一：下载 SimHei 字体（或者其他的支持中文显示的字体也行）
步骤二：安装字体
1，linux下：拷贝字体到 usr/share/fonts 下：
sudo cp ~/SimHei.ttf /usr/share/fonts/SimHei.ttf,
2,windows和mac下：双击安装
步骤三：删除~/.matplotlib中的缓存文件
cd ~/.matplotlib
rm -r *
步骤四：修改配置文件matplotlibrc
vi ~/.matplotlib/matplotlibrc
将文件内容修改为：
font.family         : sans-serif
font.sans-serif         : SimHei
axes.unicode_minus  : False


-- 基础绘图功能
1 添加自定义x,y刻度
通过fontsize参数可以修改图像中刻度字体的大小
注意:在传递进去的第一个参数必须是数字,不能是字符串,如果是字符串,需要进行替换操作
>> plt.xticks(x, **kwargs,fontsize=xx)
x:要显示的刻度值
>> plt.yticks(y, **kwargs,fontsize=xx)
y:要显示的刻度值
-- 示例：
import matplotlib.pyplot as plt
import random
x = range(60)
# 0-59,60个数
y_shanghai = [random.uniform(15,18) for i in x]
# 15-18,60个平均随机数
x_ticks_label = ['11时{}分'.format(i) for i in x]
# 11时0分-11时59分，60个数
y_ticks = range(40)
plt.figure(figsize=(10,8),dpi=100)
plt.plot(x,y_shanghai)
plt.xticks(x[::5],x_ticks_label[::5])
# 步长为5，取满为止
# 如果只写x_ticks_label[::5]，会报错，因为是字符串类型；可以先用x[::5]占位，再用x_ticks_label[::5]替换；
plt.yticks(y_ticks[::5])
plt.show()


2 添加网格显示
>> plt.grid(True, linestyle='--', alpha=0.5)
# True 可以省略，linestyle 线型，alpha 透明度

3 添加描述信息
添加x轴、y轴描述信息及标题
通过fontsize参数可以修改图像中字体的大小
>> plt.xlabel("时间"，fontsize=xx)
>> plt.ylabel("温度",fontsize=xx)
>> plt.title("中午11点0分到12点之间的温度变化图示", fontsize=20)

4 图像保存
# 保存图片到指定路径
>> plt.savefig("test.png")
注意：plt.show()将图形发送到显示终端进行显示，同时释放图形内存资源，所以需要在显示图像之前保存图片；

5 在一个坐标系中绘制多个图像
# 使用多次plot可以画多个折线
>> plt.plot(x, y_beijing, color='r', linestyle='--')

6 显示图例
>> plt.legend(loc="best")
注意:一定要在plt.plot()里面设置一个label,如果不设置,没法显示
# loc 表示在图中的哪个位置显示图例
# 需要在绘制图像时，指定label
# plt.plot(x, y_shanghai, label="上海")
# plt.plot(x, y_beijing, label="北京")

-- 多个坐标系显示— plt.subplots(面向对象的画图方法)
可以通过subplots函数实现
>> import matplotlib.pyplot as plt
>> plt.subplots(nrows=1, ncols=1, **fig_kw) 
# 创建一个带有多个axes(坐标系/绘图区)的图
    nrows, ncols : 设置有几行几列坐标系
    fig : 返回图对象
    axes : 返回相应数量的坐标系
    
    设置标题等方法不同：
    set_xticks
    set_yticks
    set_xlabel
    set_ylabel
注意：plt.函数名()相当于面向过程的画图方法，axes.set_方法名()相当于面向对象的画图方法。    
    
    
# 1.创建画布
>> fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)
# 2.绘制图像
>> axes[0].plot(x, y_shanghai, label="上海")
>> axes[1].plot(x, y_beijing, label="北京")
# 刻度显示
axes[0].set_xticks(x[::5])
axes[0].set_yticks(y_ticks[::5])
axes[0].set_xticklabels(x_ticks_label[::5])
axes[1].set_xticks(x[::5])
axes[1].set_yticks(y_ticks[::5])
axes[1].set_xticklabels(x_ticks_label[::5])
# 添加描述信息
axes[0].set_xlabel("时间")
axes[0].set_ylabel("温度")
axes[0].set_title("中午11点--12点某城市温度变化图", fontsize=20)
axes[1].set_xlabel("时间")
axes[1].set_ylabel("温度")
axes[1].set_title("中午11点--12点某城市温度变化图", fontsize=20)
# 添加网格显示
axes[0].grid(True, linestyle="--", alpha=0.5)
axes[1].grid(True, linestyle="--", alpha=0.5)
# 添加图例
axes[0].legend(loc=0)
axes[1].legend(loc=0)

-- plt.plot()除了可以画折线图，也可以用于画各种数学函数图像
# 0.准备数据
x = np.linspace(-10, 10, 1000)
y = np.sin(x)
# 1.创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 2.绘制函数图像
plt.plot(x, y)
# 2.1 添加网格显示
plt.grid()
# 3.显示图像
plt.show()

-- 常见图形绘制
Matplotlib能够绘制折线图、散点图、柱状图、直方图、饼图。
1 折线图：以折线的上升或下降来表示统计数量的增减变化的统计图
# 特点：能够显示数据的变化趋势，反映事物的变化情况。(变化)
>> api：plt.plot(x, y)

2 散点图：用两组数据构成多个坐标点，考察坐标点的分布,判断两变量之间是否存在某种关联或总结坐标点的分布模式。
# 特点：判断变量之间是否存在数量关联趋势,展示离群点(分布规律)
>> api：plt.scatter(x1, x2)
Parameters:    
x1 : 横坐标序列
x2 : 纵坐标序列,长度要与x1一致

3 柱状图：排列在工作表的列或行中的数据可以绘制到柱状图中。
# 特点：绘制离散的数据,能够一眼看出各个数据的大小,比较数据之间的差别。(统计/对比)
>>> api：plt.bar(x, height, width, align='center', **kwargs)
Parameters: 
# x,y相当于两列数据
x : 横坐标序列；
height: 柱高-与x对应的用来表示柱高的序列,长度跟x要一致；
width : 柱状图的宽度
align : 每个柱状图的位置对齐方式
    {‘center’, ‘edge’}, optional, default: ‘center’
**kwargs :
color:选择柱状图的颜色

4 直方图：由一系列高度不等的纵向条纹或线段表示数据分布的情况。 一般用横轴表示数据范围，纵轴表示分布情况。
# 特点：绘制连续性的数据展示一组或者多组数据的分布状况(统计)
>> api：matplotlib.pyplot.hist(x, bins=None)
Parameters:    
x : 需要查看分布情况的数据
bins : 分箱数

5 饼图：用于表示不同分类的占比情况，通过弧度大小来对比各种分类。
# 特点：分类数据的占比情况(占比)
>> api：plt.pie(x, labels=,autopct=,colors)
Parameters:  
x:数量序列，自动算百分比
labels:每个部分标签的序列,长度与x一致
autopct:占比数据显示格式 指定%1.2f%%
colors:每部分颜色
```
