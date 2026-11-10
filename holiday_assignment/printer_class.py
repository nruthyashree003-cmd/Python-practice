class Printer:
    def __init__(self, capacity, color, printer_type):
        self.capacity = capacity
        self.color = color
        self.printer_type = printer_type

    def display(self):
        print("Print Capacity:", self.capacity, "pages")
        print("Color Printing:", self.color)
        print("Printer Type:", self.printer_type)


# Creating three printer objects
printer1 = Printer(1000, "Yes", "Inkjet")
printer2 = Printer(2000, "No", "Laser")
printer3 = Printer(1500, "Yes", "All-in-One")

# Displaying printer details and object identities
print("Printer 1:")
printer1.display()
print("Object Identity:", id(printer1))

print("\nPrinter 2:")
printer2.display()
print("Object Identity:", id(printer2))

print("\nPrinter 3:")
printer3.display()
print("Object Identity:", id(printer3))