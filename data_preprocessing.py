import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data():
    # Load data from the database or CSV
    data = pd.read_csv('user_logs.csv')  # Replace with actual data source

    # Select relevant features for the model
    features = ['temperature', 'diet', 'exercise', 'sleep_hours', 'mood']
    X = data[features]
    y = data['fertility_window']  # Target variable (0 or 1 for fertility window)

    # Handle categorical data (e.g., mood, diet, exercise)
    X = pd.get_dummies(X)

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test
