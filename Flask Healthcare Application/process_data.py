# process_data.py

from pymongo import MongoClient
import csv
from user import User

# MongoDB Atlas URI
uri = "mongodb+srv://razbinokelly01:DO9SznxYxfzr22uc@cluster0.pkxj0ek.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(uri)
db = client['healthcare_survey']
collection = db['user_data']

# Fetch all user documents
documents = collection.find()

#csv output file
output_file = 'user_data.csv'

# open and write to csv

with open(output_file, mode='w', newline='', encoding="utf-8") as csv_file:
    fieldnames = ["Age", "Gender", "Income", "Utilities", "Entertainment", "School_fees", "Shopping", "Healthcare"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    # Write each user document to the CSV
    for doc in documents:
        user = User(
            age=doc.get("age"),
            gender=doc.get("gender"),
            income=doc.get("income"),
            expenses=doc.get("expenses", {})
        )
        writer.writerow(user.to_dict())

print("Data exported to user_data.csv")