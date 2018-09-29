import conn
import pandas

def mean_val(df_par, column):
	return df_par.loc[df_par.index, column].mean()

mean_val(df_mean, 'val')
	
