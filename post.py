#from logging import debug
from deta import Deta
#from flask import *

# deta Base
deta = Deta("c08p64s1_M2NsZiEzbdCh4fCCK7SqBv4XAKWr3dZ3")
db = deta.Base("term")
drive = deta.Drive("term")

def add(title,url):
    judul = title.replace(" ","-")
    data = {'title': judul,'link': url+'.cast'}
    return db.put(data, judul)
def get():
    res = db.fetch()
    all_items = res.items
#    print(all_items)
    for x in all_items:
        i = x['key']
        print(i)
def delall():
    res = db.fetch()
    all_items = res.items
    print(all_items)
    # for x in all_items:
    #     i = x['key']
    #     print(i)
    #     p = db.delete(i)
    #     print(p)

#get()
delall()
# judul = input("judul > ")
# url = input("link > ")

# x = add(judul,url)
# print(x)
