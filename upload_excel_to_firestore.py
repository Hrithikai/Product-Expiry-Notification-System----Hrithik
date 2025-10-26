import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("productexpirychecker-firebase-adminsdk-fbsvc-773d9d8ff1.json")  # Replace with your JSON key file
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()

# Read Excel File
df = pd.read_excel("data.xlsx")  # Replace with your Excel file

# Convert and Upload Data
for index, row in df.iterrows():
    product_data = {
        "name": row["name"],
        "expiry_date": pd.to_datetime(row["expiry_date"]),  # Keep as Timestamp (Firestore accepts this)
        "user_email": row["user_email"]
    }
    
    # Add document to Firestore in "products" collection
    db.collection("products").add(product_data)

print("✅ Data successfully uploaded to Firestore!")
