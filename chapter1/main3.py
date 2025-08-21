from fastapi import FastAPI, status

app = FastAPI()

Product = [
    {
        'id': 1,
        'title': 'Dell'
    },
    {
        'id': 2,
        'title': 'HP'
    },
]

@app.get('/products',status_code=status.HTTP_200_OK)
async def all_products():
    return Product

@app.get('/products/{id}',status_code=status.HTTP_200_OK)
async def single_product(id: int):
    for product in Product:
        if product['id'] == id:
            return product

@app.post('/products',status_code=status.HTTP_201_CREATED)
async def create_post(new_product: dict):
    Product.append(new_product)
    return {'status': 'created', 'message': new_product}


@app.put('/products/{id}')
async def update_product(id:int, new_product:dict):
    for index, product in enumerate(Product):
        if product['id'] == id:
            Product[index] = new_product
            return {'status': 'updated','product_id':id,'message': new_product}
        
@app.patch('/products/{id}')
async def patial_product(id:int, new_product:dict):
    for product in Product:
        if product['id'] == id:
            Product.append(new_product)
            return {'status': 'updated','product_id':id,'message': new_product}
        
        
@app.delete('/products/{id}')
async def delete_product(id:int, new_product:dict):
    for index, product in enumerate(Product):
        if product['id'] == id:
            Product.pop(index)
            return {'status': 'updated','product_id':id}