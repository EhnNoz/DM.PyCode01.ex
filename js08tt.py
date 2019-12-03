# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:21:27 2019

@author: USER
"""

from IPython import get_ipython
get_ipython().magic('reset -sf')

import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import CountVectorizer



df1=pd.read_excel('cap010.xlsx')

df1['caption'] = df1['caption'].astype(str)



vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df1["caption"])
#print(vectorizer.get_feature_names())

#print(X.toarray())

feature_names = vectorizer.get_feature_names()

#print(feature_names)

df2=pd.DataFrame(X.toarray(), columns=feature_names)


df2.to_excel('ar03.xlsx')
df2.loc['Total',:]= df2.sum(axis=0)


#df2=df2.set_index(0).T
#df2.columns=['name','freq']

#df5=df4.groupby(['name']).sum().reset_index()
#print(len(df5))
#df5['name'] = df4['name'].str[:5]
#df5 = df5[df5['freq'] > 100] 
#print(len(df5))

#df4['name'] = df4['name'].map(lambda x: x.lstrip('تر'))
#df4['name'] = df4['name'].map(lambda x: x.lstrip('ترین'))

#df4['name'] = df4['name'].apply(lambda x: '{0:0<5}'.format(x))

#if df4['name2']<

#df4[~df4.name.str.match('')]

#df6=df4['name']

#df6.columns=['name']
#df6['name'] = df6['name'].astype(str)


#df6 = df6.drop_duplicates()

df2.to_excel('cap02.xlsx')
#df5.to_excel('cap03.xlsx')
#df4.to_excel('cap04.xlsx')
#print(df2)

#df6.to_excel('cap06.xlsx', index=False)  
    
