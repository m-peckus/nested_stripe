#!/usr/bin/env python3

import stripe
from dotenv import load_dotenv
import os
from flask import Flask, jsonify, request, render_template


load_dotenv() # take environment variables from .env
stripe.api_key = os.getenv("stripe_test_api_key")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_api_key', methods=['GET'])
def get_api_key():
    # Serve the publishable key to the client
    return jsonify({'publishable_key': os.getenv("stripe_publishable_key")})

@app.route('/create_subscription', methods=['POST'])
def create_subscription():
    token = request.json.get('token')
    #
    product = stripe.Product.create(name="Soap") # Create a product

    # Create a recurring price for the product
    price = stripe.Price.create( 
        unit_amount=5000, # Amount in cents
        currency="usd",
        recurring={"interval": "month"},
        product=product.id,
    )

    # Create a customer object to associate with the subscription
    customer = stripe.Customer.create(
        email="customer@example.com",
        name="Martin Bogazc",
    )

    # Create payment method using the token
    payment_method = stripe.PaymentMethod.create(
        type="card",
        card={"token": token},
    )

    # Attach the payment method to the customer
    stripe.PaymentMethod.attach(
        payment_method.id,
        customer=customer.id,
    )

    # Set the payment method as the default for the customer
    stripe.Customer.modify(
        customer.id,
        invoice_settings={
            "default_payment_method": payment_method.id
        },
    )

    # Create subscription for the customer using the price ID
    subscription = stripe.Subscription.create(
        customer=customer.id,
        items=[{"price": price.id}]
    )

    return jsonify({"subscription_id": subscription.id})

if __name__ == '__main__':
    app.run(port=5000)
