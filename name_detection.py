import numpy as np
import pandas as pd
from transformers import pipeline
import os

nlp = pipeline("ner", model='dslim/bert-base-NER-uncased')

name_count = 1
name_dict = {}
text_out = []
for file_name in os.listdir('./data'):
  text_out = []
  data = pd.read_csv('./data/'+file_name)
  
  for i in data['transcript']:
    print(i)
    text = i
    ner = nlp(i, grouped_entities=True)
    print(ner)
    text = text.lower()
    if ner != []:
      for j in ner:
        if j['entity_group'] == 'PER':
          print(j['word'])
          if j['word'] in name_dict.keys():
            name_index = name_dict[j['word']]
            text = text.replace(j['word'], name_index)
          else:
            name_dict[j['word']] = "name_"+str(name_count)
            text = text.replace(j['word'], "name_"+str(name_count))
            name_count += 1
    text_out.append(text)
  data['transcript'] = text_out
  data.to_csv('./output/'+file_name[:len(file_name)-4]+'-out.csv')
  print(file_name, " processed.\n")

              

pd.DataFrame.from_dict(name_dict, orient='index', columns=['code']).to_csv('name_keys.csv')

