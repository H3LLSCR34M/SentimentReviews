from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup 
import csv
import re
from lxml import html
from json import dump,loads
import json
from re import sub
from dateutil import parser as dateparser
from time import sleep
import re


def convertUrl(prodName):
    mainUrl = "https://www.amazon.com/s?k="+ prodName
    return mainUrl

url=convertUrl("macbookpro")
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
r = requests.get(convertUrl(url),headers =headers)

root = html.fromstring(r.content)
link = root.xpath('''//a[contains(@class,'a-link-normal') and contains(@class, 'a-text-normal')]/a''')
#print (link[0].attrib["href"])

#print(link)

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
r = requests.get(convertUrl("https://www.amazon.com/s?k=iphone+11&i=electronics&ref=nb_sb_noss_1"),headers =headers)

soup=BeautifulSoup(r.text,'lxml')
list1=[]
list2=[]

temp=soup.findAll("a")
for t in temp:
    string=str(t.get("class"))
    if string.__contains__("a-link-normal") and string.__contains__("a-text-normal") and not string.__contains__("s-no-hover"):
          list1.append(t.get("href"))

temper=soup.findAll("div")
for s in temper:
    string=str(s.get("data-asin"))
    if not string=="None":
        list2.append(s.get("data-asin"))

print(list1[0])