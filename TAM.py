# coding: utf-8

import nltk
from hazm import *
import json
import numpy as np

# normalizer = Normalizer()
# normalizer.normalize('اثلاح نويسه ها رئیس ری رئ و استفاده ق از نیم‌فاصله پردازش را آسان مي كند ')

# j = ['،', '؟']

# for i in word_tokenize('ما هم برای وصل کردن آمدیم ولی برای پردازش، جدا بهتر نیست؟'):
#     if not(i in j):
#         print(i)


outfile = open("twt_text.json", ‘r’)

for i in outfile:
data = json.loads(i)

def TAM(data):
	tweet = []
	normalizer = Normalizer()

	for j in [x[1] for x in data.values()]:
	tweet.append(normalizer.normalize(j))
#         print(tweet[k])')

	weed = ['،', 'و','؟', '!','؟!', '!؟',':', 'RT','https', '//t','یه', 'به','برای', 'را','این', ')','(', 'در','یا', 'با','اگر', 'که','.', 'از','رو', '|','', '','']
    # weed = ['.', '']

    for i in range(len(tweet)):
        for k in range(i+1, len(tweet)):
            findword = list(set([t for t in word_tokenize(tweet[i]) if t not in weed])&set([t for t in word_tokenize(tweet[k]) if t not in weed]))
            if (len(findword) > 2):
                indexi = []
                indexk = []
                vocab = []
                for fi in findword:
                    vocab.append(fi)

                    indexi.append(tweet[i].index(fi))
                    indexk.append(tweet[k].index(fi))

                indi = sorted(indexk)
                intk = [indi.index(v)+1 for v in indexk]
                indexk = intk

                indi = sorted(indexi)
                intk = [indi.index(v)+1 for v in indexi]
                indexi = intk

                print('\n')
                print(indexi)
                print(indexk)
                print(vocab)
#             print(tweet[i])
#             print('\n\n')
#             print(tweet[k])

                l = len(vocab)
                cosim = (6 * np.dot(indexi, indexk)) / ((l+1)*(1+2*l))

                print(cosim)
				print('\n \t next tweet \n \n')


# In[ ]:
