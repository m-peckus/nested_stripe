#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import stripe

load_dotenv() # take environment variable from .env

# stripe API key
stripe.api_key = os.getenv("stripe_test_api_key") 



print("stripe is ready")
# get invoices for a specific customer

#customer id
customer_id = "cus_SgUGbPisnDOg3Q"

#1 create a product 
product = stripe.Product.create(name="Test Product")

#2 create a one-time invoice item
stripe.InvoiceItem.create(
    customer=customer_id,
    amount=1500,
    currency="usd",
    description="Test charge for practice",
)

#3 create and finalize an invoice
invoice = stripe.Invoice.create(customer=customer_id)
finalized_invoice = stripe.Invoice.finalize_invoice(invoice.id)

#4 fetch and print all invoices for that customer

invoices = stripe.Invoice.list(customer=customer_id)
#print(f"invoices print {invoices}")

invoice_summary = []
for invoice in invoices.auto_paging_iter():
    invoice_summary.append(f"Invoice ID: {invoice.id}, Amount Due: {invoice.amount_due}, Account Country: {invoice.account_country}, Invoice PDF: {invoice.invoice_pdf}")

# print everything just once
print("\n".join(invoice_summary))