# Takes a password in string format containing only integers. After passing the password into the encoder, the encoder stores the encoded password to a new
# variable, with each digit being shifted up by 3 numbers.
def encode(password):
    encoded_password = ''
    for digit in password:
        if int(digit) < 7:
            variable = int(digit) + 3
        elif int(digit) == 7:
            variable = 0
        elif int(digit) == 8:
            variable = 1
        elif int(digit) == 9:
            variable = 2
        encoded_password += str(variable)
        # adds the variable to an empty string
    return encoded_password

#  Takes in the encoded password and returns the original password.
def decode(encoded_password):
    # FIXME Sara, please write the decoder function
    pass

# Provides a looping menu that prompts the user to choose from a menu with encoder and decoder options.
def main():
    condition = True
    while condition == True:
        print("Menu\n-------------")
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        choice = input('Please enter an option:')

        if choice == '1':
            password = input('Please enter your password to encode: ')
            print(f"Your password has been encoded and stored!")
        elif choice == '2':
            print(f'The encoded password is {encode(password)}, and the original password is {decode(encode(password))}.')
        elif choice == '3':
            break
if __name__ == '__main__':
    main()

