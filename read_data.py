import pandas as pd

from os.path import getmtime
import datetime 
import streamlit as st


# @st.cache
def read_vouzela_excel(name):

# check if cell contents are missing ,...
	def do_replacement(x, by='???'): 
		return x if type(x) == str and len(x) > 0 and x != 'Nil' else by

# try reading ...
	t = pd.read_excel(name)

# get date
	born = datetime.datetime.fromtimestamp(getmtime(name))

# sanitize column names by allowing only strings
	v = [str(v).split('.')[-1].strip() for v in t.columns] 
	t.columns = v
	for v in list(zip(range(999),t.columns,v)): print('\n',v)

# sort by time finished, just in case this was not done
	t.sort_values(by='dateEnd',inplace=True,axis=0,ascending=False,ignore_index=True)

# in columns where missing is allowed, replace by '???'
	for c in [t.columns[12]] + list(t.columns[26:33]):               # <<<<<<<<<< check these columns
		t[c] = t.apply(lambda cols: do_replacement(cols[c]), axis=1) 

# from remaining lines, remove any lines with (any) missing values
# missing can be seen when row index shows a gap ...
	t.dropna(axis=0,inplace=True)

	return t,born

