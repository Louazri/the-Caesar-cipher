In this project, you are tasked to implement a Python class (call it TranspositionCipher) that can encrypt and decrypt a message using the transposition cipher—a simple yet effective way of encrypting a text in a way that becomes unreadable to anyone who doesn’t possess the key to decryption. It relies on scrambling the words in plaintext by rearranging its characters according to a specific algorithm.

The project requires you to implement a TranspositionCipher class incorporating the following elements:

A constructor function that accepts the cipher's key as an argument
A method designated for encrypting a message requiring a single parameter—the plaintext message to be encrypted
A method dedicated to decrypting a message that calls for one argument—the previously encrypted message in ciphertext format
Optional: As an additional challenge—not required for completing the project—you can implement a function outside the TranspositionCipher class, which hacks the columnar transposition cipher, i.e., it decrypts a ciphertext without knowing the key. The function should return the decrypted message and the key.
