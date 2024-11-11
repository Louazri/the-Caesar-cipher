def shift_amount(i):
  return i%26

def encrypt(text, required_shift):
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''

    # Convert text to lowercase
    text = text.lower()

    # Loop through each character in the text
    for char in text:
        if char not in alphabet:
            # If character is not a letter, add it as is
            output += char
        else:
            # Find the index in the alphabet and shift
            alpha_index = alphabet.find(char)
            shifted_index = shift_amount(alpha_index + required_shift)
            output += alphabet[shifted_index]

    return output


    
encrypted_quote = "bj fwj ozxy fs fiafshji gwjji tk rtspjdx ts f rnstw uqfsjy tk f ajwd fajwflj xyfw. gzy bj hfs zsijwxyfsi ymj zsnajwxj. ymfy rfpjx zx xtrjymnsl ajwd xujhnfq."

decrypted_quote = "we are just an advanced breed of monkeys on a minor planet of a very average star. but we can understand the universe. that makes us something very special."

#print(decrypted_quote)
required_shift = -5
print(f"Encrypted text: {encrypt(encrypted_quote, required_shift)}")
