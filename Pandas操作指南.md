Pandas操作指南

```
-- pandas
专门用于数据挖掘的开源python库
以Numpy为基础，借力Numpy模块在计算方面性能高的优势
基于matplotlib，能够简便的画图
独特的数据结构

-- pandas学习的目的
增强图表可读性
便捷的数据处理能力
读取文件方便
封装了Matplotlib、Numpy的画图和计算

1. -- Pandas数据结构
数组可以转变为series,dataframe,数据结构发生改变，多了索引行或列
1.1 --Series
Series类似于一维数组，由数据和索引构成。
1.1.1-- Series的创建
>> import pandas as pd
>> pd.Series(data=None, index=None, dtype=None)
	参数：
    data：传入的数据，可以是ndarray、list等
    index：索引，必须是唯一的，且与数据的长度相等。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
    dtype：数据的类型

-- 通过已有数据创建
1 -- 指定内容，不指定索引，数组使用默认索引
>> pd.Series(np.arange(10)+3)
2 -- 指定内容，指定索引
pd.Series([2.3,4.3,5,2.1],index=(1,2,3,4))

-- 通过字典数据创建，数组会自动把键作为索引
pd.Series({'red':100, 'blue':200, 'green': 500, 'yellow':1000})

1.1.2 Series的属性
-- index，返回键组成的数组
>>> colors.index
Index(['blue', 'green', 'red', 'yellow'], dtype='object')
--- values 返回数组
>>> colors.values
array([ 200,  500,  100, 1000])

>>> series.unique()
去重
返回新对象，一维数组，不改变原数组；

-- Pandas Series.to_frame()函数用于将系列对象转换为DataFrame。
Series.to_frame(name=None)
参数
name：指对象。
其默认值为无。
如果有一个值, 则将使用传递的名称代替系列名称。
>> s = pd.Series(["a", "b", "c"], name="vals")
>> s.to_frame()


1.2 -- DataFrame
DataFrame类似二维数组，既有行索引，又有列索引
1.2.1 -- DataFrame的创建
>> import pandas as pd
>> pd.DataFrame(data=None, index=None, columns=None)
    参数：
    index：行索引，表明不同行，横向索引，叫index，0轴，axis=0
    columns：列索引，表名不同列，纵向索引，叫columns，1轴，axis=1
    行标签和列标签,如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。

-- 通过已有数据创建
score = np.random.randint(40, 100, (10, 5))
-- 增加行、列索引
1 构造行索引序列
subjects = ["语文", "数学", "英语", "政治", "体育"]
2 构造列索引序列
stu = ['同学' + str(i) for i in range(score.shape[0])]
3 添加行索引
score_df = pd.DataFrame(score,index=stu，columns=subjects )

1.2.2 -- DataFrame属性 
-- shape 返回数组维度结构
>>> score_df.shape
(10, 5)
--- index，返回行索引组成的数组
>>> data.index
Index(['同學_0', '同學_1', '同學_2', '同學_3', '同學_4', '同學_5', '同學_6', '同學_7', '同學_8',
       '同學_9'],dtype='object') 
       
-- columns,返回列索引组成的数组
>>> data.columns
Index(['语文', '数学', '英语', '政治', '体育'], dtype='object')

-- values，返回array数组
>>> data.values
array([[96, 80, 63, 59, 44],
       [73, 60, 45, 55, 48],
       [48, 90, 89, 48, 88],
       [95, 47, 58, 78, 97],
       [76, 51, 55, 60, 53],
       [86, 54, 46, 81, 65],
       [71, 55, 51, 94, 91],
       [86, 63, 87, 82, 55],
       [63, 94, 68, 67, 43],
       [58, 57, 90, 60, 98]])
       
-- T 返回行列索引互换的数组
>>> data.T

--info() 方法
>>> data.info() 返回数组相关的信息
<class 'pandas.core.frame.DataFrame'>
Index: 10 entries, 同學_0 to 同學_9
Data columns (total 5 columns):
语文    10 non-null int64
数学    10 non-null int64
英语    10 non-null int64
政治    10 non-null int64
体育    10 non-null int64
dtypes: int64(5)
memory usage: 800.0+ bytes

-- 显示指定行数
-- 如果不补充参数，默认5行。填入参数N则显示前N行
1 head() 方法，返回数组的前几行
>>> data.head()

2 tail() 方法，返回数组的后几行
>>> data.tail()

1.2.3 -- DatatFrame索引的设置
-- 修改行、列索引值
df.index = 新索引
df.columns = 新索引
-- 修改整个索引对象(只能整体修改，不能部分修改，因为index对象是不可变对象)
>>> stu = ['學生_{}'.format(i)for i in range(score_df.shape[0])]
>>> data.index = stu

-- 修改指定的某些索引(实质还是整体修改)
df.rename(
          index={原行索引名1:新行索引名1,原行索引名2:新行索引名2,...}
          columns={原列索引名1:新列索引名1,原列索引名2:新列索引名2,...}
)

>>> data = data.rename(index={'學生_3':'學生3'},columns={'体育':'物理'})

-- 重设索引,原行索引变成列索引，新增行索引
>>> reset_index(drop=False)
drop:默认为False，不删除原来索引，如果为True,删除原来的索引值
>>> data.reset_index()

-- 以某列值设置为新的索引,把列索引变成行索引
-- set_index(keys, drop=True)
keys : 列索引名成或者列索引名称的列表
drop : boolean, default True.当做新的索引，删除原来的列

2.--  基本数据操作
# 读取指定的文件
data = pd.read_csv("路径")
# 按照指定维度，删除一些索引列
data = data.drop([列索引名，，，], axis=1)

2.1 -- 索引操作，二维数组，支持索引和切片
2.1.1-- series方式访问 
-- df[columns][index]
-- 二维数组底层是一列一列存储的，一列是一个series的一维数组，一维数组就可以用k-v方式取值，就可以直接使用行列索引(先列后行)
# 根据键取值
>>> data['open']['2018-02-27']
23.53
# 一个列索引组成series一维数组,两个列索引组成dataframe二维数组
>>> data['open']， 返回series
>>> data[['open','close']]，返回dataframe

2.1.2-- 结合loc或者iloc使用索引
-- loc[行索引范围][列索引范围]
-- loc[行索引范围,列索引范围]
-- loc:根据行列索引名或者索引范围，返回数组
>>> data.loc['2018-02-27':'2018-02-22', 'open']
指定一个列索引名，返回series一维数组
2018-02-27    23.53
2018-02-26    22.80
2018-02-23    22.88

>>> data.loc['2018-02-27':'2018-02-22', ['open']]
加了[]，代表你想返回多列，返回dataframe二维数组

-- iloc[行索引范围][列索引范围]
-- iloc[行索引范围,列索引范围]
-- iloc：根据行列索引的下标，返回数组
指定多个列索引，返回dataframe二维数组
>>> data.iloc[:3, :4]

            open    high    close    low
2018-02-27    23.53    25.88    24.16    23.53
2018-02-26    22.80    23.78    23.53    22.80
2018-02-23    22.88    23.37    22.82    22.71

2.1.3-- ix：使用行列索引名和行列索引下标范围，返回数组
>>> data.ix[0:4, ['open', 'close', 'high', 'low']]

-- 推荐使用loc和iloc来获取的方式
data.loc[data.index[0:4], ['open', 'close', 'high', 'low']]
data.iloc[0:4, data.columns.get_indexer(['open', 'close', 'high', 'low'])]

            open    close    high    low
2018-02-27    23.53    24.16    25.88    23.53
2018-02-26    22.80    23.53    23.78    22.80
2018-02-23    22.88    22.82    23.37    22.71
2018-02-22    22.25    22.28    22.76    22.02

2.2-- 赋值操作,获取指定列并赋值，直接修改原数组，返回元素为修改值的数组
>>> data['close'] = 1
>>> data.close = 1

2.3-- 排序
dataframe 按照行列索引排序，返回新数组，不改变原数组,
>>> df.sort_values(by=索引名或者索引数组, ascending=True/False)
默认升序，True为升序，False为降序

2.3.1 按列索引名排序，指定一个列索引名，或者指定多个列索引名，返回dataframe二维数组；
>>> data = data.sort_values(by="open", ascending=False)
>>> data = data.sort_values(by=['open', 'high'])
>>> data = data.sort_values(by=['open', 'high'], ascending=False)

2.3.2 按行索引名排序，返回dataframe二维数组
>>> data.sort_index()
>>> data.sort_index(ascending=False)

Series 按照行列索引排序，排序只有一列，不需要参数，默认升序，True为升序，False为降序
2.3.3 按照列索引排序
>>> series.sort_values(ascending=True)
>>> data['p_change'].sort_values(ascending=True).head()

2.3.4 按照行索引排序
>>> series.sort_index()
>>> data['p_change'].sort_index()

3.-- DataFrame运算
3.1-- 算术运算，加减乘除,实则一维数组的计算
-- 唯一和python不同，是可以校验参数
--  add(other)加
>>> data['open'].add(1)
--- sub(other)减
--- div(other)除


3.2-- 实现数组的逻辑筛选

3.2.1 >>> df[单个或多个筛选条件]
返回符合布尔索引为真的元素组成的数组
>>> data["open"] > 23
返回布尔索引组成的数组
2018-02-27     True
2018-02-26    False
2018-02-23    False
2018-02-22    False
2018-02-14    False
>>> data[data["open"] > 23]
>>> data[(data["open"] > 23) & (data["open"] < 24)].head()
# 相当于and
>>> data[(data["open"] > 23) | (data["open"] < 24)].head()
# 相当于or

3.2.2 >>> query(单个或多个筛选条件的字符串)
>>> query(expr)
	expr:查询字符串
返回符合布尔索引数组的元素构成的数组
>>> data.query("open<24 & open>23").head()
>>> data.query('open<23 | open>25').head()

3.2.3 >>> isin([一个或多个值])
>>> data[data["open"].isin([23.53, 23.85])]
>>> data[data["open"].isin([23.53,])]

3.3-- 统计运算
>>> -- data.describe()
能够直接得出数值列min(最小值), max(最大值), mean(平均值), median(中位数), var(方差), std(标准差),mode(众数)，count,sum和，mode，abs，prod积，idxmax最大值行索引，idxmin最小值行索引以及四分位数等很多统计结果

3.3.2--统计函数
默认axis=0，行索引方向；指定axis=1，列索引方向
-- max()、min()
>>> data.max(0)
-- idxmax()、idxmin()
行索引方向，返回符合最大值元素的对应的行索引组成一维数组
>>> data.idxmax(axis=0)
>>> data.idxmin(axis=0)
-- median()：中位数
中位数为将数据从小到大排列，在最中间的那个数为中位数。如果没有中间数，取中间两个数的平均值。
>>> data.median(0)

3.3.3-- 累计统计函数
cumsum	计算前1/2/3/…/n个数的和
cummax	计算前1/2/3/…/n个数的最大值
cummin	计算前1/2/3/…/n个数的最小值
cumprod	计算前1/2/3/…/n个数的积
排序之后，进行累计求和
>>> data = data.sort_index()
>>> stock_rise = data['p_change'].cumsum()

3.4-- 自定义运算，返回一维数组
-- apply(func, axis=0)
func:自定义函数
>>> data['open'](np.max,axis=0)
>>> data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0)
>>>
def topn(df,n=5,col='Revenue (Millions)'):
    if df.shape[0]<n:
        return np.nan
    else:
        return df.sort_values('Revenue (Millions)',ascending=False)[:n][col].sum()
df.groupby('Director').apply(topn).dropna()
分组后，将函数应用于各个分组

-- 也可以自定义函数
>>> def mymax(x):
		return max(x)
>>> data[['open', 'close']].apply(mymax,axis=0）

4-- dataframe 一维或者二维数组根据行索引作为x轴，列索引作为y轴，自动绘制图型；
默认折线图，列索引名有几个返回几条线；
>>> df.plot(kind='line')
>>> plt.show()
kind : str，内容为字符串，需要绘制图形的种类
‘line’ : line plot (default) 默认折线图
‘bar’ : vertical bar plot 柱状图
‘barh’ : horizontal bar plot 横着的柱状图
‘hist’ : histogram 直方图
‘pie’ : pie plot 饼图，subplots=True
‘scatter’ : scatter plot 离散图，scatter requires an x and y column

5-- 文件读取与存储，都有对应的API，只需要调用即可
优先选择使用HDF5文件存储
HDF5在存储的时候支持压缩，使用的方式是blosc，这个是速度最快的也是pandas默认支持的;
使用压缩可以提磁盘利用率，节省空间;
HDF5还是跨平台的，可以轻松迁移到hadoop 上面;
5.1 -- Excel表格，二进制文件
-- read_excel 读取api
>>>pd.read_excel（filepath，sheet_name = 0，header = 0，names = None，index_col = None，usecols = None）
	前两个参数比较常用，其他不常用
    filepath:字符串，文件的路径对象。
    sheet_name：None、string、int、字符串列表或整数列表，默认为下标0。
    字符串用于工作表名称,
    整数用于零索引工作表位置,
    字符串列表或索引列表用于请求多个工作表，为None时获取所有工作表。
    #如果报xlrd错误就安装这个包  pip install xlrd   
>>> data=pd.read_excel('data/2019.01.xlsx',sheetname='酒店订单')
>>> data.head()

     订单号             入住日期       离店日期     房间数
0    114311622368512    2019-02-01    2019-02-02    1
1    114311066222592    2019-01-31    2019-02-01    1
2    114311045054464    2019-01-31    2019-02-01    1
3    114311030996992    2019-01-31    2019-02-01    1
4    114310813687040    2019-01-31    2019-02-01    1

-- to_excel 文件存储
>>> df.to_excel(file_path, sheet_name='Sheet1', na_rep='', columns=None, header=True, index=True)
前两个参数比较常用，其他不常用
    file_path :文件路径
    sheet_name :sheet名，默认为"Sheet1"
    columns :选择需要的列索引
    header :boolean or list of string, default True,是否写进列索引
    index:是否写进行索引
    #由于有中文字符,需要安装xlsxwriter   pip install xlsxwriter   
>>> data.to_excel('data/test.xlsx',engine='xlsxwriter',sheet_name='sheet2')

5.2-- CSV 文件
-- read_csv 读取文件
>>>pd.read_csv(filepath_or_buffer, sep =',' )
一般指定路径和列名
    filepath_or_buffer:文件路径
    usecols:指定读取的列名，列表形式
>>> data = pd.read_csv("./data/stock_day.csv", usecols=['open', 'close'])
-- to_csv 存储文件
>>> df.to_csv(path_or_buf=None, sep=', ’, columns=None, header=True, index=True, mode='w', encoding=None)
一般指定路径和列名，数组元素会被分隔符隔开后进行存储
    path_or_buf :文件路径
    sep :分隔符，默认用","隔开
    columns :选择需要的列索引
    header :boolean or list of string, default True,是否写进列索引值
    index:是否写进行索引
    mode:'w'：重写, 'a' 追加
>> pd2.to_csv('test.csv',columns=['open'])
>> pd2[:10].to_csv('test1.csv',index=False,sep='#')

5.3-- HDF5文件，二进制文件
文件的读取，需要指定文件路径和key，当文件中只要一个key时，可以不给
>>> pd.read_hdf(path_or_buf，key =None，** kwargs)
    path_or_buffer:文件路径
    key:读取的键
>>> pd.read_hdf("./data/stock_data/day/day_eps_ttm.h5")
文件的存储，需要指定文件路径和key，key必须给
>>> df.to_hdf(path_or_buf, key, *\kwargs*)  
>>> df.to_hdf("./data/test.h5", key="day_eps_ttm")
需要安装tables模块避免不能读取HDF5文件
pip install tables

5.4-- JSON文件,orient指定存储的json格式，lines指定按照行去变成一个样本
-- read_json读取文件
>>> pandas.read_json(path_or_buf=None, orient=None, typ='frame', lines=False)
读取文件，必须指定orient和lines,records代表每行以json字符串形式存储，lines代表内容每一行是一个 json字符串,True代表每一行，False代表整体
    orient : string,Indication of expected JSON string format.
    'split' : dict like {index -> [index], columns -> [columns], data -> [values]}
    'records' : list like [{column -> value}, ... , {column -> value}]
    records 以columns：values的形式输出
    'index' : dict like {index -> {column -> value}}
    index 以index：{columns：values}...的形式输出
    'columns' : dict like {column -> {index -> value}}
>>> pd.read_json("./data/Sarcasm_Headlines_Dataset.json", orient="records", lines=True)
-- to_json存储文件，必须指定orient和lines,lines代表内容每一行是一个 json字符串,True代表每一行，False代表整体
>>> df.to_json(path_or_buf=None, orient=None, lines=False)
    path_or_buf=None：文件地址
    orient:存储的json形式，{‘split’,’records’,’index’,’columns’,’values’}
    lines:一个对象存储为一行
>>> df.to_json("./data/test.json", orient='records', lines=False)

6.1 高级处理--缺失值处理 
-- 处理nan
>> df.info()
查看数组信息，包含各列非空数值数量对比信息
>> df.head()
查看缺失值是不是NaN
>> df.describe()
查看数组分布信息

>> 是nan  np.nan
1 删除：
	删除行；
	删除列；
2 填充：
	将nan填充为指定的值

>> 不是nan ?
   replace 将指定的值替换为nan
  

6.1.1 判断数据中是否包含NaN,返回布尔索引数组；
>> pd.isnull(df)
NaN为True,非NaN为False
>> pd.notnull(df)
非NaN为True,NaN为False

>>>pd.isnull(df).sum()
判断各列含有空值的数量,false为0，true为1，和就是空值的数量
>>> pd.isnull(df).sum/df.shape[0] 
一般计算数组缺失比例,每列的空值数量除以总行数，来判断是否有空值

>> df.dropna()
删除存在空值的行，不会修改原数据，返回新对象

value:替换成的值，
>> df.fillna(value)
将空值替换成指定值，任意给定，不会修改原数据，返回新对象
>> df.fillna(df.mean())
可以是统计函数的series,
>> fill_dict={
    'Revenue (Millions)':-100,  #Revenue (Millions)列用-100填充
    'Metascore':-10             #Metascore列用-10填充
}
>> df.fillna(fill_dict)
也可以是字典，键为列索引名：值为替换的指定值


>> 想要改变原数组，
1 赋值
>> df = df.fillna(df.mean())
2 使用Inplace
>> df.fillna(value, inplace=True)
inplace=True:修改原数组,不返回新对象
inplace=False:不修改原数组，返回新对象

6.2 -- 如何处理非nan
>>> df.replace(旧数据，新数据)
先替换‘?’为np.nan
>>> df.dropna()
>>> df = df.fillna(value)或者df.fillna(value,inplace=True)

7 高级处理--数据离散化

将连续数值型数据映射成离散化类别；
离散化会丢掉部分数据的差异，丢掉部分信息；会让模型变得简单，模型就不容易过拟合；离散化的太厉害，模型就会太简单，就会欠拟合；

7.1等深分箱、等频分箱，频次相同，样本数近似相等    
-- pd.qcut(指定数组，分箱数量)
>> df.loc[:,列索引名] = pd.qcut(指定数组，分组数量)
>> df.loc[:,'qcut'] = pd.qcut(df1['low'],10)
数组多出一列qcut,显示各个元素所属区间
>> df['qcut'].value_counts()
返回series一维数组，数据已经按照统计结果的大小，按照降序显示各个区间的样本数量
>> df['qcut'].value_counts(1)
返回series一维数组，样本数据占比已经按照统计结果的大小，按照降序显示各个区间的样本占比

7.2等宽分组，宽度相等，样本数不相同，有差异  
-- pd.cut(指定数组，分箱数量) 
>> df.loc[:,列索引名] = pd.cut(指定数组，分组数量)
数组多出一列cut,显示各个元素所属区间
>> df['cut'].value_counts()
返回series一维数组，显示各个区间的样本数量

7.3自定义分箱           
>> pd.cut(指定数组，自定义分组列表)
>> df.loc[:,'cut1']=pd.cut(df['high'],[0,5,10,15,20,25,30,35,40])
数组多出一列cut,显示各个元素所属的自定义区间
>> pd.Series(genre_list).value_counts()
返回series一维数组，显示各个区间的样本数量

>> series.value_counts()
返回series一维数组，元素为指定列元素在等分区间的频次或数量

8.-- one-hot编码
什么是one-hot编码
把每个类别生成一个布尔列，这些列中只有一列可以为这个样本取值为1.其又被称为热编码。
1）把每个类别生成一个列向量，离散向量映射成one-hot向量
2）数据挖掘算法，需要数据都是数值型的
3）将数组的类别类型的列,全部映射成列向量数组,新增若干列.列索引名自动生成,返回新对象

>> pandas.get_dummies(data, prefix=None)
    prefix可以省略不写；
    data:array-like, Series, or DataFrame
    prefix:分组名字
>> pd.get_dummies(df)
将离散向量映射成one-hot向量
>> pd.get_dummies(df1)

9. 高级处理-- 时间序列处理

9.1-- 将日期字符串转换成日期
将数组元素object对象类型转换成 ns日期类型对象
   
>> df.loc[：，‘列索引名’] = pd.to_datetime(df['列索引名'])
动态新增列
>> df1['入住日期'] = pd.to_datetime(df1['入住日期'])
赋值方法
>> df1.loc[:,'离店日期'] = pd.to_datetime(df1['离店日期'])
动态新增列

9.2-- 生成日期序列
>> pd.date_range(start=None, end=None, periods=None, freq='D')
    至少指定start、end、periods中的两个参数值，否则报错。
    start:起始日期,字符串
    end:终止日期,字符串
    periods:期数，取值为整数或None
    freq:频率或日期偏移量，取值为string或DateOffset，默认为'D'天，还有其他'H'小时，'B'工作日等
>> pd.date_range('20200601','20200710')
>> pd.date_range('20200530',periods=7)
>> pd.date_range('20080901','20080902',freq='H')
>> pd.date_range('2020-05-30',periods=10,freq='H')

9.3-- series.dt对象.属性
提取年,月,日,周等日期时间信息
>> df['列索引名'].dt.指定参数
返回series一维数组,
元素为经过日期类型转换的指定参数的值
参数可以是year年/month月/weekday周几/date日期/time时间/quarter季度等
>> df.loc[:,'列索引名'] = df['列索引名'].dt.指定参数
动态生成列
>> df1.loc[:,'入住月份'] = df1['入住日期'].dt.month

9.4-- strftime,to_period格式化日期
>> from datetime import datetime
   datetime.strftime
   strftime函数实际上是datetime模块中的函数,并不是pandas中的成员
-- series.datetime.strftime(data,format_str)
    date:需要格式化的日期
    format_str:格式化字符串，%Y年/%m月/%d日/%H时/%M分/%S秒
>> df1.loc[:,'离店时间']=df1['离店日期'].apply(lambda x:datetime.strftime(x,'%Y-%M'))
动态生成列

-- series.dt.to_period(参数)
>> df['列索引名'].dt.to_period(参数)
返回series一维数组,元素为经过日期类型转换的格式化的指定参数的值
参数可以是 M 表示月份，Q 表示季度，A 表示年度，D 表示按天，这几个参数比较常用。
>> df1.loc[:,'入住年月']= df1['入住日期'].dt.to_period('M')
动态生成列


9.5-- 时间差timedelta
timedelta(series).dt.days/seconds/microseconds
访问timedelta对象的属性来提取天数
一般用来表示两个日期之间的差距。
>> series.dt.指定参数
返回series一维数组,
元素为经过日期类型转换的指定参数的值
timedelta对象有属性：days、seconds、microseconds
>> time= df1['离店日期']-df1['入住日期']
>> df.loc[:,'新增列索引名']=time.dt.days

10.高级处理 -- 合并
10.1>> pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,keys=None)
axis=0:沿0轴(纵向)进行合并
axis=1:沿1轴(横向)进行合并
# 按照0轴方向进行拼接,列对齐
result= pd.concat([df1,df2])

# 按照1轴方向拼接,行对齐
result1 = pd.concat([df1,df4],axis=1)

# 按照1轴方向拼接后,按照行索引取交集
result2 = pd.concat([df1,df4],axis=1,join='inner')

# 按照0轴方向拼接后,按照列索引取并集
result3 = pd.concat([df1,df4],axis=0,join='outer')

# 按照0轴方向拼接,列对齐,行索引重新生成
result5 = pd.concat([df1,df4],axis=0,ignore_index=True)

# 按照0轴方向拼接,列对齐,指定分组键
result6 = pd.concat([df1,df2,df3],keys=['x','y','z'],axis=0)
result7 = pd.concat({'x':df1,'y':df2,'z':df3},axis=0)

# append 相当于pd.concat([df1,df2],axis=0)
# 按照0轴方向拼接,列对齐
result8 = df1.append(df2)

>> pd.merge(left, right, how='inner', on=None)
可以指定按照两组数据的共同键值对合并或者左右各自
    left: DataFrame
    right: 另一个DataFrame
    on: 指定的共同键
    how:按照什么方式连接

# 按照1轴方向拼接,行对齐,内联接,按照行索引取交集
df5 = pd.merge(left,right,on=['key1','key2'])

# 按照1轴方向拼接,行对齐,左联接,按照左表行索引保留空值行
df6 = pd.merge(left,right,how='left',on=['key1','key2'])

# 按照1轴方向拼接,行对齐,右联接,按照右表行索引保留空值行
df7 = pd.merge(left,right,how='right',on=['key1','key2'])

# 按照1轴方向拼接,行对齐,外链接,按照行索引取并集
df8 = pd.merge(left,right,how='outer',on=['key1','key2'])


11 高级处理 -- 分组、聚合
一个用于表示分组运算的术语"split-apply-combine"（拆分－应用－合并）。第一个阶段，pandas对象（无论是Series、DataFrame还是其他的）中的数据会根据你所提供的一个或多个键被拆分（split）为多组。拆分操作是在对象的特定轴上执行的。例如，DataFrame可以在其行（axis=0）或列（axis=1）上进行分组。然后，将一个函数应用（apply）到各个分组并产生一个新值。最后，所有这些函数的执行结果会被合并（combine）到最终的结果对象中。结果对象的形式一般取决于数据上所执行的操作。

>> df.groupby(key, as_index=False)
    key:分组的列索引名，可以是多个列索引名
    as_index=False 分组列索引不作为行索引，是单独的列，返回二维数组
    as_index=True  分组列索引作为行索引，返回一维数组

>> df1.groupby(['color'])['price1'].mean()
# 先按照color列索引名分组,再按照price1列索引名聚合,也就是进行统计计算
# 返回以color作为行索引名的一维数组

# 效果同上
>> df1['price1'].groupby(df1['color']).mean()

--as_index参数
>> df1.groupby(['color'],as_index=False)['price1'].mean()
# 默认as_index=True,
分组列索引作为行索引,
返回一维数组;
# as_index=False,分组列索引不作为行索引,而是作为单独一列,返回二维数组

>> df1.groupby(['color','object'])['price2'].max()
>> df1.groupby(['color','object'],as_index=False)['price2'].max()

# 先分组后聚合,指定多个列索引名作为行索引,返回一维数组
# 默认多个分组列索引名作为行索引,as_index=True,返回一维数组
# as_index=False ,多个列索引名不会作为行索引,会单独作为列,返回二维数组


12 高级处理 -- 交叉、透视表
12.1 透视表
>> pandas.pivot_table(data, values=None, index=None, columns=None,aggfunc='mean', margins=False)
四个最重要的参数index、values、columns、aggfunc
    data:[必须]需要操作数据,DataFrame
    values:
    要进行计算操作的列名,
    一个列名或列名组成的列表,不给代表对所有列操作，进行聚合运算的列索引名
    index:
    [必须]分组后作为行索引的列名,
    一个列名或列名组成的列表,用来分组
    columns:
    分组后作为列索引的列名,一个列名或列名组成的列表，用来分组
    aggfunc:
    指定对values参数所给的列做什么计算操作,
    可以是字典(分别为不同的列指定不同的计算操作),默认为mean(计算均值)，聚合运算的操作
    margins:是否进行行汇总和列汇总
>> pivot_table(score,index=['对手','主客场'])
'对手','主客场',两列作为行索引
>> pd.pivot_table(score,index=['对手','胜负'],values=['得分','助攻','篮板'])

>> import numpy as np
>> pd.pivot_table(score,index=['胜负','主客场','对手'],values=['得分','助攻','篮板'],aggfunc=[np.sum,np.mean])

12.2 轴转换(透视功能)unstack
unstack对应的是excel中的透视功能,stack正好相反是逆透视
>> df.unstack(level=-1)
level:
需要进行逆透视(取消堆叠)的索引级别,
默认为-1,即最后一级索引
取行层级索引下标[-1]，将行索引直接变成列索引，数据结构发生改变
>> score.groupby(['胜负','主客场','对手'])['得分'].sum().unstack()

>> df.stack()
不需要指定参数,功能为逆透视所有列

```

​	