---
layout: default
title: 网页配置使用指南
---

================================

## 配置流程
================================

### 软件与模板下载

1. 软件下载：*QKDLAB Bib 管理软件*（点击下载：[Windows](http://qkdlab.gaokeyan.xyz/files/QkdlabBibUpdater.exe) or [macOS](http://qkdlab.gaokeyan.xyz/files/QkdlabBibUpdater.dmg)）



2. 「个人主页」模板文件：[点击下载](http://qkdlab.gaokeyan.xyz/files/example_template.zip)
3. 「研究项目」模板文件：[点击下载](http://qkdlab.gaokeyan.xyz/files/projects_template.zip)
4. 「新闻」模板文件：[点击下载](http://qkdlab.gaokeyan.xyz/files/posts_template.zip)

### 个人网页配置
--------------
1. 下载个人主页的模板文件
2. 编辑 _people/xxx.md 文件，并将所用到的资源文件（如图片）放置于同一目录下
3. 具体编辑 md 文件的步骤可以参看这个[网页](https://qkdlab.gaokeyan.xyz/people/faculty_example/faculty_example.html)
4. 使用 *QKDLAB Bib 管理软件* 打开临时文件目录
5. 将编辑好的文件放置于如图所示的目录下
6. 点击软件的上传并布署网页的按钮，等待约 10 秒后即可在本网站查看修改效果

<div style="text-align:center">
    <img src="/img/help/upload_personal_page.png" title="如何上传个人主页" width="100%"/>
</div>


### 发表工作维护
-------------

* 根据要求修改 Bib 文件，如下图所示。(*~辛苦一分钟，造福全组人~*)
    1. 为确保信息的完整、准确与统一，请老师同学从学术出版商的页面上获取原始 bibtex 条目信息，（如 PR 系列到 aps 官网，ol、oe 等到 osa 网站上去下载）
    2. 如果只能下载到 ris 格式的，可以到这个[在线网站](https://www.bruot.org/ris2bib/)进行转换
    3. 检查作者信息，确保 bib 条目中的名字格式为“姓，名”或“名 姓”的其中之一；三个字以上的作者的名之间用短横相连。例如，"Han, Zheng-Fu"或"Zheng-Fu Han"。这一点非常重要，关系到文章作者的识别。[这里]()有一份组内成员 Bib 条目中的使用名称列表，请仔细比对。
    4. 添加 pdf 文件，放置在 `bib/pdf` 路径下，格式为 `pdf_path={/bib/pdf/xxx.pdf},` 如图所示。
    5. 检查以上条目结尾是否缺少逗号

<div style="text-align:center">
    <img src="/img/help/Bib_setup_standards.png" title="Bib 条目设置标准" width="100%"/>
</div>

* 使用软件上传修改后的文件
    1. 登陆服务器（登陆信息请咨询管理员），指示灯亮后表示连通
    2. 下载 Bib 文件，按上面的要求添加并修改（可以调换顺序，个人主页的展示顺序会同步修改）
    3. 上传 Bib 与 PDF 文件
    4. 点击确认修改，稍等 10 秒左右后到网站上即可查看到更新

<div style="text-align:center">
    <img src="/img/help/qkdbibupdater.png" title="QKDLAB Bib 管理软件" width="100%" style="max-width:600px"/>
</div>


### 研究项目
--------------
添加并编辑 `_projects/yyyymm_some_project/yyyymm_some_project.md` 文件，并将所用到的资源文件（如图片）放在同一目录下，最后使用软件上传。（yyyy 指年，mm 指月）
语法可参照上面个人主页配置时提到的链接。
可选变量：

<pre class="pre-scrollable">
    title: 主标题      // 主标题
    notitle: true     // 可根据需求设置显示或不显示主标题
    subtitle: 副标题   // 副标题
    description: |
        这是一个示例项目 // 放在标题下的简短介绍
    image: "/projects/yyyymm_some_project/xxx.png" // 标题配图

    people:                   // 项目参与人员
    - faculty_hanzhengfu
    - faculty_chenwei

    status: inactive  // 项目状态，设置为 "inactive" 时仅在“研究项目“板块出现，
                    // 而不在首页出现，用于比较简短或久远的项目
    link: "http://lqcc.ustc.edu.cn" // 配合 "status:inactive" 可设置点击标题的跳转链接
    no-link: false    // 是否启用链接
    layout: project           // 使用的模板为 "project"
    last-updated: 2022-01-17  // 更新时间
</pre>




### 新闻（大事纪）
---------------
添加并编辑 _posts/yyyy-mm-dd-some_news.md，命令格式必须如此。（yyyy 指年，mm 指月，dd 指日）
可选变量：

<pre class="pre-scrollable">
    layout: post        // 模板选择为 "post"
    title: "标题"        // 标题
    shortnews: true     // "shortnews" 为 "true" 时主页上不显示详情链接
    icon: newspaper-o   // 新闻前的小图标，"font awesome" 定义的图标包（类似表情包）
    image: /img/posts/yyyy-mm-dd-some_news/xxx.png             // 标题配图路径
    image_style: "max-height: 100px;"     // 图片样式
    image_link: "http://lqcc.ustc.edu.cn" // 点击图片跳转的链接
</pre>


### 其他页面
--------------
可选用不同的 layout，参考上述板块进行自定义配置。或者直接用网页编辑软件进行编辑，生成 html 后让管理员链接一下即可。


## 管理员网站配置
================================

详情参考[Gitee 仓库](https://gitee.com/white8chimney/research-group-web)
