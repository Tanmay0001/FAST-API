from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd
import os

# Initialize FastAPI app
app = FastAPI()

# Global variable for the model
model = None

# Define city tiers
tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

# Pydantic model for user input
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120)]
    weight: Annotated[float, Field(..., gt=0)]
    height: Annotated[float, Field(..., gt=0, lt=2.5)]
    income_lpa: Annotated[float, Field(..., gt=0)]
    smoker: bool
    city: str
    occupation: Literal[
        'retired', 'freelancer', 'student', 'government_job',
        'business_owner', 'unemployed', 'private_job'
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3

# Startup event: load the model
@app.on_event("startup")
def load_model():
    global model
    model_path = os.path.join(os.path.dirname(__file__), "model", "model.pkl")
    if os.path.exists(model_path):
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        print(f"Model loaded successfully from {model_path}")
    else:
        print(f"Warning: Model file not found at {model_path}")
        model = None


# Endpoint to predict insurance premium category
@app.post("/predict")
def predict_premium(data: UserInput):
    if model is None:
        return JSONResponse(
            {"error": "Model is not loaded. Please check if model/model.pkl exists."}, 
            status_code=500
        )

    input_df = pd.DataFrame([{
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation,
    }])

    prediction = model.predict(input_df)[0]
    return JSONResponse({"predicted_category": prediction})
