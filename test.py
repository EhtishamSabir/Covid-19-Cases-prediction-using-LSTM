for i in range(30):
    print(i)

exit()
print(int(float('26595.51513749361')))
exit()
import pandas as pd

df = pd.read_csv('./data/pkcrona.csv')
lastline = df.tail(1)
lastdate=str(lastline.iloc[0][0])
print(lastdate)