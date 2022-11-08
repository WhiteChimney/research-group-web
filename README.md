# 量子密码组网页配置指南
================================

原 Github 项目[链接][https://github.com/uwsampa/research-group-web]
使用的 [License][https://creativecommons.org/licenses/by-nc/4.0/]

## 文件结构
-------------------
* 配置文件
    * _config.yml: 主要版块的配置文件
    * _data/people.yml: 成员信息及个人主页链接
    * _includes/xxx.html: 各个网页组件的模板/定义
    * _layouts/xxx.html: 各个板块的网页模板/定义
    * _posts/xxx.md: 主页新闻的配置文件
    * _projects/xxx.md: 研究项目板块的配置文件
    * bib/pubs.bib: 发表工作的 bibtex 文件，publications.tmpl 为临时文件，不用管
    * img/xxx: 用于存放图片文件
    * code.md: 自定义更多页面的配置文件
    
* 网页文件（本地生成的）
    * blog.html
    * css
    * img
    * index.html
    * js
    * people.html
    * publications.html
    * research.html
    
* 网页文件（打包完用于发布）
    * _site/xxx
    
    
## 配置流程
---------------------
1. 安装编译工具
    * > pip install bibble
    * > gem install jekyll
    
2. 编辑各项内容，添加信息
    * 编辑 _config.yml，布置板块
    * 编辑 _data/people.yml，添加成员信息
    * 编辑 _projects/xxx.md，添加组内项目
    * 编辑 bib/pubs.bib，整理组内发表文章的 bibtex 文件
    * 编辑 _posts/xxx.md，整理关于组内的新闻、大事
    * 修改 code.md，配置对应的 layout，添加自定义页面
    * 添加图片至 img 文件夹内
    
3. 编译生成网页
    * > make 
    * > make serve
    
4. 检查并提交生成完的网页

