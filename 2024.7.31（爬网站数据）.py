import requests    # 请求网站的数据
import pandas      # 操作表格数据
import re          # 筛选数据（处理字符串）

for page in range(1, 282):
    # ====================请求数据====================
    # （1）确定目标网址：
    url = "https://96.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112407653684782443808_1722427201364&pn=1&pz=20&po=1&np={page}&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&dect=1&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1722427201365"
    # （2）以什么样的身份去请求？伪装成一个浏览器：wz = {"user-agent": "浏览器标识"
    wz = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
    # （3）请求数据：数据 = 模块.功能.(参数)----requests中的get功能，给定网址与身份，便能给我们数据
    res = requests.get(url, wz)
    # （4）res不是一个东西:而是由很多很多参数构成的----如res.text、res.content(二进制代码)、res.status_code(反应)···200表示成功；403表示拒绝；404表示该网址不存在；500表示该网址出问题了（没了）
    # print(res.text)
    # 最后返回的数据即网址上展示的数据，但有很多数据是不需要的数据，需要进行下一步筛选


    # ====================筛选数据====================
    # mess = "我喜欢沃玛，我喜欢憨色"
    # names = re.findall("我喜欢")
    code_list = re.findall('"f12":"(.*?)","f13"', res.text)
    name_list = re.findall('"f14":"(.*?)","f15"', res.text)
    price_list = re.findall('"f2":(.*?),"f3"', res.text)


    # ====================组合数据====================
    # name = []                 大陆叫列表、港澳台新马叫清单、英文叫list
    # print(len(name))          返回列表name中元素的个数
    # for i in range(0, 2):    # i的范围是0-2，左闭右开，即打印2次warma
    #    print("warma")
    for i in range(0, len(code_list)):
        new_list = [code_list[i], name_list[i], price_list[i]]
        print(new_list)
    # pn=1----pagenumber=1
