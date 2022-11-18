---
layout: default
title: 网页配置使用指南
---

================================

## 配置流程
================================

### 软件与模板下载

1. **视频教程**：[睿客网盘](https://rec.ustc.edu.cn/share/5a1d26a0-674d-11ed-b618-f96531483a4d)可直接观看
2. 软件下载：*QKDLAB Bib 管理软件*（点击下载：[Windows](http://qkdlab.gaokeyan.xyz/files/QkdlabBibUpdater.exe) or [macOS](http://qkdlab.gaokeyan.xyz/files/QkdlabBibUpdater.dmg)）
3. 本「指南」页面及示例[个人网页](https://qkdlab.gaokeyan.xyz/people/faculty_example/faculty_example.html)的 [md 原文件](http://qkdlab.gaokeyan.xyz/files/md_template.zip)，可以作为一些 Markdown 语法使用的参考。

<br>

### 个人网页配置
--------------
1. 打开软件，按图所示步骤**下载**个人主页的 md 文件（第一次下载下来的是模板文件，请将文件名改为自己的**科大邮箱前缀**）
2. **编辑** _people/xxx.md 文件，并将所用到的资源文件（如图片）放置于同一目录下
3. 具体编辑 md 文件的步骤可以参看这个[**网页**](https://qkdlab.gaokeyan.xyz/people/faculty_example/faculty_example.html)
4. 点击软件的**上传并布署网页**的按钮，等待一会即可在本网站查看修改效果

<div style="text-align:center">
    <img src="/img/help/upload_personal_page.png" title="如何上传个人主页" width="100%"/>
</div>

<br>

### 发表工作维护
-------------
<div style="text-align:center">
    <img src="/img/help/Upload_bib.png" title="通过软件维护 bib 条目" width="100%"/>
</div>

1. 打开软件，按上图所示步骤**下载**个人的 bib 文件
2. **编辑** `bib/personal_bib/xxx.bib` 文件(*~辛苦三分钟，造福全组人~*)
    1. 为确保信息的完整、准确与统一，请老师同学从学术出版商的页面上获取原始 BibTeX 条目信息（如 PR 系列到 APS 官网，OL、OE 等到 OSA 网站上去下载），务必获取**准确的 DOI 号**
    2. 如果只能下载到 RIS 格式的（如 Springer 旗下的网站），可以到这个[在线网站](https://www.bruot.org/ris2bib/)进行转换（如下图左所示）
    3. **检查作者信息**，确保 bib 条目中的名字格式为“姓，名”或“名 姓”的其中之一。且所用名称与组内成员发表文章时常用的名称一致。一般三个字以上的作者的名之间用短横相连，例如，"Han, Zheng-Fu"或"Zheng-Fu Han"。[这里](http://qkdlab.gaokeyan.xyz/files/组内成员BIB使用名称列表.txt)有一份组内成员 Bib 条目中的名称列表，请仔细比对（如有遗漏，请联系管理员添加）。这一点非常重要，关系到文章作者的识别。
    4. 如果要**添加 pdf 文件**，请放置在 `bib/pdf` 路径下，格式为 `pdf_path={/bib/pdf/xxx.pdf},` 如下图右所示
3. 点击软件的**上传并布署网页**的按钮，等待一会即可在本网站查看修改效果

<div style="text-align:center">
    <img src="/img/help/online_ris2bib.png" title="RIS 在线转成 BIB" width="44%"/>
    <img src="/img/help/Bib_setup_standards.png" title="Bib 条目设置标准" width="55%"/>
</div>



### 研究项目
--------------
打开软件下载文件，复制之前的项目文件作为模板，编辑 `_projects/yyyymm_some_project/yyyymm_some_project.md` 文件，并将所用到的资源文件（如图片）放在同一目录下，最后使用软件上传。（yyyy 指年，mm 指月）
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
打开软件下载文件，复制之前的 posts 文件作为模板，编辑 _posts/yyyy-mm-dd-some_news.md，命令格式必须如此。（yyyy 指年，mm 指月，dd 指日）
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
