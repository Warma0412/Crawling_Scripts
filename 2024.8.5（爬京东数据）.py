# 目标：获取京东某个冰箱商品的评论
# 1.为每一个评论创建一个文件夹
# 2.评论的文本保存为一个text文档，评论的图片、评论的视频都下载到文件夹中
import os

# ====================数据获取======================
# 开发者工具——放大镜——搜索关键词——标头中复制网址
import requests    # 导入请求模块
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36", "cookie": "jsavif=1; __jdv=181111935|direct|-|none|-|1722857358459; shshshfpa=e7b60ff5-852e-03c0-dd1b-d263f15db71c-1722857358; shshshfpx=e7b60ff5-852e-03c0-dd1b-d263f15db71c-1722857358; __jdu=17228573584591203546266; areaId=2; ipLoc-djd=1-72-55653-0; mba_muid=17228573584591203546266; mba_sid=17228573591453963417831325215.1; 3AB9D23F7A4B3C9B=XFNL7NGIXHTZBNMS4D377HJILMFH4NN45X5C6GVHK5E5HWMCCKD5SCFPUSN4ATC33BBQPLIGI4CUTVODGJTQ5PNDEE; TrackID=1-W8LeU2H9JoFhNGarGRiYJ2LNcJn0GAilVKZ4aHIvShsad2av0idjOZPMbe9_vAacWBYjJHkCBzjzMpv8rMBrmxrR31sxUGBGmKKRJrcOA9PwqliGZHeyDt0-gRLTCzX; thor=AE0AAA6EF7D372735AAE88D78252A99687069AB8BFFCA41E650F55CA4183928996D30C34DFF10887868339A085B1B255C74A47420D2C17ABA8AD2F44FA8B93CF07BD0EE20DCA27974987168218EC596C04EAF81479904D253737D6D891EC3658D601A2F1C026916AC82A263FC094124B477D4DED900D586C690B991E7CF113B229B2D0E37B93CCD8C206362769B827BB8DF7128A88FDD7E7BB0288C4EA73227F; pinId=6THHwptVTizcQz6pTpW-8LV9-x-f3wj7; pin=jd_63029eb667890; unick=jd_180745bvn; ceshi3.com=000; _tp=cCGt1fZUkJFiOtGGtgA3jy%2FQapK19EBk5jP15s9A5Cg%3D; _pst=jd_63029eb667890; __jda=181111935.17228573584591203546266.1722857358.1722857358.1722857358.1; __jdc=181111935; token=11e89a8b31e2e0bb46652aafaa106d2e,3,957143; __jdb=181111935.9.17228573584591203546266|1.1722857358; 3AB9D23F7A4B3CSS=jdd03XFNL7NGIXHTZBNMS4D377HJILMFH4NN45X5C6GVHK5E5HWMCCKD5SCFPUSN4ATC33BBQPLIGI4CUTVODGJTQ5PNDEEAAAAMREJKTMMIAAAAACRXUJO7MMW2GDYX; _gia_d=1; flash=3_UMb4CXALJY-hppNz4jWRzBpxHnYNQPcrjT0Jf07fiXzDVNmPcBNASsT_NIKc1WZKKRlv1lf_IQ7TDqDvhPMKzgf9u9bVFo9c9HYay4XFvay1HYFKXDf98-gqhdbMh_wIQpa9Tk8JnMw3ITiYFvm8w-NUpv7u6AmgXmstJBn7cOvMV8_09iTZaV**; shshshfpb=BApXSBqFdIfRAQKHld2ntdG_SuxRKmwbGBmDEdHdo9xJ1MhCMrYC2"}     # 伪装
page = 0
count = 1
while True:
    url = "https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1722857897404&body=%7B%22productId%22%3A100053932894%2C%22score%22%3A0%2C%22sortType%22%3A5%2C%22page%22%3A{page}%2C%22pageSize%22%3A10%2C%22isShadowSku%22%3A0%2C%22fold%22%3A1%2C%22bbtf%22%3A%22%22%2C%22shield%22%3A%22%22%7D&h5st=20240805193817407%3Bi69g96mnzyt5mm93%3Bfb5df%3Btk03wa7081b6718nNNcmofTHgHVfByZ9h6oAjGR5sMzRBPAw_pn-b2VgkcMQAfTGGr-V-B61wnWLgLNK96RL5l-EpAJz%3B01a7800c81458852dc0f40671aeae85e%3B4.7%3B1722857897407%3BVOL_D-5iFxUUVsU7qYqplP-Fmz0uWldTf_uHv8GF74g3A8GNrHzAcjHuRzCCOSHMZWfrVNZEX7qx0P1knIwod9XnQr8ngxokc3hveXYtyTrej-H24xfpkLPI5c_ZL_pGLHv4-h4yrpEPX89QmzHLnfkTzNSMxOBIZ8FehOdYYLrFO3z5thv4njjl6Ml2-iHbd_n10jGtdcvqQphBGCT3l9W7J5npKoKvUu5Av84LwaAjkxY4aQmDZOgXyjfw46cJdC259HvoknQHEnr5eqb0cXYlHeNSnWiCH5ALehFU44ig6wFiPcklXIH_UR3MfMSYMktVJft5vU834fAa6-uPBPxMmP1dCCR_prnFsNTaI_H4Un0urjt9g3mA4zJqXX4RKQfaY0YJ-nPmhqvvCfLa8kGALhFDFNGSsVDAEV9FyiuNZbpyWKqMsM1NEiijrORScBwAjS1pZ3Kt8NxNmTCCJP5B7ITvmiQHtDOHEMWu2cxAZe8aS1emYEA4gngPj1UE1lZRJA9LkhDmRmBKDprbZf5VyecRnKD0cyv7ucQjoC4nWIhP33N25uJPmXAUvexp6mZafgDOnAWJO_RKT_kgWZ60QCJ4pBu3aWHAKjuvyYyDwxL3E2UTOq5A8_dGSqEiSU1MrfZy--K3O56hREYguSt09mu3Rb6RtORJu8aBFo5n%3Bd6b2fdcf2eacb148c070e1a33012f868&x-api-eid-token=jdd03XFNL7NGIXHTZBNMS4D377HJILMFH4NN45X5C6GVHK5E5HWMCCKD5SCFPUSN4ATC33BBQPLIGI4CUTVODGJTQ5PNDEEAAAAMREJKTMMIAAAAACRXUJO7MMW2GDYX&loginType=3&uuid=181111935.17228573584591203546266.1722857358.1722857358.1722857358.1"
    res = requests.get(url, headers=headers)    # 带上伪装去请求网站

    print(res.text)

    # ====================数据筛选======================
    # 新的东西：json（轻量级的数据交换格式----即字典与字典的嵌套）
    # {
    #     "name": "warma",
    #     "age": "18",
    #     "sex": "female",
    #     "x": {
    #         "x1": "xxx1",
    #         "x2": "xxx2"
    #     }
    # }
    JSON = res.json()    # 通过观察发现将获取的文件数据是（像）json数据，将转换为json数据----jason数据有利于筛选

    # 发现一个数字 在JSON里面的 soType里面（preview中）
    number = JSON["soType"]
    # print(number)

    # 发现有若干条评论的数据，在JSON中的comments里面（preview中）
    comments = JSON["comments"]
    # print(comment)
    for comment in comments:           # 将评论一条条拿出来，其中评论中的文字在comment中的content里面
        os.makedirs(f'{count}')
        # 评论的文本：
        text = comment["content"]
        print(text)
        open(f'{count}/content.text')

        # 评论的图片：
        try:                                # 处理异常指try·exept
            images = comment["images"]      # 将图片一张张拿出来，其中评论中的图片在comment中的images里面
            for image in images:            # 一个个图片数据
                imgUrl = "https:" + image["imgUrl"]    # 图片的链接在 该图片数据中的 imgUrl ---- 图片的链接也就是网址，即使用requests
                imgUrl = imgUrl.replace("n0/s128x96", "shaidan/s616x405")    # 得到的链接前面缺少https： ---- 以及这样得到的图片是缩略图（评论区所见图片·未点开放大版本·需要修改链接格式）
                print(imgUrl)
        except:
            print("此评论无图片")

        # 评论的视频：
        try:
            videos = comment["videos"]
            for video in videos:
                videoUrl = "https:" + video["remark"]  # 视频的链接在 该视频数据中的 remark
                print(videoUrl)
        except:
            print("此评论无视频")
        print("=============================================")
    page += 1

# 上述仅获取了十条评论相关信息：
#                         为了获取更多：
#                         （1）换页：网址url中的page或者page number即pg ---- command F ：查找
#                                  page%22%3A0  转码后为"page":0 （即第一页）
#                         （2）加载