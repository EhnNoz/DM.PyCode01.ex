# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:13:47 2019

@author: USER
"""


import math
import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm

# =============================================================================
bf0 = pd.read_excel('tvak.xlsx')
bf2 = pd.read_excel('tvak.xlsx')


bf0['Name'] = bf0['Name'].str.replace('ي','ی')
bf0['Name'] = bf0['Name'].str.replace('فیلم سینمایی-','فیلم سینمایی ')
bf0['Name'] = bf0['Name'].str.replace('سینمایی -',' ')

bf2['Name'] = bf2['Name'].str.replace('ي','ی')
bf2['Name'] = bf2['Name'].str.replace('فیلم سینمایی-','فیلم سینمایی ')
bf2['Name'] = bf2['Name'].str.replace('سینمایی -',' ')
#dfn = bf0.Name.str.extract(r'(?P<val>[0-9.]*)')
#dfn['Name']=bf0['Name']
dfn=pd.DataFrame()
#dfn = bf0['Name'].str.split('(\d+)([A-Za-z]+)', expand=True)
#dfn = dfn.loc[:,[1,2]]
#dfn.rename(columns={1:'x', 2:'y'}, inplace=True)
dfn['Name']=bf0['Name'].str.replace('\D+','')
dfn['Name2']=bf0['Name'].str.replace('\d+','')


#dfn = bf0.Name.str.extract('([a-zA-Z]+)([^a-zA-Z]+)', expand=True)
#dfn.columns = ['Text', 'Number']
#dfn.to_excel('dfn.xlsx')
#    
    

bf0['Num'] = ""
rrl=[]
rrl2=[]
rrl3=[]
rrl4=[]
rrl5=[]
rrl6=[]
rrl7=[]
rrl8=[]
rrl9=[]

rrl=bf2['اپراتور']
rrl2=bf2['مدت بازدید']
rrl3=bf2['تعداد بازدید']
rrl4=bf2['تاریخ شروع']
rrl5=bf2['تاریخ پایان']
rrl6=bf2['ساعت']
rrl7=bf2['تاریخ']
rrl8=bf2['جنس']
rrl9=bf0['Name2']
bf1=bf0.groupby(['Name']).first().reset_index()

bf11=bf0.groupby(['Name']).first().reset_index()

for h in range(0,len(bf1)):
    bf1.loc[h,'Num']=h


bf0.set_index('Name2', inplace=True)
bf0.update(bf1.set_index('Name2'))
bf0.reset_index()
bf0['Name2'] = bf0['Name']

sse = pd.Series(rrl)
sse2 = pd.Series(rrl2)
sse3 = pd.Series(rrl3)
sse4 = pd.Series(rrl4)
sse5 = pd.Series(rrl5)
sse6 = pd.Series(rrl6)
sse7 = pd.Series(rrl7)
sse8 = pd.Series(rrl8)
sse9 = pd.Series(rrl9)

bf0['اپراتور'] = sse.values
bf0['مدت بازدید']=sse2.values
bf0['تعداد بازدید']=sse3.values
bf0['تاریخ شروع'] = sse4.values
bf0['تاریخ پایان']=sse5.values
bf0['ساعت']=sse6.values
bf0['تاریخ']=sse7.values
bf0['جنس']=sse8.values
#bf0['Num']=sse9.values

bf0.to_excel('tschof22.xlsx', index=False)


df0 = pd.read_excel('tschof22.xlsx')
df115=pd.read_excel('tschof22.xlsx')
df225=pd.read_excel('tschof22.xlsx')
df0=df0.dropna(subset=['Name'])
df0 = df0.reset_index(drop=True)

df115=df115.dropna(subset=['Name'])
df115 = df115.reset_index(drop=True)

df0=df0.groupby(['Name']).first().reset_index()
df115=df115.groupby(['Name']).first().reset_index()





rl=[]
rl2=[]
rl3=[]
rl4=[]
rl5=[]
rl6=[]
rl7=[]
rl8=[]
rl9=[]

rl=df225['اپراتور']
rl2=df225['مدت بازدید']
rl3=df225['تعداد بازدید']
rl4=df225['تاریخ شروع']
rl5=df225['تاریخ پایان']
rl6=df225['ساعت']
rl7=df225['تاریخ']
rl8=df225['جنس']
rl9=df225['Num']

# =============================================================================
df0['Name'] = df0['Name'].apply(lambda x: x.split('(')[0])
df0['Name'] = df0['Name'].apply(lambda x: x.split('-')[0])
df0['Name'] = df0['Name'].apply(lambda x: x.split('(')[0])
df0['Name'] = df0['Name'].apply(lambda x: x.split('-')[0])
df0['Name'] = df0['Name'].apply(lambda x: x.split('قسمت')[0])
df0['Name'] = df0['Name'].apply(lambda x: x.split('فصل')[0])
df0['Name'] = df0['Name'].apply(lambda x: x.split('شبکه')[0])
df0['Name'] = df0['Name'].apply(lambda x: x.split('–')[0])

df0['Name'] = df0['Name'].apply(lambda x: x.split('_')[0])
df0['Name'] = df0['Name'].apply(lambda x: x.split(':')[0])
df0['Name'] = df0['Name'].apply(lambda x: x.split('(')[0])
#cf2250['Name'] = cf2250['Name'].apply(lambda x: x.split('خلاصه')[0])
df0['Name'] = df0['Name'].apply(lambda x: x.split('؛')[0])           
# =============================================================================
#df0['num2']=df0['Name'].str.replace('\D+','')
#if len(df0['num2'])==1:
#    df0['Name']=df0['Name'].str.replace('\d+','')
    
    
df0['num2']=df0['Name'].str.replace('\D+','')
df0['Name7']=df0['Name'].str.replace('\d+','')
#for jj in range(0,len(df0)):
#
#    nn=df0.loc[jj,'num2']
#    if len(nn)<2:
#        df0.loc[jj,'Name']=df0.loc[jj,'Name7'].replace('\d+','')
#df0.to_excel('df0test.xlsx')
        
#df0['Name']=df0['Name'].str.replace('\d+','')

df0['Name'] = df0['Name'].str.replace('ئ','ی')
#df0['Name'] = df0['Name'].str.replace('فیلم سینمایی-','فیلم سینمایی ')
#df0['Name'] = df0['Name'].str.replace('فیلم سینمایی-','فیلم سینمایی ')
#df0['Name'] = df0['Name'].str.replace('سینمایی -',' ')

df0['Name'] = df0['Name'].str.replace('ي','ی')
df0['Name'] = df0['Name'].str.replace('فیلم سینمایی-','فیلم سینمایی ')
df0['Name'] = df0['Name'].str.replace('سینمایی -',' ')
df0['Name'] = df0['Name'].str.replace('آ','ا')
df0['Name'] = df0['Name'].str.replace('شبکه ۱','')
df0['Name'] = df0['Name'].str.replace('مجموعه','')
df0['Name'] = df0['Name'].str.replace('برنامه','')
df0['Name'] = df0['Name'].str.replace('قصه','')
df0['Name'] = df0['Name'].str.replace('انیمیشن','')
df0['Name'] = df0['Name'].str.replace('سریال','')
df0['Name'] = df0['Name'].str.replace('مستند','')
df0['Name'] = df0['Name'].str.replace('مسلسل','')
df0['Name'] = df0['Name'].str.replace('فیلم تلویزیونی','')
df0['Name'] = df0['Name'].str.replace('فیلم سینمایی','')
df0['Name'] = df0['Name'].str.replace('شرکت','')

df0['Name'] = df0['Name'].str.replace('سینمایی','')
df0['Name'] = df0['Name'].str.replace('فیلم','')
df0['Name'] = df0['Name'].str.replace('ة','ه')
df0['Name'] = df0['Name'].str.replace('ادامه ','')
df0['Name'] = df0['Name'].str.replace(')','')
df0['Name'] = df0['Name'].str.replace('(','')
df0['Name'] = df0['Name'].str.replace('_','')
df0['Name'] = df0['Name'].str.replace('تکرار','')
df0['Name'] = df0['Name'].str.replace('نیمه اول','')
df0['Name'] = df0['Name'].str.replace('نیمه دوم','')
df0['Name'] = df0['Name'].str.replace('"','')
df0['Name'] = df0['Name'].str.replace('/','')
df0['Name'] = df0['Name'].str.replace('-','')
df0['Name'] = df0['Name'].str.replace('/','')
df0['Name'] = df0['Name'].str.replace('فیلم سینمایی','')
df0['Name'] = df0['Name'].str.replace('فیلم تلویزیونی','')
df0['Name'] = df0['Name'].str.replace('گزارش','')
df0['Name'] = df0['Name'].str.replace('زنده','')

df0['Name'] = df0['Name'].str.replace(' ','')
df0['Name'] = df0['Name'].str.replace('«','')
df0['Name'] = df0['Name'].str.replace('»','')
df0['Name'] = df0['Name'].str.replace('\\','')
df0['Name'] = df0['Name'].str.replace('سری جدید','')
df0['Name'] = df0['Name'].str.replace('بازپخش','')
df0['Name'] = df0['Name'].str.replace('تکرار','')
df0['Name'] = df0['Name'].str.replace('ویژه','')
df0['Name'] = df0['Name'].str.replace('ادامه','')
df0['Name'] = df0['Name'].str.replace('ي','ی')
df0['Name'] = df0['Name'].str.replace(' ','')
df0['Name'] = df0['Name'].str.replace('ة','ه')
df0['Name'] = df0['Name'].str.replace(' ','')
df0['Name'] = df0['Name'].str.replace('گلچین','')
df0['Name'] = df0['Name'].str.replace('گزیده','')
df0['Name'] = df0['Name'].str.replace('ات','')
df0['Name'] = df0['Name'].str.replace('ها','')
df0['Name'] = df0['Name'].str.replace('های','')
df0['Name'] = df0['Name'].str.replace('ان','')

df0['Name'] = ' ' + df0['Name'].astype(str)
# =============================================================================

# =============================================================================
df115['Name'] = df115['Name'].str.replace('ي','ی')
df115['Name'] = df115['Name'].str.replace('ادامه ','')

#df115['Name'] = df115['Name'].str.replace('های','\u200cهای')
#df115['Name'] = df115['Name'].str.replace(' ‌های','\u200cهای')
#df115['Name'] = df115['Name'].str.replace(' ها','\u200cها')
#df115['Name'] = df115['Name'].str.replace('ها\u200c','\u200cها')
#df115['Name'] = df115['Name'].str.replace('می','\u200cمی')
#df115['Name'] = df115['Name'].str.replace('می ','\u200cمی')
df115['Name'] = df115['Name'].str.replace('\u200cهای','های')
df115['Name'] = df115['Name'].str.replace('\u200cهای',' های')
df115['Name'] = df115['Name'].str.replace('\u200cها','ها')
df115['Name'] = df115['Name'].str.replace('\u200cها',' ها')

df115['Name'] = df115['Name'].str.replace('\u200cمی','می')
df115['Name'] = df115['Name'].str.replace('\u200cمی',' می')

df115['Name'] = ' ' + df115['Name'].astype(str)

# =============================================================================

df1=df0

Row_list =[] 
Row_list2 =[]
Row_list3 =[] 
Row_list4 =[]
Row_list5 =[]

Row_list25 =[]
Row_list35 =[] 
Row_list45 =[]
Row_list55 =[] 

df101=pd.DataFrame()

df1['Name'] = df1['Name'].str[:10]  

df4 = pd.read_excel('test03.xlsx')
df4=df4['Name'].apply(lambda x: pd.Series(list(x)))

df4=df4.set_index(0).T
#df4.to_excel('test08.xlsx')
df5=df4


#************************************
df10 = df0
df10['Name'] = df10['Name'].str[:10]  

df100=df10

df11=df10['Name'].apply(lambda x: pd.Series(list(x)))  
df11=df11.set_index(0).T

#df11.to_excel('test071.xlsx')
df51=df4
x=len(df115)
for t in range(0,x):
    print(t)
    df51.loc[:,t] = df4.iloc[:,0].isin(df11.iloc[:,t]).astype(np.int8)

#df51.to_excel('test091.xlsx')
df51=df51.set_index(0).T
#df51.to_excel('test101.xlsx')
df51=df51.drop('1',axis='rows')
df511=df51    

d=df51.values.astype(str).tolist()
def destringifyTupleData(d):
    return [tuple(destringifyList(l)) for l in d]

def destringifyList(l):
    return map(float, l)


d = destringifyTupleData(d)

#d=np.array(d,dtype=float)
df100=df100.drop(0,axis='rows')
df100['vec']=d
#############################

###############################
def get_intersection(s1, s2): 
    res = ''
    l_s1 = len(s1)
    for t in range(l_s1):
       for u in range(t + 1, l_s1):
           q = s1[t:u]
           if q in s2 and len(q) > len(res):
               res = q
    return res
#############################

#############################
for k in range(1,x):
    a=df100.loc[k,'vec']

    d30=df100.loc[k,'Name']
    d20=df115.loc[k,'Name']
    print(k)
    for j in range(1,len(df115)):
        b=df100.loc[j,'vec']
        b20=df115.loc[j,'Name']
        o2=df115.loc[j,'Name2']
        result = dot(a, b)/(norm(a)*norm(b))
#        print(result)
        try:
            
            x=math.acos(result)
        except:
            pass

        if result>0.9:
            df115.loc[j,'Name3']=k
            s1=d20
            s2=b20
            gc=get_intersection('aa' + s1 + 'bb', 'cc' + s2 + 'dd')
#            print(gc)
            r=len(gc)

            if r<4:
                df115.loc[j,'Name']=b20
            else:
                if len(d20)>len(b20):
                    df115.loc[j,'Name']=b20
                else:
                    df115.loc[j,'Name']=d20

df115.to_excel('ftest01.xlsx', index=False) 

df225.set_index('Name2', inplace=True)
df225.update(df115.set_index('Name2'))
df225.reset_index()
#df225['Name'] = df225['Name2'].map(df115.set_index('Name2')['Name'])

#df225['Name2'] = bf2['Name']

df225['اپراتور'] = sse.values
df225['مدت بازدید']=sse2.values
df225['تعداد بازدید']=sse3.values
df225['تاریخ شروع'] = sse4.values
df225['تاریخ پایان']=sse5.values
df225['ساعت']=sse6.values
df225['تاریخ']=sse7.values
df225['جنس']=sse8.values
df225['Name2']=df225['Name']

df225.to_excel('df225.xlsx', index=False) 
df335=pd.read_excel('df225.xlsx', index=False)
# =============================================================================
# Game dovvom
# =============================================================================


cf0 = pd.read_excel('df225.xlsx')
cf115=pd.read_excel('df225.xlsx')
cf225 = pd.read_excel('df225.xlsx')

cf0=cf0.dropna(subset=['Name'])
cf0 = cf0.reset_index(drop=True)

cf115=cf115.dropna(subset=['Name'])
cf115 = cf115.reset_index(drop=True)

cf225=cf225.dropna(subset=['Name'])
cf225 = cf225.reset_index(drop=True)

cf117=cf0.groupby(['Name']).first().reset_index()

cf116=cf115.groupby(['Name']).first().reset_index()

cf2250=cf225.groupby(['Name']).first().reset_index()
# =============================================================================
cf2250['Name'] = cf2250['Name'].apply(lambda x: x.split('(')[0])
cf2250['Name'] = cf2250['Name'].apply(lambda x: x.split('-')[0])
cf2250['Name'] = cf2250['Name'].apply(lambda x: x.split('(')[0])
cf2250['Name'] = cf2250['Name'].apply(lambda x: x.split('-')[0])
cf2250['Name'] = cf2250['Name'].apply(lambda x: x.split('قسمت')[0])
cf2250['Name'] = cf2250['Name'].apply(lambda x: x.split('فصل')[0])
cf2250['Name'] = cf2250['Name'].apply(lambda x: x.split('شبکه')[0])
#cf2250['Name'] = cf2250['Name'].apply(lambda x: x.split('خلاصه')[0])
cf2250['Name'] = cf2250['Name'].apply(lambda x: x.split('؛')[0])
# =============================================================================
#cf117['Name']=cf117['Name'].str.replace('\d+','')

cf117['Name'] = cf117['Name'].apply(lambda x: x.split('(')[0])
cf117['Name'] = cf117['Name'].apply(lambda x: x.split('-')[0])
cf117['Name'] = cf117['Name'].apply(lambda x: x.split('(')[0])
cf117['Name'] = cf117['Name'].apply(lambda x: x.split('-')[0])
cf117['Name'] = cf117['Name'].apply(lambda x: x.split('قسمت')[0])
cf117['Name'] = cf117['Name'].apply(lambda x: x.split('فصل')[0])
cf117['Name'] = cf117['Name'].apply(lambda x: x.split('شبکه')[0])
cf117['Name'] = cf117['Name'].apply(lambda x: x.split('خلاصه')[0])
cf117['Name'] = cf117['Name'].apply(lambda x: x.split('؛')[0])
#cf117['Name'] = cf117['Name'].apply(lambda x: x.split('(')[0]
cf117['Name'] = cf117['Name'].apply(lambda x: x.split('(')[0])
cf117['Name'] = cf117['Name'].apply(lambda x: x.split('–')[0])

cf117['Name'] = cf117['Name'].apply(lambda x: x.split('_')[0])
cf117['Name'] = cf117['Name'].apply(lambda x: x.split(':')[0])

cf117['Name'] = cf117['Name'].str.replace('ئ','ی')
cf117['Name'] = cf117['Name'].str.replace('فیلم سینمایی-','فیلم سینمایی- ')

cf117['Name'] = cf117['Name'].str.replace('ي','ی')
cf117['Name'] = cf117['Name'].str.replace('آ','ا')
cf117['Name'] = cf117['Name'].str.replace('شبکه ۱','')
cf117['Name'] = cf117['Name'].str.replace('مجموعه','')
cf117['Name'] = cf117['Name'].str.replace('برنامه','')
cf117['Name'] = cf117['Name'].str.replace('قصه','')
cf117['Name'] = cf117['Name'].str.replace('انیمیشن','')
cf117['Name'] = cf117['Name'].str.replace('ادامه','')
#cf117['Name'] = cf117['Name'].str.replace('\','')
cf117['Name'] = cf117['Name'].str.replace('مسابقه','')

cf117['Name'] = cf117['Name'].str.replace('مسلسل','')
cf117['Name'] = cf117['Name'].str.replace('فیلم تلویزیونی','')
cf117['Name'] = cf117['Name'].str.replace('فیلم سینمایی','')
cf117['Name'] = cf117['Name'].str.replace('شرکت','')

cf117['Name'] = cf117['Name'].str.replace('سریال','')
cf117['Name'] = cf117['Name'].str.replace('گزارش','')

cf117['Name'] = cf117['Name'].str.replace('مستند','')
cf117['Name'] = cf117['Name'].str.replace('سینمایی','')
cf117['Name'] = cf117['Name'].str.replace('فیلم','')
cf117['Name'] = cf117['Name'].str.replace('ة','ه')
cf117['Name'] = cf117['Name'].str.replace('ادامه ','')
cf117['Name'] = cf117['Name'].str.replace(')','')
cf117['Name'] = cf117['Name'].str.replace('(','')
cf117['Name'] = cf117['Name'].str.replace('_','')
cf117['Name'] = cf117['Name'].str.replace('تکرار','')
cf117['Name'] = cf117['Name'].str.replace('نیمه اول','')
cf117['Name'] = cf117['Name'].str.replace('نیمه دوم','')
cf117['Name'] = cf117['Name'].str.replace('پشت صحنه','')
cf117['Name'] = cf117['Name'].str.replace('تلویزیونی','')

cf117['Name'] = cf117['Name'].str.replace('"','')
cf117['Name'] = cf117['Name'].str.replace('/','')
cf117['Name'] = cf117['Name'].str.replace('-','')
cf117['Name'] = cf117['Name'].str.replace('/','')
cf117['Name'] = cf117['Name'].str.replace('فیلم سینمایی','')
cf117['Name'] = cf117['Name'].str.replace(' ','')
cf117['Name'] = cf117['Name'].str.replace('«','')
cf117['Name'] = cf117['Name'].str.replace('»','')
#cf117['Name'] = cf117['Name'].str.replace("\",'')115
cf117['Name'] = cf117['Name'].str.replace('\\','')
cf117['Name'] = cf117['Name'].str.replace('سری جدید','')
cf117['Name'] = cf117['Name'].str.replace('بازپخش','')
cf117['Name'] = cf117['Name'].str.replace('تکرار','')
cf117['Name'] = cf117['Name'].str.replace('ویژه','')
cf117['Name'] = cf117['Name'].str.replace('سری جدید','')

cf116['Name'] = cf116['Name'].str.replace('ئ','ی')
cf116['Name'] = cf116['Name'].str.replace('آ','ا')
#cf116['Name'] = cf116['Name'].str.replace('های','\u200cهای')
#cf116['Name'] = cf116['Name'].str.replace(' ‌های','\u200cهای')
#cf116['Name'] = cf116['Name'].str.replace('ها','\u200cها')
#cf116['Name'] = cf116['Name'].str.replace(' ها','\u200cها')
#
#cf116['Name'] = cf116['Name'].str.replace('می ','می')
#cf116['Name'] = cf116['Name'].str.replace('می','می\u200c')
cf116['Name'] = cf116['Name'].str.replace('ادامه','')
cf116['Name'] = cf116['Name'].str.replace(' های','های')
cf116['Name'] = cf116['Name'].str.replace(' ها','ها')
cf116['Name'] = cf116['Name'].str.replace('\u200c',' ')

cf116['Name'] = cf116['Name'].str.replace('\u200cهای','های')
cf116['Name'] = cf116['Name'].str.replace('\u200cهای',' های')
cf116['Name'] = cf116['Name'].str.replace('\u200cها','ها')
cf116['Name'] = cf116['Name'].str.replace('\u200cها',' ها')
cf116['Name'] = cf116['Name'].str.replace('\\',' ')
cf116['Name'] = cf116['Name'].str.replace('"',' ')
#cf116['Name'] = cf116['Name'].str.replace('می ','می')
#cf116['Name'] = cf116['Name'].str.replace('می','می\u200c')
cf116['Name'] = cf116['Name'].str.replace('«',' ')
cf116['Name'] = cf116['Name'].str.replace('»',' ')

cf116['Name'] = cf116['Name'].str.replace('می‌رد','میرد')
cf116['Name'] = cf116['Name'].str.replace('ن‌می','نمی')
cf116['Name'] = cf116['Name'].str.replace('اختتا‌می‌ه','اختتامیه')
cf116['Name'] = cf116['Name'].str.replace('انی‌می‌شن','انیمیشن')
cf116['Name'] = cf116['Name'].str.replace('خ‌مینی','خمینی')
cf116['Name'] = cf116['Name'].str.replace('ا‌می‌ر','امیر')
cf116['Name'] = cf116['Name'].str.replace('ا‌می‌د','امید')
cf116['Name'] = cf116['Name'].str.replace('می‌راث','میراث')
cf116['Name'] = cf116['Name'].str.replace('‌می‌دان','میدان')
cf116['Name'] = cf116['Name'].str.replace('خات‌می‌','خاتمی')
cf116['Name'] = cf116['Name'].str.replace('ن‌‌هایت','نهایت')

cf116['Name'] = cf116['Name'].str.replace('انی‌میشن','انیمیشن')
cf116['Name'] = cf116['Name'].str.replace('ن‌‌هایی','نهایی')
cf116['Name'] = cf116['Name'].str.replace('بد‌می‌نتون','بدمینتون')
cf116['Name'] = cf116['Name'].str.replace('می‌ز','میز')
cf116['Name'] = cf116['Name'].str.replace('می‌دان','میدان')
cf116['Name'] = cf116['Name'].str.replace('ج‌هانی','جهانی')
cf116['Name'] = cf116['Name'].str.replace('‌می‌ان','میان')

#cf116['Name'] = cf116['Name'].str.replace('\u200cهای','های')
#cf116['Name'] = cf116['Name'].str.replace('\u200cهای',' های')
cf116['Name'] = cf116['Name'].str.replace('\u200cمی','می')
cf116['Name'] = cf116['Name'].str.replace('\u200cمی',' می')

#rl4=cf115['تعداد بازدید']



#cf117['Name'] = ' ' + cf117['Name'].astype(str)
#
#cf116['Name'] = ' ' + cf116['Name'].astype(str)


cf1=cf117

Row_list =[] 
Row_list2 =[]
Row_list3 =[] 
Row_list4 =[]
Row_list5 =[]

Row_list25 =[]
Row_list35 =[] 
Row_list45 =[]
Row_list55 =[] 

cf101=pd.DataFrame()

cf1['Name'] = cf1['Name'].str[:10]  

cf1=cf1['Name'].apply(lambda x: pd.Series(list(x)))  
cf1=cf1.set_index(0).T

#cf1.to_excel('test07.xlsx')
cf4 = pd.read_excel('test03.xlsx')
cf4=cf4['Name'].apply(lambda x: pd.Series(list(x)))

cf4=cf4.set_index(0).T
#cf4.to_excel('test08.xlsx')
cf5=cf4

#************************************
cf10 = cf117
cf10['Name'] = cf10['Name'].str[:10]  

cf100=cf10

cf11=cf10['Name'].apply(lambda x: pd.Series(list(x)))  
cf11=cf11.set_index(0).T

cf11.to_excel('test071.xlsx')
cf51=cf4

x=len(cf116)
for t in range(0,x):
    print(t)
    cf51.loc[:,t] = cf4.iloc[:,0].isin(cf11.iloc[:,t]).astype(np.int8)

cf51.to_excel('test091.xlsx')
cf51=cf51.set_index(0).T
cf51.to_excel('test101.xlsx')
cf51=cf51.drop('1',axis='rows')
cf511=cf51    

c=cf51.values.astype(str).tolist()
def destringifyTupleData(c):
    return [tuple(destringifyList(l)) for l in c]

def destringifyList(l):
    return map(float, l)


c = destringifyTupleData(c)

#d=np.array(d,dtype=float)
cf100=cf100.drop(0,axis='rows')
cf100['vec']=c
#############################

###############################
def get_intersection(s1, s2): 
    res = ''
    l_s1 = len(s1)
    for t in range(l_s1):
       for u in range(t + 1, l_s1):
           q = s1[t:u]
           if q in s2 and len(q) > len(res):
               res = q
    return res
#############################


#############################
for k in range(1,x):
    ac=cf100.loc[k,'vec']
    dc30=cf100.loc[k,'Name']
    dc20=cf116.loc[k,'Name']
    dc200=cf117.loc[k,'Name']
#    cf116.loc[k,'len']=len(dc20)

    print(k)
    for j in range(1,len(cf116)):
        bc=cf100.loc[j,'vec']
        bc20=cf116.loc[j,'Name']
        oc2=cf116.loc[j,'Name2']
        
        bc200=cf117.loc[j,'Name']
#        cf116.loc[j,'len']=len(bc20)

        result = dot(ac, bc)/(norm(ac)*norm(bc))
        try:
            
            x=math.acos(result)
        except:
            pass
#        print(result)
        if result>0.9:

            
            cf116.loc[j,'Name4']=k
            s1=dc20
            s2=bc20
            gc=get_intersection('aa' + s1 + 'bb', 'cc' + s2 + 'dd')
#            print(gc)
            r=len(gc)
            
#            if len(s1)>len(s2):
#                cf116.loc[j,'Name']=s2
#            else:
#                cf116.loc[j,'Name']=s1
                

            if r <4:
                
                cf116.loc[j,'Name']=oc2
            else:

                if len(d20)>len(b20):
                    cf116.loc[j,'Name']=bc20
                else:
                    cf116.loc[j,'Name']=dc20


                    
                    

                
            
            
   
cf116.to_excel('ftest012.xlsx', index=False)  

# =============================================================================


df335.set_index('Name2', inplace=True)
df335.update(cf116.set_index('Name2'))
df335.reset_index()


#df115.set_index('Name3', inplace=True)
#df115.update(cf116.set_index('Name3'))
#df115.reset_index()





#sse = pd.Series(rrl)
#sse2 = pd.Series(rrl2)
#sse3 = pd.Series(rrl3)
#sse4 = pd.Series(rrl4)
#sse5 = pd.Series(rrl5)
#sse6 = pd.Series(rrl6)
#sse7 = pd.Series(rrl7)
#sse8 = pd.Series(rrl8)
#sse9 = pd.Series(rrl9)

df335['اپراتور'] = sse.values
df335['مدت بازدید']=sse2.values
df335['تعداد بازدید']=sse3.values
df335['تاریخ شروع'] = sse4.values
df335['تاریخ پایان']=sse5.values
df335['ساعت']=sse6.values
df335['تاریخ']=sse7.values
df335['جنس']=sse8.values
df335['Name2']=sse9.values

#df115['Num']=se9.values

#df115['اپراتور']= rl
#df115=pd.DataFrame(simple_list,columns=['col1','col2'])
#df115['مدت بازدید']=rl2
#df115['تعداد بازدید']=rl3
# =============================================================================
#df335['Name'] = df335['Name'].str.replace('‌','ه ها')
df335['Name'] = df335['Name'].str.replace('هها','ه ها')
#nn=len(df335)
#df335['Name5'] = df335['Name']
#df335['Name'] = df335['Name'].apply(lambda x: x.split('(')[0])
#
#df335=df335.Name.fillna(df335.Name5, inplace=True)
#nn=len(df335)
df335['Name5'] = df335['Name']
##df335['Name'] = df335['Name'].apply(lambda x: x.split('(')[0])
##
##df335=df335.Name.fillna(df335.Name5, inplace=True)
#for ii in range(0,nn):
#    kk=df335.loc[ii,'Name5']
    


df335.to_excel('omidtest.xlsx', index=False)  
bf335 = pd.read_excel('omidtest.xlsx', index=False)
df0['Name'] = df0['Name'].astype(str)

bf335['Name'] = bf335['Name'].str.replace('فیلم سینمایی-','فیلم سینمایی ')

bf335['Name'] = bf335['Name'].apply(lambda x: str(x).split('(')[0])
bf335['Name'] = bf335['Name'].apply(lambda x: str(x).split('_')[0])
bf335['Name'] = bf335['Name'].apply(lambda x: str(x).split('-')[0])
bf335['Name'] = bf335['Name'].apply(lambda x: str(x).split('–')[0])
bf335['Name'] = bf335['Name'].apply(lambda x: str(x).split('-')[0])
bf335['Name'] = bf335['Name'].apply(lambda x: str(x).split('-')[0])
bf335['Name'] = bf335['Name'].apply(lambda x: x.split('قسمت')[0])

for ii in range(0,len(bf335)):
    kk=bf335.loc[ii,'Name5']
    pp=bf335.loc[ii,'Name']

    if len(pp)==1:
        bf335.loc[ii,'Name']=kk

#bf335['num3']=bf335['Name'].str.replace('\D+','')
#
#for jj in range(0,len(bf335)):
#
#    nn=bf335.loc[jj,'num3']
#    if len(nn)<2:
#        bf335.loc[jj,'Name']=bf335.loc[jj,'Name'].replace('\d+','')


bf335.to_excel('tvakout.xlsx', index=False)  
      
#bf0.set_index('Num', inplace=True)
#bf0.update(df115.set_index('Num'))
#bf0.reset_index()
#
#sse = pd.Series(rrl)
#sse2 = pd.Series(rrl2)
#sse3 = pd.Series(rrl3)
#sse4 = pd.Series(rrl4)
#sse5 = pd.Series(rrl5)
#sse6 = pd.Series(rrl6)
#sse7 = pd.Series(rrl7)
#sse8 = pd.Series(rrl8)
#sse9 = pd.Series(rrl9)
#
#bf0['اپراتور'] = sse.values
#bf0['مدت بازدید']=sse2.values
#bf0['تعداد بازدید']=sse3.values
#bf0['تاریخ شروع'] = sse4.values
#bf0['تاریخ پایان']=sse5.values
#bf0['ساعت']=sse6.values
#bf0['تاریخ']=sse7.values
#bf0['جنس']=sse8.values
#bf0['Num']=sse9.values
#
#bf0.to_excel('ftest01111.xlsx', index=False)  
