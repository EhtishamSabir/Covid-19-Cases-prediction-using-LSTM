import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
dataframe = pd.read_csv("deathtol.csv")
x = dataframe.Date[:58]
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in x]

y = dataframe.TotalDeaths[:58]
plt.plot(x, y,label='Actual')
x = dataframe.Date[57:]
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in x]
y = dataframe.TotalDeaths[57:]
plt.plot(x, y,label='Prediction')

plt.xlabel('Dates')
plt.ylabel('Deaths')

plt.title("Total Death Prediction")
plt.legend()
plt.xticks(rotation=90)

  # or plt.savefig("name.png")
plt.savefig("totaldeaths.png")