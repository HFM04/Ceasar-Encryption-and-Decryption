# Midterm Project starter

def caesar(message, key, encrypt):
    
    # Every possible symbol that can be encrypted:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.#'

    # Stores the encrypted/decrypted form of the message:
    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if encrypt == True:
                translatedIndex = symbolIndex + key
            else:
                translatedIndex = symbolIndex - key
                
            # Handle wrap-around, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
                
            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol
    return translated

# The string to be encrypted/decrypted:
message = input('Please input a message:')

# The encryption/decryption key:
key = int(input('Please enter a key:'))

# Whether the program encrypts or decrypts:
while True:
    mode = input('Enter a mode (1 = Encrypt, 0 = Decrypt)')
    if mode in ['0','1']:       # if mode is 0 or 1
        mode = bool(mode)   # convert it to Boolean
        break               # and break out of loop
                            # otherwise, try again

# Call the Caesar function, passing appropriate arguments.
edmsg = caesar(message, key, mode)

# Output the translated string:
print(edmsg)
