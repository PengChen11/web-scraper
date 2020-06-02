import requests as req
from bs4 import BeautifulSoup as BS


def get_citations_needed_count(url):
    '''the function to return the number of cases that needed Citations'''
    response = req.get(url)

    content = response.content

    info = BS(content, 'html.parser')

    count = len(info.findAll(href="/wiki/Wikipedia:Citation_needed"))
    return count


def get_citations_needed_report(url):
    '''the function to return the paragrahs that need Citations'''
    
    response = req.get(url)

    content = response.content

    info = BS(content, 'html.parser')

    para = info.findAll(href="/wiki/Wikipedia:Citation_needed")

    txt_list =[]

    for txt in para:

        start = txt.parent
        start_str = str(start)
        while start_str.startswith("<p") != True:#go find the parent p tag
            if not start:
                break
            start = start.parent
            start_str = str(start)
        
        modified_str = start_str
        for i in range(start_str.count("<")):# converting p tag into pure string of words
            
            begin = modified_str.find("<")
            end = modified_str.find(">",begin+1)

            modified_str = modified_str[:begin] + modified_str[end+1:]
        
        txt_list.append(modified_str)
    output = f'There are {len(para)} cases need Citation' + '\n' +'\n'
    for info in txt_list:
        output += info + '\n'

    return output



if __name__ == "__main__":
    test = get_citations_needed_count('https://en.wikipedia.org/wiki/Battle_of_the_Bulge')
    print(test)
    
    test2 = get_citations_needed_report('https://en.wikipedia.org/wiki/Battle_of_the_Bulge')

    print(test2)
