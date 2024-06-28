def decrypt_message(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_message += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_message += chr(shifted)
        else:
            decrypted_message += char
    return decrypted_message

encrypted_message = "Uifsf jt b tfdsfu nfttbhf xijdi dpoubjot uif gmbh!"
shift = 1

decrypted_message = decrypt_message(encrypted_message, shift)
<<<<<<< HEAD
print(f"WEST{tsewDNAtsae2napaj})

=======
print(f"") #変更
>>>>>>> origin/main
