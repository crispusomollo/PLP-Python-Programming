def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.

    Returns:
        float: The final price after applying the discount, 
               or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Main program
try:
    # Prompt the user for inputs
    original_price = float(input("Enter the original price of the item: $"))
    discount = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount)

    # Print the results
    if discount >= 20:
        print(f"A discount of {discount}% was applied.")
        print(f"The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied since the discount is less than 20%.")
        print(f"The original price is: ${original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
