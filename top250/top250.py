import requests
from bs4 import BeautifulSoup

def gethtml(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def dealhtml(html,path):
    lis={}
    if html=='':
        print('html==0')
    else:
        soup=BeautifulSoup(html,'html.parser')
        l=soup.find_all('li')
        for i in l:
            try:
                span1=i.find('span',attrs={'class':"title"})
                title=span1.string
                lis.update({'名字':title})
                span2=i.find('span',attrs={'class':"rating_num"})
                ranting=span2.text
                lis.update({'评分':ranting})
                span3=i.find('span',attrs={'class':"inq"})
                inq=span3.text
                lis.update({'   ':inq})
                with open(path,'a',encoding='utf-8') as f:
                    f.write(str(lis)+'\n')
            except:
                continue
        
def main():
    path=r'C:\Users\hello world\Desktop\top250\top250.txt'
    ym=2
    url0='https://movie.douban.com/top250?start='
    for i in range(ym):
        url=url0+str(i*25)
        html=gethtml(url)
        dealhtml(html,path)

main()
