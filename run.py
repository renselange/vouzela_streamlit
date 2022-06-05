import streamlit as st
import typing_extensions
import pandas as pd
import numpy as np


from read_data import read_vouzela_excel, collect_enchantment_responses, enchantment_order
from word_cloud import make_image

uploadFile = 'POCPWA_AppExport_15-3-2022.xlsx'


if uploadFile:

	dd,born = read_vouzela_excel(uploadFile)

	st.write('Carregado de "%s"'%uploadFile,'com',dd.shape[0],'casos completos')


when = '''Dados Vouzela até %s'''%born


page = st.sidebar.radio(
    when, ["1. Inspecione o arquivo de dados", "2. Contagens de frequência simples", "3. Wordclouds de respostas escritas"], index=0
)

##################### show entire data table ##################

if page.startswith('1.'):

	dd,born = read_vouzela_excel(uploadFile)
	st.write('Casos classificados mais recentes primeiro')
	st.dataframe(dd)

	#print(collect_enchantment_responses(dd.columns[20]))

##################### show frequency + figute + stats (if possible) ########
elif page.startswith('2.'):

	for v in list(dd.columns): 
		'# Questão: %s'%v
		'[Clique no cabeçalho da coluna para classificar]'
		st.write(dd[v].value_counts())
		try:
			st.bar_chart(dd[v].value_counts())
			st.write(dd[v].describe())
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

	# for now, do by sex, but by location would be far better
	"# enchantment"




