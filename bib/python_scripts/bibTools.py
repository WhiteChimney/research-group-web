import re

class Person(object):
    bib_name = ''
    enable_website = False
    def __init__(self,name):
        self.name = name


class Bib(object):
    title = ''
    author = ''
    year = 1958
    doi = ''
    featured = False
    def __init__(self,label):
        self.label = label


def personListFromConfigFile(config_fileName):
    fConfig = open(config_fileName, 'r')
    textList = fConfig.read().split('\n\n')

    personList = []
    for text in textList:
        personInfoText = text.split('\n')
        temp_person = Person(personInfoText[0].strip().replace(':',''))
        for item in personInfoText:
            if (item.find('bib_name') != -1):
                temp_person.bib_name = item.strip().replace('bib_name: ','').replace('"','')
                personList.append(temp_person)
            if (item.find('webpage: "http://') != -1):
                temp_person.enable_website = True
    
    return personList


def revert_author_name(author_name):
    author_list = author_name.split(' and ')
    reverted_name = ''
    for name in author_list:
        if (name.find(',') != -1):
            temp = name.split(', ')
            reverted_name += temp[-1].strip() + ' ' + temp[0].strip() + ' and '
        else:
            reverted_name += name.strip() + ' and '
    reverted_name = reverted_name[0:-5]
    return reverted_name


def importBib(bib_file):
    fBib = open(bib_file, 'r')
    bibList = []
    tempBib = ''
    line = fBib.readline()

    while (line):
        if (line[0] == "@"):
            if (tempBib != ''):
                bibList.append(tempBib)
                tempBib = ''
        tempBib += line
        line = fBib.readline()
    if (tempBib != ''):
        bibList.append(tempBib)

    fBib.close()

    bibListNew = [];
    for bib in bibList:
        author_start = bib.find('{',bib.find('author'))+1
        author_end = bib.find('}',author_start)
        author_text = bib[author_start:author_end]
        author_text_ordered = revert_author_name(author_text.replace('\n',' ').replace('\r',' '))
        bibListNew.append(bib.replace(author_text,author_text_ordered))

    return bibListNew


def bib2html(bib_file, html_file, author_name):
    bibList = importBib(bib_file)
    findWork = False

    fHtml = open(html_file,'w')
    for bib in bibList:
        if (bib.find(author_name) != -1):
            if (not findWork):
                fHtml.write('<h2 id="发表工作">发表工作</h2>\n<ol>\n')
                findWork = True

            fHtml.write('<li>\n<p>')

            # author
            author_start = bib.find('{',bib.find('author'))+1
            author_end = bib.find('}',author_start)
            author_text = bib[author_start:author_end].replace(' and ',', ')
            author_text = author_text.replace(author_name,'<strong><em>'+author_name+'</strong></em>')
            author_text += ', '
            fHtml.write(author_text)
        
            # title
            title_start = bib.find('{',bib.find('title'))+1
            title_end = bib.find('}',title_start)
            title_text = bib[title_start:title_end]
            title_text += ', '
            fHtml.write(title_text)

            # journal
            journal_start = bib.find('{',bib.find('journal'))+1
            journal_end = bib.find('}',journal_start)
            journal_text = '<em>' + bib[journal_start:journal_end] + '</em>'
            journal_text += ', '
            fHtml.write(journal_text)

            # volume
            index = bib.find('volume')
            if (index != -1):
                volume_start = bib.find('{',index)+1
                volume_end = bib.find('}',volume_start)
                volume_text = bib[volume_start:volume_end]
            else:
                volume_text = ''
            fHtml.write(volume_text)

            # number
            index = bib.find('number')
            if (index != -1):
                number_start = bib.find('{',index)+1
                number_end = bib.find('}',number_start)
                number_text = '(' + bib[number_start:number_end] + ')'
                number_text += ', '
            else:
                number_text = ''
            fHtml.write(number_text)

            # pages
            index = bib.find('pages')
            if (index != -1):
                pages_start = bib.find('{',index)+1
                pages_end = bib.find('}',pages_start)
                pages_text = bib[pages_start:pages_end]
                pages_text += ', '
            else:
                pages_text = ''
            fHtml.write(pages_text)

            # ISSN
            index = bib.find('ISSN')
            if (index != -1):
                ISSN_start = bib.find('{',index)+1
                ISSN_end = bib.find('}',ISSN_start)
                ISSN_text = bib[ISSN_start:ISSN_end]
                ISSN_text += ','
            else:
                ISSN_text = ''
            fHtml.write(ISSN_text)

            # year
            year_start = bib.find('{',bib.find('year'))+1
            year_end = bib.find('}',year_start)
            year_text = bib[year_start:year_end]
            year_text += '.'
            fHtml.write(year_text)

    fHtml.write('</p>\n</li>\n</ol>')
    fHtml.close()


def sortBibForWebpage(orig_bib_fileName, sorted_bib_fileName):
    origBib = importBib(orig_bib_fileName)
    fOrderedBib = open(sorted_bib_fileName, 'w')
    order = 10000
    for bib in origBib:
        index = bib.find('featured')
        if (index != -1):
            if (bib[bib.find('{',index)+1:bib.find('}',index)] == 'true'):
                order -= 1
                yearToWrite = str(order)
        else:
            yearToWrite = bib[bib.find('{',bib.find('year'))+1:bib.find('}',bib.find('year'))]
        ordered_bib = bib.replace('year','year={'+yearToWrite+'},\n  realyear')
        if (bib.find('pdf_path') != -1):
            ordered_bib = ordered_bib.replace('url','webUrl')
            ordered_bib = ordered_bib.replace('pdf_path','url')
        fOrderedBib.write(ordered_bib.replace('abstract','noabstract'))
    fOrderedBib.close()

def extractPersonalBib(bib_name, original_bib_file, personal_bib_file):
    origBib = importBib(original_bib_file)

    fPersonalBib = open(personal_bib_file,'w')
    for bib in origBib:
        if (bib.find(bib_name) != -1):
            fPersonalBib.write(bib)
    
    fPersonalBib.close()

def text2bib(bib_text):
    index = bib_text.find('@')
    label = bib_text[bib_text.find('{',index)+1:bib_text.find('\n',index)]
    label = label.strip()
    if (label[-1] == ','):
        label = label[0:-1]
    bib = Bib(label)

    index = bib_text.casefold().find('title')
    bib.title = bib_text[bib_text.find('{',index)+1:bib_text.find('}',index)]

    index = bib_text.casefold().find('author')
    bib.author = bib_text[bib_text.find('{',index)+1:bib_text.find('}',index)]

    index = bib_text.casefold().find('year')
    bib.year = int(bib_text[bib_text.find('{',index)+1:bib_text.find('}',index)])

    index = bib_text.casefold().find('doi')
    if (index != -1):
        bib.doi = bib_text[bib_text.find('{',index)+1:bib_text.find('}',index)]

    index = bib_text.casefold().find('featured')
    if (index != -1):
        feature = bib_text[bib_text.find('{',index)+1:bib_text.find('}',index)]
        if (feature == 'true' or feature == 'True'):
            bib.featured = True
    else:
        bib.featured = False

    return bib