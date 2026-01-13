# exporting.py

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

# Address input
address_dict = {
    "city": "Gurgaon",
    "state": "Haryana",
    "pin": "1234"
}

# Create Address object
address = Address(**address_dict)

# Patient input  ← THIS was missing or misnamed before
patient_dict = {
    "name": "Tommy",
    "gender": "male",
    "age": "35",     # string → int conversion by Pydantic
    "address": address
}

# Create Patient object
patient1 = Patient(**patient_dict)

# Export model to dictionary
temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))
