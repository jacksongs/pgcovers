# This script is designed to download covers of the major Australian newspapers.

import requests
import datetime
import shutil
import subprocess


year =  datetime.datetime.now().strftime("%Y")
month =  datetime.datetime.now().strftime("%m")
day =   datetime.datetime.now().strftime("%d")

subprocess.call(["mkdir","img"+year+month+day])

def newscorp(y,m,d):
    papers = ["http://mfeeds.news.com.au/smedia/AUSTRALIAN/NCAUS_1_%s_%s_%s_thumb_big.jpg"%(y,m,d),
        "http://mfeeds.news.com.au/smedia/HERALDSUN/NCHRS_1_%s_%s_%s_thumb_big.jpg"%(y,m,d),
        "http://mfeeds.news.com.au/smedia/TELEGRAPH/NCTELE_1_%s_%s_%s_thumb_big.jpg"%(y,m,d),
        "http://mfeeds.news.com.au/smedia/NCCOURIER/NCCM_1_%s_%s_%s_thumb_big.jpg"%(y,m,d),
        "http://mfeeds.news.com.au/smedia/ADVERTISER/NCADV_1_%s_%s_%s_thumb_big.jpg"%(y,m,d),
        ]
    for p in papers:
        r = requests.get(p, stream=True)
        if r.status_code == 200:
            with open("img"+y+m+d+"/"+p.split("/")[-1], 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        else:
            print r.status_code

newscorp(year,month,day)

subprocess.call(["convert","-delay","300","-loop","0","img"+year+month+day+"/*.jpg","covers"+year+month+day+".gif"])

subprocess.call(["rm","-rf","img"+year+month+day])
