# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zR76S5tkKrsfdib68y2FLOlei0Ch6Xmz
"""

def login_feehive(vtuno,password,pb):
  print('vtuno : ',vtuno)
  print('password : ',password)

  import requests
  #from termcolor import colored
  r = requests.Session()
  host = "https://www.vijayabankonline.com"
  url = 'https://www.vijayabankonline.com/FeeHiveWeb/FeeHive/Login/VELTECHUNI'
  match_text = 'Incorrect Username or Password.'
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
  "Accept": "*/*",
  'Host': "www.vijayabankonline.com",
  'Referer': 'https://www.google.com/'

  }
  data = r.get(url,headers=headers)
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
  "Accept": "*/*",
  'Host': "www.vijayabankonline.com",
  'Referer': 'https://www.google.com/'}
  data = r.get(url,headers=headers)
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(data.text,'html.parser')
  CaptchaImage = soup.find_all('img',attrs={'id':'CaptchaImage'})[0]
  captcha_url = host+CaptchaImage['src']
  headers['Referer'] = 'https://www.vijayabankonline.com/FeeHiveWeb/FeeHive/Login/VELTECHUNI'
  data = r.get(captcha_url,headers=headers)
  with open('captcha.png','wb+') as f:
    f.write(data.content)
  #from IPython.display import Image,display
  #display(Image(data=data.content))
  def img_to_text():
    import requests
    api_key = 'acc_43f272278ea3f13'
    api_secret = 'dbbd9b26869cde1d188e81aa97d1a71a'
    image_path = 'captcha.png'
    response = requests.post(
        'https://api.imagga.com/v2/text',
        auth=(api_key, api_secret),
        files={'image': open(image_path, 'rb')})
    img_data = response.json()
    captcha_text = img_data['result']['text'][0]['data']
    return captcha_text
  CaptchaDeText = lambda text:text.split('=')[-1]
  img_text = img_to_text()
  img_text = img_text.replace('.','')
  img_text = img_text.replace(':','')
  img_text = img_text.replace(',','')
  img_text = img_text.replace('*','')
  print('image text : ',img_text)
  data = {
      "Username":vtuno,
      "Password":password,
      "chkTerms":"Remember+Me",
      "CaptchaDeText":CaptchaDeText(captcha_url),
      "CaptchaInputText":img_text
  }
  rsp1 = r.post(url,headers=headers,data=data)
  if match_text in rsp1.text:
    #print(colored('Incorrect Password','red'))
    push = pb.push_note("Feehive Login Failed", vtuno+"\n"+password)
    push = pb.push_file(file_url="https://e7.pngegg.com/pngimages/907/821/png-clipart-thumbs-down-emoji-smiley-emoji-face-emoticon-thumb-smiley-thumbnail.png", file_name="Failed.png", file_type="image/png")
  elif 'Error: captcha is not valid!' in rsp1.text:
    #print(colored('captcha is nor valid','red'))
    print('-'*35)
    login_feehive(vtuno,password)
  else:
    #print(colored('Login Success','green'))
    push = pb.push_note("Feehive Login Success", vtuno+"\n"+password)
    push = pb.push_file(file_url="https://i.pinimg.com/originals/74/fb/dc/74fbdc181cf987f832be99b71810b682.png", file_name="success.png", file_type="image/png")
  print('-'*35)

from pushbullet import Pushbullet
pb = Pushbullet("o.XQlmD2OWaMGQZysvlc9fUbK1pyM0FE2z")
'''with open('data.txt','r') as f:
  credentials = f.readlines()
for password in credentials:
  login_feehive('vtu14236',password,pb)'''
import time
for i in range(1,100):
    login_feehive('vtu14236',"999107201014236",pb)
    time.sleep(60*30)



