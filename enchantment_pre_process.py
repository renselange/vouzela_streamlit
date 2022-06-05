

# mix in any language, making sure of course that the same
# "words" end up with the same row index

# eu escrevi em português, inglês, francês,

item_to_seq = {           ####### place Portuguese first, and use its order everywhere

  "Admirado": (0,'português'),
  "Alegre": (1,'português'),
  "Calmo / Tranquilo": (2,'português'),
  "Ciente (percepção ou compreensão aumentada)": (3,'português'),
  "Conectado (unido a algo maior do que você)": (4,'português'),
  "Deslumbrado (impressionado pela beleza de algo)": (5,'português'),
  "Encantado": (6,'português'),
  "Especial (sorte ou privilégio de estar lá)": (7,'português'),
  "Expectante (agradável sensação de ansiedade ou expectativa)": (8,'português'),
  "Importante (grande valorização do momento e seu significado)": (9,'português'),
  "Inspirado": (10,'português'),
  "Introspetivo (atenção concentrado no lugar e tempo)": (11,'português'),
  "Realizado (sentindo-se profundamente satisfeito, gratificado ou completo)": (12,'português'),
  "Rendido (no presença de grandeza ou algo incrível)": (13,'português'),
  "Revigorado": (14,'português'),
  "Surpreendido (sentindo-se perplexo ou surpreso)": (15,'português'),

  "Admirable": (0,'inglês'),
  "Blij": (1,'holandes')

}

seq_to_item = {}

for w in item_to_seq:
  seq ,lang= item_to_seq[w]
  if lang == 'português':    # use portuguese
    if not seq in seq_to_item: seq_to_item[seq] = w

def pre_process(country_col,enchantment_col):

	pass