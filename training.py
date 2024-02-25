#!/usr/bin/python3

from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from features import process_dataset
import joblib
  
process_dataset()
df = pd.read_csv("final_set.csv")
df.head()

X = df[['use_of_ip','abnormal_url', 'count.', 'count-www', 'count@',
       'count_dir', 'count_embed_domian', 'short_url', 'count-https',
       'count-http', 'count%', 'count?', 'count-', 'count=', 'url_length',
       'hostname_length', 'sus_url', 'fd_length', 'tld_length', 'count-digits',
       'count-letters', 'google_index']]

y = df['verdict']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2,shuffle=True, random_state=5)

rf = RandomForestClassifier(n_estimators=200,max_features='sqrt')
rf.fit(X_train.values,y_train)

joblib.dump(rf, 'phishing_ml.pkl')


# Testing the ML
y_pred_rf = rf.predict(X_test)
print(classification_report(y_test,y_pred_rf,target_names=['benign','phishing']))

score = accuracy_score(y_test, y_pred_rf)
print("accuracy:   %0.3f" % score)