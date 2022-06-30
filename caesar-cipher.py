alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
def caesar(text, shift, direction):
    result_text = ""
    for letter in text:
        idx = alphabet.index(letter)
        char = alphabet[(idx + shift) % len(alphabet)]\
        if direction == "encode"\
        else alphabet[(idx-shift+len(alphabet)) % len(alphabet)]
        result_text += char
    print(f"The {direction}d text is {result_text}")
caesar(text, shift, direction)