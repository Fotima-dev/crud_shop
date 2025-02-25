import requests

def get_all_carts():
    response = requests.get('https://fakestoreapi.com/carts')
     if response.status_code == 200:
        carts= response.json()
        return carts

def get_single_cart(cart_id):
    response = requests.get('https://fakestoreapi.com/carts/{cart_id}')
     if response.status_code == 200:
        cart = response.json()
        return cart

def get_sorted_carts(desc):
    response = requests.get('https://fakestoreapi.com/carts?sort={desc}')
     if response.status_code == 200:
        product = response.json()
        return product

def get_limited_carts(limit):
    response = requests.get('https://fakestoreapi.com/carts?limit={limit}')
     if response.status_code == 200:
        carts = response.json()
        return carts
