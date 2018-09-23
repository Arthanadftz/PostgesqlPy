import psycopg2 as p
import pandas as pd
con = p.connect(database = 'postgres', user = 'postgres', password = 'Fkktujhbz1', host = '127.0.0.1', port = '5432')

df_mean=pd.read_sql('select val from test1', con)
def mean_val():
	return df_mean.loc[df_mean.index,'val'].mean()

mean_val()