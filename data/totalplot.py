import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
dataframe = pd.read_csv("pkcronatotalcases.csv")
x = dataframe.Date[:84]
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in x]
y = dataframe.TotalCases[:84]
plt.plot(x, y,label='Actual')
x = dataframe.Date[83:]
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in x]
y = dataframe.TotalCases[83:]
plt.plot(x, y,label='Prediction')

plt.xlabel('Dates')
plt.ylabel('Cases')

plt.title("Total Cases Prediction")

plt.legend()
plt.xticks(rotation=90)
plt.savefig("totalcases.png")