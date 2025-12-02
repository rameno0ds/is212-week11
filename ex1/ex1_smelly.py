class OrderProcessor:
    def validate_order(self, order):        
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")

    def get_discount(self, order):
        if order.get("discount_code") == "SUMMER20":
            return 0.8  # 20% discount
        elif order.get("discount_code") == "WELCOME10":
            return 0.9  # 10% discount
        return 1.0  # No discount
    
    def calculate_total(self, items, order):
        total_price = 0
        for item in items:
            total_price += item["price"] * item["quantity"]
        return total_price*self.get_discount(order)
    
    def update_inventory(self, items):
        for item in items:
            item_id = item["id"]
            quantity = item["quantity"]
            # Code to update inventory for each item
            # (for simplicity, let's assume a simple print statement here)
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")
    
    def generate_receipt(self, order, total_price):
        receipt = f"Customer ID: {order['customer_id']}\n"
        receipt += "Items:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"
        return receipt
    
    def process_order(self, order):
        # Step 1: Validate order details
        self.validate_order(order)
        
        # Step 2: Calculate total price with discount
        total_price = self.calculate_total(order["items"], order)
        
        # Step 3: Update inventory
        self.update_inventory(order["items"])

        # Step 5: Generate receipt
        receipt = self.generate_receipt(order, total_price)

        # Step 6: Send confirmation email
        print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")

        return receipt

