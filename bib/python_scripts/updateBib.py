# 用户上传了更新后的 bib 文件，e.g. zhangsan.modified.bib
# 现需要更新 QKDLAB.bib 及其他相关用户的 bib 文件

import bibTools
import os
import sys

site_dir = '/home/data/BA21038029/ssh_update_bib_test/research-group-web/'
main_bib_fileName = site_dir + 'bib/QKDLAB.bib'
sorted_bib_fileName = site_dir + 'bib/pubs.bib'
config_fileName = site_dir + '_data/people.yml'
personalbib_path = site_dir + 'bib/personal_bib/'
personalhtml_path = site_dir + '_includes/personal_bib_autogen/'

username = sys.argv[1]
old_bib_file = personalbib_path + username + '.bib'
new_bib_file = personalbib_path + username + '.modified.bib'

# 读取旧 bib 文件内容
old_bib_label = []
old_bib_items = bibTools.importBib(old_bib_file)
for item in old_bib_items:
    old_bib_label.append(bibTools.text2bib(item).label)

# 读取修改后的 bib 文件内容
new_bib_label = []
new_bib_items = bibTools.importBib(new_bib_file)
for item in new_bib_items:
    new_bib_label.append(bibTools.text2bib(item).label)

# 提取出新增的 bib 条目
added_bib_label = []
added_label_index = []
index = 0
for label in new_bib_label:
    if (label not in old_bib_label):
        added_bib_label.append(label)
        added_label_index.append(index)
    index += 1

# 处理新 bib 条目
personList = bibTools.personListFromConfigFile(config_fileName)
if(len(added_bib_label)):
    for index in added_label_index:
        new_bib = new_bib_items[index]

        # 更新条目至主 bib 文件
        if (bibTools.text2bib(new_bib).featured):
            # 插入条目至 QKDLAB.bib 的开头
            f = open(main_bib_fileName,'r+')
            old_content = f.read()
            f.seek(0)
            f.write(new_bib)
            f.write('\n\n')
            f.write(old_content)
            f.close()
        else:
            # 插入条目至 QKDLAB.bib 的末尾
            f = open(main_bib_fileName,'a+')
            f.write(new_bib)
            f.write('\n\n')
            f.close()
        
        # 添加条目至别的作者的 bib 开头
        for person in personList:
            if (new_bib.find(person.bib_name) != -1):
                f = open(personalbib_path+person.name+'.bib','r+')
                old_content = f.read()
                f.seek(0)
                f.write(new_bib)
                f.write('\n\n')
                f.write(old_content)
                f.close()

os.remove(old_bib_file)
os.rename(new_bib_file,old_bib_file)
for person in personList:
    bibTools.bib2html(personalbib_path+person.name+'.bib', personalhtml_path+person.name+'.bib.html', person.bib_name)

bibTools.sortBibForWebpage(main_bib_fileName, sorted_bib_fileName)
