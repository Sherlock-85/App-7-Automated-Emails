import yagmail
import pandas
import openpyxl
import datetime
import time
from news import NewsFeed


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(topic=row['topic'], from_date=yesterday, to_date=today, language='en')
    email = yagmail.SMTP(user="c.wheezy@gmail.com", password="hol1985c")
    email.send(to=row['email'],
               subject=f"Your {row['topic']} news for today!",
               contents=f"Hi {row['name']}\n  See what is on about {row['topic']} today."
                        f"\n{news_feed.get()} \n Chris")


while True:
    if datetime.datetime.now().hour == 11 and datetime.datetime.now().minute == 35:
        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)