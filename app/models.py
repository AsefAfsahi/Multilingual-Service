
from pydantic import BaseModel, Field
from typing import Dict

class Document(BaseModel):
    identifier: str = Field(..., description="The unique identifier for the document.")
    body: Dict[str, str] = Field(..., description="A dictionary of language codes to text content. e.g., {'en': 'Hello', 'fa': 'سلام'}")
