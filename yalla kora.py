<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
date=input('please write the date like this mm/dd/yy ')
page= requests.get(f'https://www.yallakora.com/match-center/?date={date}#')
def main(page):
    src= page.content
    soup= BeautifulSoup(src , 'lxml')
    matches_detalies=[]
    championships=soup.find_all("div",{'class':'matchCard'})
    def get_match_info(championships):
        championship_title=championships.find('h2').text.strip()
        all_matches=championships.find_all("div",{'class':'item finish liItem'})
        number_of_matches=len(all_matches)
        
        for i in range(number_of_matches):
            #get team names
            teamA=all_matches[i].find("div",{'class':'teamA'}).text.strip()
            teamB=all_matches[i].find("div",{'class':'teamB'}).text.strip()
            #get score
            match_result=all_matches[i].find("div",{'class':'MResult'}).find_all("span",{'class':'score'})
            score=f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            #get match time
            matches_time=all_matches[i].find("div",{'class':'MResult'}).find("span",{'class':'time'}).text.strip()
            #get date 
            matches_date=all_matches[i].find("div",{'class':'topData'}).find("div",{'class':'date'}).text.strip()

            matches_detalies.append({'اسم البطوله':championship_title,
                                     'الفريق الاول':teamA,'الفريق الثاني':teamB,
                                     'نتيجه المباراه':score,'ميعاد المباراه':matches_time ,'رقم المباراه':matches_date})
    for i in range(len(championships)):        
        get_match_info(championships[i])
    df=pd.DataFrame(matches_detalies)
    print(df)
    df.to_csv('yallakora1.csv',index=False,encoding='utf-8')
main(page)
=======
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
date=input('please write the date like this mm/dd/yy ')
page= requests.get(f'https://www.yallakora.com/match-center/?date={date}#')
def main(page):
    src= page.content
    soup= BeautifulSoup(src , 'lxml')
    matches_detalies=[]
    championships=soup.find_all("div",{'class':'matchCard'})
    def get_match_info(championships):
        championship_title=championships.find('h2').text.strip()
        all_matches=championships.find_all("div",{'class':'item finish liItem'})
        number_of_matches=len(all_matches)
        
        for i in range(number_of_matches):
            #get team names
            teamA=all_matches[i].find("div",{'class':'teamA'}).text.strip()
            teamB=all_matches[i].find("div",{'class':'teamB'}).text.strip()
            #get score
            match_result=all_matches[i].find("div",{'class':'MResult'}).find_all("span",{'class':'score'})
            score=f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            #get match time
            matches_time=all_matches[i].find("div",{'class':'MResult'}).find("span",{'class':'time'}).text.strip()
            #get date 
            matches_date=all_matches[i].find("div",{'class':'topData'}).find("div",{'class':'date'}).text.strip()

            matches_detalies.append({'اسم البطوله':championship_title,
                                     'الفريق الاول':teamA,'الفريق الثاني':teamB,
                                     'نتيجه المباراه':score,'ميعاد المباراه':matches_time ,'رقم المباراه':matches_date})
    for i in range(len(championships)):        
        get_match_info(championships[i])
    df=pd.DataFrame(matches_detalies)
    print(df)
    df.to_csv('yallakora1.csv',index=False,encoding='utf-8')
main(page)
#edit
>>>>>>> d0bf004c07e09d66ead28f806959850d6f5f7c75
