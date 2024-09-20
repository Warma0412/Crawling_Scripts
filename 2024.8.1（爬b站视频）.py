import requests    # 请求网站的数据
# 另一种导入情况：from requests import get    即只导入requests库中的get工具，今后无需requests.get()，只需要get()

# ()元组、()函数的参数、[]列表、[]索引、{"key":"value"}字典
# 网址：打开开发者工具——"network"（网络)——刷新——按大小size排序——复制size最大的网址
# 200成功、403被拒绝、404没有此网页、500网页没了

# （1）准备网址：
url = "https://upos-sz-mirror08h.bilivideo.com/upgcxcode/60/22/1632642260/1632642260-1-100024.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1722524898&gen=playurlv2&os=08hbv&oi=3082878886&trid=ac3436861acc4359bdec4176ef9fbca6u&mid=422508231&platform=pc&og=hw&upsig=4410b351365dcf5ba7e971b65917c6e9&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=20786876-AF12-B787-4447-D413CE6ADC9B00895infoc&build=0&f=u_0_0&agrr=0&bw=80056&logo=80000000"

# （2）伪装爬虫：应付网站的检查，其中user-agent只是最简单的一种，还有cookie、referer、host(一个个试，缺少的就不会用它）
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "referer": "https://www.bilibili.com/video/BV1fb421E7Hr/?spm_id_from=333.337.search-card.all.click&vd_source=b353457f50aa58b841d06cec52340b71"
}
# headers = {"user-agent": "浏览器标识",
#    "cookie": "用户标识",
#     "referer": "引荐页",
#    "host": "主页"
#    }

# （3）准备网址：res不是一个东西:而是由很多很多参数构成的----如res.text、res.content(二进制代码)、res.status_code(反应)···
res = requests.get(url, headers=headers)
# print(res.content)
# wb:write-binary  二进制写   把二进制数据写到文件里面文件里面去
file = open("视频.mp4", "wb")
file.write(res.content)
# open("视频.mp4", "wb").write(res.content)    结合为一条代码也可以


# 上面爬了mp4，现在爬mp3

url = ("https://xy118x184x254x9xy.mcdn.bilivideo.cn:8082/v1/resource/1632642260-1-30232.m4s?agrr=0&build=0&buvid=20786876-AF12-B787-4447-D413CE6ADC9B00895infoc&bvc=vod&bw=15168&deadline=1722524898&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv2&logo=80000000&mid=422508231&nbs=1&nettype=0&og=cos&oi=3082878886&orderid=0%2C3&os=coso1bv&platform=pc&sign=d67864&traceid=trwxEMHkXDblhD_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform%2Cog&upsig=aef54ede95e99f360cf91ba48752ede5")
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "referer": "https://www.bilibili.com/video/BV1fb421E7Hr/?spm_id_from=333.337.search-card.all.click&vd_source=b353457f50aa58b841d06cec52340b71",
}
res = requests.get(url, headers=headers)
open("音频.mp3", "wb").write(res.content)


# 爬完了mp3和mp4，将两者合在一起


# python视频剪辑
# pip install moviepy    视频剪辑模块：加载素材——剪辑——导出
# （1）加载素材：
from moviepy.editor import *
from moviepy.editor import *
video = VideoFileClip("视频.mp4")
audio = AudioFileClip("音频.mp3")
# （2）剪辑：
final = video.set_audio(audio)    # 将mp3添加到mp4中
# （3）导出：
final.write_videofile("完整的视频.mp4")

# _下划线：区分句读，即充当句子中的标点符号的作用，用于区分

# 重新配音频
# new_video = video.without_audio_audio("新音频.mp3")          # 消音,m4a的音频格式也可以
# new_audio = audio.subclip(0, 22)    # 剪切音频，取22s
# final_video = new_video.set_audio(new_audio)
# final_video.write_vediofile("重新配音频的视频.mp3")

# 伪装：音乐有不同的隐藏内容