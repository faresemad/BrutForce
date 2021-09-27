from requests import post
url=input("Enter Website Url: ")
login_data={"username":'USER' , "passowrd":'PASSWORD' , "login":'SUBMIT'}
req =post(url,data=login_data)
#print(req.content)
if "اى كلمه موجوده ف الصفحه بعد ما تفتح".encode() in req.content:
    print("Welcome in your Account")
else:
    print("Login Faild")