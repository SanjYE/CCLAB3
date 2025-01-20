import json
import products
from cart import dao
from products import Product


class Cart:
    def _init_(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []

    # Directly parse JSON contents and retrieve products in a single loop
    items = []
    for cart_detail in cart_details:
        contents = json.loads(cart_detail['contents'])  # Use json.loads instead of eval
        product_ids = [content for content in contents]  # Extract product IDs directly
        items.extend(product_ids)

    # Retrieve all products in one go using a batch operation
    products_list = products.get_products_batch(items)  # Assuming batch retrieval is supported
    return products_list


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)