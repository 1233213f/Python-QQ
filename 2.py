# 做一个滑动验证码的通过
from selenium import webdriver
from lxml import etree
from time import sleep
from selenium.webdriver import ChromeOptions, ActionChains # 实现规避检测
import requests
from test_distance_1 import main


# 这个是用来模拟人为拖动滑块行为，快到缺口位置时，减缓拖动的速度，服务器就是根据这个来判断是否是人为登录的。
def get_tracks(dis):
v = 0
t = 0.3
# 保存0.3内的位移
tracks = []
current = 0
mid = distance * 4 / 5
while current <= dis:
if current < mid:
a = 2
else:
a = -3
v0 = v
s = v0 * t + 0.5 * a * (t ** 2)
current += s
tracks.append(round(s))
v = v0 + a * t
return tracks

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',
'connection': 'close',
}

# 实现规避检测
options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])

bro = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)

url = 'https://qzone.qq.com/'

bro.get(url=url)

sleep(2)

# 切换iframe
bro.switch_to.frame('login_frame')

# 点击输入密码的地方进入
btn_1 = bro.find_element_by_xpath('//*[@id="switcher_plogin"]')

btn_1.click()

# 填入用户名，密码
user_input = bro.find_element_by_xpath('//*[@id="u"]')
password_input = bro.find_element_by_xpath('//*[@id="p"]')
submit_btn = bro.find_element_by_xpath('//*[@id="login_button"]')

user_input.send_keys('111111')
sleep(0.5)
password_input.send_keys('111111')
sleep(0.5)
submit_btn.click()

sleep(1)

# 获取img图片，将其下载或者截取下来
# 因为这是另一个frame，所以需要换个域
bro.switch_to.frame('tcaptcha_iframe')
tree = etree.HTML(bro.page_source)

bg_link = 'https://t.captcha.qq.com' + tree.xpath('//*[@id="slideBg"]/@src')[0]
block_link = 'https://t.captcha.qq.com' + tree.xpath('//*[@id="slideBlock"]/@src')[0]

fp = open('qq_bg.jpg', 'wb')
fp.write(requests.get(url=bg_link, headers=headers).content)
fp.close()

sleep(1)

fp = open('qq_block.jpg', 'wb')
fp.write(requests.get(url=block_link, headers=headers).content)
fp.close()

# 判断这个距离有多长,然后去按它
distance = main()

# 如果是有错误就不断的再计算
while distance == -1:
distance = main()

# # 原图的像素是680*390，而网页的是340*195，图像缩小了一倍。
# # 经过尝试，发现滑块的固定x坐标为70，这个地方有待加强，这里加20的原因上面已经解释了。
# double_distance = int((distance - 70 + 20) / 2)
# tracks = get_tracks(double_distance)
# # 由于计算机计算的误差，导致模拟人类行为时，会出现分布移动总和大于真实距离，这里就把这个差添加到tracks中，也就是最后进行一步左移。
# tracks.append(-(sum(tracks) - double_distance))

tracks = get_tracks(distance - 20)

element = bro.find_element_by_id('tcaptcha_drag_thumb')
ActionChains(bro).click_and_hold(on_element=element).perform()
for track in tracks:
ActionChains(bro).move_by_offset(xoffset=track, yoffset=0).perform()
sleep(0.5)
ActionChains(bro).release(on_element=element).perform()

sleep(10)

bro.close()