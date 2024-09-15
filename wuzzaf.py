import requests
from bs4 import BeautifulSoup
import pandas as pd 
import csv
page_number=input('please inter the number of page start from 0')
page= requests.get(f'https://wuzzuf.net/search/jobs/?a=navbl&q=sustainable%20&start={page_number}')
def main(page):
    scr=page.content
    soup=BeautifulSoup(scr ,'lxml')
    jobs=soup.find_all("div",{'class','css-1gatmva'})
    number_of_jobs=len(jobs)
    job_detalies=[]
   
    def get_job_info(jobs):
        jobs_title=jobs.find("h2",{'class':'css-m604qf'}).text.strip()
        jobs_link=jobs.find("h2",{'class':'css-m604qf'}).a['href']
        company_name=jobs.find("a",{'class':'css-17s97q8'}).text.strip()
        location=jobs.find("span",{'class':'css-5wys0k'}).text.strip()
        job_status=jobs.find("span",{'class':'css-1ve4b75'}).text.strip()
        #job_site=jobs.find("span",{'class':'css-o1vzmt'}).text.strip()
        job_detalies.append({'job title':jobs_title,
                             'joblink':jobs_link,
                             'company name':company_name,
                             'location':location,
                             'job status':job_status})

    for i in range(number_of_jobs):
         get_job_info(jobs[i])
    df=pd.DataFrame(job_detalies)
    print(df) 
    df.to_csv('wuzzaf.csv',index=False,encoding='utf-8')   

main(page)    

        

   
    