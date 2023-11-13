#Olivia Booth
#CIS261
#Week 6 Invoice Line Item Calculator

#Heading
#print("Welcome to the Invoice Line Item Calculator")

#Function to asks user to input a price
def inputPrice():
    while True:
        try:
            print("\n")
            price = float(input("Enter a price:$ "))
            return price
        except ValueError:
            print("Use the format 0.00, Please try again.")
            
#function to ask user to input a quantity
def inputQuantity():
    while True:
        try:
            quantity = int(input("Enter the quantity:  "))
            return quantity
        except ValueError:
            print("Please enter a numerical value. ")

#Main Code below - commented out for now
if __name__ == "__main__":
    print("Welcome to the Invoice Line Item Calculator")  
    addMore = "y"
    while addMore.lower() == "y":
        price = inputPrice()
        quantity = inputQuantity()
        itemTotal = price*quantity
        print("Price:$", f"{price: .2f}")
        print("Quantity:", quantity)
        print("Total:$", f"{itemTotal: .2f}")
        addMore = input("\nAdd another line item? Choose y or n:  ")
    print("See you later! ")