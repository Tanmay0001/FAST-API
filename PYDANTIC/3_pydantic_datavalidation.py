from pydantic import BaseModel, email, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# type valoidation

class Patient(BaseModel):
    name: str = Field(max_length=50)
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print('inserted')


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name': 'nitish', 'age': 18, 'weight': 25, 'married':True, 'allergies':['polen', 'dust'], 'contact_details':{'email': 'abc@gmail.com', 'phone':'235456787'}}


patient1 = Patient(**patient_info)
update_patient_data(patient1)