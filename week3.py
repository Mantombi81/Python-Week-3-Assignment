def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to apply.
    
    Returns:
    - float: The final price after applying the discount if discount is 20% or higher, 
             otherwise returns the original price.
    """
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after discount
        final_price = price - discount_amount
    else:
        # Return the original price if discount is less than 20%
        final_price = price
    
    return final_price

def main():
    # Prompt the user for input
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)
        
        # Print the result
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numerical values for price and discount percentage.")

# Call the main function
if __name__ == "__main__":
    main()
