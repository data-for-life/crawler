import sys
import requests

http_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'Referer': 'https://www.104.com.tw/jobs/search/'
}

parameters = {
    "ro":0,                 
    'jobcat':2003000000     # Job type
}

url_104 = "https://www.104.com.tw/jobs/search/list?"

# res = requests.get('https://www.104.com.tw/jobs/search/list?',params=parameters)
res = requests.get(
    # url='https://www.104.com.tw/jobs/search/list?ro=0&jobcat=2003000000&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=16&asc=0&page=2&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1',
    url = url_104,
    headers=http_header,
    params=parameters
)

res.encoding="UTF-8"

sys.stdout = open("result","w+",encoding='UTF-8')

for i in range(1):
    for k,v in res.json()['data']['list'][i].items():
        print("|"+str(k)+"|"+str(v)+"|")