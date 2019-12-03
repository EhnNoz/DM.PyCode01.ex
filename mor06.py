## -*- coding: utf-8 -*-
#"""
#Created on Sat Oct 26 15:10:38 2019
#
#@author: USER
#"""
#
#import pandas as pd
#
#
#df0=pd.read_excel('mor05.xlsx')
#
#df0['نام برنامه'] = df0['نام برنامه'].str.replace('-',' ')
#df0['نام برنامه'] = df0['نام برنامه'].str.replace(')',' ')
#df0['نام برنامه'] = df0['نام برنامه'].str.replace('(',' ')
#
#df0.to_excel('mor06.xlsx')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 03:22:35 2019

@author: ehsan
"""

#from IPython import get_ipython
#get_ipython().magic('reset -sf')

import pandas as pd
import numpy as np
import datetime

df0=pd.DataFrame()
#aio*************
#try:
#    df0 = pd.read_excel('aio02.xlsx')
#    df0 = df0.rename(columns={'Channel name': 'ch', 'title': 'نام برنامه', 'start_datetime': 'TIME', 'visite': 'تعداد بازدید'})
#    df0["تاریخ پایان"] = ""
#    df0["مدت بازدید"] = ""
#    df0["اپراتور"] = "آیو" 
#    df0 = df0[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
#except:
#    pass    

#*********************

#anten*******************
df1 = pd.read_excel('anten02.xlsx')
df1 = df1.rename(columns={'نام کانال': 'ch', 'زمان پایان': 'تاریخ پایان',' تعدا بازدید یر حسب ساعت ': 'مدت بازدید','بازدید': 'تعداد بازدید', 'نام برنامه ': 'نام برنامه', 'زمان شروع': 'TIME'})
df1["اپراتور"] = "آنتن" 
df1 = df1[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
df1.to_excel('anten03.xlsx')
#*************************

#fam***************
df2 = pd.read_excel('fam02.xlsx')
df2["مدت بازدید"] = ""
df2 = df2.rename(columns={'نام شبکه': 'ch', 'زمان پایان': 'تاریخ پایان',' تعدا بازدید یر حسب ساعت ': 'مدت بازدید','تعداد بازدید': 'تعداد بازدید', 'نام برنامه': 'نام برنامه', 'زمان آغاز': 'TIME'})
df2["اپراتور"] = "فام" 
df2 = df2[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
df2.to_excel('fam03.xlsx')
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
del df4['Subtitle']
del df4['Users']
df4["مدت بازدید"] = ""
df4 = df4.rename(columns={'Channel': 'ch', 'Name': 'نام برنامه', 'Start At': 'TIME', 'Sessions': 'تعداد بازدید'})
df4 = df4.rename(columns={'End At': 'تاریخ پایان'})
df4 = df4[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
df4.to_excel('tva03.xlsx')
#***********************


df0=df0.append(df1)
df0=df0.append(df2)
df0=df0.append(df3)
df0=df0.append(df4)

df0.to_excel('shah01.xlsx')

df0['TIME'] = pd.to_datetime(df0.TIME)
df0['سال'] = df0['TIME'].dt.year
df0['ماه'] = df0['TIME'].dt.month
df0['ماه'] = df0['ماه'].apply(lambda x: '{0:0>2}'.format(x))
df0['روز'] = df0['TIME'].dt.day
df0['روز'] = df0['روز'].apply(lambda x: '{0:0>2}'.format(x))
df0['ساعت'] = df0['TIME'].dt.hour
df0['ساعت'] = df0['ساعت'].apply(lambda x: '{0:0>2}'.format(x))
df0['تاریخ'] = df0[df0.columns[7:]].apply(
    lambda x: ''.join(x.dropna().astype(str).astype(str)),
    axis=1
)


df0 = df0.rename(columns={'TIME': 'تاریخ شروع'})
del df0['ماه']
del df0['روز']
del df0['سال']

df0['ch'] = df0['ch'].str.replace('شبکه ','')
df0['ch'] = df0['ch'].str.replace('ي','ی')

df0['نام برنامه'] = df0['نام برنامه'].str.replace('سریال ','مجموعه ')
df0['نام برنامه'] = df0['نام برنامه'].str.replace(' سریال',' مجموعه')
df0['نام برنامه'] = df0['نام برنامه'].str.replace('سریال','مجموعه ')

df0 = df0.rename(columns={'نام برنامه': 'Name'})

df0['Name'] = df0['Name'].astype(str)
df0['Name'] = df0['Name'].str.replace('ي','ی')
df0['Name'] = df0['Name'].str.replace('قسمت','قسمت ')
#df0['Name'] = df0['Name'].str.replace(')','')
#df0['Name'] = df0['Name'].str.replace('(','')
#df0['Name'] = df0['Name'].str.replace('_','')
#df0['Name'] = df0['Name'].str.replace('تکرار','')
#df0['Name'] = df0['Name'].str.replace('زنده','')
#df0['Name'] = df0['Name'].str.replace('نیمه اول','')
#df0['Name'] = df0['Name'].str.replace('نیمه دوم','')
#df0['Name'] = df0['Name'].str.replace('"','')
#df0['Name'] = df0['Name'].str.replace('/','')
#df0['Name'] = df0['Name'].str.replace('-','')
#df0['Name'] = df0['Name'].str.replace('/','')
#df0['Name'] = df0['Name'].str.replace(' ها','ها')
#df0['Name'] = df0['Name'].str.replace('می ','می')
#df0['Name'] = df0['Name'].str.replace('  ',' ')
#df0['Name'] = df0['Name'].str.replace(' \','')
df0.loc[df0['Name'].str.contains('خبر آگهی'), 'Name'] = 'خبر'
df0 = df0[~df0['Name'].str.contains('اذان')]
df0 = df0[~df0['Name'].str.contains('میان برنامه')]
df0 = df0[~df0['Name'].str.contains('میانبرنامه')]
df0 = df0[~df0['Name'].str.contains('میان‌برنامه')]
df0 = df0[~df0['Name'].str.contains('بازرگانی')]
df0 = df0[~df0['Name'].str.contains('آگهی')]
df0 = df0[~df0['Name'].str.contains('اگهی')]
df0 = df0[~df0['Name'].str.contains('وله')]
df0 = df0[~df0['Name'].str.contains('ارم استیشن')]
df0 = df0[~df0['Name'].str.contains('آرم استیشن')]
df0 = df0[~df0['Name'].str.contains('ارم تایم')]
df0 = df0[~df0['Name'].str.contains('آرم تایم')]
df0 = df0[~df0['Name'].str.contains('برنامه بعدی')]
df0 = df0[~df0['Name'].str.contains('اعلام برنامه')]
df0 = df0[~df0['Name'].str.contains('معرفی برنامه')]
df0 = df0[~df0['Name'].str.contains('نماهنگ')]
df0 = df0[~df0['Name'].str.contains('کپشن')]
df0 = df0[~df0['Name'].str.contains('مولودی')]
df0 = df0[~df0['Name'].str.contains('آنونس')]
df0 = df0[~df0['Name'].str.contains('انونس')]
df0 = df0[~df0['Name'].str.contains('تیتراژ')]
df0 = df0[~df0['Name'].str.contains('تیزر')]
df0 = df0[~df0['Name'].str.contains('هم خوانی')]
df0 = df0[~df0['Name'].str.contains('همخوانی')]
df0 = df0[~df0['Name'].str.contains('هم‌خوانی')]
df0 = df0[~df0['Name'].str.contains('ارتباط مستقیم')]
df0 = df0[~df0['Name'].str.contains('کلیپ')]
df0 = df0[~df0['Name'].str.contains('آگهی قبل ')]
df0 = df0[~df0['Name'].str.contains('ذکر')]
df0 = df0[~df0['Name'].str.contains('دعا')]
df0 = df0[~df0['Name'].str.contains('تقدیم برنامه')]
df0 = df0[~df0['Name'].str.contains('برنامه از')]
df0 = df0[~df0['Name'].str.contains('حسنی')]
df0 = df0[~df0['Name'].str.contains('پیش پرده')]

#df0.loc[df0['Name'].str.contains('دوردست'), 'Name'] = 'مجموعه دور دست ها'
#df0.loc[df0['Name'].str.contains('دور دست'), 'Name'] = 'مجموعه دور دست ها'
#df0.loc[df0['Name'].str.contains('عبرت'), 'Name'] = 'مجموعه آیینه عبرت'
#df0.loc[df0['Name'].str.contains('مختار'), 'Name'] = 'مجموعه مختارنامه'
#df0.loc[df0['Name'].str.contains('مادری'), 'Name'] = 'خانه مادری'
#df0.loc[df0['Name'].str.contains('به نما'), 'Name'] = 'مسابقه نما به نما'
##df0.loc[df0['Name'].str.contains('صلح بانان'), 'Name'] = 'کلاه قرمزی'
#df0.loc[df0['Name'].str.contains('حلقه سبز'), 'Name'] = 'مجموعه حلقه سبز'
#df0.loc[df0['Name'].str.contains('تعطیلات'), 'Name'] = 'مجموعه تعطیلات رویایی'
#df0.loc[df0['Name'].str.contains('خانه دار'), 'Name'] = 'مجموعه یادداشت های یک زن خانه دار'
##df0.loc[df0['Name'].str.contains('مسافر'), 'Name'] = 'مجموعه مسافر'
#df0.loc[df0['Name'].str.contains('لیسانسه ها 2'), 'Name'] = 'مجموعه لیسانسه ها 2'
#df0.loc[df0['Name'].str.contains('لیسانسه ها2'), 'Name'] = 'مجموعه لیسانسه ها 2'
#df0.loc[df0['Name'].str.contains('دیوار2'), 'Name'] = 'مجموعه دیوار به دیوار 2'
#df0.loc[df0['Name'].str.contains('دیوار 2'), 'Name'] = 'مجموعه دیوار به دیوار 2'
##df0.loc[df0['Name'].str.contains('خنده خانه'), 'Name'] = 'دیروز امروز فردا'
#df0.loc[df0['Name'].str.contains('کلانتر'), 'Name'] = 'مجموعه کلانتر'
#df0.loc[df0['Name'].str.contains('مثبت'), 'Name'] = 'مجموعه اُ مثبت'
#df0.loc[df0['Name'].str.contains('مردکوچک'), 'Name'] = 'مجموعه بزرگ مرد کوچک'
#df0.loc[df0['Name'].str.contains('مرد کوچک'), 'Name'] = 'مجموعه بزرگ مرد کوچک'
#df0.loc[df0['Name'].str.contains('فراموشی'), 'Name'] = 'مجموعه فراموشی'
#df0.loc[df0['Name'].str.contains('خط شکن'), 'Name'] = 'مجموعه خط شکن'
##df0.loc[df0['Name'].str.contains('دانستنا'), 'Name'] = 'دیوار به دیوار 2'
##df0.loc[df0['Name'].str.contains('میشه'), 'Name'] = 'مجموعه لیسانسه ها'
#df0.loc[df0['Name'].str.contains('ششمین'), 'Name'] = 'مجموعه ششمین نفر'
#df0.loc[df0['Name'].str.contains('لیلا'), 'Name'] = 'مجموعه تنهایی لیلا'
#df0.loc[df0['Name'].str.contains('خط قرمز'), 'Name'] = 'مجموعه خط قرمز'
#df0.loc[df0['Name'].str.contains('همسایه'), 'Name'] = 'مجموعه همسایه ها'
#df0.loc[df0['Name'].str.contains('شوق'), 'Name'] = 'مجموعه شوق پرواز'
#df0.loc[df0['Name'].str.contains('شیدایی'), 'Name'] = 'مجموعه شیدایی'
#df0.loc[df0['Name'].str.contains('سرخ'), 'Name'] = 'مجموعه خاک سرخ'



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
df0.loc[df0['Name'].str.contains('مجموعه'), 'tag'] = 'مجموعه تلویزیونی'
df0.loc[df0['Name'].str.contains('فیلم'), 'tag'] = 'فیلم سینمایی'
df0.loc[df0['Name'].str.contains('سینمایی'), 'tag'] = 'فیلم سینمایی'
df0.loc[df0['Name'].str.contains('اخبار'), 'tag'] = 'اخبار'
#df0.loc[df0['Name'].str.contains('خبر'), 'tag'] = 'اخبار'
#df0.loc[df0['tag'].str.contains(''), 'tag'] = 'سایر'


#if df0['ch']!="قرآن":
#    df0 = df0[~df0['Name'].str.contains('تلاوت')]
#df0.loc[df0['Name'].str.contains('جشن‌رمضان'), 'Name'] = 'جشن رمضان'
#df0.loc[df0['Name'].str.contains('جشن رمضان'), 'Name'] = 'جشن رمضان'
#df0.loc[df0['Name'].str.contains('شیدایی'), 'Name'] = 'شبهای شیدایی'
#df0.loc[df0['Name'].str.contains('این شب'), 'Name'] = 'این شبها'
#df0.loc[df0['Name'].str.contains('مسافرماه'), 'Name'] = 'مسافر ماه'
#df0.loc[df0['Name'].str.contains('مسافر ماه'), 'Name'] = 'مسافر ماه'
#df0.loc[df0['Name'].str.contains('عطررمضان'), 'Name'] = 'عطر رمضان'
#df0.loc[df0['Name'].str.contains('عطر رمضان'), 'Name'] = 'عطر رمضان'
#df0.loc[df0['Name'].str.contains('ماه من'), 'Name'] = 'ماه من'
#df0.loc[df0['Name'].str.contains('ماه‌من'), 'Name'] = 'ماه من'
#df0.loc[df0['Name'].str.contains('ماه خدا'), 'Name'] = 'ماه خدا'
#df0.loc[df0['Name'].str.contains('خوان نیاز'), 'Name'] = 'خوان نیاز'
#df0.loc[df0['Name'].str.contains('خوان‌نیاز'), 'Name'] = 'خوان نیاز'
#df0.loc[df0['Name'].str.contains('سحور'), 'Name'] = 'سحوری'
#df0.loc[df0['Name'].str.contains('سر سفره'), 'Name'] = 'سرسفره'
#df0.loc[df0['Name'].str.contains('سرسفره'), 'Name'] = 'سرسفره'
#df0.loc[df0['Name'].str.contains('اختیار'), 'Name'] = 'اختیاریه'
#df0.loc[df0['Name'].str.contains('دعوت'), 'Name'] = 'دعوت'
#df0.loc[df0['Name'].str.contains('قاچ'), 'Name'] = 'قاچ'
#df0.loc[df0['Name'].str.contains('ماه بهشت'), 'Name'] = 'ماه بهشت'
#df0.loc[df0['Name'].str.contains('ماه نشان'), 'Name'] = 'ماه نشان'
#df0.loc[df0['Name'].str.contains('فضای زندگی'), 'Name'] = 'فضای زندگی'
#df0.loc[df0['Name'].str.contains('مل مل'), 'Name'] = 'مل مل'
#df0.loc[df0['Name'].str.contains('ململ'), 'Name'] = 'مل مل'
#df0.loc[df0['Name'].str.contains('مل‌مل'), 'Name'] = 'مل مل'
#df0.loc[df0['Name'].str.contains('ها رفته'), 'Name'] = 'از یادها رفته'
#df0.loc[df0['Name'].str.contains('دلدار'), 'Name'] = 'دلدار'
#df0.loc[df0['Name'].str.contains('دل دار'), 'Name'] = 'دلدار'
#df0.loc[df0['Name'].str.contains('دل‌دار'), 'Name'] = 'دلدار'
#df0.loc[df0['Name'].str.contains('برادرجان'), 'Name'] = 'برادرجان'
#df0.loc[df0['Name'].str.contains('برادر جان'), 'Name'] = 'برادرجان'






df0 = df0.rename(columns={'ch': 'نام شبکه'})
df0 = df0.rename(columns={'Name': 'نام برنامه'})
df0 = df0.rename(columns={'tag': 'جنس'})
#df0["avg"] = ""
#df0[['تعداد بازدید']].where(df0[['نام شبکه']].values == 'شبکه 1').stack().mean()
del df0['ch1']
#df0['avg']=df0[['تعداد بازدید']].where(df0[['نام شبکه']].values == 'تماشا').stack().mean()
#df0['avg1']=df0['تماشا']['avg']
df0.to_excel('shah05.xlsx')
#************


