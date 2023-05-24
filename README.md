# 网页配置指南
================================

原 Github 项目[链接](https://github.com/uwsampa/research-group-web)

Fork 过来的[Gitee 仓库](https://gitee.com/white8chimney/research-group-web)

使用的 License 为 [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/)

## 文件结构
-------------------
* 配置文件
    * _config.yml: 主要版块的配置文件
    * _data/people.yml: 成员信息及个人主页链接
    * _includes/xxx.html: 各个网页组件的模板/定义
    * _layouts/xxx.html: 各个板块的网页模板/定义
    * _people/xxx.md: 个人主页的配置文件
    * _posts/xxx.md: 主页新闻的配置文件
    * _projects/xxx.md: 研究项目板块的配置文件
    * bib/pubs_original.bib: 发表工作的 bibtex 文件，其余为临时文件，不用管
    * bib/pdf: 用于存放对应的文献 pdf
    * img/xxx: 用于存放图片文件
    * others.md: 自定义更多页面的配置文件
    
* 网页文件
    * blog.html
    * css
    * img
    * index.html
    * js
    * people.html
    * publications.html
    * research.html
    
* 网页文件（打包完用于发布）
    * ../qkdlab_website
    
    
## 配置流程
---------------------

### 编辑个人网页
编辑 _people/xxx.md 文件，并将所用到的资源文件（如图片）一起提交给管理员处理即可。
具体编辑步骤可以参看这个[网页](https://qkdlab.gaokeyan.xyz/people/faculty_example.html)。

### 编辑研究项目页面
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

### 编辑新闻（大事纪）页面
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

### 编辑发表的工作页面
1. 获取原始 bibtex，并按需求从上到下排序
2. 将编辑好的文件命名为 "pubs_original.bib"，上传至 bib/ 目录下
3. 添加 pdf 文件路径（如果需要附上 pdf）
```
url={/bib/pdf/xxx.pdf},
```
4. 检查以上条目结尾是否缺少逗号
5. 提交给管理员

### 编辑其他页面
可选用不同的 layout，参考上述板块进行自定义配置。或者直接用网页编辑软件进行编辑，生成 html 后让管理员链接一下即可。

### 管理员网站配置
1. 使用组内服务器（server.gaokeyan.xyz)，环境已经配置好。（推荐使用 VS Code，安装 ssh 插件）

2. 或者在自己的电脑上安装编译工具
```
pip install bibble
gem install jekyll
```
* 注：macOS 下由于自带 Ruby 环境，安装最为方便。Linux 下可能需要手动安装 Ruby 及其开发环境（e.g. [这个教程](https://www.digitalocean.com/community/tutorials/how-to-install-ruby-on-rails-with-rbenv-on-ubuntu-20-04)）。Windows 下由于缺少 make 工具，需要更多折腾。

3. 整理各项内容
    * _config.yml，板块布置
    * _data/people.yml，成员信息
    * index.html，主页信息
    * _projects/xxx.md，组内项目
    * bib/pubs.bib，组内发表文章的 bibtex 文件
    * _posts/xxx.md，关于组内的新闻、大事
    * others.md，添加自定义页面
    * 以上步骤中，添加图片至 img 文件夹内（或其他对应的文件夹）

4. 编译生成网页
```
cd research-group-web
make
```

5. 挂载生成的网页至本机/服务器上
```
make serve
```

6. 用浏览器打开 makefile 文件中配置的网页地址（`SERVER_HOST:SERVER_PORT`，e.g. `127.0.0.1:5000`），查看效果

7. 将生成的网页（上级目录中 qkdlab_website 文件夹）打包，即已完成

## 待办事项
-------
1. 密码组 LOGO
2. 密码组简介（一小段话，放在主页，得文采好一点）
3. 组内成员信息（姓名、别称、靓照）
4. 各个项目的内容撰写（_projects/xxx.md）
5. 大事/新闻材料整理（_posts/xxx.md）
6. 往年发表的工作整理成 bibtex 文档
7. 招生/工页面的信息填写（joinus.md）
8. 个人主页编写
    1. 修改模板文件：_layouts/personal_page_template_N.html
    2. 配置个人主页：_people/xxx.md: 个人主页的配置文件

