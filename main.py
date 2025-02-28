class DeliveryOrder:
    """Represents a delivery order with details such as order number, reference number, delivery date, delivery method, recipient, and package."""
    
    def __init__(self, order_number, reference_number, delivery_date, delivery_method, recipient, package):
        self.order_number = order_number
        self.reference_number = reference_number
        self.delivery_date = delivery_date
        self.delivery_method = delivery_method
        self.recipient = recipient
        self.package = package

    def set_order_number(self, order_number):
        self.order_number = order_number

    def get_order_number(self):
        return self.order_number

    def set_reference_number(self, reference_number):
        self.reference_number = reference_number

    def get_reference_number(self):
        return self.reference_number

    def set_delivery_date(self, delivery_date):
        self.delivery_date = delivery_date

    def get_delivery_date(self):
        return self.delivery_date

    def set_delivery_method(self, delivery_method):
        self.delivery_method = delivery_method

    def get_delivery_method(self):
        return self.delivery_method

    def set_recipient(self, recipient):
        self.recipient = recipient

    def get_recipient(self):
        return self.recipient

    def set_package(self, package):
        self.package = package

    def get_package(self):
        return self.package
    
    def print_delivery_information(self):
        print('Delivery Information:')
        print(f'Order Number: {self.order_number}')
        print(f'Reference Number: {self.reference_number}')
        print(f'Delivery Date: {self.delivery_date}')
        print(f'Delivery Method: {self.delivery_method}')
        print(f'Package Dimensions: {self.package.dimensions}')
        print(f'Total Weight: {self.package.weight}')

class Recipient:
    """Represents the recipient of a delivery with details such as name, email, address, phone number, and postal code."""
    
    def __init__(self, name, email, address, phone, postal_code):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.postal_code = postal_code

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    def set_postal_code(self, postal_code):
        self.postal_code = postal_code

    def get_postal_code(self):
        return self.postal_code


class Package:
    """Represents a package with details such as weight, dimensions, items, fragile status, tracking number, and recipient."""
    
    def __init__(self, weight, dimensions, items, is_fragile, tracking_number):
        self.weight = weight
        self.dimensions = dimensions
        self.items = items
        self.is_fragile = is_fragile
        self.tracking_number = tracking_number

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_dimensions(self, dimensions):
        self.dimensions = dimensions

    def get_dimensions(self):
        return self.dimensions

    def set_items(self, items):
        self.items = items

    def get_items(self):
        return self.items

    def set_is_fragile(self, is_fragile):
        self.is_fragile = is_fragile

    def get_is_fragile(self):
        return self.is_fragile

    def set_tracking_number(self, tracking_number):
        self.tracking_number = tracking_number

    def get_tracking_number(self):
        return self.tracking_number


class DeliveryNote:
    """Represents a delivery note with details such as delivery_order, subtotal, taxes, total charges, and delivery date."""
    
    def __init__(self, delivery_order, delivery_date):
        self.delivery_order = delivery_order
        self.delivery_date = delivery_date
        self.subtotal = self.calculate_subtotal()
        self.taxes = self.calculate_taxes()
        self.total_charges = self.calculate_total_charges()

    def set_delivery_order(self, delivery_order):
        self.delivery_order = delivery_order

    def get_delivery_order(self):
        return self.delivery_order

    def set_delivery_date(self, delivery_date):
        self.delivery_date = delivery_date

    def get_delivery_date(self):
        return self.delivery_date
    
    def calculate_subtotal(self):
        sub_total = 0
        for item in self.delivery_order.package.items:
            sub_total += item["Total Price"]
        return sub_total
    
    def set_subtotal(self, subtotal):
        self.subtotal = subtotal

    def get_subtotal(self):
        return self.subtotal
    
    def calculate_taxes(self):
        return self.subtotal * 0.05
    
    def set_taxes(self, taxes):
        self.taxes = taxes

    def get_taxes(self):
        return self.taxes
    
    def calculate_total_charges(self):
        return self.subtotal + self.taxes

    def set_total_charges(self, total_charges):
        self.total_charges = total_charges

    def get_total_charges(self):
        return self.total_charges
    
    def print_delivey_note(self):
        print('Delivery Note')
        print('Thank you for using our delivery service! Please print your delivery receipt and present it upon erceiving your items')
        print(f'\nRecipient Details:\nName: {self.delivery_order.recipient.name}\nContact: {self.delivery_order.recipient.email}\nDelivery Address: {self.delivery_order.recipient.address}')
    
    def print_summary_of_delivered_items(self):
        print('Summary of items Delivered: ')
        print('Item Code       Description    Quantity Unit Price (AED) Total Price (AED)')
        for item in self.delivery_order.package.items:
            print(f' {item["Item Code"]}     {item["Description"]}     {item["Quantity"]}      {item["Unit Price"]}              {item["Total Price"]}')
        print(f"Sub Totla: {self.subtotal}")
        print(f'Taxes and Fees: {self.taxes}')
        print()
        print(f'Total Charges {self.total_charges}')
    
    
    
    
recipient = Recipient("Sarah Johnson", "sarah.johnson@example.com", "45 Knowledge Avenue, Dubai, UAE", '+971502143723', '20034')
items = [
    {"Item Code": "ITM001", "Description": "Wireless Keyboard", "Quantity": 1, "Unit Price": 100.00, "Total Price": 100.00},
    {"Item Code": "ITM002", "Description": "Wireless Keyboard", "Quantity": 4, "Unit Price": 200.00, "Total Price": 800.00},
    {"Item Code": "ITM003", "Description": "Wireless Keyboard", "Quantity": 1, "Unit Price": 300.00, "Total Price": 300.00},
    {"Item Code": "ITM004", "Description": "Wireless Keyboard", "Quantity": 2, "Unit Price": 150.00, "Total Price": 300.00},
    {"Item Code": "ITM005", "Description": "Wireless Keyboard", "Quantity": 1, "Unit Price": 100.00, "Total Price": 100.00},
]
package = Package(7, "7 X 3",items,True, '00543')
order = DeliveryOrder("DEL123456789", 'DN-2025-001', "January 25, 2025", "Courier", recipient, package)
delivery_note = DeliveryNote(order, "January 25, 2025")
order.print_delivery_information()
print('-----------------------------------')
delivery_note.print_delivey_note()
print('-----------------------------------')
delivery_note.print_summary_of_delivered_items()


print('\n-----------------------------------')
print('-----------------------------------\n')



recipient1 = Recipient("Sarah Johnson", "sarah.johnson@example.com", "45 Knowledge Avenue, Dubai, UAE", '+971502143723', '20034')
items1 = [
    {"Item Code": "ITM001", "Description": "Wireless Keyboard", "Quantity": 1, "Unit Price": 100.00, "Total Price": 100.00},
    {"Item Code": "ITM002", "Description": "Wireless Keyboard", "Quantity": 4, "Unit Price": 200.00, "Total Price": 800.00},
    {"Item Code": "ITM003", "Description": "Wireless Keyboard", "Quantity": 1, "Unit Price": 300.00, "Total Price": 300.00},
    {"Item Code": "ITM004", "Description": "Wireless Keyboard", "Quantity": 2, "Unit Price": 150.00, "Total Price": 300.00},
    {"Item Code": "ITM005", "Description": "Wireless Keyboard", "Quantity": 1, "Unit Price": 100.00, "Total Price": 100.00},
]
package1 = Package(3, "2 X 2",items1,True, '00544')
order1 = DeliveryOrder("DEL123456790", 'DN-2025-002', "January 26, 2025", "Courier", recipient1, package1)
delivery_note1 = DeliveryNote(order1, "January 26, 2025")
order1.print_delivery_information()
print('-----------------------------------')
delivery_note1.print_delivey_note()
print('-----------------------------------')
delivery_note1.print_summary_of_delivered_items()
