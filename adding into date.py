from datetime import datetime
import pandas as pd
from datetime import timedelta
your_date_string = "2020-05-07"
for x in range(50):
    new_date = pd.to_datetime(your_date_string) + timedelta(1)

    print(new_date.date())
    your_date_string=str(new_date.date())

