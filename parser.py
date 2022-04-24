import requests

def parse(  jobcat: int, 
            page: int = 1,
            ro: int = 0,
            order: int = 17, 
            isnew: int = 14 ):

    http_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
        'Referer': 'https://www.104.com.tw/jobs/search/'
    }

    parameters = {
        "ro": ro,                 
        'jobcat': jobcat,
        "order": order,
        "isnew": isnew,
        "page": page
    }

    url_104 = "https://www.104.com.tw/jobs/search/list?"

    # res = requests.get('https://www.104.com.tw/jobs/search/list?',params=parameters)
    res = requests.get(
        # url='https://www.104.com.tw/jobs/search/list?ro=0&jobcat=2003000000&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=16&asc=0&page=2&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1',
        url = url_104,
        headers=http_header,
        params=parameters
    )
    return res
