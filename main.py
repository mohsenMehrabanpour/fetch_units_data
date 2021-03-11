"""
	@Author_name : Mohsen Mehrabanpour
	@Author_email : flash2000w@gmail.com
	@date : Wed, 11 Mar 2021
	@version : 1.000
"""

from tools import md5_generator
import requests
import time
from parser import unit_parser

class User():
    headers = {
            'Host': 'pooya.khayyam.ac.ir',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive'
            }


    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.session = requests.session()


    def login(self):
        url = "https://pooya.khayyam.ac.ir/gateway/UserInterim.php"
        body = {
            'UserPassword' : md5_generator(self.password),
            'pswdStatus': 'mediocre',
            'UserID': self.username,
            'DummyVar': ''
        }
        for _ in range(3):
            try:
                login = self.session.get(
                    url, headers=self.headers, timeout=8
                    )  
                login = self.session.post(
                    url, data=body,headers=self.headers,timeout=8
                    )  
                return True
            except:
                    time.sleep(3)
        return False


    def get_courses(self):
        url = 'https://pooya.khayyam.ac.ir/educ/stu_portal/PresentedCoursesForm.php'
        body = {
            'FacCode' : '54',
            'EducGrp' : 'all',
            'ShowBtn' : 'نمایش'
        }
        for _ in range(3):
            try:
                response = self.session.post(
                    url, data=body,headers=self.headers,timeout=4
                    )
                return response.text
            except:
                time.sleep(5)


if __name__ == '__main__':
    username = input('import your username :')
    password = input('import your password :')
    user = User(username=username,password=password)
    if user.login():
        print('**user logged in successfully**')
        html = user.get_courses()
        f = open("units.json", "w")
        f.write(unit_parser(html))
        f.close()
        print('*'*80)
        print('units fetched and saved as a json file sucessfully...')
        print('*'*80)
    else:
        print('something wrong happend , please report this bug...')