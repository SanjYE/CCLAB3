from products import dao

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        # Fixed the init method name (should be __init__ not *init*)
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data):
        # Static method for creating a Product instance
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])

def list_products() -> list[Product]:
    # Assuming dao.list_products() returns a list of product dictionaries
    products = dao.list_products()
    return [Product.load(product) for product in products]

def get_product(product_id: int) -> Product | None:
    # Added proper return type annotation to include None
    product = dao.get_product(product_id)
    return Product.load(product) if product else None

def add_product(product: dict) -> None:
    # Added return type annotation
    dao.add_product(product)

def update_qty(product_id: int, qty: int) -> None:
    # Added return type annotation
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)