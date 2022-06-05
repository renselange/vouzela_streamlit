import pandas as pd

from os.path import getmtime
import datetime 
import streamlit as st
import openpyxl
from unidecode import unidecode


############### re-read only if necessary (via cache)
############### make column names into strings
############### change enchantment answers from strings to lists (in: "enchantment_iems")


enchantment_order = {           ####### here alphabetictally ....
  "Admirado": 0,
  "Alegre": 1,
  "Calmo / Tranquilo": 2,
  "Ciente (percepção ou compreensão aumentada)": 3,
  "Conectado (unido a algo maior do que você)": 4,
  "Deslumbrado (impressionado pela beleza de algo)": 5,
  "Encantado": 6,
  "Especial (sorte ou privilégio de estar lá)": 7,
  "Expectante (agradável sensação de ansiedade ou expectativa)": 8,
  "Importante (grande valorização do momento e seu significado)": 9,
  "Inspirado": 10,
  "Introspetivo (atenção concentrado no lugar e tempo)": 11,
  "Realizado (sentindo-se profundamente satisfeito, gratificado ou completo)": 12,
  "Rendido (no presença de grandeza ou algo incrível)": 13,
  "Revigorado": 14,
  "Surpreendido (sentindo-se perplexo ou surpreso)": 15
}


@st.cache
def read_vouzela_excel(name):

# check if cell contents are missing ,...
	def do_replacement(x, by='??'): 
		return unidecode(x.lower()) if type(x) == str and len(x) > 0 and x != 'Nil' else by

# try reading ...
	t = pd.read_excel(name)

# get date
	born = datetime.datetime.fromtimestamp(getmtime(name))

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
	t.dropna(axis=0,inplace=True)

	return t,born



# call this on column with list of endorsed enchantment items - then store

def collect_enchantment_responses(col):

	r = set()

	for lv in col: 

		if lv: r.update(lv)

	s = {k:at for at,k in enumerate(sorted((list(r))))}

	return s



