#!/usr/bin/env python3
import stripe

# stripe API key
stripe.api_key = "sk_test_51RKE5uQrXX9kTXGyCO5cHmoYk5fH1sk7EqQpdXnCS2QvKVC4nPw9egX87DycPupk4c0mtIustOe7ySJnUeOe623Z00k4kkd9uT"

# List all products
products = stripe.Product.list()
for product in products.auto_paging_iter():
    print(f"Product: {product.name} | ID: {product.id}")

# List all prices
prices = stripe.Price.list()
for price in prices.auto_paging_iter():
    print(f"Price ID: {price.id} | Unit amount: {price.unit_amount} {price.currency}")