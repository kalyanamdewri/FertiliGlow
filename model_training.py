from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from data_preprocessing import load_and_preprocess_data

def train_model():
    X_train, X_test, y_train, y_test = load_and_preprocess_data()

    # Train a random forest classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")

    # Save the trained model
    with open('fertility_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    return model

if __name__ == "__main__":
    train_model()
