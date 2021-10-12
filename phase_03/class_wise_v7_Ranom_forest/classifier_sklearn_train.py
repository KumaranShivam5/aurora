import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 
np.random.seed(91828)
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix 

data = pd.read_csv('processed_data/train_norm_corr')
data = data.sample(frac=1)
#x =  data.drop(columns=['class' , 'src_n' ,'src_id' ,'significance'])
x = data.copy()
y = data['class']
x_train , x_test , y_train , y_test = train_test_split(x,y , test_size=0.2 , stratify=y)
id_train = x_train[['src_id']]
id_test = x_test[['src_id']]
x_train = x_train.drop(columns=['class' , 'src_n' ,'src_id' ,'significance'])
x_test = x_test.drop(columns=['class' , 'src_n' ,'src_id' ,'significance'])


clf = RandomForestClassifier(n_estimators=300 ,random_state=1)
clf.fit(x_train, y_train)
test_score = clf.score(x_test , y_test)
train_score =clf.score(x_train , y_train)
print(train_score)
print(test_score)

import pickle
with open('models/sklearn_rf', 'wb') as f:
    pickle.dump(clf, f)



    