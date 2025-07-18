# Codecademy off-platform challenge

# Instructions:
# Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a Caesar Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. 

# For example, if I chose an offset of 3 and a message of "hello", I would encode my message by shifting each letter 3 places to the left with respect to the alphabet. So "h" becomes "e", "e" becomes "b", "l" becomes "i", and "o" becomes "l". Then I have my encoded message, "ebiil"! Now I can send you my message and the offset and you can decode it by shifting each letter 3 places to the right. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer encoded message that you have to decode yourself!

#     xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!

# This message has an offset of 10. Can you decode it?

message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'

reply = "i got your message! it took me a while to decode it but i managed it." # (Use a negative shift value to encode it)

def caesar_cipher(message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    deciphered_message = []
    
    for char in message:
        if char.isalpha():
            index = alphabet.index(char)
            deciphered_message.append(alphabet[(index+shift) % 26])
        else:
            deciphered_message.append(char)
    
    return "".join(deciphered_message)

print(caesar_cipher(message, 10))
# hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!
print(caesar_cipher(reply, -10)) # negative shift to encode
# y wej oekh cuiiqwu! yj jeea cu q mxybu je tusetu yj rkj y cqdqwut yj


# Alternative:
import string

# def caesar_cipher(text, shift):
#     lowercase = string.ascii_lowercase
#     shifted = lowercase[shift:] + lowercase[:shift]
#     table = str.maketrans(lowercase, shifted)
#     return text.translate(table)

# message = "i got your message! it took me a while to decode it but i managed it."
# print(caesar_cipher(message, 10))

# Unknown offset value:
unknown_offset_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# for index in range(26):
#     print(caesar_cipher(unknown_offset_message, index))

# The Vigenère Cipher

# Salutations! As you can see, technology has made brute forcing simple ciphers like the Caesar Cipher extremely easy, and us crypto-enthusiasts have had to get more creative and use more complicated ciphers. This next cipher I'm going to teach you is the Vigenère Cipher, invented by an Italian cryptologist named Giovan Battista Bellaso (cool name eh?) in the 16th century, but named after another cryptologist from the 16th century, Blaise de Vigenère.
        
# The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher. What this means is that opposed to having a single shift that is applied to every letter, the Vigenère Cipher has a different shift for each individual letter. The value of the shift for each letter is determined by a given keyword.
       
# Consider the message:
       
#     barry is the spy

# If we want to code this message, first we choose a keyword. For this example, we'll use the keyword
       
#     dog
           
# Now we repeat the keyword over and over to generate a keyword phrase that is the same length as the message we want to code. So if we want to code the message "barry is the spy" our keyword phrase is "dogdo gd ogd ogd". Now we are ready to start coding our message. We shift each letter of our message by the place value of the corresponding letter in the keyword phrase, assuming that "a" has a place value of 0, "b" has a place value of 1, and so forth.

#               message:    b  a  r  r  y    i  s    t  h  e    s  p  y
            
#        keyword phrase:    d  o  g  d  o    g  d    o  g  d    o  g  d
             
# resulting place value:    24 12 11 14 10   2  15   5  1  1    4  9  21
  
# So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us an place value of 24, which is "y". Remember to loop back around when we reach either end of the alphabet! Then continue the trend: we shift "a" by the place value of "o", 14, and get "m", we shift "r" by the place value of "g", 15, and get "l", shift the next "r" by 4 places and get "o", and so forth. Once we complete all the shifts we end up with our coded message:
        
#     ymlok cp fbb ejv
            
# As you can imagine, this is a lot harder to crack without knowing the keyword! So now comes the hard part. I'll give you a message and the keyword, and you'll see if you can figure out how to crack it! Ready? Okay here's my message:
        
#     txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!
            
# and the keyword to decode my message is 
        
#     friends
            
# Because that's what we are! Good luck friend!

def vigenere_cipher_decode(message, keyword):
    message = message.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # keyword_numbers = []
    shift_values = []
    deciphered_message = []

    # List comprehension. Loop over the keyword. If the char is an alphabetical letter, add the index of that letter from 'alphabet' to the keyword_number_code list
    keyword_numbers = [alphabet.index(char) for char in keyword if char.isalpha()]

    # Same thing with standard loop:
    # for char in keyword:
    #     if char.isalpha():
    #         keyword_numbers.append(alphabet.index(char))

    # Loop over the chars in message. If the char is an alphabetical letter, add the corresponding value based on the index to the shift_values list. Otherwise just add the char to the list as it is (eg.space/punctuation marks). Using the modulo operator (%) allows the loop to go back round.
    index = 0
    for char in message:
        if char.isalpha():
            shift_values.append(keyword_numbers[index%len(keyword)])
            index+=1
        else:
            shift_values.append(char)
            
    # Loop over a range of the message length. If the value at shift_values[i] is an integer, then call the decipher_message() function on that letter and append it to the deciphered_message list. Otherwise append the char to the list as it is (eg.space/punctuation marks)
    for i in range(len(message)):
        if isinstance(shift_values[i], int): 
            decoded_letter = caesar_cipher(message[i], shift_values[i])
            deciphered_message.append(decoded_letter)
        else:
            deciphered_message.append(shift_values[i])

    return "".join(deciphered_message)

secret_message = 'Txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!'
keyword = 'friends'
my_message = 'raf, e iem df.'
my_keyword = 'forever'

print(vigenere_cipher_decode(secret_message, keyword))
# you were able to decode this? nice work! you are becoming quite the expert at crytography!
print(vigenere_cipher_decode(my_message, my_keyword))
# wow, i did it.

# For your final task, write a function that can encode a message using a given keyword and write out a message to send to Vishal!

def vigenere_cipher_encode(message, keyword):
    message = message.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # keyword_numbers = []
    shift_values = []
    encoded_message = []

    # the only change to encode rather than decode is to change the shift values to negative integers as below.
    
    # List comprehension. Loop over the keyword. If the char is an alphabetical letter, add the index of that letter from 'alphabet' to the keyword_number_code list
    keyword_numbers = [-alphabet.index(char) for char in keyword if char.isalpha()]

    # Same thing with standard loop:
    # for char in keyword:
    #     if char.isalpha():
    #         keyword_numbers.append(-abs(alphabet.index(char)))
    #         keyword_numbers.append(-alphabet.index(char))
       
    index = 0
    for char in message:
        if char.isalpha():
            shift_values.append(keyword_numbers[index%len(keyword)])
            index+=1
        else:
            shift_values.append(char)

    for i in range(len(message)):
        if isinstance(shift_values[i], int): 
            encoded_letter = caesar_cipher(message[i], shift_values[i])
            encoded_message.append(encoded_letter)
        else:
            encoded_message.append(shift_values[i])
    return "".join(encoded_message)

print(vigenere_cipher_encode("wow, i did it.", "forever"))
# raf, e iem df.