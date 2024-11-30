import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset (replace this with your actual file path if needed)
file_path = '/Users/himeshdilankananayakkara/Desktop/Y4S1/reseach/model/stress-management-dataset.csv'  # Update path if necessary
df = pd.read_csv(file_path)

# Preprocessing and encoding
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['gender'])  # Female=0, Male=1
df['Stress Level'] = label_encoder.fit_transform(df['stress_level'])  # High=0, Moderate=1, Low=2
df['Age Group'] = label_encoder.fit_transform(df['age'])  # Teenager=0, Young Adult=1

# Features and target
X = df[['Gender', 'Stress Level', 'Age Group']]
df['Category'] = df['Stress Level']  # Example: Classify based on Stress Level
y = df['Category']  

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Evaluate model accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model to a file
model_filename = 'stress_management_model.pkl'
joblib.dump(classifier, model_filename)
print(f"Model saved as {model_filename}")
