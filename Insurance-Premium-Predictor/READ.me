"Insurance Premium Category Predictor"

End-to-End ML → API → Docker → AWS EC2 Project

1️⃣ About

This project was built to practice and demonstrate an end-to-end Machine Learning system, not just model training.

The goal was to:

Train an ML model on tabular insurance data

Engineer features consistently for both training and inference

Serve predictions via a FastAPI backend

Package the system using Docker

Deploy it on AWS EC2 (Free Tier) over HTTP

This repository acts as a reference implementation for future ML-backend projects.

2️⃣ What Problem This Solves

Insurance companies often classify customers into premium categories:

Low

Medium

High

based on:

Demographics

Health indicators

Lifestyle risks

Location

Income & occupation

This system predicts the insurance premium category for a user using those factors.

3️⃣ High Level Architecture (Mental Model)
Raw User Input
   ↓
Pydantic Validation (FastAPI)
   ↓
Feature Engineering (runtime)
   ↓
Pickled ML Pipeline
   ↓
Prediction + Probabilities
   ↓
JSON API Response


And at the infrastructure level:

FastAPI App
   ↓
Docker Container
   ↓
AWS EC2 (Free Tier)
   ↓
HTTP API

4️⃣ Dataset & Training (Offline – Colab)
🔹 Dataset

File: insurance.csv

Rows: 100

Target: insurance_premium_category

🔹 Raw Features
Feature	Description
age	User age
weight	Weight (kg)
height	Height (meters)
income_lpa	Annual income
smoker	Smoking status
city	City name
occupation	Employment type
5️⃣ Feature Engineering Logic (CRITICAL)

To ensure training = inference, feature logic was replicated exactly in backend code.

Engineered Features
Feature	Logic
bmi	weight / height²
age_group	young / adult / middle_aged / senior
lifestyle_risk	based on BMI + smoker
city_tier	Tier 1 / Tier 2 / Tier 3
income_lpa	unchanged
occupation	unchanged

Important Design Choice
Feature engineering is done:

In training notebook

Again inside FastAPI (via computed fields)

This avoids data leakage and mismatch.

6️⃣ Model Training Pipeline
Model Type

RandomForestClassifier

Pipeline Structure
ColumnTransformer
 ├─ OneHotEncoder (categorical)
 └─ Passthrough (numeric)
        ↓
RandomForestClassifier

Training Details

Train/Test Split: 80/20

Accuracy: ~90%

Saved using pickle

Output Artifact
model/model.pkl


This file contains:

Preprocessing

Encoding

Model
(all in one pipeline)

7️⃣ Backend Design (FastAPI)
Folder Structure
Insurance-Premium-Predictor/
├── app.py                  # API entry point
├── Dockerfile              # Container config
├── requirements.txt
├── config/
│   └── city_tier.py        # City → Tier mapping
├── model/
│   ├── model.pkl           # Trained pipeline
│   └── predict.py          # Inference logic
├── schema/
│   ├── user_input.py       # Request validation + features
│   └── prediction_response.py

8️⃣ Input Validation & Runtime Feature Engineering
UserInput (Pydantic)

Validates raw user data

Normalizes city names

Computes:

BMI

Age group

Lifestyle risk

City tier

This ensures:

Clean API inputs

No invalid data reaches the model

9️⃣ Prediction Flow (Runtime)

Client sends raw user data

FastAPI validates input

Computed features are generated

Pickled pipeline predicts:

Class

Probabilities

API returns structured JSON response

🔌 API Endpoints
Home
GET /

Health Check
GET /health


Used to confirm:

App is running

Model is loaded

Version is correct

Prediction
POST /predict


Returns:

Predicted category

Confidence score

Probability distribution

🐳 Dockerization

The application is fully containerized.

Why Docker?

Environment consistency

Easy cloud deployment

No dependency issues

Docker Flow
docker build -t insurance-premium-predictor .
docker run -p 8000:8000 insurance-premium-predictor

☁️ AWS EC2 Deployment (Free Tier)
Setup

Instance: t2.micro

OS: Ubuntu / Amazon Linux

Ports opened:

22 (SSH)

8000 (HTTP)

Deployment Steps (Conceptual)

Launch EC2

Install Docker

Clone repo

Build image

Run container

Access
http://<EC2_PUBLIC_IP>:8000
