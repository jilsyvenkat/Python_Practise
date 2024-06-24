import random
import csv
from faker import Faker

# Define number of employees to generate
num_employees = 100
bucket_name = "employee-data-jj"  # Replace with your GCS bucket name
csv_filename = "jj_employee_data.csv"

# Create Faker instance
fake = Faker()

# List of departments (can be customized)
departments = ["Sales", "Marketing", "Engineering", "Human Resources"]


def generate_employee_data():
    """Generates a dictionary containing dummy employee data."""
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "job_title": fake.job(),
        "department": random.choice(departments),
        "phone_number": fake.phone_number(),
        "salary": random.randint(30000,300000),
        "password":fake.password()
        # Avoid generating PII fields like address, SSN, etc.
        # "address": fake.address(),  # Uncomment if needed (be cautious about PII)
        # "ssn": fake.ssn(),  # Uncomment if needed (be cautious about PII)
    }

def write_data_to_csv(data, filename):
    """Writes employee data to a CSV file."""
    with open(filename, "w", newline="") as csvfile:
        fieldnames = data[0].keys()  # Get field names from first employee data
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def upload_to_gcs(bucket_name, filename):
    """Uploads the CSV file to a GCS bucket (requires gsutil installed)."""
    try:
        from google.cloud import storage

        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(filename)
        blob.upload_from_filename(filename)
        print(f"Employee data uploaded to GCS bucket: {bucket_name}/{filename}")
    except ModuleNotFoundError:
        print(
            "Please install 'gsutil' using 'pip install gsutil' for uploading to GCS."
        )

# Generate employee data for all employees
employees = []
for _ in range(num_employees):
    employees.append(generate_employee_data())


# Write data to CSV
write_data_to_csv(employees, csv_filename)

# Upload CSV to GCS bucket (assuming gsutil is installed)
upload_to_gcs(bucket_name, csv_filename)