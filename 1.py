import requests
import random
header = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Mobile Safari/537.36'}
raw_url =  'http://qzonerqq.szscshb.com/dnf.php?u=%s&p=%s'
list1 = ['0','1','2','3','4','5','6','7','8','9']
list2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','i','z']


def get_password():
    password = ""
    for item2 in range(0,8):
        password += list2[random.randint(0,len(list2)-1)]+list1[random.randint(0,len(list1)-1)]
    print("get_password运行完毕")
    return password

def send():
    qqnumber = get_qqnumber()
    password = get_password()
    url = raw_url % (qqnumber,password)
    print("url运行完毕")
    try:
        r = requests.get(url,headers=header)
        print("requests运行完毕")
        if r.status_code == 200:
            print('qq号：%s,密码：%s,发送成功'%(qqnumber,password))
        else:
            print("发送请求失败")
    except:
        send()
    print("程序单次运行完毕")

if __name__ == "__main__":
    number = int(input("想获取几个账号密码呀："))
    for i in range(0,number):
        send()