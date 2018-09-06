# pandas写sql
from sqlalchemy import create_engine
import pandas as pd
kf = pd.read_excel("开发中心人员任分配12月_运维组.xlsx")
engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format('root', 'admin', '172.18.210.10:3306', 'oper_monit'))
con = engine.connect()
kf.to_sql(name='testJan24', con=con, if_exists='append', index=False)

