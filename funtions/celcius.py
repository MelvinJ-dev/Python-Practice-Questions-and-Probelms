# Convert celsius to farenhiet and farendhiet to celcius

# HOW TO GET INPUT 30 C

def temp_converter(temp_input):
    value,notation = temp_input.split()
    notation = notation.upper()
    value = float(value)
    if notation == 'C':
        farenhiet = (value * 1.8) + 32
        return(f'{farenhiet} degreee farenhiet')
    elif notation == 'F':
        celcius = (value-32)//1.8
        return f'{celcius} degree celcius'
    else:
        print("Invalid input")





temp_input = input("Enter the temp value : ")

converted_value = temp_converter(temp_input)

print(converted_value)