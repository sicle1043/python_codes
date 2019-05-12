from selenium import webdriver
import time
import random
from selenium.common.exceptions import ElementNotVisibleException, UnexpectedAlertPresentException


# 填写单选题的function：传入题目的xpath和各个答案的概率
def sigle_choose(qxpath, p1, p2, p3, p4, p5, p6, p7, p8):
    rannum = random.randint(1, 10)
    if rannum < 1 + p1:
        ansnum = 1
    elif rannum < 1 + p1 + p2:
        ansnum = 2
    elif rannum < 1 + p1 + p2 + p3:
        ansnum = 3
    elif rannum < 1 + p1 + p2 + p3 + p4:
        ansnum = 4
    elif rannum < 1 + p1 + p2 + p3 + p4 + p5:
        ansnum = 5
    elif rannum < 1 + p1 + p2 + p3 + p4 + p5 + p6:
        ansnum = 6
    elif rannum < 1 + p1 + p2 + p3 + p4 + p5 + p6 + p7:
        ansnum = 7
    else:
        ansnum = 8
    qxpath = qxpath.replace('99', str(ansnum))
    try:
        chioce = browser.find_element_by_xpath(qxpath)
        chioce.click()
        time.sleep(1)
    except ElementNotVisibleException:
        print("此题有关联题目，无法填写")


# 填写多选题的function：传入题目的xpath 答案数量
def mul_choose(qxpath, ansqul):
    aList = random.sample(range(1, ansqul+1), 2)
    for i in aList:
        axpath = qxpath.replace('99', str(i))  # 更换为所选答案的xpath
        try:
            chioce = browser.find_element_by_xpath(axpath)
            chioce.click()
            time.sleep(1)
        except ElementNotVisibleException:
            print('此题有关联题目，无法填写')


# 自动填问卷的function，传入网站的url，调用single_choose和mul_choose两个方法进行题目的填写
def autofill(url):
    browser.get(url)
    time.sleep(1)
    xpath = "//li/a[@rel='q0_99']"  # 初始xpath，其中的99和0方便替换为题目和题号的xpath
    sigle_choose(xpath.replace('0', str(1)), 8, 2, 0, 0, 0, 0, 0, 0)
    sigle_choose(xpath.replace('0', str(2)), 5, 3, 1, 1, 0, 0, 0, 0)
    sigle_choose(xpath.replace('0', str(3)), 1, 1, 2, 4, 2, 0, 0, 0)
    sigle_choose(xpath.replace('0', str(4)), 1, 1, 2, 1, 2, 3, 0, 0)
    sigle_choose(xpath.replace('0', str(5)), 2, 5, 1, 1, 1, 0, 0, 0)
    sigle_choose(xpath.replace('0', str(6)), 2, 3, 2, 3, 0, 0, 0, 0)
    sigle_choose(xpath.replace('0', str(7)), 3, 1, 1, 1, 1, 2, 1, 0)
    sigle_choose(xpath.replace('0', str(8)), 3, 5, 2, 0, 0, 0, 0, 0)
    mul_choose(xpath.replace('0', str(9)), 8)
    sigle_choose(xpath.replace('0', str(10)), 1, 2, 1, 1, 1, 4, 0, 0)
    sigle_choose(xpath.replace('0', str(11)), 1, 2, 5, 2, 0, 2, 0, 0)
    mul_choose(xpath.replace('0', str(12)), 7)
    sigle_choose(xpath.replace('0', str(13)), 2, 3, 3, 1, 1, 0, 0, 0)
    sigle_choose(xpath.replace('0', str(14)), 2, 5, 2, 1, 0, 0, 0, 0)

    try:
        submit = browser.find_element_by_class_name('submitbutton')
        submit.click()
        time.sleep(10)
    except UnexpectedAlertPresentException:
        print('有一篇问卷内容填写不正确')  


# 主函数，控制次数
if __name__ == "__main__":
    browser = webdriver.Chrome()
    url = 'https://www.wjx.cn/jq/35195657.aspx'
    for index in range(1, 30):
        autofill(url)
        print('第%s次完成' % index)
