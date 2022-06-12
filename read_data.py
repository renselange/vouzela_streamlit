import pandas as pd

from os.path import getmtime
import datetime as dt
import streamlit as st
import openpyxl
from unidecode import unidecode
from enchantment_pre_process import item_to_seq, seq_to_item


############### re-read only if necessary (via cache)
############### make column names into strings
############### change enchantment answers from strings to lists (in: "enchantment_iems")

@st.cache(allow_output_mutation=True)
def read_vouzela_excel(name,first_day=0,last_day=0):

# check if cell contents are missing ,...
	def do_replacement(x, by='??'): 
		return unidecode(x.lower()) if type(x) == str and len(x) > 0 and x != 'Nil' else by

	t = pd.read_excel(name)

	t['dateEnd'] = pd.to_datetime(t['dateEnd'])

# get date
	born = dt.datetime.fromtimestamp(getmtime(name))

# sanitize column names by allowing only strings
	v = [str(v).strip() for v in t.columns] 
	t.columns = v

# sort by time finished, just in case this was not done
	t.sort_values(by='dateEnd',inplace=True,axis=0,ascending=False,ignore_index=True)

# in columns where missing is allowed, replace by '???'
	for c in [t.columns[12]] + list(t.columns[26:33]):               # <<<<<<<<<< check these columns
		t[c] = t.apply(lambda cols: do_replacement(cols[c]), axis=1) 

# turn \n separated string into a list ....
	#c = t.columns[20]
	#t[c] = t.apply(lambda cols: cols[c].split('\n'), axis=1)  # make lists from strings + turn into response rec
	#t['enchantment01'] = t.apply(lambda cols: ''.join(['1' if k in cols[c] else '0' for k in enchantment_order]),axis=1)

# from remaining lines, remove any lines with (any) missing values
# missing can be seen when row index shows a gap ...

	#t = t[(t['dateEnd'].dt.date >= first_day.dt.date) & (t['dateEnd'].dt.date <= last_day.dt.date)]
	t = t[(t['dateEnd'].dt.data >= first_day) & (t['dateEnd'].dt.date <= last_day)]

	t.dropna(axis=0,inplace=True)

	return t,born



# call this on column with list of endorsed enchantment items - then store

def collect_enchantment_responses(col):

	r = set()

	for lv in col: 

		if lv: r.update(lv)

	s = {k:at for at,k in enumerate(sorted((list(r))))}

	return s



