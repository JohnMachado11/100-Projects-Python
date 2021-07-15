from caesar_alphabet import alphabet

def main():
    Flag = True
    while Flag:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in ("encode", "decode"):
            Flag = False
        else:
            print("\nERROR: Please only respond with 'encode' or 'decode'.\n")
    text_input(direction)

def text_input(direction):
    Flag = True
    while Flag:
        text = ""
        text = input("Type your word:\n")
        if not text: # not an empty input exception catch
            print("\nERROR: Please input a word.\n") 
        elif text.isspace(): # no spaces exception catch
            print("\nERROR: Please do not input any spaces.\n")
        elif text.isalpha() != True: # only alpha characters and no spaces
            print("\nERROR: Please only respond with letters and no spaces.\n")
        else:
            Flag = False
    shift_input(direction, text)

def shift_input(direction, text):
    print("We are at the shift function")
    print(f"The direction is {direction} and text is {text}")
    shift = int(input("Type the shift number:\n"))
    if shift > 25: ## breaks on very big number
        shift = shift % 26 
        print(shift)
    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)

def encrypt(text, shift):
    cipher_text = ""
    for i in range(len(text)):
        new_index = alphabet.index(text[i])  
        if new_index + shift > 25:
            new_index = new_index + shift - 26
        else:
            new_index = new_index + shift
        cipher_text += alphabet[new_index]
    print(f"The encoded text is {cipher_text}")

def decrypt(text, shift):
    cipher_text = ""
    for i in range(len(text)):
        new_index = alphabet.index(text[i])  
        if new_index - shift < 25:
            new_index = new_index - shift - 26
        else:
            new_index = new_index - shift
        cipher_text += alphabet[new_index]
    print(f"The decoded text is {cipher_text}")

main()