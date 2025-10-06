# FILE NAME - convert_C_to_F_02.py

# NAME: Mike Rahne 
# DATE: 10/6/2025
# BRIEF DESCRIPTION: My convert_C_to_F_02 submission  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########


def main():
    convert_C_F_02()
def convert_C_F_02():

#                  celsius = input("Enter a temperature in Celsius: ")
#                  print()
#                  print (f'{float(celsius)} degrees Celsius is {float(celsius)* 9/5 + 32} degrees Fahrenheit.')

                print('===== Temperature Converter =====')
                print()
                print('  1. Convert from Celsius to Fahrenheit')
                print('  2. Convert from Fahrenheit to Celsius')
                print()  
                choice = input('Please choose from the above menu: ')

                if choice == '1':
                        celsius = input('Enter a temperature to convert: ')
                        print()
                        print (f'{float(celsius)} degrees Celsius is {float(celsius)* 9/5 + 32} degrees Fahrenheit.')
                elif choice == '2':
                        fahrenheit = input('Enter a temperature to convert: ')
                        print()
                        print (f'{float(fahrenheit)} degrees Fahrenheit is {(float(fahrenheit)-32) * 5/9:.1f} degrees Celsius.')


main()







########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

# I actually learned 2. 
# 1) Always make sure to close out your "def" or your code won't work and you'll waste a lot of time wondering what is going on
# 2) Make sure you label your code properly so you can find code that you might want to use or use part of/slightly alter for a different project







'''
