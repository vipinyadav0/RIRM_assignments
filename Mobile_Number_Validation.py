import re # importing regular expression

# ● 2124567890
# ● 212-456-7890
# ● (212)456-7890
# ● (212)-456-7890
# ● 212.456.7890
# ● 212 456 7890
# ● +12124567890
# ● +12124567890
# ● +1 212.456.7890
# ● +212-456-7890
# ● 1-212-456-7890

def valid_number(number):
    '''Validating the given mobile number.'''

    # combining re pattern into pattern objects for pattern matching 
    pattern = re.compile("[+(]?[1]?[-\s]?[1-2]{3}?[)]?[-\s.]?[0-9]{3}[-\s.]?[0-9]{4}") 

    if pattern.match(number):
        print("Valid Number")
    else:
        print("Invalid Number")

if __name__ == "__main__":
    number = input("Enter the Number to validate: ")
    valid_number(number)


