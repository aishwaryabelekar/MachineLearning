# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:48:12 2024

@author: abelekar
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_excel('dataset.xlsx')

# 'X' contains features and 'y' contains target variable
X = df.drop(columns=['Mission_Time_Secs'])  
y = df['Mission_Time_Secs']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest classifier
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train, y_train)

# Predictions on the testing set
y_pred = rf_classifier.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
