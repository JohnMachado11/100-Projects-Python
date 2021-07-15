from alphabet import alphabet
from art import logo

def start():
    print(f"{logo}\n")
    Flag = True
    while Flag:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in ("encode", "decode"):
            Flag = False
        else:
            print("\nERROR: Please only respond with 'encode' or 'decode'.\n")
    text_and_shift_input(direction)

def text_and_shift_input(direction):
    text = input("Type your word:\n").lower()
    Flag = True
    while Flag:
        try:
            shift = int(input("Type the shift number:\n"))
            if shift > 25: 
                shift = shift % 26 
        except ValueError:
            print("Not an integer.\n")
            continue
        else:
            Flag = False
            caesar(text, shift, direction)

def caesar(text, shift, direction):
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for i in range(len(text)):
        if text[i] in alphabet: 
            new_index = alphabet.index(text[i])
            if new_index + shift > 25:
                new_index = new_index + shift - 26
            else:
                new_index = new_index + shift
            cipher_text += alphabet[new_index]
        else:
            cipher_text += text[i]
    print(f"We are executing a {direction} algorithm on '{text}' and the result is: {cipher_text}")


if __name__ == "__main__":
    start()