#       #               #               #               #               #
#
#   The Poly-alphabetic Shift Cypher (Vigenere Cypher)
#       
#       The Vigenere Cypher is a lot like the regular shift cypher, but instead
#   of shifting all the letters by the same number, the letters are shifted by the 
#   values of a repeated key, usually given as another string. With a sufficiently long
#   and random key, the Vigenere Cypher is actually pretty secure, but with shorter keys
#   and known plaintext attacks, there are statistical methods to find the length of the
#   key used, and then from there to find the statistically most likely shifts applied (though
#   this is not an easy process). 
#           
#       #               #               #               #               #

alphabet_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 
                 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
alphabet_list = list(alphabet_dict.keys())
test = 'test.txt'


# This function filters a .txt file or a string into only
#       plain lowercase text which is what
#       is required for analysis using the Vigenere Cypher
def filter_plaintext(txtfile):
    filteredtext = ""
    try:
        with open(txtfile) as f:
            plaintext = f.readlines()
            for line in plaintext:
                for character in line.lower():
                    try:
                        number = alphabet_dict[character]
                        filteredtext += character
                    except: pass
    except: 
        for character in txtfile.lower():
                    try:
                        number = alphabet_dict[character]
                        filteredtext += character
                    except: pass
        return filteredtext
    return filteredtext


# The Vigenere Encrypt function works by looping through the message and the 
#       key at the same time, and applying a letter shift by adding the positional 
#       value of the key mod 26
def vigenere_encrypt(message, key):

    # Inits variables to store the cyphertext and for looping
    cyphertext = ''
    key_length = len(key) - 1
    counter = 0

    # Loops through the plaintext, while also looping through the key
    #   and applying the shift mod 26
    for i in (filter_plaintext(message)):
        if (counter % key_length) == 0:
            counter = 0
        cyphertext += alphabet_list[((int((alphabet_dict[i] + int(alphabet_dict[key[counter]]))) % 26)) - 1] 
        counter += 1
    return cyphertext


# The Vigenere Decrypt method works in much the same way as the encryption except the
#       key is subtracted instead
def vigenere_decrypt(cyphertext, key):
    plaintext = ''
    key_length = len(key) - 1
    counter = 0
    for i in (cyphertext):
        if (counter % key_length) == 0:
            counter = 0
        plaintext += alphabet_list[((int((alphabet_dict[i] - int(alphabet_dict[key[counter]]))) % 26)) - 1] 
        counter += 1
    return plaintext


# This is a test. It takes an input file and runs it through the cypher and back again
if(__name__ == "__main__"):
    a = 'The Big Oxmox advised her not to do so, because there were thousands of bad Commas'
    b = vigenere_encrypt(a, 'banana')
    print('Plaintext: ', a)
    print('Key: ', '"banana"')
    print('Encrypted: ', b)
    print('Decrypted: ', vigenere_decrypt(b, 'banana'))