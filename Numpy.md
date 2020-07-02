Numpy操作指南

```
Numpy（Numerical Python）是一个开源的Python科学计算库，用于快速处理任意维度的数组。
Numpy支持常见的数组和矩阵操作。对于同样的数值计算任务，使用Numpy比直接使用Python要简洁的多。
Numpy使用ndarray对象来处理多维数组，该对象是一个快速而灵活的大数据容器。
NumPy提供了一个N维数组类型ndarray，它描述了相同类型的“items”的集合。
Numpy专门针对ndarray的操作和运算进行了设计，所以数组的存储效率和输入输出性能远优于Python中的嵌套列表，数组越大，Numpy的优势就越明显。
-- ndarray的优势
1 内存块风格
ndarray在存储元素时内存可以连续
2 ndarray支持并行化运算（向量化运算）
numpy内置了并行运算功能，当系统有多个核心时，做某种计算时，numpy会自动做并行计算
3 效率远高于纯Python代码
Numpy底层使用C语言编写，内部解除了GIL（全局解释器锁）

1，-- 用ndarray进行存储数组：
>> import numpy as np
# 创建ndarray
>> score = np.array(数组)
# 数组格式必须一致，否则生成n维数组的n个一维数组
# 通过%time魔法方法, 查看当前行的代码运行一次所花费的时间

2，-- ndarray的属性：
数组属性反映了数组本身固有的信息。
属性名字	     属性解释
ndarray.shape	数组维度的元组
ndarray.ndim	数组维数
ndarray.size	数组中的元素数量
ndarray.itemsize	一个数组元素的长度（字节）
ndarray.dtype	数组元素的类型

3, -- dtype是numpy.dtype类型，数组都有哪些类型：
注意：若不指定，整数默认int64，小数默认float64
名称	       描述	                                         简写
np.bool	     用一个字节存储的布尔类型（True或False）	        'b'
np.int8	     一个字节大小，-128 至 127	                      'i'
np.int16	 整数，-32768 至 32767	                         'i2'
np.int32	 整数，-2^31 至 2^32 -1	                         'i4'
np.int64	 整数，-2^63 至 2^63 - 1	                     'i8'
np.uint8	 无符号整数，0 至 255	                           'u'
np.uint16	 无符号整数，0 至 65535	                       'u2'
np.uint32	 无符号整数，0 至 2^32 - 1	                       'u4'
np.uint64	 无符号整数，0 至 2^64 - 1	                        'u8'
np.float16	 半精度浮点数：16位，正负号1位，指数5位，精度10位	'f2'
np.float32	 单精度浮点数：32位，正负号1位，指数8位，精度23位	'f4'
np.float64	 双精度浮点数：64位，正负号1位，指数11位，精度52位	'f8'
np.complex64 复数，分别用两个32位浮点数表示实部和虚部	          'c8'
np.complex128复数，分别用两个64位浮点数表示实部和虚部	          'c16'
np.object_	 python对象	                                    'O'
np.string_	 字符串	                                       'S'
np.unicode_	unicode类型	                                    'U'

4，-- 生成数组的方法
4.1-- 生成0,1,随机数的数组：
np.ones(shape, dtype)
# 生成全是1的数组
np.ones_like(array, dtype)
# 把其他数组转换为全是1的数组
np.zeros(shape, dtype)
# 生成全是0的数组
np.zeros_like(array, dtype)
# 把其他数组转换成全是0的数组
np.random.random(shape,dtype)
# 生成随机数的数组

4.2-- 从现有数组生成：
np.array(object, dtype)
# 相当于深拷贝，原数组改变，自身不改变
np.asarray(a, dtype)
# 相当于浅拷贝，原数组改变，自身也改变

4.3-- 生成固定范围的数组：
4.3.1-- np.linspace (start, stop, num, endpoint)
创建等差数组 — 指定数量
参数:
start:序列的起始值
stop:序列的终止值
num:要生成的等间隔样例数量，默认为50；可以随意指定；
endpoint:序列中是否包含stop值，默认为ture；false为不包含

4.3.2-- np.arange(start,stop, step, dtype)
创建等差数组 — 指定步长
参数
step:步长,默认值为1

-- np.logspace(start,stop, num)
创建等比数列
# 其实是先生成等差数列，再取10**n,返回数组
参数:
num:要生成的等比数列数量，默认为50

4.4-- 生成随机数组
-- 正态分布是一种概率分布。正态分布是具有两个参数μ和σ的连续型随机变量的分布，第一参数μ是服从正态分布的随机变量的均值，第二个参数σ是此随机变量的方差，所以正态分布记作N(μ，σ )。
-- 正态分布特点
μ决定了其位置，其标准差σ决定了分布的幅度。当μ = 0,σ = 1时的正态分布是标准正态分布。
-- 方差
是在概率论和统计，方差衡量一组数据时离散程度的度量
其中M为平均值，n为数据总个数，σ 为标准差，σ ^2可以理解一个整体为方差
-- 标准差与方差的意义
可以理解成数据的一个离散程度的衡量

4.4.1-- 正态分布创建方式:
-- np.random.randn(n)
n: 取任意int
功能：从标准正态分布中返回一个或多个样本值

-- np.random.normal(loc=0.0, scale=1.0, size=None)
    loc：float
    均值（对应着整个分布的中心centre）
    scale：float
    标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
    size：int or tuple of ints
    输出指定元素数或者shape的数组，默认为None，只输出一个值

-- np.random.standard_normal(size=None)
	size：int or tuple of ints
    输出指定元素数或者shape的数组，默认为None，只输出一个值
	返回指定形状的标准正态分布的数组。

4.4.2-- 均匀分布
-- np.random.rand(n)
    n: 取任意int
    返回：
    [0.0，1.0)内的一组均匀分布的数。
-- np.random.uniform(low=0.0, high=1.0, size=None)
	功能：
	从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.
	参数介绍:
    low: 采样下界，float类型，默认值为0；随意指定；
    high: 采样上界，float类型，默认值为1；随意指定；
    size: 输出样本数目，为int或元组(tuple)类型，例如，size=(m,n,k), 则输出mnk个样本，缺省时输出1个值。
	返回值：
	ndarray类型，其形状和参数size中描述一致。
-- np.random.randint(low, high=None, size=None, dtype='l')
	从一个均匀分布中随机采样，生成一个整数或N维整数数组，
	low,high： 随意指定；
	size：输出样本数目，为int或元组(tuple)类型
    取数范围：
    若high不为None时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数。

5-- 数组的索引、切片
索引:
通过下标访问数组元素
切片:
用:来进行切片
本质都是通过不同轴的元素下标来进行定位

6-- 形状修改
6.1-- ndarray.reshape(shape, order)
返回一个具有相同数据域，但shape不一样的视图
修改数组的形状并返回一个新对象，原数组形状没有改变
注意：
可以给一个-1，只能给一个-1，-1: 表示通过待计算
保证前后数组元素个数相同；
ndarray 的数据在内存里以一维线性存放，reshape 之后，数据并没有移动，只是访问方式变了而已。

6.2-- ndarray.resize(new_shape)
直接修改原数组本身的形状，不返回对象（需要保持元素个数前后相同）

6.3-- ndarray.T
数组的转置
将数组的行、列进行互换，原数组没有发生改变

7-- 类型修改
7.1-- ndarray.astype(type)
type：string形式的类型 或者np.类型
返回修改了类型之后的新对象，不改变原数组类型

-- ndarray.tostring([order])或者ndarray.tobytes([order])
返回新对象，将数组转换为二进制，不改变原数组
构造包含数组中原始数据字节的Python字节

-- jupyter输出太大可能导致崩溃问题
这个问题是在jupyer当中对输出的字节数有限制，需要去修改配置文件
1，创建配置文件
jupyter notebook --generate-config
vi ~/.jupyter/jupyter_notebook_config.py,
2，取消注释,多增加
## (bytes/sec) Maximum rate at which messages can be sent on iopub before they
#  are limited.
c.NotebookApp.iopub_data_rate_limit = 10000000


7.2-- 数组的去重
-- np.unique(ndarray)
ndarray为任意数组
返回新对象，一维数组，不改变原数组

8-- 逻辑运算
8.1-- 逻辑判断, 得到布尔索引数组；如果元素大于60就标记为True 否则为False
>>> test_score > 60
array([[ True,  True,  True, False,  True],
       [ True,  True,  True, False,  True],
       [ True,  True, False, False,  True],
       [False,  True,  True,  True,  True]])
-- BOOL赋值, 将数组中满足布尔索引条件的元素设置为指定的值；
>>> test_score[test_score > 60] = 1
>>> test_score
array([[ 1,  1,  1, 52,  1],
       [ 1,  1,  1, 59,  1],
       [ 1,  1, 44, 44,  1],
       [59,  1,  1,  1,  1]])

8.2-- 通用判断函数
-- 返回布尔值True/False，跟统计运算一样，也存在轴向问题
-- np.all()
相当于Python中的and
-- np.any()
相当于Python中的or

8.3-- np.where（三元运算符，相当于python中的if判断）
-- 不加条件，返回值为数组元素所在各轴的下标形成的一维数组，几维返回几个；
>>> np.where(score>60)
>>> (array([0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5,
        6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9]),
 array([1, 2, 3, 4, 0, 2, 4, 0, 1, 2, 3, 1, 3, 0, 1, 2, 3, 4, 0, 2, 3, 4,
        2, 4, 0, 2, 3, 0, 2, 3, 4, 1, 3, 4]))
-- 加条件，返回值为符合布尔索引的替换为指定值的数组
>>> np.where(score>60,1,0)
>>> array([[0, 1, 1, 1, 1],
       [1, 0, 1, 0, 1],
       [1, 1, 1, 1, 0],
       [0, 1, 0, 1, 0],
       [1, 1, 1, 1, 1],
       [1, 0, 1, 1, 1],
       [0, 0, 1, 0, 1],
       [1, 0, 1, 1, 0],
       [1, 0, 1, 1, 1],
       [0, 1, 0, 1, 1]])
       
8.4-- 复合逻辑np.logical_and，np.logical_or,np.logical_not
-- 相当于python 中的与，或，非
>>> np.logical_and(score>=60,score<70)
>>> array([[False, False, False, False,  True],
       [False, False, False, False, False],
       [False, False, False, False,  True],
       [False,  True,  True, False, False],
       [False, False,  True, False,  True],
       [ True, False, False,  True,  True],
       [False, False, False, False, False],
       [False,  True,  True, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False]])
>>> np.where(np.logical_and(score>=60,score<70),1,0)
>>> array([[0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1],
       [0, 1, 1, 0, 0],
       [0, 0, 1, 0, 1],
       [1, 0, 0, 1, 1],
       [0, 0, 0, 0, 0],
       [0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]])
 
9.-- 统计运算
-- min(a, axis)
-- max(a, axis)
-- median(a, axis)
-- mean(a, axis, dtype)
-- std(a, axis, dtype)
-- var(a, axis, dtype)
-- np.argmax(axis=) — 返回最大值在计算轴上的下标
-- np.argmin(axis=) — 返回最小值在计算轴上的下标
axis=0:表示统计运算在0轴上进行,结果是沿着0轴方向的元素求一个最大值,然后该轴长度塌缩为1,最终该轴被消减
axis=1:表示统计运算在0轴上进行,结果是沿着1轴方向的元素求一个最大值,然后该轴长度塌缩为1,最终该轴被消减
如果数组有多个维度,则axis的取值可以是任意轴的下标,计算方式同上
如果不指定axis,则数组依次在所有轴上做计算,结果只要一个值.
>>> data = np.arange(24).reshape(2,3,4)
>>> data
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]],

       [[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]]])
-- 方式一：np.min(data,axis=0)
>>> np.min(data,axis=0)
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
       
-- 方式二：data.min(axis=0)
>>> data.min(axis=0)
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> data.argmax(axis=0)
array([[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]])
       
10.
-- 数组与数的运算
返回新对象，数组各元素与数进行运算

-- 数组与数组的运算
-- 数组在进行矢量化运算时，要求数组的形状是相等的。当形状不相等的数组执行算术运算的时候，就会出现广播机制，该机制会对数组进行扩展，使数组的shape属性值一样，这样，就可以进行矢量化运算了。

-- 广播机制
广播机制需要扩展维度小的数组，使得它与维度最大的数组的shape值相同，以便使用元素级函数或者运算符进行运算。
1.前提是将数组的维度变得相等。
注意:增加维度一定是在前面增加
2.对应维度要么长度相等，要么一个为1 。
>>> arr2 = np.array([1,2,3])
>>> arr2.shape
(3,)
>>> arr2=arr2.reshape(1,3)
array([[1, 2, 3]])
>>> arr2=arr2.repeat(4,axis=0)
array([[1, 2, 3],
       [1, 2, 3],
       [1, 2, 3],
       [1, 2, 3]])
>>> arr2.shape
(4, 3)

11.-- 矩阵和向量
-- 矩阵，英文matrix，和array的区别矩阵必须是2维的，但是array可以是多维的。
矩阵的维数即行数×列数
-- 向量是一种特殊的矩阵，讲义中的向量一般都是列向量
11.1-- 矩阵：二维数组 MXN 大写字母
-- 向量：特殊的二维矩阵 小写字母
	列向量：n * 1 的矩阵，后续公式中提到的向量都是列向量
	行向量：1 * n 的矩阵，代码实现的时候都是行向量
-- 加法和标量乘法
矩阵的加法:行列数相等的可以加。
矩阵的乘法:每个元素都要乘。

11.2-- 矩阵乘法遵循准则：
(M行, N列)*(N行, L列) = (M行, L列)
左矩阵的列数等于右矩阵的行数
-- 矩阵的乘法不满足交换律：A×B≠B×A
-- 矩阵的乘法满足结合律。即：A×（B×C）=（A×B）×C
-- 单位矩阵：
类比标量中的1，
在矩阵的乘法中，有一种矩阵起着特殊的作用，如同数的乘法中的 1,我们称 这种矩阵为单位矩阵．它是个方阵，一般用 I 或者 E 表示，从 左上角到右下角的对角线（称为主对角线）上的元素均为 1 以外全都为 0。

11.3--  矩阵的逆：
类比标量中倒数，
如矩阵 A 是一个 m×m 矩阵（方阵），如果有逆矩阵，则：
AA^{-1} = A^{-1}A = I
标量中的x=0,就没有倒数；
矩阵的行列式=0，就没有逆矩阵；

-- 低阶矩阵求逆的方法:
1.待定系数法
2.初等变换
矩阵的转置：设 A 为 m×n 阶矩阵（即 m 行 n 列），第 i 行 j 列的元素是 a(i,j)，即：
A=a(i,j)
定义 A 的转置为这样一个 n×m 阶矩阵 B，满足 B=a(j,i)，即 b (i,j)=a (j,i)（B 的第 i 行第 j 列元素是 A 的第 j 行第 i 列元素），记 A^T =B。
直观来看，将 A 的所有元素绕着一条从第 1 行第 1 列元素出发的右下方 45 度的射线作 镜面反转，即得到 A 的转置。

11.4-- 矩阵乘法api：
-- a,b均为矩阵，
11.4.1-- np.matmul
np.matmul(a,b)

11.4.1-- np.dot
相乘有两种写法：
1，np.dot(a,b),
2，a.dot(b)
a矩阵也可以跟常量相乘
np.dot(a,10)
-- np.matmul和np.dot的区别:
二者都是矩阵乘法。 np.matmul中禁止矩阵与标量的乘法。 在矢量乘矢量的內积运算中，np.matmul与np.dot没有区别。

```

