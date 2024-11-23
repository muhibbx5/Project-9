# Ask the user for a decimal number
n = int(input("Enter a decimal number: "))

# Convert the decimal number to binary and remove the '0b' prefix
binary = bin(n)[2:]

# Print the binary representation
print("Binary:", binary)
