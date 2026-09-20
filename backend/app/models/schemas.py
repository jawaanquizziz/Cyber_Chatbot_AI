from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Entity(BaseModel):
    type: str
    value: str


class Indicator(BaseModel):
    name: str
    explanation: str


class AnalyzeRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=5000)
    demo_mode: bool = False


class AnalyzeResponse(BaseModel):
    category: str
    risk_level: RiskLevel
    intent: str
    intent_explanation: str
    entities: List[Entity]
    indicators: List[Indicator]
    recommended_actions: List[str]
    explanation: str
    is_demo: bool = False
    preprocessed: Optional[dict] = None


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=1000)
    analysis_context: dict


class ChatResponse(BaseModel):
    answer: str
    is_demo: bool = False
