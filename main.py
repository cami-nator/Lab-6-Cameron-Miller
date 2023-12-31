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
    decoded_password = ''
    for i in encoded_password:
        # subtracts 3 from each digit
        if int(i) >= 3:
            variable = int(i)-3
        if int(i) == 2:
            # since 2-3=-1, the digit is 9
            variable = 9
        if int(i) == 1:
            # since 1-3=-2, the digit is 8
            variable = 8
        if int(i) == 0:
            # since 0-3=-3, the digit is 7
            variable = 7
        decoded_password += str(variable)

    return decoded_password

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

