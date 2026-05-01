import numpy as np, os, joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler

MODEL_PATH  = "../../models/pollution_classifier.pkl"
SCALER_PATH = "../../models/scaler.pkl"
CLASS_NAMES = ["Low Pollution", "Medium Pollution", "High Pollution"]

def generate_data(n=3000, seed=42):
    rng = np.random.default_rng(seed)
    low  = rng.normal([0.08,0.15,0.09,0.30,0.45,0.25,0.10], 0.02, (n//3,7))
    med  = rng.normal([0.12,0.18,0.14,0.22,0.20,0.15,0.30], 0.03, (n//3,7))
    high = rng.normal([0.20,0.22,0.25,0.12,0.05,0.05,0.65], 0.04, (n//3,7))
    X = np.vstack([low,med,high])
    y = np.array([0]*(n//3)+[1]*(n//3)+[2]*(n//3))
    return X, y

def train():
    print("=== AURA DRAIN — AI Model Training ===")
    X, y = generate_data()
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test  = scaler.transform(X_test)
    model = RandomForestClassifier(n_estimators=200,max_depth=12,random_state=42,n_jobs=-1)
    model.fit(X_train,y_train)
    acc = (model.predict(X_test)==y_test).mean()*100
    print(f"Accuracy: {acc:.2f}%")
    print(classification_report(y_test,model.predict(X_test),target_names=CLASS_NAMES))
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model,MODEL_PATH)
    joblib.dump(scaler,SCALER_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()
