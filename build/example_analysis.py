# Load your dataset
from archetypes.patient_db.patient_db import create_dataset

dataset = create_dataset()
print(f"Dataset size: {len(dataset)} records")

for record in dataset:
    print(record.patient.patient_id)
