import streamlit as st
import typing_extensions
import pandas as pd
import numpy as np


from read_data import read_vouzela_excel #, collect_enchantment_responses, enchantment_order
from word_cloud import make_image
from enchantment_pre_process import item_to_seq, seq_to_item

uploadFile = 'POCPWA_AppExport_15-3-2022.xlsx'


if uploadFile:

	dd,born = read_vouzela_excel(uploadFile)

	st.write('Carregado de "%s"'%uploadFile,'com',dd.shape[0],'casos completos')


when = '''Dados Vouzela até %s'''%born


page = st.sidebar.radio(
    when, ["1. Inspecione o arquivo de dados", 
    "2. Contagens de frequência simples", 
    "3. Wordclouds de respostas escritas",
    "4. Analyze enchantment"], index=0
)

##################### show entire data table ##################

if page.startswith('1.'):

	dd,born = read_vouzela_excel(uploadFile)
	st.write('Casos classificados mais recentes primeiro')
	st.dataframe(dd)

	#print(collect_enchantment_responses(dd.columns[20])) ### needed during development only

##################### show frequency + figute + stats (if possible) ########

elif page.startswith('2.'):

	for seq,v in enumerate(list(dd.columns)): 
		'# Questão: %s [%d]'%(v,seq)
		'[Clique no cabeçalho da coluna para classificar]'
		st.write(dd[v].value_counts())
		try:
			st.bar_chart(dd[v].value_counts())
			st.write(dd[v].describe()) # this will crash if vals are non-numeric
		except:
			pass

##################### show word clouds for open-ended questions ###########

elif page.startswith('3.'):

	for f in dd.columns[28:33]:
		'**%s**'%f
		text = ' '.join(list(dd[f].astype(str)))
		st.image(make_image(text))
		'Por favor, também inspecione as listas de respostas abaixo:'
		st.write(dd[f].value_counts())

##################### show % of enhcantment items being endorsed #########

elif page.startswith('4.'):

	#### to include the other languages, translate to Portuguese first
	#### "prefix" the translation by country: PT-Encantando, EN-Encantando

	dd['temp_country'] = dd.apply(lambda cols: 'pt' if cols['Sexo'].startswith('F') else 'en',axis=1)

### add the items in portuguese

	item_list = [seq_to_item[seq] for seq in range(16)]  # even those with freq=0 will occur

	enchantment = pd.DataFrame(index= item_list)

	st.write(enchantment.index)

	st.write('now loop')

	for country in dd['temp_country'].unique():

		'# %s'%country

		xdd = dd.copy()

		this_country = xdd[xdd['temp_country'] == country]

		as_list      = pd.DataFrame({'t':((this_country[dd.columns[20]] + '\n').astype(str).values.sum()[:-1]).split('\n')})

		counts       = as_list['t'].value_counts()

		st.write(counts)

		enchantment.join(counts,how='left')

		st.write(enchantment)

	# add newline between cases, but remove the last one before splitting
	#st.write(((dd[c]+'\n').astype(str).values.sum()[:-1]).split('\n'))

	






