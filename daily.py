# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:32:53 2019

@author: USER
"""
import pandas as pd
import numpy as np
import datetime

df0=pd.DataFrame()
df1 = pd.read_excel('anten02.xlsx')
df1 = df1.rename(columns={'نام کانال': 'ch', 'زمان پایان': 'تاریخ پایان',' تعدا بازدید یر حسب ساعت ': 'مدت بازدید',' بازدید': 'تعداد بازدید', 'نام برنامه ': 'نام برنامه', 'زمان شروع': 'TIME'})
df1["اپراتور"] = "آنتن" 
df1 = df1[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
df1.to_excel('anten03.xlsx')
#*************************

#fam***************
#df2 = pd.read_excel('fam02.xlsx')
#df2["مدت بازدید"] = ""
#df2 = df2.rename(columns={'نام شبکه': 'ch', 'زمان پایان': 'تاریخ پایان',' تعدا بازدید یر حسب ساعت ': 'مدت بازدید','تعداد بازدید': 'تعداد بازدید', 'نام برنامه': 'نام برنامه', 'زمان آغاز': 'TIME'})
#df2["اپراتور"] = "فام" 
#df2 = df2[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
#df2.to_excel('fam03.xlsx')
#***********************

#lenz***************
df3 = pd.read_excel('lenz02.xlsx')

df3["اپراتور"] = "لنز" 
df3.columns=['nm','ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','نامشخص','اپراتور']
del df3['nm']
del df3['نامشخص']
df3.to_excel('lenz03.xlsx')
#***********************
#tva***************
df4 = pd.read_excel('tva02.xlsx')

df4["اپراتور"] = "تیوا" 
#del df4['Subtitle']
del df4['Users']
del df4['Traffic (bytes)']
df4["Name"] = ""
df4["TIME"] = ""
df4["تاریخ پایان"] = ""
df4 = df4.rename(columns={'Channel': 'ch', 'Name': 'نام برنامه', 'Avg. Duration (sec)': 'مدت بازدید', 'Sessions': 'تعداد بازدید'})
df4 = df4.rename(columns={'End At': 'تاریخ پایان'})
df4 = df4[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
df4.to_excel('tva03.xlsx')


df0=df0.append(df1)
#df0=df0.append(df2)
df0=df0.append(df3)
df0=df0.append(df4)

df0.to_excel('daily.xlsx')


df0['ch'] = df0['ch'].str.replace('استانی ','')
df0['ch'] = df0['ch'].str.replace('شبکه ','')
df0['ch'] = df0['ch'].str.replace('ي','ی')
df0['ch'] = df0['ch'].str.replace(' (fa)','')
#df0['ch'] = df0['ch'].str.replace('(fa)','')
df0['ch'] = df0['ch'].apply(lambda x: x.split('(')[0])
df0['ch']=df0['ch'].str.strip()

df0 = df0.rename(columns={'نام برنامه': 'Name'})



df0['ch'] = df0['ch'].astype(str)
df0['ch1']=df0.loc[(df0.ch == 'دو'), 'ch'] = 'شبکه 2' 
df0['ch1']=df0.loc[(df0.ch == 'سه'), 'ch'] = 'شبکه 3'
df0['ch1']=df0.loc[(df0.ch == 'چهار'), 'ch'] = 'شبکه 4'
df0['ch1']=df0.loc[(df0.ch == 'تهران'), 'ch'] = 'شبکه 5'
df0['ch1']=df0.loc[(df0.ch == 'یک'), 'ch'] = 'شبکه 1'

df0['ch1']=df0.loc[(df0.ch == '۱'), 'ch'] = 'شبکه 1' 
df0['ch1']=df0.loc[(df0.ch == '۲'), 'ch'] = 'شبکه 2'
df0['ch1']=df0.loc[(df0.ch == '۳'), 'ch'] = 'شبکه 3'
df0['ch1']=df0.loc[(df0.ch == '۴'), 'ch'] = 'شبکه 4'
df0['ch1']=df0.loc[(df0.ch == '۵'), 'ch'] = 'شبکه 5'
df0['ch1']=df0.loc[(df0.ch == '3 HD'), 'ch'] = 'شبکه 3'
df0['ch1']=df0.loc[(df0.ch == 'بازار'), 'ch'] = 'ایران کالا'
df0['ch1']=df0.loc[(df0.ch == 'ifilm'), 'ch'] = 'آی فیلم'
df0['ch1']=df0.loc[(df0.ch == 'Press TV'), 'ch'] = 'پرس تی وی'
df0['ch1']=df0.loc[(df0.ch == 'اچ دی تماشا'), 'ch'] = 'تماشا'

df0['ch1']=df0.loc[(df0.ch == '1'), 'ch'] = 'شبکه 1' 
df0['ch1']=df0.loc[(df0.ch == '2'), 'ch'] = 'شبکه 2'
df0['ch1']=df0.loc[(df0.ch == '3'), 'ch'] = 'شبکه 3'
df0['ch1']=df0.loc[(df0.ch == '4'), 'ch'] = 'شبکه 4'
df0['ch1']=df0.loc[(df0.ch == '5'), 'ch'] = 'شبکه 5'

df0['ch1']=df0.loc[(df0.ch == 'تماشا HD'), 'ch'] = 'تماشا'
df0['ch1']=df0.loc[(df0.ch == 'سه HD'), 'ch'] = 'شبکه 3'
df0['ch1']=df0.loc[(df0.ch == 'پنج'), 'ch'] = 'شبکه 5'
df0['ch1']=df0.loc[(df0.ch == 'قرآن'), 'ch'] = 'قرآن و معارف اسلامی'









df0 = df0.rename(columns={'ch': 'نام شبکه'})
df0 = df0.rename(columns={'Name': 'نام برنامه'})
df0 = df0.rename(columns={'tag': 'جنس'})
#df0["avg"] = ""
#df0[['تعداد بازدید']].where(df0[['نام شبکه']].values == 'شبکه 1').stack().mean()
del df0['ch1']
#df0['avg']=df0[['تعداد بازدید']].where(df0[['نام شبکه']].values == 'تماشا').stack().mean()
#df0['avg1']=df0['تماشا']['avg']
df2=df0.groupby(['اپراتور']).sum().reset_index()

df3.groupby('اپراتور').mean().reset_index()



df0=df0.groupby(['نام شبکه']).sum().reset_index()
# =============================================================================
#df0.loc[df0['نام شبکه'].str.contains('شبکه 1'), 'Name'] = 1
#df0.loc[df0['نام شبکه'].str.contains('شبکه 2'), 'Name'] = 2
#df0.loc[df0['نام شبکه'].str.contains('شبکه 3'), 'Name'] = 3
#df0.loc[df0['نام شبکه'].str.contains('شبکه 4'), 'Name'] = 4
#df0.loc[df0['نام شبکه'].str.contains('شبکه 5'), 'Name'] = 5
#df0.loc[df0['نام شبکه'].str.contains('خبر'), 'Name'] = 6
#df0.loc[df0['نام شبکه'].str.contains('افق'), 'Name'] = 7
#df0.loc[df0['نام شبکه'].str.contains('قرآن'), 'Name'] = 8
#df0.loc[df0['نام شبکه'].str.contains('امید'), 'Name'] = 9
#df0.loc[df0['نام شبکه'].str.contains('ایران کالا'), 'Name'] = 10
#df0.loc[df0['نام شبکه'].str.contains('آی فیلم'), 'Name'] = 11
#df0.loc[df0['نام شبکه'].str.contains('نمایش'), 'Name'] = 12
#df0.loc[df0['نام شبکه'].str.contains('تماشا'), 'Name'] = 13
#df0.loc[df0['نام شبکه'].str.contains('مستند'), 'Name'] = 14
#df0.loc[df0['نام شبکه'].str.contains('شما'), 'Name'] = 15
#df0.loc[df0['نام شبکه'].str.contains('آموزش'), 'Name'] = 16
#df0.loc[df0['نام شبکه'].str.contains('سلامت'), 'Name'] = 17
#df0.loc[df0['نام شبکه'].str.contains('ورزش'), 'Name'] = 18
#df0.loc[df0['نام شبکه'].str.contains('نسیم'), 'Name'] = 19
#df0.loc[df0['نام شبکه'].str.contains('پویا'), 'Name'] = 20
#df0.loc[df0['نام شبکه'].str.contains('العالم'), 'Name'] = 21
#df0.loc[df0['نام شبکه'].str.contains('الکوثر'), 'Name'] = 22
#df0.loc[df0['نام شبکه'].str.contains('پرس تی وی'), 'Name'] = 23
#df0.loc[df0['نام شبکه'].str.contains('سپهر'), 'Name'] = 24
# =============================================================================
# =============================================================================
df1=df0
df1.to_excel('dailyf0.xlsx')
df0["num"] = ""
df5 = pd.read_excel('ost1.xlsx')
df5.set_index('نام شبکه', inplace=True)
df5.update(df0.set_index('نام شبکه'))
df5.reset_index()
#df4["تعداد بازدید"] = df4["تعداد بازدید"]
df5.update(df0)
#df0['num'] = df0['num'].str.replace(' ',100)
#df0['num'] = df0['num'].astype('float')

#df0=df0.sort_values('num', ascending=False, na_position='last')


    

#for i in range (0,31):
#    a=df5.loc[i,'ch']
#    t=len(df0)
#    print(t)
#    for j in range (0,t):
#        b=df0.loc[j,'نام شبکه']
#        if a==b:
#            df0.loc[t,'Name']=i
#page=380
#avgh=32
#avgp=100
#lenz_duration=page*avgh*16*60
#lenz_play=page*avgp*16
list=[]
q=len(df2)
for w in range (0,q):
    a=df2.loc[w,'اپراتور']
    if a=="آنتن":
        b=df2.loc[w,'مدت بازدید']
        b=b*60
        print('Anten_Duration', b)
    if a=="لنز":
        c=df2.loc[w,'مدت بازدید']
        d=df2.loc[w,'تعداد بازدید']
        c=c*60
        print('Lenz_Duration', c)
        print('Lenz_Play', d)
    if a=="تیوا":
#        g=df2.loc[w,'مدت بازدید']
        h=df2.loc[w,'تعداد بازدید']
#        g=h*g/60
        print('Tva_Play', h)
y=len(df4)

for x in range (0,y):
    u1=df4.loc[x,'مدت بازدید']
    u2=df4.loc[x,'تعداد بازدید']
    df4.loc[x,'Dur']=u1*u2/60
u4=df4['Dur'].sum()
print('Tva_Duration', u4)

#telewebion
site=241841
app=2636771
e= site+app       
print('Telewebion_Play', e)
#sepehr
play=41230
avg_D=6
f= play*avg_D       
print('Sepehr_Duration', f)
print('Sepehr_Play', play)
#Tva
          
# =============================================================================
df5.to_excel('dailyf.xlsx')

#df6 = pd.read_excel('ost1.xlsx')
#df0.set_index('نام شبکه', inplace=True)
#df0.update(df5.set_index('نام شبکه'))
#df0.reset_index()
#df0.to_excel('dailyf2.xlsx')

#************