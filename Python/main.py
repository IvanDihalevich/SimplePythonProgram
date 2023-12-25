from flask import Flask, request

app = Flask(__name__)


class Product:
    def __init__(self, product_id: str, title: str, price: int):
        self.product_id = product_id
        self.title = title
        self.price = price


class Shop:
    def __init__(self):
        self.__products: list[Product] = self.__get_products()

    def __get_products(self):
        products_file = open("products.csv", "r")

        products = []
        for line in products_file:
            product_parts = line.split(';')
            if len(product_parts) == 3:
                products.append(Product(product_parts[0], product_parts[1], int(product_parts[2])))

        return products

    def __update_file(self):
        products_file = open("products.csv", "w")

        products_file.writelines([f"\n{p.product_id};{p.title};{p.price}" for p in self.__products])

    def get_products_api(self):
        return [{"product_id": p.product_id, "title": p.title, "price": p.price} for p in self.__products]

    def add_product(self, p: Product):
        self.__products.append(p)
        self.__update_file()

    def remove_product(self, product_id: str):
        self.__products = [p for p in self.__products if p.product_id != product_id]
        self.__update_file()

    def get_most_expensive_product(self):
        return max(self.__products, key=lambda product: product.price)


shop = Shop()


@app.get("/get-products")
def get_products():
    return shop.get_products_api()


@app.post('/create-product')
def create_product():
    request_body = request.json

    product_id = request_body["product_id"]
    title = request_body["title"]
    price = request_body["price"]

    shop.add_product(Product(product_id, title, price))

    return {"Success": True}


@app.delete('/delete-product/<product_id>')
def delete_product(product_id):
    shop.remove_product(product_id)

    return {"Success": True}


@app.get('/most-expensive-product')
def get_m_e_p():
    p = shop.get_most_expensive_product()

    return {"product_id": p.product_id, "title": p.title, "price": p.price}


if __name__ == "__main__":
    app.run(debug=True)
