
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Customer Churn Prediction API")


class Customer(BaseModel):
    customer_id: int = Field(gt=0)
    tenure_months: int = Field(ge=0)
    monthly_spend: float = Field(ge=0)


class PredictionResponse(BaseModel):
    customer_id: int
    risk_level: str


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse)
def predict(customer: Customer):
    risk = "high" if customer.tenure_months < 12 else "low"

    return PredictionResponse(
        customer_id=customer.customer_id,
        risk_level=risk
    )
