# Format text

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)


# :.2f ---> quiere decir que solo muestre 2 digitos despues de la coma
# :.2f ---> This tells python to show only 2 digits after the Floating Point



# reverse a string

txt = "Hello World"[::-1]