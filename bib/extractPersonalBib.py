site_dir = '/home/ubuntu/research-group-web/'
orig_bib_fileName = site_dir + 'bib/pubs_original.bib'
ordered_bib_fileName = site_dir + 'bib/pubs.bib'
config_fileName = site_dir + '_data/people.yml'
personalbib_path = site_dir + '_includes/personal_bib_autogen/'

def revert_author_name(author_name):
    author_list = author_name.split(' and ')
    reverted_name = ''
    for name in author_list:
        temp = name.split(', ')
        reverted_name += temp[-1] + ' ' + temp[0] + ', '
    reverted_name = reverted_name[0:-2]
    return reverted_name

def bib2html(bib_text, author_name):
    head_text = '<li>\n<p>'
    foot_text = '</p>\n</li>\n'

    # author
    author_start = bib_text.find('{',bib_text.find('author'))+1
    author_end = bib_text.find('}',author_start)
    author_text = bib_text[author_start:author_end]
    author_text = revert_author_name(author_text)
    author_text = author_text.replace(author_name,'<strong><em>'+author_name+'</strong></em>')
    author_text += ', '
    
    # title
    title_start = bib_text.find('{',bib_text.find('title'))+1
    title_end = bib_text.find('}',title_start)
    title_text = bib_text[title_start:title_end]
    title_text += ', '

    # journal
    journal_start = bib_text.find('{',bib_text.find('journal'))+1
    journal_end = bib_text.find('}',journal_start)
    journal_text = '<em>' + bib_text[journal_start:journal_end] + '</em>'
    journal_text += ', '

    # volume
    index = bib_text.find('volume')
    if (index != -1):
        volume_start = bib_text.find('{',index)+1
        volume_end = bib_text.find('}',volume_start)
        volume_text = bib_text[volume_start:volume_end]
    else:
        volume_text = ''

    # number
    index = bib_text.find('number')
    if (index != -1):
        number_start = bib_text.find('{',index)+1
        number_end = bib_text.find('}',number_start)
        number_text = '(' + bib_text[number_start:number_end] + ')'
        number_text += ', '
    else:
        number_text = ''

    # pages
    index = bib_text.find('pages')
    if (index != -1):
        pages_start = bib_text.find('{',index)+1
        pages_end = bib_text.find('}',pages_start)
        pages_text = bib_text[pages_start:pages_end]
        pages_text += ', '
    else:
        pages_text = ''

    # ISSN
    index = bib_text.find('ISSN')
    if (index != -1):
        ISSN_start = bib_text.find('{',index)+1
        ISSN_end = bib_text.find('}',ISSN_start)
        ISSN_text = bib_text[ISSN_start:ISSN_end]
        ISSN_text += ','
    else:
        ISSN_text = ''

    # year
    year_start = bib_text.find('{',bib_text.find('year'))+1
    year_end = bib_text.find('}',year_start)
    year_text = bib_text[year_start:year_end]
    year_text += '.'

    return head_text+author_text+title_text+journal_text+volume_text+number_text+pages_text+ISSN_text+year_text+foot_text

class Person(object):
    bib_name = ''
    enable_website = False
    def __init__(self,name):
        self.name = name


# 读取配置文件 people.yml
fConfig = open(config_fileName, 'r')
tempList = fConfig.read().split('\n\n')

personList = []
index = 0
for person_text in tempList:
    tempPersonList = tempList[index].split('\n')
    temp_person = Person(tempPersonList[0].strip().replace(':',''))
    for item in tempPersonList:
        if (item.find('bib_name') != -1):
            temp_person.bib_name = item.strip().replace('bib_name: ','').replace('"','')
            personList.append(temp_person)
        if (item.find('webpage: "http://') != -1):
            temp_person.enable_website = True
    index += 1


# 打开原始文件读取 bib 条目

fOrigBib = open(orig_bib_fileName, 'r')
origBib = []
tempBib = ''
line = fOrigBib.readline()

while (line):
    if (line[0] == "@"):
        origBib.append(tempBib)
        tempBib = ''
    tempBib += line
    line = fOrigBib.readline()
origBib.append(tempBib)

fOrigBib.close()

# 将原始 bib 文件排序，用以在网页以定序显示
fOrderedBib = open(ordered_bib_fileName, 'w')
index = 0
for bib in origBib:
    index += 1
    ordered_bib = bib.replace('year','\n  year={'+str(index)+'},\n  realyear')
    fOrderedBib.write(ordered_bib)
fOrderedBib.close()

# 处理 bib 条目
for person in personList:
    if (person.enable_website):
        author_name = person.bib_name
        personalbib_name = personalbib_path + person.name + '.bib.html'
        fPersonalBib = open(personalbib_name,'w')
        fPersonalBib.write('<h2 id="发表工作">发表工作</h2>\n<ol>\n')
        for bib in origBib:
            if (bib.find(author_name) != -1):
                fPersonalBib.write(bib2html(bib,revert_author_name(author_name)))
        fPersonalBib.write('</ol>')
        fPersonalBib.close()
