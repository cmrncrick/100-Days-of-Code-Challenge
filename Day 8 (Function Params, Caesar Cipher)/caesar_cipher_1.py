alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input(
#     "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text: str, shift_amount: int):

    # encoded_word = ""

    # # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
    # #  by the shift amount and print the encrypted text.
    # for t in original_text:
    #     pos = alphabet.index(t)
    #     print(f"Pos: {pos}")

    #     shifted = pos + shift_amount
    #     encoded_letter = alphabet[shifted]
    #     print(f"Encoded: {encoded_letter}")
    #     encoded_word += encoded_letter

    # return encoded_word

    cipher_text = ""
    for letter in original_text:
        print(alphabet.index(letter))
        shifted_position = alphabet.index(letter) + shift_amount
        print(f"1: {shifted_position}")
        shifted_position %= len(alphabet)
        print(f"2: {shifted_position}")
        cipher_text += alphabet[shifted_position]
        print(f"3: {cipher_text}")


word = encrypt("z", 9)
print(word)
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?


# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
