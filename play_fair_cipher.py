class PlayfairCipher:
    # User input receiver function to be decrypted/encrypted
    def receiveInput(self, input_text):
        for i in range(len(input_text)):
            if i < len(input_text)-1:
                if input_text[i] == input_text[i+1]:
                    input_text = input_text[:i+1] + 'X' + input_text[i+1:]
        
        if len(input_text)%2 != 0:
            input_text += 'X'
        return input_text
              
    # Create the Playfair matrix/table
    def createPlayFairMatrix(self,key_word):
        self.playfair_matrix = [[0 for i in range(5)] for i in range(5)]
        key_array = []
        for c in key_word:
            if c not in key_array:
                if (c == 'J') or (c == 'j'):
                    key_array.append('i')
                else:
                    key_array.append(c)
        letter_I_exist = 'I' in key_array
        for i in range(65,91):
            if chr(i) not in key_array:
                if i==73 and not letter_I_exist:
                    key_array.append("I")
                    letter_I_exist = True
                elif i==73 or i==74 and letter_I_exist:
                    pass
                else:
                    key_array.append(chr(i))       
        
        index = 0
        for i in range(5):
            for j in range(5):
                self.playfair_matrix[i][j] = key_array[index]
                index+=1
        
        return self.playfair_matrix
    
    # Used to specify index of a char from matrix table
    def indexer(self,char,cipher_matrix):
        index_alphabet = []
        if char == "J":
            char = "I"
        for i,j in enumerate(cipher_matrix):
            for m, n in enumerate(j):
                if char == n:
                    index_alphabet.append(i)
                    index_alphabet.append(m)
                    return index_alphabet
      
    # Encryption function
    def encrypt(self,plain_text,key):
        key_matrix = self.createPlayFairMatrix(key)
        cipher_text = []
        i = 0
        
        while i <  len(plain_text):
            n1 = self.indexer(plain_text[i],key_matrix)
            n2 = self.indexer(plain_text[i+1], key_matrix)
            # if pair of characters found in the same column
            if n1[1] == n2[1]:
                i1 = (n1[0] + 1) % 5
                j1 = n1[1]
                
                i2 = (n2[0] + 1) % 5
                j2 = n2[1]
                
                cipher_text.append(key_matrix[i1][j1])
                cipher_text.append(key_matrix[i2][j2])
                cipher_text.append(" ")
            # if pair of characters found in same row
            elif n1[0] == n2[0]:
                i1 = n1[0]
                j1 = (n1[1] + 1) % 5
                i2 = n2[0]
                j2 = (n2[1] + 1) % 5
                cipher_text.append(key_matrix[i1][j1])
                cipher_text.append(key_matrix[i2][j2])
                cipher_text.append(" ")
            
            # if pair of characters found in different row and column
            else:
                i1 = n1[0]
                j1 = n1[1]

                i2 = n2[0]
                j2 = n2[1]

                cipher_text.append(key_matrix[i1][j2])
                cipher_text.append(key_matrix[i2][j1])
                cipher_text.append(" ")

            i += 2        
        converted_text = ''
        for i in range(len(cipher_text)):
            converted_text += cipher_text[i]
        
        print("Out put: {}".format(converted_text))    
    
    # Decryption function
    def decrypt(self,plain_text,key):
        key_matrix = self.createPlayFairMatrix(key)
        cipher_text = []
        i = 0
        
        while i <  len(plain_text):
            n1 = self.indexer(plain_text[i],key_matrix)
            n2 = self.indexer(plain_text[i+1], key_matrix)
            if n1[1] == n2[1]:
                i1 = (n1[0] - 1) % 5
                j1 = n1[1]
                
                i2 = (n2[0] - 1) % 5
                j2 = n2[1]
                
                cipher_text.append(key_matrix[i1][j1])
                cipher_text.append(key_matrix[i2][j2])
                cipher_text.append(" ")
                
            # if pair of characters found in same row
            elif n1[0] == n2[0]:
                i1 = n1[0]
                j1 = (n1[1] - 1) % 5
                i2 = n2[0]
                j2 = (n2[1] - 1) % 5
                cipher_text.append(key_matrix[i1][j1])
                cipher_text.append(key_matrix[i2][j2])
                cipher_text.append(" ")
                
            # if pair of characters found in different row and column
            else:
                i1 = n1[0]
                j1 = n1[1]

                i2 = n2[0]
                j2 = n2[1]

                cipher_text.append(key_matrix[i1][j2])
                cipher_text.append(key_matrix[i2][j1])
                cipher_text.append(" ")

            i += 2        
        converted_text = ''
        for i in range(len(cipher_text)):
            converted_text += cipher_text[i]
        
        print("Out put: {}".format(converted_text))    
        
    def main(self):
        play_fair = PlayfairCipher()
        input_text = input("Enter input text: ").upper()
        key = input("Enter a key: ").upper()
        converted_plainText = play_fair.receiveInput(input_text)
        operation_type = input("Please Enter the type of Operation you want to perform. Enter \n(E) for Encryption: \n(D) for Decryption:  ")
        if operation_type == "E":
            self.encrypt(converted_plainText,key)
        elif operation_type == "D":
            self.decrypt(converted_plainText, key)
        else:
            print("Invalid Input, please Enter a valid operation name.")
               
if __name__ == "__main__":
    play_cipher = PlayfairCipher()
    play_cipher.main()
               



