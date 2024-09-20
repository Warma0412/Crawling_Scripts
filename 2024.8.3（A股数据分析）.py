import akshare            # 获取股票数据模块
import pandas             # 表格模块
import matplotlib.pyplot  # 绘图模块
# matplotlib.pyplot.rcParams["font.family"] = "SemHei"    # 设置中文黑体（需要自己下载字体）
matplotlib.pyplot.figure(figsize=(10, 5))               # 画布大小：10*5

# 获取实时A股数据：
data = akshare.stock_zh_a_spot_em()
print(data)

# 获取某一只股票的历史数据：
data_hist = akshare.stock_zh_a_hist(symbol="600519", period="daily", start_date="20240101", end_date="20240803")
print(data_hist)
data_hist.to_csv("贵州茅台[600519]历史股价.csv", index=False, encoding="gbk")
# gbk 是针对汉字的编码标准

# 五日（十日）均值：股票、基金、黄金、期货、电商销售额···window=n
df = pandas.read_csv("贵州茅台[600519]历史股价.csv", index_col=0, encoding="gbk")
print(df)
# index_col=0 即以索引0列作为区分值，一直存在
df["收盘"].rolling(window=5).mean().plot(label="5日均值")    # 最后一个参数 label="5日均值" 是设置图例
df["收盘"].rolling(window=10).mean().plot(label="10日均值")
df["收盘"].rolling(window=15).mean().plot(label="15日均值")
df["收盘"].rolling(window=20).mean().plot(label="20日均值")
matplotlib.pyplot.legend()    # 绘制图例（必须图例在折线图前）
matplotlib.pyplot.show()      # 绘制折线图

# 归一化：
df = df[["开盘", "收盘", "最高", "最低"], "成交额"]
df.plot(figsize=(10, 5))    # 因为"成交额"的单位体量太大了，导致其他数值几乎看不到
matplotlib.pyplot.show()
df_max_min = (df-df.min())/(df-df.max())
df_max_min.plot(figsize=(10, 5))
matplotlib.pyplot.show()
# 有时候，我们在不考虑具体数值的情况下，我们想要看到两个指标的走势关系
# 归一化：对于不同体量单位的数据 在0-1之间找到一个对应值
# [100 150 200 250]
# [0-------------1]