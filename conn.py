import psycopg2 as p
import pandas as pd
import db

con = p.connect(database = db.database, user = db.user, password = db.password, host = db.host, port = db.port)

df_mean=pd.read_sql('select * from test1', con)
