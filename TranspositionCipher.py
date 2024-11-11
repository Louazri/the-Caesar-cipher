class TranspositionCipher(object): 
    def __init__(self, key):
        self.key = key  # Key represents the number of columns
    
    def encrypt_message(self, message):
        # Define grid size based on key (columns)
        message = message.lower()
        cols = self.key
        rows = (len(message) + cols - 1) // cols  # Calculate rows needed
        
        
        # Initialize the grid and fill it with characters from the message
        grid = []
        index = 0
        for r in range(rows):
            row = []
            for c in range(cols):
                if index < len(message):
                    row.append(message[index])
                    index += 1
                else:
                    # Fill remaining spaces if message ends
                    row.append(' ')
            grid.append(row)
        
        # For debugging, print the grid (optional)
        print("Grid for encryption:")
        for row in grid:
            print(row)
        
        # Transpose the grid (column-wise read) for encryption
        encrypted_message = ''
        for c in range(cols):
            for r in range(rows):
                encrypted_message += grid[r][c]
        
        return encrypted_message.strip()
    
    def decrypt_message(self, message):
        # Rows = the key (columns are fixed as the key)
        rows = self.key
        cols = (len(message) + rows - 1) // rows  # Calculate columns needed
        
        # Rebuild the grid column by column
        grid = [['' for _ in range(cols)] for _ in range(rows)]  # Empty grid
        # Fill the grid column by column
        index = 0
        for c in range(rows):
            for r in range(cols):
                if index < len(message):
                    grid[c][r] = message[index]
                    index += 1
        
        # For debugging, print the grid (optional)
        print("Grid for decryption:")
        for row in grid:
            print(row)
        
        # Read the grid row by row to get the decrypted message
        decrypted_message = ''
        for r in range(cols):
            for c in range(rows):
                decrypted_message += grid[c][r]
        
        return decrypted_message.strip()  # Remove trailing spaces
    
# Test the TranspositionCipher class
alawi_habibe_galbi = TranspositionCipher(7)  # 3 columns (key)
encrypted_message = alawi_habibe_galbi.encrypt_message('''I confess at these words a shudder passed
through me. There was a thrill in the doctor’s voice
which showed that he was himself deeply moved
by that which he told us. Holmes leaned forward
in his excitement and his eyes had the hard, dry
glitter which shot from them when he was keenly
interested.''')
print("Encrypted Message:", encrypted_message)

decrypted_message = alawi_habibe_galbi.decrypt_message(encrypted_message)
print("Decrypted Message:", decrypted_message)

