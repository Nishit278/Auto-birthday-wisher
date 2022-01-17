import pandas
import smtplib
import os
import datetime as dt
from dotenv import load_dotenv
load_dotenv()

MY_NAME = os.getenv("MY_NAME")
MY_MAIL = os.getenv("MY_MAIL")
PASSWORD = os.getenv("PASSWORD")
curr = dt.datetime.now()
date_today = curr.strftime("%m-%d")
# print(date_today)

def send_mail(name, mail):
    with open("./Input/template.txt") as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[name]", name)
        letter = letter.replace("[My Name]",MY_NAME )
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=mail, msg=f"Subject:HAPPY BIRTHDAY\n\n{letter}")

data = pandas.read_csv("./Input/dates.csv")
data["dob"] = data["dob"].astype('datetime64')

for (index, data_frame) in data.iterrows():
    # date = dt.datetime(year=curr.year, month=data_frame["month"], day=data_frame["day"]).strftime("%m-%d")
    date = data_frame["dob"].strftime("%m-%d")
    if(date_today == date):
        send_mail(data_frame["name"], data_frame["email"])









# data_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in data.iterrows()}
# # print(data_dict)
# if today_tuple in data_dict:
#     birthday_person = data_dict[today_tuple]
#     # print(birthday_person)
#     print(birthday_person["name"], birthday_person["email"])
#     send_mail(birthday_person["name"], birthday_person["email"])


# months = data["month"].to_list()
# days = data["day"].to_list()
# names = data["name"].to_list()
# mails = data.email.to_list()
# print(months)
# print(years)
# for i in range(len(data)):
#     if(curr.month == months[i] and curr.weekday() == days[i]):
#         send_mail(names[i], mails[i])