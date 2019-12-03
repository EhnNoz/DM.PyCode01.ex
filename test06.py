
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import json
from ast import literal_eval
from itertools import chain

df0 = pd.read_excel('data011.xlsx')
df9 = pd.read_excel('test08.xlsx')
df01 = pd.read_excel('data02.xlsx')
Row_list =[] 
Row_list2 =[]
Row_list3 =[] 
Row_list4 =[]
Row_list5 =[]

Row_list25 =[]
Row_list35 =[] 
Row_list45 =[]
Row_list55 =[] 


  
#df0=df0.set_index(0).T
#df0.to_excel('test08.xlsx')
#df0['Name'] = df0['Name'].str.rstip()
df1=df0['Name'].apply(lambda x: pd.Series(list(x)))  
df1=df1.set_index(0).T
#df1.columns=['Name']
#df0.Name.str.extractall('(.)', flags=re.U)[0].unstack().rename_axis(None, 1)
#df2=df1.rename(index={0:'Name'}, inplace=True)
df1.to_excel('test07.xlsx')
df4 = pd.read_excel('test03.xlsx')
df4=df4['Name'].apply(lambda x: pd.Series(list(x)))

df4=df4.set_index(0).T
df4.to_excel('test08.xlsx')
df5=df4
#df4.columns=['Name']
for i in range(0,14):
    print(i)
    df5.loc[:,i] = df4.iloc[:,0].isin(df1.iloc[:,i]).astype(np.int8)

    
df5.to_excel('test09.xlsx')
df5=df5.set_index(0).T
df5.to_excel('test10.xlsx')
df6=df0
df6['vec'] = df5[df5.columns[30:]].apply(
    lambda x: ''.join(x.dropna().astype(str).astype(str)),
    axis=1
)
df6['vec'] = df6['vec'].astype(str)
df6['vec'] = ('1' + df6['vec'])
df6=df6.drop(0,axis='rows')
df6.to_excel('test11.xlsx')

#************************************
df10 = pd.read_excel('data012.xlsx')

df11=df10['Name'].apply(lambda x: pd.Series(list(x)))  
df11=df11.set_index(0).T

df11.to_excel('test071.xlsx')
df51=df4
for t in range(0,14):
    print(t)
    df51.loc[:,t] = df4.iloc[:,0].isin(df11.iloc[:,t]).astype(np.int8)

    
df51.to_excel('test091.xlsx')
df51=df51.set_index(0).T
df51.to_excel('test101.xlsx')
df61=df10
df61['vec2'] = df51[df51.columns[30:]].apply(
    lambda x: ''.join(x.dropna().astype(str).astype(str)),
    axis=1
)
df61['vec2'] = df61['vec2'].astype(str)
df61['vec2'] = ('1' + df61['vec2'])
df61=df61.drop(0,axis='rows')
df61.to_excel('test111.xlsx')
#**************************************
df103 = pd.read_excel('data013.xlsx')
df103['Name'] = df103['Name'].astype(str)

df104 = pd.read_excel('data014.xlsx')
df104['Name'] = df104['Name'].astype(str)




#****************************************

#df7 = pd.read_excel('test12.xlsx')
Row_list = df6["vec"].tolist()
print (Row_list)
m = Row_list

df8 = pd.read_excel('test14.xlsx')
Row_list2 = df61["vec2"].tolist()
print (Row_list2)
n= Row_list2

Row_list4 = df103["Name"].tolist()
print (Row_list4)
p= Row_list4

Row_list3 = df104["Name"].tolist()
print (Row_list3)
g= Row_list3


Row_list5 = [list(a) for a in zip(Row_list, Row_list2, Row_list4, Row_list3)]
q=Row_list5

#b = [[j] for j in q]

print(q)


#X = [['1100000010010010000000100001011', '1100000010010010000000100001011'], ['1100000010010000000000000000000', '1100000010010000000000000000000'], ['1100000010010000000000100000011', '1100000010010000000000100000011'], ['1000000001000000000000000001100', '1000000001000000000000000001100'], ['1000000000000000000000000001000', '1000000000000000000000000001000'], ['1000000001000000000001000001100', '1000000001000000000001000001100'], ['1000000001010000000000010011010', '1000000001010000000000010011010'], ['1000000001010000000000000011011', '1000000001010000000000000011011'], ['1000000000010010000000010010001', '1000000000010010000000010010001'], ['1001000000010000000000000100001', '1001000000010000000000000100001'], ['1000000000010010000000000100001', '1000000000010010000000000100001'], ['1001000000010000000000000000000', '1001000000010000000000000000000'], ['1001000000010000000000000000001', '1001000000010000000000000000001']]
#Y = ['news','news','news','ser','ser','ser','doc','doc','doc','film','film','film','film']
#****************************











#*************************
df105 = pd.read_excel('data015.xlsx')

df115=df105['Name'].apply(lambda x: pd.Series(list(x)))  
df115=df115.set_index(0).T

df115.to_excel('test075.xlsx')
df515=df4
for t in range(0,14):
    print(t)
    df515.loc[:,t] = df4.iloc[:,0].isin(df115.iloc[:,t]).astype(np.int8)

    
df515.to_excel('test095.xlsx')
df515=df515.set_index(0).T
df515.to_excel('test1015.xlsx')
df615=df105
df615['vec25'] = df515[df515.columns[30:]].apply(
    lambda x: ''.join(x.dropna().astype(str).astype(str)),
    axis=1
)
df615['vec25'] = df615['vec25'].astype(str)
df615['vec25'] = ('1' + df615['vec25'])
df615=df615.drop(0,axis='rows')
df615.to_excel('test1115.xlsx')

Row_list25 = df615["vec25"].tolist()
#print (Row_list25)
mm = Row_list25

#df85 = pd.read_excel('test14.xlsx')
#Row_list2 = df61["vec2"].tolist()
#print (Row_list2)
#n= Row_list2
#
#Row_list4 = df103["Name"].tolist()
#print (Row_list4)
#p= Row_list4
#
#Row_list3 = df104["Name"].tolist()
#print (Row_list3)
#g= Row_list3


Row_list55 = [list(a) for a in zip(Row_list25, Row_list2, Row_list4, Row_list3)]
qq=Row_list55

#b = [[j] for j in q]

print(qq)

#***************************
X = q
Y = ['news','news','news','ser','ser','ser','doc','doc','doc','film','film','film','film']

test_data = qq
test_labels = ['news','news','news','ser','ser','ser','doc','doc','doc','film','film','film','film']
################

#test_data = [[190, 70, 43],[154, 75, 42],[181,65,40]]
#test_labels = ['male','female','male']

#DecisionTreeClassifier
dtc_clf = tree.DecisionTreeClassifier()
dtc_clf = dtc_clf.fit(X,Y)
dtc_prediction = dtc_clf.predict(test_data)
print (dtc_prediction)

#RandomForestClassifier
rfc_clf = RandomForestClassifier()
rfc_clf.fit(X,Y)
rfc_prediction = rfc_clf.predict(test_data)
print (rfc_prediction)

#Support Vector Classifier
s_clf = SVC()
s_clf.fit(X,Y)
s_prediction = s_clf.predict(test_data)
print (s_prediction)

#X =  pd.DataFrame(data=X) 
#X = X.astype(float)
#LogisticRegression
#l_clf = LogisticRegression()
#l_clf.fit(X,Y)
#l_prediction = l_clf.predict(test_data)
#print (l_prediction)

#accuracy scores
dtc_tree_acc = accuracy_score(dtc_prediction,test_labels)
rfc_acc = accuracy_score(rfc_prediction,test_labels)
#l_acc = accuracy_score(l_prediction,test_labels)
s_acc = accuracy_score(s_prediction,test_labels)

classifiers = ['Decision Tree', 'Random Forest', 'Logistic Regression' , 'SVC']
accuracy = np.array([dtc_tree_acc, rfc_acc, s_acc])
max_acc = np.argmax(accuracy)
print(classifiers[max_acc] + ' is the best classifier for this problem')





