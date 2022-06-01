
from unidecode import unidecode
#import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer


portuguese_stop_set = set(['ano', 'as', 'com', 'da', 'das', 'de', 
                'dos', 'eira', 'em', 'epoca', 'etc', 
                'fora', 'ha', 'ma', 'mae', 'manha', 'meo', 
                'meus', 'na',  'nao', 'nenhum', 'nil', #'nada'
                'oais', 'ou', 'pela', 'pelo', 'que', 
                'saiba', 'sei', 'tenha', 'tenho', 'ter',
                'todo', 'um', 'uma','no'])


def clean(t,min_length=3,stop_set={}):
    
    t = unidecode(t.lower()) # remove all diacritics and make lower case
    
    for c in '.~`",:;<>?!@#$%^&*()[]{}_-+=/|\\': t = t.replace(c,' ')
    
    t = ''.join([v for v in t if v in ' abcdefghijklmnopqrstuvwxyz'])
    
    return ' '.join([v for v in t.split() if (len(v)>=min_length) and (not v in stop_set)])
    



def make_image(all_text):

	cleaner = clean(all_text,stop_set=portuguese_stop_set)

	word_cloud = WordCloud(collocations = False, background_color = 'white').generate(cleaner)

	return word_cloud.to_image()
    