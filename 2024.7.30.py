import pandas                                       # Pandas是一个开源的Python数据分析库，提供高性能、易用的数据结构和数据分析工具
import seaborn
import matplotlib.pyplot
import statsmodels.api
# pip3 install

# （1）用pandas把数据读取出来：
data = pandas.read_csv("/Users/warma/Desktop/python/salary_years.csv")
print(data)
# （2）用seaborn把图像画出来----拟合线
seaborn.lmplot(x="years", y="salary", data=data, fit_reg=True)
# （3）用statsmodels计算出一元线性回归系数
fit = statsmodels.api.formula.ols("salary ~ years", data=data).fit()
print(fit.params)
# （4）用matplotlib.pyplot.show显示出图形
matplotlib.pyplot.show()

