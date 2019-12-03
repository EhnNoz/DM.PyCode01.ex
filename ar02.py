import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import CountVectorizer



with open('iribchannel4-media metadata.json', 'r', encoding='utf-8') as f:
    y = json.load(f)
    f.close()
 
df0 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df6 = pd.DataFrame()
t=10

for k in range(0,t):
    try:
        z=y["GraphImages"][k]["edge_media_to_caption"]
        df0[k] = pd.DataFrame.from_dict(z)
    except:
        pass


df0 = df0.unstack()   
df0 = df0.to_frame(name='caption')
df0=df0.reset_index()

df1=df0['caption']
df1 = df1.to_frame(name='caption')
df1['caption'] = df1['caption'].astype(str)

df1.to_excel('ar04.xlsx')
#
#Row_list2=[]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df1["caption"])
print(vectorizer.get_feature_names())

print(X.toarray())

feature_names = vectorizer.get_feature_names()
#feature_names = [x[:-3] for x in feature_names]
#feature_names = [e for e in feature_names if e not in ('گفت')]
print(feature_names)
#feature_names=str(feature_names).encode('utf-8','ignore')
df2=pd.DataFrame(X.toarray(), columns=feature_names)

#
#for i in range (0,10):
#    df2.iloc[0,i]= df2.iloc[0,i].str[:2]

#data['result'] = data['result'].map(lambda x: str(x)[2:])

df2.to_excel('ar03.xlsx')

    
#df2=df2.set_index(1).T
df4 = pd.read_excel('js109.xlsx')
#
#for i in range(0,500):



#df5=pd.concat([df4,df2]),keep='last')

#df4=df4.set_index(1).T
df6 = df4.append(df2, ignore_index=True, sort=False)
df6=df6.drop(df6.columns[5:], axis=1)
df6=df6.fillna(0)

#feature_names = [e for e in feature_names if e not in ('گفت')]


#df4=df2.fillna(0))
#print(df6)

# Create an empty list 
Row_list =[] 
Row_list=df6.values.tolist()  
#Row_list = [e for e in Row_list if e not in ('احسان')]

print(Row_list)
# Iterate over each row 
#for index, rows in df6.iterrows(): 
#    # Create list for the current row 
#    my_list =[rows] 
#      
#    # append the list to the final list 
#    Row_list.append(my_list) 
#  
## Print the list 
#print(Row_list)

#df5 = pd.merge(df2, df4, , on='company'))

df6.to_excel('ar02.xlsx')
