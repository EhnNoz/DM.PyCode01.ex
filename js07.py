
import json
import pandas as pd
import numpy as np


with open('iribchannel4-media metadata.json', 'r', encoding='utf-8') as f:
    y = json.load(f)
    f.close()
 
df0 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df6 = pd.DataFrame()


for k in range(0,5):
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




df7=df1['caption'].str.split(expand=True)
#print (df1)

df7=df7.set_index(0).T
df7.to_excel('tr0104.xlsx', index=False)    






#b = len(df1)
#
df8 = pd.read_excel('cap06.xlsx')
df9 = pd.read_excel('tr0104.xlsx')
df10=df8
##b=10
b = len(df1)
for i in range(0,b):
##    print(i)
#    try:
        df10.loc[:,i] = df8.iloc[:,0].isin(df9.iloc[:,i]).astype(np.int8)
#    except:
#        pass

df10.to_excel('tr0103.xlsx', index=False)


numeric_cols = [col for col in df10 if df10[col].dtype.kind != 'O']
df10[numeric_cols] += 1
df10=df10.set_index(0).T


df10.iloc[0]=df10.iloc[1]
df10.to_excel('tr0105.xlsx')

from IPython import get_ipython
get_ipython().magic('reset -sf')
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

df13=pd.read_excel('tr0105.xlsx')
#df13.iloc[0]=df13.iloc[1]
df12=pd.read_excel('cap01.xlsx')
#df13=df13.drop(0,axis='rows')
df13.to_excel('tr0107.xlsx', index=False)

c=len(df13.columns)-3
#df12 = pd.DataFrame()

df12['vec'] = df13[df13.columns[1:]].apply(
    lambda x: ''.join(x.dropna().astype(str).astype(str)),
    axis=1
)

df12['vec'] = df12['vec'].astype(str)

df12=df12.drop(0,axis='rows')
df12.to_excel('tr0106.xlsx')

Row_list2 = df12["vec"].tolist()
print (Row_list2)
m = Row_list2
b = [[j] for j in m]
print (b)

X = b
Y = ['پزشکی','فرهنگی','فرهنگی','پزشکی']

test_data = b
test_labels = ['پزشکی','فرهنگی','فرهنگی','پزشکی']
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
