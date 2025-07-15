import stripe

print("stripe is ready")

stripe.api_key = "sk_test_51RKE5uQrXX9kTXGyCO5cHmoYk5fH1sk7EqQpdXnCS2QvKVC4nPw9egX87DycPupk4c0mtIustOe7ySJnUeOe623Z00k4kkd9uT"

# get invoices for a specific customer

customer_id = "cus_12345"

invoices = stripe.Invoice.list(customer=customer_id)

for invoice in invoices.auto_paging_iter():
    print(f"Invoice ID: {invoice.id}, Amount Due: {invoice.amount_due}")
