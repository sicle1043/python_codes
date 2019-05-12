from selenium import webdriver
from PIL import Image
import tesserocr
import time
from selenium.common.exceptions import UnexpectedAlertPresentException


# 有识别结果时返回结果，无识别结果时返回字符串abcd
def coimage_recognize():  # 验证码识别
    vecode = '1234'
    coimage = Image.open("code.png")
    box = (984+250, 277+68, 984+320, 277+100)
    coimage.crop(box).save("rcode.png")  # 截取截图的验证码部分，存为rcode.png

    # 打开图片验证码，进行灰度处理及二值化
    coimage = Image.open('rcode.png')
    coimage = coimage.convert('L')
    threshold = 127
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    coimage = coimage.point(table, '1')

    # 对验证码进行8邻域降噪
    pixdata = coimage.load()
    w, h = coimage.size
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            count = 0
            if pixdata[x, y - 1] > 0:
                count = count + 1
            if pixdata[x, y + 1] > 0:
                count = count + 1
            if pixdata[x - 1, y] > 0:
                count = count + 1
            if pixdata[x + 1, y] > 0:
                count = count + 1
            if pixdata[x - 1, y - 1] > 0:
                count = count + 1
            if pixdata[x - 1, y + 1] > 0:
                count = count + 1
            if pixdata[x + 1, y - 1] > 0:
                count = count + 1
            if pixdata[x + 1, y + 1] > 0:
                count = count + 1
            if count > 5:
                pixdata[x, y] = 255
    vecode = tesserocr.image_to_text(coimage)  # 返回图片识别结果
    return vecode


# 登录信息的填写
def browser_operate():
    # 填写账号密码
    txtname = browser.find_element_by_id('txtUserName')
    txtname.send_keys('417190116')
    txtpassword = browser.find_element_by_id('TextBox2')
    txtpassword.send_keys("zly888000")
    browser.save_screenshot('code.png')  # 截图，存为code.png
    txtcode = browser.find_element_by_id('txtSecretCode')
    txtcode.send_keys(coimage_recognize())
    submitbutton = browser.find_element_by_id('Button1')
    submitbutton.click()


# 打开浏览器，尝试用broser_operate()函数填写信息并登录教务系统
if __name__ == "__main__":
    browser = webdriver.Chrome()
    browser.maximize_window()
    alertword = '1234'
    count = 0
    while count < 2:
        count = count + 1
        browser.get('http://119.145.67.59/(suz43p55ytmcr0b4x5kq0vit)\
        /xs_main.aspx?xh=417190117#')
        try:
            browser_operate()
        except UnexpectedAlertPresentException:
            webalert = browser.switch_to.alert
            alertword = webalert.text
            if alertword == '评价完后请完善个人信息和修改登入密码！！':
                print('第%s次成功' % count)
                break
            webalert.accept()
        print('第%s次失败' % count)
        time.sleep(1)
    time.sleep(10)
