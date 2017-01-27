# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 10:14:40 2016

@author: Daniel
"""

import urllib.request,re


data = []

for i in range(1,100):
    i_str_list = list(str(i))
    shenzhen_stock_id_list = list('000000') #initial 
    for j in range(len(i_str_list)):
        shenzhen_stock_id_list.pop()
    while i_str_list: 
        shenzhen_stock_id_list.append(i_str_list.pop(0))
    stock_id = ''.join(shenzhen_stock_id_list)
    
    print (stock_id)
    html = urllib.request.urlopen\
    ('http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=%s2&sty=MCSS&st=a&sr=1&p=1&ps=1000&cb=&js=var/%%c20hgticon=(x)&token=de1161e2380d231908d46298ae339369&_=1485487781886'\
     %stock_id).read().decode('UTF-8')
    html = html[html.find('"')+1:len(html)-1].split(',')
    data.append(html)
    
                                 
#    stock_add = 'http://quote.eastmoney.com/sz%s.html'%stock_id
#    html = ''
#    try:
#        html = download(stock_add)
#    except Exception as e:
#        print (e)
#    try:
#        data.append(meta(html))
#    except Exception as e:
#        print (e)
#        
  
    

    
