python
import joblib
from sklearn.datasets import fetch_califorina_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing importstandardScaler
housing = fetch_califorina_housing(as_frame=True)
df = housing.frame
X = df.drop(columns=[MedHouseVal"])
y =df["MedHouseVal"]
 X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.2,random_state=42)
 scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
# Model Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_Scaled, y_train)
# Save Model
joblib.dump(model, "house_price_model.pKl")
joblib.dump(scaler, "scaler.pKl")
print("Model Trained and saved Successfully!")
