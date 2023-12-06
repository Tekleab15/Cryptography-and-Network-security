class CaesarCipher:
    def receiveUserInput(self):
        self.text_tobe_processed = input("Enter Text to processed(Letters only): ")
        self.valid_input = False
        while self.text_tobe_processed:
            if self.text_tobe_processed.strip() == ("") or self.text_tobe_processed.strip() == None:
                print("No input received. please try another.")
            # for i in range(len(self.text_tobe_processed)):
            elif self.text_tobe_processed.isalpha():
                self.valid_input = True
            else:
                print("Please Enter only letters.")
                return
            if self.valid_input:
                try:
                    self.key_tobe_used = int(input("Enter key[0-25]: "))
                except Exception:
                    print("Key should be only number[0-25]")
                    return
            if type(self.key_tobe_used) == int:
                if int(self.key_tobe_used) in range(-25, 26):
                    process_type = input("\t--Enter Process type--\n(E) for Encryption\n(D) for Decryption: ")
                    if process_type == 'E':
                        self.encrypt()
                        return
                    elif process_type == "D":
                        self.decrypt()
                        return
                    else:
                        print("Invalid input!! Please enter valid process type.")
                else:
                    print("Key out of range.")
            else:
                print("Enter a valid value.")
    
    def encrypt(self):
        encrypted_text = ''
        for letter in self.text_tobe_processed:
            if letter.isupper():
                encrypted_text += chr((ord(letter) + int(self.key_tobe_used) - 65) % 26 + 65)
            elif letter.islower():
                encrypted_text += chr((ord(letter) + int(self.key_tobe_used) - 97) % 26 + 97)
            elif letter == ' ':
                encrypted_text += " "
            else:
                pass
        print("Ciphered text: {}" .format(encrypted_text))

    def decrypt(self):
        decrypted_text = ''
        for letter in self.text_tobe_processed:
            if letter.isupper():
                decrypted_text += chr((ord(letter) - int(self.key_tobe_used) - 65) % 26 + 65)
            elif letter.islower():
                decrypted_text += chr((ord(letter) - int(self.key_tobe_used) - 97) % 26 + 97)
            elif letter == ' ':
                decrypted_text += " "
            else:
                pass
        print("Decrypted text: {}" .format(decrypted_text))

trial1 = CaesarCipher()
trial1.receiveUserInput()
