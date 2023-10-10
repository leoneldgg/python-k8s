from pydantic import BaseModel, Field


class ProductIn(BaseModel):
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Price of the product")

class ProductOut(BaseModel):
    id: str = Field(..., description="Product ID")
    name: str =  Field(..., description="Product name") 
    price: float = Field(..., description="Price of the product")




