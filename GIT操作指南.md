usage: git [--version][--help] [-C <path>][-c =]
           [--exec-path[=<path>]][--html-path] [--man-path][--info-path]
           [-p | --paginate | --no-pager][--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

```
# 安装 git 
sudo apt-get install git
# 密码：chuanzhi
# 参数解读:
sudo : 超级管理员权限, 如果使用该权限, 需要添加密码
apt-get : 包管理工具
install : 安装的意思


# 查看 git 是否安装成功
git
# 调用该命令后, 如果出现大篇幅的命令, 代表安装 git 成功.
如果出现 'git 不是内部或外部命令' 字样. 则 git 安装失败


# 初始化 git 得到本地仓库
git init


# 配置个人的用户名: 
git config user.name '张三'
# 配置个人的邮箱地址: 
git config user.email 'zhangsan@163.com'


# 查看文件状态:
git status
# 如果为红色, 表示新建的文件或者修改的文件, 在工作区.
如果为绿色, 表示文件在暂存区


#工作区提交到暂存区 
# 第一种提交方式: 
git add .
# 第二种提交方式:
git  add  login.py


# 暂存区提交到仓库区: 
git commit -m  '描述信息'**~~****~~**
# commit 会进行一次本地仓库提交
-m 后面是添加的是本次提交的描述信息


# 工作区直接提交到仓库区: 
git commit -am  '描述信息'



# 查看提交的历史记录: 
# 第一种:太详细 
git log
# 第二种: 简洁
git reflog
# git reflog 可以查看所有分支的所有操作记录（包括 commit 和 reset 的操作），包括已经被删除的commit 记录，git log 则不能察看已经删除了的 commit 记录


#回退版本: 
#第一种:
git reset --hard 版本
#HEAD 表示当前最新版本
HEAD^表示当前最新版本的前一个版本
HEAD^^ 表示当前最新版本的前两个版本，以此类推...
HEAD~1 表示当前最新版本的前一个版本
HEAD~10表示当前最新版本的前10个版本，以此类推...
#第二种:
git reset --hard 版本号
#通过每个版本的版本号回退到指定版本


# 工作区代码撤销: 
git checkout 文件名
# 只能撤销工作区、暂存区的代码, 不能撤销仓库区的代码
撤销仓库区的代码就相当于回退版本操作


# 暂存区代码撤销:
# 第一步：将暂存区代码撤销到工作区
git reset HEAD  文件名
# 第二步：撤销工作区代码
git checkout 文件名


#通过 https 的方式, 从 Github 获取远端仓库:
git clone https://github.com/weiguangfan/test.git

#使用 SSH 的方式从 Github 上获取远端仓库
#配置 Github 的注册邮箱和用户名: 
vim .gitconfig
# 修改下列字段: 
[user]
    email = 邮箱@163.com
    name = 注册的 github 名称
#生成 SSH 公钥
ssh-keygen -t rsa -C "zhangjiesharp@163.com"
# 查看公钥文件: 
cat ~/.ssh/id_rsa.pub
#完善 Github 中 SSH 公钥信息
#删除~/.ssh目录
rm -r .ssh
git  clone  git@github.com:weiguangfan/test.git


# 推送到远程仓库
git push
# 如果在每次 push 都需要设置账号与密码，那么可以设置记住密码
# 设置记住密码（默认15分钟）：
git config --global credential.helper cache
# 如果想自己设置时间，可以这样做(1小时后失效)：
git config credential.helper 'cache --timeout=3600'
# 长期存储密码：
git config --global credential.helper store


# 拉取远端工程: 
git  pull

#容易冲突的操作方式
多个人同时操作了同一个文件
一个人一直写不提交
修改之前不更新最新代码
提交之前不更新最新代码
擅自修改同事代码


#减少冲突的操作方式
养成良好的操作习惯,先pull在修改,修改完立即commit和push
一定要确保自己正在修改的文件是最新版本的
各自开发各自的模块
如果要修改公共文件,一定要先确认有没有人正在修改
下班前一定要提交代码,上班第一件事拉取最新代码
一定不要擅自修改同事的代码


#设置标签: 
git tag -a 标签名 -m '标签描述'
#推送标签到远程仓库
git push origin 标签名


# 删除本地标签
git tag -d 标签名
# 删除远程仓库标签
git push origin --delete tag 标签名


#查看当前分支
git branch

#创建并切换到 dev 分支
git checkout -b dev
#基于dev 分支创建并切换到 feature 分支
git checkout -b feature dev
#基于dev 分支创建并切换到 release 分支
git checkout -b release dev

#将分支推送到远程
git push -u origin dev

#dev 分支合并到 master 分支
#先切换到 master 分支
git checkout master
#dev 分支合并到 master 分支
git merge dev
#推送合并分支操作到远程仓库
git push
#只要有合并到 master 分支，就应该打好Tag 以方便跟踪
git tag -a 0.1 -m "Initial public release" master
git push --tags
```

这些是各种场合常见的 Git 命令：

开始一个工作区（参见：git help tutorial）
   clone      克隆一个仓库到一个新目录
   init       创建一个空的 Git 仓库或重新初始化一个已存在的仓库

在当前变更上工作（参见：git help everyday）
   add        添加文件内容至索引
   mv         移动或重命名一个文件、目录或符号链接
   reset      重置当前 HEAD 到指定状态
   rm         从工作区和索引中删除文件

检查历史和状态（参见：git help revisions）
   bisect     通过二分查找定位引入 bug 的提交
   grep       输出和模式匹配的行
   log        显示提交日志
   show       显示各种类型的对象
   status     显示工作区状态

扩展、标记和调校您的历史记录
   branch     列出、创建或删除分支
   checkout   切换分支或恢复工作区文件
   commit     记录变更到仓库
   diff       显示提交之间、提交和工作区之间等的差异
   merge      合并两个或更多开发历史
   rebase     在另一个分支上重新应用提交
   tag        创建、列出、删除或校验一个 GPG 签名的标签对象

协同（参见：git help workflows）
   fetch      从另外一个仓库下载对象和引用
   pull       获取并整合另外的仓库或一个本地分支
   push       更新远程引用和相关的对象

命令 'git help -a' 和 'git help -g' 显示可用的子命令和一些概念帮助。
查看 'git help <命令>' 或 'git help <概念>' 以获取给定子命令或概念的
帮助。

