from fastapi import FastAPI, Path, HTTPException, Query
import json

# app object of fast api to define for fastapi
app = FastAPI()


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
        return data
    

@app.get("/")
def hello():
    return {'message': 'Patient MnagementSystem API'}

    # another endpoint

@app.get("/about")
def about():
    return {'message': 'A fully functionsl API to manage patient records'}

@app.get("/view")
def view():
    data = load_data()
    return data



# setting path parameter

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., desciption='ID  of the patient in the DB', example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return HTTPException(status_code=404, detail='Patient not found')




# Query parameter

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str= Query('asc', description='Sort in asc or desc order')):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invaid field select from {valid_fields}')
    
    if order not in ['asc' , 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()
    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data
   