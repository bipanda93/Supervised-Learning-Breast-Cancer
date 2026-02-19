import pandas as pd
import numpy as np
import sklearn
import matplotlib as mpl
import seaborn as sns
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from sklearn.datasets import load_breast_cancer
breast_cancer = load_breast_cancer()
print("Type de l'objet breast_cancer :", type(breast_cancer))
print("Clés disponibles :", breast_cancer.keys())
print("\nNoms des features (colonnes) :", breast_cancer.feature_names)
print("Noms des classes :", breast_cancer.target_names)

X = breast_cancer.data
Y = breast_cancer.target
#X.shape -> (nombre_lignes, nombre_features)
# y.shape -> (nombre_lignes,)
print("\nDimension de X :", X.shape)
print("Dimension de Y :", Y.shape)

df = pd.DataFrame(X,columns=breast_cancer.feature_names)
df["target"]= Y
print("\nAperçu du dataset (5 premières lignes) :")
print(df.head(10))

X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.2, random_state=42)
print("X_train :", X_train.shape)
print("X_test :", X_test.shape)
print("Y_train :", Y_train.shape)
print("Y_test :", Y_test.shape)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # apprend la moyenne/écart-type sur train
X_test = scaler.transform(X_test)        # applique la même transformation sur test

model = SVC()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print("\nValeurs réelles (Y_test) :", Y_test)
print("Valeurs prédites (Y_pred):", Y_pred)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy :", accuracy)

cm = confusion_matrix(Y_test, Y_pred)
print("\nConfusion Matrix :")
print(cm)

print("\nClassification Report :")
print(classification_report(Y_test, Y_pred))

print("\nTest de plusieurs valeurs de C :")
for c in [0.1, 1, 10, 100]:
    model = SVC(C=c, kernel='rbf')
    model.fit(X_train, Y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(Y_test, y_pred)
    print("C =", c, "-> Accuracy =", acc)