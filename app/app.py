from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model_utils import load_model, predict_risk
import yaml
import logging
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Load config.yaml
try:
    with open("app/config.yaml", encoding="utf-8") as f:
        config = yaml.safe_load(f)
except Exception as e:
    raise RuntimeError(f"Error loading config file: {e}")

# Setup logging
logging.basicConfig(
    filename="logs/monitoring.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load ML model
try:
    model = load_model(config["model_path"])
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

# Define input schema
class InputData(BaseModel):
    thalachh: float
    exng: int
    oldpeak: float

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Heart attack risk predictor is running."}

@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert input to dict
        input_dict = data.model_dump()  # For Pydantic v2.x
        prediction, result = predict_risk(model, input_dict)

        logging.info(f"Input: {input_dict} → Pred: {result}")
        return {
            "prediction": int(prediction),
            "result": result,
            "input": input_dict
        }

    except Exception as e:
        logging.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Internal prediction error")

