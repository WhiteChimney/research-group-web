---
name: 张三
position: 教授
tutor: 博导
phone: 010-66260702
email: zhangsan@ustc.edu.cn

description: |
  个人简介

image: faculty_example/faculty_example.png
layout: personal_page_template_1
---


## 简介
--------------
本文档是用 *Markdown* 语言撰写的个人主页文件，使用近乎**普通文本的语言**填写信息，就能产生较为整洁的排版效果。各位老师同学只需要编辑本文档就能较为轻松地更新、维护个人主页的信息。

本示例文档主要简单介绍文件的结构及 *Markdown* 的常用语法，帮助老师同学快速上手编辑。


## 文件结构
--------------
文件结构很简单，分为上下两部分。第一部分为标准数据，快速填写个人基本信息。第二部分从 `layout` 那一行代码往下开始，即为正文。如下图所示。`image` 为头像照片路径，文档提交后统一处理。`layout` 那一行代码用于选择网页模板，目前暂时只有一个模板，遂不可更改。

<div style="text-align:center">
    <img src="/people/faculty_example/文件结构.png" title="文件结构" width="100%"/>
</div>


## 关于修改
---------------
如果不想太多了解语法，可以直接下载[模板文件](http://qkdlab.gaokeyan.xyz/files/example_template.zip)修改即可，图片等资源文件交给管理员统一处理。效果如下图所示，左图为编辑文本，右图为显示效果。
<div style="text-align:center">
    <img src="/people/faculty_example/模板编辑效果.png" title="模板编辑效果" width="39%"/>
    <img src="/people/faculty_example/模板网页效果.png" title="模板网页效果" width="60%"/>
</div>

## *Markdown* 语法
-----------------

首先还是推荐 *Markdown* 语法的[中文官网](https://markdown.com.cn/basic-syntax/)，里面提供了简洁明了的例子，非常适合快速上手。

下面我列举几个常用的语法，并给出简单的例子。

### 标题
n 级标题前使用 n 个 # 号，即 n 越小，字号越大。如：

<div style="text-align:center">
    <img src="/people/faculty_example/标题语法.png" title="标题语法" width="80%"/>
</div>

配合分隔线语法（单起一行的三个以上的短横线 `---`）可以清晰地划分区块。

### 列表
* 有序列表：数字+英文句号+空格+内容
* 无序列表：星号(\*)+空格

### 强调
* 斜体：将内容左右两边加上*星号\**
* 加粗：将待加粗的内容左右两边加上**双星号\*\***
* 加粗并斜体：将内容左右两边加上***三星号\*\*\****

### 超链接
这是一个链接 [Markdown语法](https://markdown.com.cn)。

### 图片
图片路径统一为
`/people/你的USTC邮箱前缀/xxx.png(或其他格式）`
可以使用简单的语法
![简单的图片语法](/people/faculty_example/图片语法1.png "简单的图片语法")
也可以使用更复杂一些的 html 语言，设置选项更多一些
<div style="text-align:center">
    <img src="/people/faculty_example/图片语法2.png" title="复杂一些的图片语法" width="80%"/>
</div>
