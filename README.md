# Poly-alphabetic Shift Cypher (a.k.a. Vigenere Cypher)
This is just a basic set of encryption functions for encoding text using a basic Vigenere Cypher

---
### Overview of The Encryption    
 The Vigenere Cypher is a lot like the regular shift cypher, but instead
   of shifting all the letters by the same number, the letters are shifted by the 
   values of a repeated key, usually given as another string. With a sufficiently long
   and random key, the Vigenere Cypher is actually pretty secure, but with shorter keys
   and known plaintext attacks, there are statistical methods to find the length of the
   key used, and then from there to find the statistically most likely shifts applied (though
   this is not an easy process). 

#### Encryption Function
```python
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
```

This function when ran on an appropriate plaintext will return an illegible cyphertext. The following testing code on a sample string:
```python
    a = 'The Big Oxmox advised her not to do so, because there were thousands of bad Commas'
    b = vigenere_encrypt(a, 'banana')
    print('Plaintext: ', a)
    print('Key: ', '"banana"')
    print('Encrypted: ', b)
    print('Decrypted: ', vigenere_decrypt(b, 'banana')
```
produces the following output
```
Plaintext:  The Big Oxmox advised her not to do so, because there were thousands of bad Commas
Key:  "banana"
Encrypted:  viscwiplnczbrwwufristocuhqectcdfqbiufhistfkffguvpiubbegqgpbrepanou
Decrypted:  thebigoxmoxadvisedhernottodosobecausetherewerethousandsofbadcommas
```
