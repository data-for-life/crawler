import json

class Job():
    def __init__(self, id: int):
        self.id = id
    
    @property
    def total_page(self):
        return self._total_page
    
    @total_page.setter
    def total_page(self, total_page):
        self._total_page = total_page

    @property 
    def job(self):
        return self._job

    @job.setter
    def job(self, jobs):
        self._job = jobs

    @property
    def job_cnt(self):
        return self._job_cnt

    @job_cnt.setter
    def job_cnt(self, job_cnt):
        self._job_cnt = job_cnt

