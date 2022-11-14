---
layout: default
title: 网页配置使用指南
---

================================

## 配置流程
================================

### 个人网页
--------------
编辑 _people/xxx.md 文件，并将所用到的资源文件（如图片）一起提交给管理员处理即可。
具体编辑步骤可以参看这个[网页](https://qkdlab.gaokeyan.xyz/people/faculty_example.html)。

### 发表工作
-------------

A. 根据要求修改 Bib 文件，如下图所示。

    1. 为确保统一性，从谷歌学术上获取原始 bib 条目信息，
    2. 检查作者信息，确保其名字格式为“姓，名”的形式，e.g. "Han, Zheng-Fu"，注意逗号后、姓名前后有空格
    3. 添加 pdf 文件路径，格式为 `url={/bib/pdf/xxx.pdf},` 如下，建议命名为 bib 的 Label
    4. 检查以上条目结尾是否缺少逗号

<div style="text-align:center">
    <img src="/img/Bib_setup_standards.png" title="Bib 条目设置标准" width="100%"/>
</div>

B. 使用软件上传修改后的文件 [下载地址](https://gitee.com/white8chimney/QkdlabBibUpdater/releases)

    1. 登陆服务器，指示灯亮后表示连通
    2. 下载 Bib 文件，按上面的要求添加并修改（可以调换顺序，即为个人主页的展示顺序）
    3. 上传 Bib 与 PDF 文件
    4. 点击确认修改，稍等 10 秒左右后到网站上即可查看到更新

<div style="text-align:center">
    <img src="/img/qkdbibupdater.png" title="QKDLAB Bib 管理软件" width="100%" style="max-width:600px"/>
</div>


### 研究项目
--------------
添加并编辑 _projects/xxx.md 文件，并将所用到的资源文件（如图片）一起提交给管理员处理即可。
语法可参照上面提到的链接。
可选变量：

```
title: 主标题      // 主标题
notitle: true     // 可根据需求设置显示或不显示主标题
subtitle: 副标题   // 副标题
description: |
    这是一个示例项目 // 放在标题下的简短介绍
image: "/img/projects/xxx.png" // 标题配图

people:                   // 项目参与人员
  - faculty_hanzhengfu
  - faculty_chenwei

status: inactive  // 项目状态，设置为 "inactive" 时仅在“研究项目“板块出现，
                  // 而不在首页出现，用于比较简短或久远的项目
link: "http://lqcc.ustc.edu.cn" // 配合 "status:inactive" 可设置点击标题的跳转链接
no-link: false    // 是否启用链接

layout: project           // 使用的模板为 "project"
last-updated: 2022-01-17  // 更新时间
```

### 新闻（大事纪）
---------------
添加并编辑 _posts/yyyy-mm-dd-xxx.md，命令格式必须如此。
可选变量：

```
layout: post        // 模板选择为 "post"
title: "标题"        // 标题
shortnews: true     // "shortnews" 为 "true" 时主页上不显示详情链接
icon: newspaper-o   // 新闻前的小图标，"font awesome" 定义的图标包（类似表情包）
image: /img/posts/xxx.png             // 标题配图路径
image_style: "max-height: 100px;"     // 图片样式
image_link: "http://lqcc.ustc.edu.cn" // 点击图片跳转的链接
```


### 其他页面
--------------
可选用不同的 layout，参考上述板块进行自定义配置。或者直接用网页编辑软件进行编辑，生成 html 后让管理员链接一下即可。


## 管理员网站配置
================================

详情参考[Gitee 仓库](https://gitee.com/white8chimney/research-group-web)
