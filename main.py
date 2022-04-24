import sys
import json
import parser
import job
import logging
from util import to_json

logging.basicConfig(
    filemode="a+",
    filename="crawler.log",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)

with open('JobCat.json', encoding="utf-8-sig") as jsonfile:
    job_type = json.load(jsonfile)

job_types = list()
job_list = list()

for i in range(18):
    for j in job_type[i]['n']:
        for k in j['n']:
            job_types.append(k['no'])
            job_list.append(job.Job(k['no']))
    
for i in range(len(job_types)):
    job_type = job_types[i]
    res = parser.parse(
        jobcat = job_type
    )
    res.encoding="UTF-8"
    job_list[i].total_page = int(res.json()['data']['totalPage'])
    job_list[i].job_cnt = int(res.json()['data']['totalCount'])

total_jobs = list()
for i in range(len(job_types)):
    tmp_jobs = list()
    for page in range(1,job_list[i].total_page+1):
        res = parser.parse(
            jobcat = job_list[i].id,
            page = page
        )
        res.encoding="UTF-8"
        for j in range(len(res.json()['data']['list'])):
            if res.json()['data']['list'][j] not in tmp_jobs:
                # total_jobs.append(res.json()['data']['list'][j])
                tmp_jobs.append(res.json()['data']['list'][j])
            # for k,v in res.json()['data']['list'][i].items():
                # print("|"+str(k)+"|"+str(v)+"|")
                # print(k,v)
    # job_list[i].jobs = tmp_jobs
    # print(len(job_list[i].jobs))
    # print(job_list[i].job_cnt)
    logging.info('ID: ' + str(job_types[i]))
    logging.info('Total count on 104: ' + str(job_list[i].job_cnt))
    logging.info('Total count parserd: ' + str(len(tmp_jobs)))
    to_json(
        filename= "./data/"+str(job_types[i])+".json",
        data=tmp_jobs
    )

# to_json(
#     data = total_jobs
# )