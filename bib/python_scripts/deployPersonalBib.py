# 基于 QKDLAB.bib 更新个人 bib 数据以搭建网站

import bibTools
from bibTools import Person

site_dir = '/home/data/BA21038029/ssh_update_bib_test/research-group-web/'
main_bib_fileName = site_dir + 'bib/QKDLAB.bib'
sorted_bib_fileName = site_dir + 'bib/pubs.bib'
config_fileName = site_dir + '_data/people.yml'
personalbib_path = site_dir + 'bib/personal_bib/'
personalhtml_path = site_dir + '_includes/personal_bib_autogen/'

# 对原 bib 文件进行排序
# 标记有 featured = {true} 的项进行加权排序
# 其余项使用年份以默认排序

# 从配置文件 people.yml 生成 person list
personList = bibTools.personListFromConfigFile(config_fileName)

# 将原始 bib 文件排序，用以在网页以定序显示
bibTools.sortBibForWebpage(main_bib_fileName, sorted_bib_fileName)

# 处理 bib 条目
for person in personList:
    author_name = person.bib_name
    personalbib_name = personalbib_path + person.name + '.bib'
    bibTools.extractPersonalBib(author_name,main_bib_fileName,personalbib_name)
    if (person.enable_website):
        personalhtml_name = personalhtml_path + person.name + '.bib.html'
        bibTools.bib2html(personalbib_name,personalhtml_name,author_name)
        
