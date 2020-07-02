

Jupyter Notebook操作指南

```
-- 库的安装
-- 新建一个用于数据分析环境的虚拟环境
>> mkvirtualenv 虚拟环境名称
-- 将所有的库放到了文件requirements.txt当中，然后统一安装
>> touch requirements.txt
>> vim requirements.txt
>> 写入以下内容：
matplotlib
numpy
pandas
tables
jupyter
>> pip3 install -r requirements.txt

-- 界面启动
# 进入虚拟环境
>> workon 指定虚拟环境
# 输入命令
>> jupyter notebook
# 会自动弹出浏览器窗口打开Jupyter Notebook
# 本地notebook的默认URL为：http://localhost:8888
# 想让notebook打开指定目录，只要进入此目录后执行命令即可
# notebook的文档格式是.ipynb

-- cell操作
# cell：一对In Out会话被视作一个代码单元，称为cell
# cell行号前的 * ，表示代码正在运行
-- 编辑模式（Enter）
命令模式下回车Enter或鼠标双击cell进入编辑模式
可以操作cell内文本或代码，剪切／复制／粘贴移动等操作
-- 命令模式（Esc）
按Esc退出编辑，进入命令模式
可以操作cell单元本身进行剪切／复制／粘贴／移动等操作

-- 快捷键操作
-- 两种模式通用快捷键
Shift+Enter，执行本单元代码，并跳转到下一单元
Ctrl+Enter，执行本单元代码，留在本单元
-- 命令模式：按ESC进入
Y，cell切换到Code模式
M，cell切换到Markdown模式
A，在当前cell的上面添加cell
B，在当前cell的下面添加cell
双击D：删除当前cell
Z，回退
L，为当前cell加上行号 <!--
Ctrl+Shift+P，对话框输入命令直接运行
快速跳转到首个cell，Crtl+Home
快速跳转到最后一个cell，Crtl+End -->
-- 编辑模式：按Enter进入
补全代码：变量、方法后跟Tab键
为一行或多行代码添加/取消注释：Ctrl+/
多光标操作：Ctrl键点击鼠标
回退：Ctrl+Z
重做：Ctrl+Y

-- 标题和缩进
# 标题, # 越多字号越小
- 缩进，- 越多缩进越多

-- Jupyter Notebook中自动补全代码等相关功能拓展
-- 安装jupyter_contrib_nbextensions库
>> python -m pip install jupyter_contrib_nbextensions
>> jupyter contrib nbextension install --user --skip-running-check
# 在原来的基础上勾选： “Table of Contents”目录索引 ； “Hinterland”代码自动补全；‘code font size’字体大小；‘spellchecker’拼写检查；‘Toggle all line numbers’代码行号；


Jupyter笔记本有两种不同的键盘输入模式. 编辑模式允许您将代码或文本输入到一个单元格中，并通过一个绿色的单元格来表示 命令模式将键盘与笔记本级命令绑定在一起，并通过一个灰色的单元格边界显示，该边框为蓝色的左边框。
命令行模式(按 Esc 生效)
F: 查找并且替换
Ctrl-Shift-F: 打开命令配置
Ctrl-Shift-P: 打开命令配置
Enter: 进入编辑模式
P: 打开命令配置
Shift-Enter: 运行代码块, 选择下面的代码块
Ctrl-Enter: 运行选中的代码块
Alt-Enter: 运行代码块并且插入下面
Y: 把代码块变成代码
M: 把代码块变成标签
R: 清除代码块格式
1
: 把代码块变成heading 1
2
: 把代码块变成heading 2
3
: 把代码块变成heading 3
4
: 把代码块变成heading 4
5
: 把代码块变成heading 5
6
: 把代码块变成heading 6
K
: 选择上面的代码块
上
: 选择上面的代码块
下
: 选择下面的代码块
J
: 选择下面的代码块
Shift-K
: 扩展上面选择的代码块
Shift-上
: 扩展上面选择的代码块
Shift-下
: 扩展下面选择的代码块
Shift-J
: 扩展下面选择的代码块
Ctrl-A
: select all cells
A
: 在上面插入代码块
B
: 在下面插入代码块
X
: 剪切选择的代码块
C
: 复制选择的代码块
Shift-V
: 粘贴到上面
V
: 粘贴到下面
Z
: 撤销删除
D,D
: 删除选中单元格
Shift-M
: 合并选中单元格, 如果只有一个单元格被选中
Ctrl-S
: 保存并检查
S
: 保存并检查
L
: 切换行号
O
: 选择单元格的输出
Shift-O
: 切换选定单元的输出滚动
H
: 显示快捷键
I,I
: 中断服务
0,0
: 重启服务(带窗口)
Ctrl-L
: autopep8 selected cell(s)
Ctrl-Shift-L
: autopep8 the whole notebook
Alt-N
: Toggle linenumbers in all codecells
Ctrl-H
: Toggle All Headers
Esc
: 关闭页面
Q
: 关闭页面
Shift-L
: 在所有单元格中切换行号，并保持设置
Shift-空格
: 向上滚动
空格
: 向下滚动
编辑模式(按 Enter 生效)
Tab
: 代码完成或缩进
Shift-Tab
: 工具提示
Ctrl-]
: 缩进
Ctrl-[
: 取消缩进
Ctrl-A
: 全选
Ctrl-Z
: 撤销
Ctrl-/
: 评论
Ctrl-D
: 删除整行
Ctrl-U
: 撤销选择
Insert
: 切换 重写标志
Ctrl-Home
: 跳到单元格起始处
Ctrl-上
: 跳到单元格起始处
Ctrl-End
: 跳到单元格最后
Ctrl-下
: 跳到单元格最后
Ctrl-左
: 跳到单词左边
Ctrl-右
: 跳到单词右边
Ctrl-删除
: 删除前面的单词
Ctrl-Delete
: 删除后面的单词
Ctrl-Y
: 重做
Alt-U
: 重新选择
Ctrl-M
: 进入命令行模式
Ctrl-Shift-F
: 打开命令配置
Ctrl-Shift-P
: 打开命令配置
Esc
: 进入命令行模式
Shift-Enter
: 运行代码块, 选择下面的代码块
Ctrl-Enter
: 运行选中的代码块
Alt-Enter
: 运行代码块并且插入下面
Ctrl-Shift-Minus
: 在鼠标处分割代码块
Ctrl-S
: 保存并检查
Ctrl-L
: autopep8 selected cell(s)
Ctrl-Shift-L
: autopep8 the whole notebook
Alt-N
: Toggle linenumbers in all codecells
下
: 光标下移
上
: 光标上移
```

