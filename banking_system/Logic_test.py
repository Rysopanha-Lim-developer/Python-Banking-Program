import uuid

unique_id = str(uuid.uuid4())[:8]

for i in range(0, 6):
    unique_id = str(uuid.uuid4())[:8]
    print(unique_id)