#

import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score




d=[]
data= pd.read_excel ("x-train5.xlsx")


#data['chan'] = data['chan'].astype(str)
#data['chan'] = data['chan'].str[:3]

data['title'] = data[data.columns[0:]].apply(
    lambda x: ''.join(x.dropna().astype(str).astype(str)),
    axis=1
)

data.to_excel('x-train20.xlsx')

data['title'] = data['title'].astype(str)

#data['title'] = data['title'].apply(lambda x: '{0:0>48}'.format(x))
data['title1'] = data['title'].str[:10]
data['title1'] = data['title1'].apply(lambda x: '{0:0<10}'.format(x))
d=data['title1'].tolist()
print (d)
ascii = []
for word in d:
    ascii_word = []
    for char in word:
        ascii_word.append(ord(char))
    ascii.append(ascii_word)  # Change this line

print (ascii)

data['dtc'] = ascii
data.to_excel('testt15.xlsx')


#####################################


#data['chan'] = data['chan'].astype(str)
#
#
#data['chan1'] = data['chan'].str[4:]
#data['chan1'] = data['chan1'].apply(lambda x: '{0:0>1}'.format(x))
#d2=data['chan1'].tolist()
#print (d2)
#ascii2 = []
#for word in d2:
#    ascii2_word = []
#    for char in word:
#        ascii2_word.append(ord(char))
#    ascii2.append(ascii2_word)  # Change this line
#
#print (ascii2)
#
#data['dtc2'] = ascii2
#data.to_excel('testt15.xlsx')
#
#
#Row_list50 = [list(a) for a in zip(ascii, ascii2)]
##q0=Row_list50
#q0=Row_list50




####################################
#cf103 = pd.read_excel('h-train.xlsx')
#cf103['hour'] = cf103['hour'].astype(str)
##cf103=cf103.drop(0,axis='rows')
#Row_list40 = cf103["hour"].tolist()
#print (Row_list40)
#p0= Row_list40
#
#
#Row_list50 = [list(a) for a in zip(ascii, Row_list40)]



df5555 = pd.read_excel('y-train5.xlsx')
Row_list55 = df5555["tag"].tolist()
print (Row_list55)
gg= Row_list55



#############################################################################################
d0=[]

data0= pd.read_excel ("x-test5.xlsx")

#data['chan'] = data['chan'].astype(str)
#data['chan'] = data['chan'].str[:3]


data0['title'] = data0[data0.columns[0:]].apply(
    lambda x: ''.join(x.dropna().astype(str).astype(str)),
    axis=1
)






data0['title'] = data0['title'].astype(str)
data0['title1'] = data0['title'].str[:10]
data0['title1'] = data0['title1'].apply(lambda x: '{0:0<10}'.format(x))
d0=data0['title1'].tolist()
print (d0)
ascii0 = []
for word0 in d0:
    ascii_word0 = []
    for char in word0:
        ascii_word0.append(ord(char))
    ascii0.append(ascii_word0)  # Change this line

print (ascii0)

data0['dtc'] = ascii0
data0.to_excel('testt150.xlsx')

#df103 = pd.read_excel('h-test.xlsx')
#df103['hour'] = df103['hour'].astype(str)
##cf103=cf103.drop(0,axis='rows')
#Row_list400 = df103["hour"].tolist()
#print (Row_list400)
##p0= Row_list40
#
#
#Row_list500 = [list(a) for a in zip(ascii0, Row_list400)]
##############################

#data0['chan'] = data0['chan'].astype(str)
#
#
#data0['chan1'] = data0['chan'].str[4:]
#data0['chan1'] = data0['chan1'].apply(lambda x: '{0:0>1}'.format(x))
#d20=data0['chan1'].tolist()
#print (d20)
#ascii20 = []
#for word in d20:
#    ascii20_word = []
#    for char in word:
#        ascii20_word.append(ord(char))
#    ascii20.append(ascii20_word)  # Change this line
#
#print (ascii20)
#
#data0['dtc2'] = ascii20
#data0.to_excel('testt150.xlsx')
#
#
#Row_list500 = [list(a) for a in zip(ascii0, ascii20)]
##q0=Row_list50
#q00=Row_list500

#########################################


df55550 = pd.read_excel('y-test5.xlsx')
Row_list550 = df55550["tag"].tolist()
print (Row_list550)
gg0= Row_list550
###############################################################################################
##############
X = ascii
Y = gg

test_data = ascii0
test_labels = gg0
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


#LogisticRegression
l_clf = LogisticRegression()
l_clf.fit(X,Y)
l_prediction = l_clf.predict(test_data)
print (l_prediction)

#accuracy scores
dtc_tree_acc = accuracy_score(dtc_prediction,test_labels)
rfc_acc = accuracy_score(rfc_prediction,test_labels)
l_acc = accuracy_score(l_prediction,test_labels)
s_acc = accuracy_score(s_prediction,test_labels)

classifiers = ['Decision Tree', 'Random Forest', 'Logistic Regression' , 'SVC']
accuracy = np.array([dtc_tree_acc, rfc_acc, l_acc, s_acc])
max_acc = np.argmax(accuracy)
print(classifiers[max_acc] + ' is the best classifier for this problem')

df55550['name'] = d0
df55550['dtc'] = dtc_prediction
df55550['rfc'] = rfc_prediction
df55550['l'] = l_prediction
df55550['s'] = s_prediction

#cf61.loc[cf61['s'].str.contains('مجموعه'), 's2'] = 'مجموعه تلویزیونی'
#cf61.loc[cf61['dtc'].str.contains('اخبار'), 's2'] = 'اخبار'
#cf61.loc[cf61['dtc'].str.contains('سینمایی'), 's2'] = 'فیلم سینمایی'



df55550.to_excel('testt155.xlsx')

#print (q0)



















