import streamlit as st
import typing_extensions
import pandas as pd
import numpy as np
from read_data import read_vouzela_excel

uploadFile = 'POCPWA_AppExport_15-3-2022.xlsx'

#uploadFile = st.file_uploader("Upload your excel file",type=["xlsx"]) ; st.write(type(uploadFile.name))

#show_freqs = range(3,33)


if uploadFile:
	#dd,born = read_vouzela_excel(fname)

	#uploadFile = st.file_uploader("Upload your excel file") #,type=["xlsx"]) ; print(uploadFile)

	dd,born = read_vouzela_excel(uploadFile)

	st.write('Carregado de "%s"'%uploadFile,'com',dd.shape[0],'casos completos')
else:
	st.write('Não pode ser carregado "%s"'%uploadFile,'   Tchau...')
	9/0

#born = 'now'

#uploadFile = st.file_uploader("Upload your excel file",type=["xlsx"])

#st.write(uploadFile)
#st.write(fname) ; uploadFile = fname
#dd,born = read_vouzela_excel(uploadFile)

t = '''Dados Vouzela até %s'''%born


page = st.sidebar.radio(
    t, ["1. Inspecione o arquivo de dados", "2. Contagens de frequência simples", "3. ?????"], index=0
)

if page.startswith('1.'):
	dd,born = read_vouzela_excel(uploadFile)
	st.write('Casos classificados mais recentes primeiro')
	st.dataframe(dd)

elif page.startswith('2.'):

	for v in list(dd.columns)[4:33]:
		#st.write('')
		#st.write('Questão',v,'[Clique no cabeçalho da coluna para classificar]')
		'# Questão: %s'%v
		'[Clique no cabeçalho da coluna para classificar]'
		st.write(dd[v].value_counts())
		try:
			st.bar_chart(dd[v].value_counts())
			st.write(dd[v].describe())
		except:
			pass


elif page.startswith('3.'):

	pass


#"# take 2: Vouzela Dashboard"

	t
