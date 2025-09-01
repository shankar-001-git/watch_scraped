import os
import time
import pandas as pd
import re
from sqlalchemy import create_engine
from watches import db_config as db
from datetime import datetime

def remove_extra_spaces(input_string):
    if isinstance(input_string, str):
        return re.sub(r'\s+', ' ', input_string).strip()
    else:
        return input_string



# Interact with Database
connection_string = f"mysql+pymysql://{db.user}:{db.password}@{db.host}:3306/{db.database}"
engine = create_engine(url=connection_string, echo=True, pool_size=10, max_overflow=20)

# this file name declared and location
done_folder = r'D:\August\self_project\flipkart_watches\flipkart_watches\Export_file'
os.makedirs(done_folder, exist_ok=True)

# Fetch data
sql1 = f'SELECT * FROM {db.pdp_table}'
df1 = pd.read_sql(sql=sql1, con=connection_string)


# Remove extra spaces
for column in df1.columns:
    df1[column] = df1[column].apply(remove_extra_spaces)

df1.rename(columns={"watch_name": "watch_name","brand":'Brand'}, inplace=True)
df1.replace('', 'N/A', inplace=True)
df1.fillna("N/A", inplace=True)

today_date = datetime.now().strftime('%Y_%m_%d')

excel_path = os.path.join(done_folder, f'FLIPKAR_WATCH_BOX{today_date}.xlsx')
with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    df1.to_excel(writer, sheet_name='Product_Details', index=False)


time.sleep(3)
print("file:-", excel_path)
print('------------ FILE EXPORT SUCCESSFULLY -----------')
time.sleep(3)
