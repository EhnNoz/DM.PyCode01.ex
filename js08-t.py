# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:23:39 2019

@author: USER
"""


#from IPython import get_ipython
#get_ipython().magic('reset -sf')

import json
import pandas as pd
import numpy as np


#with open('iribchannel4-media metadata.json', 'r', encoding='utf-8') as f:
#    y = json.load(f)
#    f.close()
# 
df0 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df6 = pd.DataFrame()
t=5
#
#for k in range(0,t):
#    try:
#        z=y["GraphImages"][k]["edge_media_to_caption"]
#        df0[k] = pd.DataFrame.from_dict(z)
#    except:
#        pass
#
#
#df0 = df0.unstack()   
#df0 = df0.to_frame(name='caption')
#df0=df0.reset_index()
#
#df1=df0['caption']
#df1 = df1.to_frame(name='caption')
#df1['caption'] = df1['caption'].astype(str)
##df1['caption'] = df1['caption'].astype(str)
#
##df1 = df1.append({'caption' : 'Sahil'} , ignore_index=True)
##df1.loc[0] = np.array(["soh"])
##df1.loc[0] = [2]
#
#df1['caption'] = df1['caption'].str.replace('text',' ')
#df1['caption'] = df1['caption'].str.replace('node',' ')
#df1['caption'] = df1['caption'].str.replace('edges',' ')
#df1['caption'] = df1['caption'].str.replace('{',' ')
#df1['caption'] = df1['caption'].str.replace('[',' ')
#df1['caption'] = df1['caption'].str.replace('#',' ')
#df1['caption'] = df1['caption'].str.replace('_',' ')
#df1['caption'] = df1['caption'].str.replace('«',' ')
#df1['caption'] = df1['caption'].str.replace(' ای ',' ')
##df1['caption'] = df1['caption'].str.replace(' می ','')
#df1['caption'] = df1['caption'].str.replace('}',' ')
#df1['caption'] = df1['caption'].str.replace(']',' ')
#df1['caption'] = df1['caption'].str.replace(':',' ')
#df1['caption'] = df1['caption'].str.replace('u',' ')
#df1['caption'] = df1['caption'].str.replace(' ها ',' ')
#df1['caption'] = df1['caption'].str.replace(' می ',' ')
#df1['caption'] = df1['caption'].str.replace('،',' ')
#df1['caption'] = df1['caption'].str.replace('200',' ')
#df1['caption'] = df1['caption'].str.replace('c',' ')
#df1['caption'] = df1['caption'].str.replace(' این ','')
#df1['caption'] = df1['caption'].str.replace('خواهد','')
#df1['caption'] = df1['caption'].str.replace('.',' ')
#df1['caption'] = df1['caption'].str.replace(' را ',' ')
#df1['caption'] = df1['caption'].str.replace('و ',' ')
#df1['caption'] = df1['caption'].str.replace('از ',' ')
#df1['caption'] = df1['caption'].str.replace('در ',' ')
#df1['caption'] = df1['caption'].str.replace('👤',' ')
#df1['caption'] = df1['caption'].str.replace('های ',' ')
#df1['caption'] = df1['caption'].str.replace(' به ',' ')
#df1['caption'] = df1['caption'].str.replace('با ',' ')
#df1['caption'] = df1['caption'].str.replace('♨',' ')
#df1['caption'] = df1['caption'].str.replace(' که ',' ')
#df1['caption'] = df1['caption'].str.replace(' چه ',' ')
#df1['caption'] = df1['caption'].str.replace(' ی ',' ')
#df1['caption'] = df1['caption'].str.replace('»',' ')
#df1['caption'] = df1['caption'].str.replace('n',' ')
#df1['caption'] = df1['caption'].str.replace('\\',' ')
#df1['caption'] = df1['caption'].str.replace(' ها ',' ')
#df1['caption'] = df1['caption'].str.replace('🔴',' ')
#df1['caption'] = df1['caption'].str.replace('•',' ')
#df1['caption'] = df1['caption'].str.replace('✔',' ')
#df1['caption'] = df1['caption'].str.replace('🎭',' ')
#df1['caption'] = df1['caption'].str.replace('🏴',' ')
#df1['caption'] = df1['caption'].str.replace('-',' ')
#df1['caption'] = df1['caption'].str.replace('⬅️',' ')
#df1['caption'] = df1['caption'].str.replace('✅',' ')
#df1['caption'] = df1['caption'].str.replace('"',' ')
#df1['caption'] = df1['caption'].str.replace('(',' ')
#df1['caption'] = df1['caption'].str.replace('برای',' ')
#
#df1['caption'] = df1['caption'].str.replace('شود',' ')
##df1['caption'] = df1['caption'].str.replace(' می',' ')
##df1['caption'] = df1['caption'].str.replace(' ا ',' ')
##df1['caption'] = df1['caption'].str.replace('ی ',' ')
##df1['caption'] = df1['caption'].str.replace('ای ',' ')
##df1['caption'] = df1['caption'].str.replace('پور',' ')
#df1['caption'] = df1['caption'].str.replace('کرد',' ')
#df1['caption'] = df1['caption'].str.replace('است',' ')
#
#
#
#
#
##df1['caption'] = df1['caption'].str.replace('✅',' ')
#
#
#
#df1['caption'] = df1['caption'].str.replace('  ',' ')
#
#df1.to_excel('cap01.xlsx')


df1=pd.read_excel('cap01.xlsx')
#df1['caption'] = df1['caption'].astype(str)

#df1=df1.str.cat(sep=', ')
#print(len(df1))
p=0
str2 = []
s=[]
bw=[]
for j in range (0,5):
    

    df3=df2
    df4=pd.concat([df3, df4], axis=1)
#    df3=df5
    str =df1.iloc[j,0]
    print(j)
    def freq(str):
        
    
        str = str.split()
#        print(str)          
        str2 = [] 
        for i in str:              
  
            if i not in str2: 
                str2.append(i)
                
              
        for i in range(0, len(str2)):
#            p=p+1
#            print(len(str2))
#            print(str2[i], ':', str.count(str2[i]))     
            df2[i]=str2[i],str.count(str2[i])
#            print(bw)
    def main():
        freq(str)    
    if __name__=="__main__": 
        main()             

df4=df4.set_index(1).T
df4.columns=['name','freq']
#df4 = df4.drop_duplicates()
#df4 = df4[df4['freq'] > 3] 

#df4['name2'] = df4['name'].str.len()
#df4['name3']=df4.sum(level=0)
#df4 = df4[df4['name2'] > 3] 
df5=df4.groupby(['name']).sum().reset_index()
print(len(df5))
#df5['name'] = df4['name'].str[:5]
#df5 = df5[df5['freq'] > 100] 
print(len(df5))

#df4['name'] = df4['name'].map(lambda x: x.lstrip('تر'))
#df4['name'] = df4['name'].map(lambda x: x.lstrip('ترین'))

#df4['name'] = df4['name'].apply(lambda x: '{0:0<5}'.format(x))

#if df4['name2']<

#df4[~df4.name.str.match('')]

df6=df4['name']

#df6.columns=['name']
#df6['name'] = df6['name'].astype(str)


df6 = df6.drop_duplicates()

df2.to_excel('cap02.xlsx')
df5.to_excel('cap03.xlsx')
df4.to_excel('cap04.xlsx')
print(df4)

df6.to_excel('cap06.xlsx', index=False)          


