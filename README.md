
# 🫀 Heart Attack Risk Predictor API

This project is a **FastAPI-based machine learning inference service** that predicts the risk of a heart attack based on input medical parameters. The model is trained with `scikit-learn` and can be deployed locally or via Docker.

---

## 🚀 Features

- Predict heart attack risk using `thalachh`, `exng`, and `oldpeak` values
- REST API with `/predict` endpoint
- Logging of prediction inputs and results
- Configuration via `config.yaml`
- Unit tests for model correctness

---

## 📁 Project Structure

```
demo_HeartAtk_ml/
│
├── app/
│   ├── app.py                # FastAPI app
│   ├── config.yaml           # Config file with model path
│   └── model_utils.py        # Model load and predict logic
│
├── model/
│   └── heart_atk_model.sav   # Trained ML model (pkl file)
│
├── notebook/
│   └── training_script.ipynb # Optional: model training notebook
│
├── tests/
│   └── test_model.py         # Unit test for prediction
│
├── logs/
│   └── monitoring.log        # Prediction logs
│
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker setup
├── .dockerignore             # Docker ignore rules
└── README.md                 # Project documentation
```

---

## ⚙️ Installation (Local)

```bash
# Clone this repo
git clone <your-repo-url>
cd demo_HeartAtk_ml

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run FastAPI app
uvicorn app.app:app --reload
```

Then open: [http://localhost:8100/docs](http://localhost:8100/docs)

---

## 🐳 Docker Setup

```bash
# Build the image
docker build -t heart-api .

# Run the container
docker run -d -p 8100:8100 heart-api
```

Then go to: [http://localhost:8100/docs](http://localhost:8100/docs)

---

## 📨 API Example (POST /predict)

```json
POST /predict
{
  "thalachh": 157.0,
  "exng": 0,
  "oldpeak": 1.6
}
```

**Response:**

```json
{
  "prediction": 1,
  "result": "more chance of heart attack",
  "input": {
    "thalachh": 157.0,
    "exng": 0,
    "oldpeak": 1.6
  }
}
```

---

## 🧪 Run Unit Tests

```bash
python -m unittest discover tests
```

---

## 🛠️ Configuration

Edit `app/config.yaml` to set model path and other runtime configs:

```yaml
model_path: "model/heart_atk_model.sav"
```

---

## 📋 Requirements

See `requirements.txt` for pinned library versions. Key dependencies include:

- fastapi
- scikit-learn
- pydantic
- uvicorn
- PyYAML

---

## 📌 License

MIT License. See `LICENSE` file if available.

---

## ✍️ Author

Polakorn Anantapakorn
