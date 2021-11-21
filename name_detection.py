import numpy as np
import pandas as pd
from transformers import pipeline
import os

nlp = pipeline("ner", model='dslim/bert-base-NER-uncased')

import os

text_without_name = ""
name_count = 1
name_dict = {}
#names_total = []
for file_name in os.listdir('./data'):
  text_without_name = ''
  with open('./data/'+file_name, "r") as f:
    for i in f.readlines():
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
      text_without_name += (text + '\n')
    text_file = open('./output/'+file_name[:len(file_name)-4]+'-out.txt', "w")
    n = text_file.write(text_without_name)
    text_file.close()

              

pd.DataFrame.from_dict(name_dict, orient='index', columns=['code']).to_csv('name_keys.csv')

