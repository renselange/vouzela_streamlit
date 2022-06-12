import streamlit as st
import typing_extensions
import pandas as pd
import numpy as np
import datetime as dt



from read_data import read_vouzela_excel #, collect_enchantment_responses, enchantment_order
from word_cloud import make_image
from enchantment_pre_process import item_to_seq, seq_to_item

uploadFile = 'POCPWA_AppExport_15-3-2022.xlsx'
#pd.set_option('display.colheader_justify', 'center')

if uploadFile:

    dd,born = read_vouzela_excel(uploadFile,'1922-03-13','3022-03-13')

    if not 'first_day' in st.session_state:
        st.session_state.first_day = min(dd['dateEnd'])
        st.session_state.last_day = max(dd['dateEnd'])

    st.session_state.first_day = st.sidebar.date_input('You may change start date', st.session_state.first_day,key='what 1')
    st.session_state.last_day  = st.sidebar.date_input('You may change the end date', st.session_state.last_day,key='what 2')

    if st.session_state.last_day < st.session_state.first_day : st.session_state.last_day = st.session_state.first_day

    dd,born = read_vouzela_excel(uploadFile,st.session_state.first_day,st.session_state.last_day)

    st.write('Carregado de "%s"'%uploadFile,'com',dd.shape[0],'casos completos. %s %s'%(st.session_state.first_day,st.session_state.last_day))
    
    when = '''Dados Vouzela até %s'''%born


page = st.sidebar.radio(
    when, [
    "1. Inspecione o arquivo de dados", 
    "2. Contagens de frequência simples", 
    "3. Wordclouds de respostas escritas",
    "4. Encantamento específico do país"], index=0
)



##################### show entire data table ##################

if page.startswith('1.'):

    dd,born = read_vouzela_excel(uploadFile) #copy.deepcopy(my_cached_function(...))                                                                                                                                            
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

    '# Os padrões de encantamento variam de acordo com o país de origem?'

    dd['temp_country'] = dd.apply(lambda cols: 'pt' if cols['Sexo'].startswith('F') else 'en',axis=1) # remove later ....

    item_list = [seq_to_item[seq] for seq in range(16)] + ['COL-TOTAL']

    enchanted = pd.DataFrame({'Fonte de Encantamento': item_list})

    for country in dd['temp_country'].unique():

        this_country = dd[dd['temp_country'] == country]

        as_list      = ((this_country[dd.columns[20]] + '\n').astype(str).values.sum()[:-1]).split('\n')   # all items in one long list
        new_freq     = [0]*17 # one more for the TOTAL
        for w in as_list: new_freq[item_to_seq[w][0]] += 1
        new_freq[-1] = sum(new_freq)
        enchanted[country.upper()+'-count'] = new_freq

    enchanted['ROW-TOTAL'] = enchanted.apply(lambda cols: sum(cols[v] for v in enchanted.columns if not v.startswith('Fonte')),axis=1)
    enchanted.sort_values(by='ROW-TOTAL',inplace=True)

    st.write(enchanted)

    'Perhaps add stacked graphs?'


################### working on time window now ###############################

elif page.startswith('5.'):

    "# time window is under construction now"







