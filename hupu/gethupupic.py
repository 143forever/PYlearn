import requests
from bs4 import BeautifulSoup

def gethtml(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print ('-1')

def gettieziurl(html,tzlist=None):
    if tzlist==None:
        tzlist=[]
        soup=BeautifulSoup(html,'html.parser')
        #print(soup.li.name)
        li=soup.find_all('li')
        #print(li)
        for i in li:
            try:
                a=i.find_all('a',attrs={'class':'truetit'})[0]
                href=a.attrs['href']
                tieziurl='https://bbs.hupu.com'+href
                tzlist.append(tieziurl)
            except:
                continue
        return tzlist

def getpicurl(html,piculist=None):
    if piculist==None:
        piculist=[]
        soup=BeautifulSoup(html,'html.parser')
        div=soup.find('div',attrs={'class':"quote-content"})
        img=div.find_all('img')
        for i in img:
            if len(i.attrs['src'].split('?'))>1:
                picurl=i.attrs['src'].split('?')[0]
            else:
                picurl=i.attrs['data-original'].split('?')[0]
            piculist.append(picurl)
        print(len(piculist))
        return piculist

def getpic(url,path):
    try:
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
    except:
        print('-3')

def main():
    m=0
    dep=5
    url0='https://bbs.hupu.com/selfie-'
    for i in range(dep):
        urlhp=url0+str(i)
        html0=gethtml(urlhp)
        tieziurllist=gettieziurl(html0)
        for i in tieziurllist:
            tiezihtml=gethtml(i)
            picurllist=getpicurl(tiezihtml)
            for j in picurllist:
                #print(j+'\n')
                path='C:/Users/hello world/Desktop/hupu/pic/'+str(m)+'.gif'
                m=m+1
                getpic(j,path)
        

main()
