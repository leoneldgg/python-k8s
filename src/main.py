from fastapi import FastAPI, APIRouter
from data.data import data
from fastapi_pagination import Page, add_pagination, paginate
from models.models import ProductIn, ProductOut
from fastapi.responses import JSONResponse
from fastapi import status
from uuid import uuid4

app = FastAPI(
    title="Python K8s",
    version="0.0.1"
)


router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=Page[ProductOut])
async def get_products():
    return paginate(data)

@router.get("/{product_uuid}", response_model=ProductOut)
async def get_product(product_uuid: str):
    results = list(filter(lambda p: p.get("id") == product_uuid, data))

    if results:
        return JSONResponse(content=results[0], status_code=status.HTTP_200_OK)
    return JSONResponse(content={"msg": "Product not found"}, status_code=status.HTTP_404_NOT_FOUND)


@router.post("/", response_model=ProductOut)
async def add_product(product: ProductIn):
    product_dict = product.model_dump()
    product_dict["id"] = str(uuid4())
    data.append(product_dict)

    return product_dict


@router.delete("/{product_uuid}", response_model=ProductOut)
async def delete_product(product_uuid: str):
    global data

    product_to_remove = list(filter(lambda p: p.get("id") == product_uuid, data))
    if not product_to_remove:
        return JSONResponse(content={"msg": "Product not found"}, status_code=status.HTTP_404_NOT_FOUND)
    product_to_remove = product_to_remove[0]

    data = list(filter(lambda p: p.get("id") != product_uuid, data))
    return product_to_remove


app.include_router(router)
add_pagination(app)
