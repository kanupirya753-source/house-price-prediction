python 
import pandas as pd 
from sklearn.datasets import fetch_ califorina_houseing 
from sklearn.model_selection import_train_test_ split 
from sklearn.preprocessing import standardscaler 
# Dataset load karna 
houseing = fetch_calinaforina_housing(as_frame=True)
df = housing.frame
# features aur target alag karna
x = df. drop(columins=["MedHouseVal"]
y = df ["MedHouseVal"]
# Train-Test Split
x_train, X_test, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
# Scaling
scaler = standardScaler()
X_train_Scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler. transform(X_train)
print("Data preprocessing Complete!")
