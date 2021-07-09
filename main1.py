from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyme(title,msg):
    notification.notify(
    title=title,
    message=msg,
    #app_icon= "C:\Users\HP\Desktop\corona project\hnet.com-image.ico",
    timeout=3
    )

def getname(url):
    r=requests.get(url)
    return r.text
if __name__=="__main__":
    while True:
        #notifyme("Arnima","Lets us together stop the covid 19 outbreak")
        html_data=getname('https://www.mohfw.gov.in/')
        #print(html_data)
        soup = BeautifulSoup(html_data, 'html.parser')
        #print(soup.prettify())
        mydatastructure = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            mydatastructure+=tr.get_text()
            #print(mydatastructure)
        mydatastructure=mydatastructure[1:]
        itemlist=mydatastructure.split("\n\n")
        #print(itemlist)
        statelist = ["Uttar Pradesh","West Bengal"]
        for item in itemlist[:23]:
            datalist =  item.split("\n")
            if datalist[1] in statelist: 
                title="Cases of COVID-19"
                msg = f"STATE {datalist[1]} \n Indian: {datalist[2]}  Foreign :{datalist[3]} \n Cured :{datalist[4]} \nDeath :{datalist[5]}"
                notifyme(title,msg)
                time.sleep(2)
        time.sleep(3600)
