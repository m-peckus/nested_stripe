#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import stripe

load_dotenv() # take environment variable from .env

# stripe API key
stripe.api_key = os.getenv("stripe_test_api_key") 


# List all products
products = stripe.Product.list()
for product in products.auto_paging_iter():
    print(f"Product: {product.name} | ID: {product.id}")

# List all prices
prices = stripe.Price.list()
for price in prices.auto_paging_iter():
    print(f"Price ID: {price.id} | Unit amount: {price.unit_amount} {price.currency}")