"""
D-Encryptor Echo Module

This module provides decryption functionality for messages encrypted with the progressive 
drift cipher algorithm. It can decrypt messages with a known drift value or attempt 
brute-force decryption by trying all possible drift values (0-25).

Author: Eniola Ajayi
Version: 0.1.0
"""

import sys


def listener(whisper, drift=None):
    """
    Decrypts a message encrypted with the progressive drift cipher algorithm.
    
    This function reverses the encryption process by applying a progressively decreasing 
    shift to each alphabetic character. It can work in two modes:
    1. Known drift: Decrypts using a specific drift value
    2. Brute force: Tries all possible drift values (0-25) and displays results
    
    Args:
        whisper (str): The encrypted message to decrypt. Should contain the cipher text
                      with special character replacements as created by the whisperer function.
        drift (int, str, or None, optional): The initial drift value used during encryption.
                                           - If provided: Uses this specific drift for decryption
                                           - If None: Tries all possible drifts (0-25) and prints results
                                           - Will be converted to integer if provided as string
    
    Returns:
        str or None: 
            - If drift is provided: Returns the decrypted plaintext message
            - If drift is None: Prints all possible decryptions and returns None
    
    Examples:
        >>> # Decrypt with known drift
        >>> listener("igopt", 1)
        'hello'
        
        >>> # Decrypt without knowing drift (shows all possibilities)
        >>> listener("igopt", None)
        Decrypted text with a drift of 0: igopt
        Decrypted text with a drift of 1: hello
        Decrypted text with a drift of 2: gdkkn
        ... (shows all 26 possibilities)
        
        >>> # Decrypt message with special characters
        >>> listener("Igopt^.Ysuni&", 2)
        'Hello, World!'
    
    Algorithm Details:
        - Each alphabetic character is shifted backward by (drift + character_position) mod 26
        - Case preservation: uppercase remains uppercase, lowercase remains lowercase
        - After processing each alphabetic character, drift increases by 1
        - Non-alphabetic characters reset drift to the original value
        - Special character reverse mappings: ^ → ,, ; → ., & → !, etc.
        
    Special Character Reverse Mapping:
        ^ → ,     ; → .     & → !     % → ?
        _ → _     # → (     " → )     . → space     .. → tab
        
    Brute Force Mode:
        When drift=None, the function systematically tries all possible initial 
        drift values from 0 to 25, displaying each result. This is useful when 
        you have encrypted text but don't know the original drift value.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Reverse mapping for special character restoration
    non_alphabet_replacement = {
        '^': ',',   
        ';': '.',   
        '&': '!',   
        '%': '?',   
        '_': '_',   
        '#': '(',   
        '"': ')',   
        '.': ' ',   
        '..': '\t' 
    }
    
    if drift is not None:
        # Decrypt with known drift value
        drift = int(drift)  
        whisper_heard = ''
        current_drift = drift 
        
        # Process each character in the encrypted message
        for character in whisper:
            if character.lower() in alphabet:
                # Handle alphabetic characters with progressive reverse shift
                character_index = alphabet.index(character.lower())
                decrypted_character_index = (character_index - current_drift) % 26
                
                # Preserve original case
                if character.islower():
                    decrypted_character = alphabet[decrypted_character_index]
                else:
                    decrypted_character = alphabet[decrypted_character_index].upper()
                
                whisper_heard += decrypted_character
                current_drift += 1  # Increment drift for next alphabetic character
            else:
                # Handle non-alphabetic characters with reverse mapping
                whisper_heard += non_alphabet_replacement.get(character, character)
                current_drift = drift  # Reset drift to original value
        
        return whisper_heard
    
    else:
        # Brute force mode: try all possible drift values
        print("Trying all possible drift values:")
        print("-" * 50)
        
        for drift in range(26):
            whisper_heard = ''
            current_drift = drift
            
            # Process each character with current drift attempt
            for character in whisper:
                if character.lower() in alphabet:
                    character_index = alphabet.index(character.lower())
                    decrypted_character_index = (character_index - current_drift) % 26
                    decrypted_character = (alphabet[decrypted_character_index] 
                                         if character.islower() 
                                         else alphabet[decrypted_character_index].upper())
                    whisper_heard += decrypted_character
                    current_drift += 1
                else:
                    whisper_heard += non_alphabet_replacement.get(character, character)
                    current_drift = drift
            
            print(f"Drift {drift:2d}: {whisper_heard}")
        
        print("-" * 50)
        print("Look for the result that makes the most sense!")
        return None  # No single result to return in brute force mode


if __name__ == "__main__":
    """
    Command-line interface for the listener function.
    
    Usage:
        python echo.py <encrypted_text> [drift]
    
    Arguments:
        encrypted_text: The encrypted message to decrypt (wrap in quotes if it contains spaces)
        drift (optional): The drift value used during encryption
                         - If provided: Decrypts using this specific drift
                         - If omitted: Tries all possible drifts (0-25)
    
    Examples:
        python echo.py "igopt" 1
        python echo.py "Igopt^.Ysuni&" 5  
        python echo.py "mysterious_message"  # tries all drifts
    """
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python echo.py <encrypted_text> [drift]")
        print("\nExamples:")
        print('  python echo.py "igopt" 1          # decrypt with known drift')
        print('  python echo.py "mysterious_text"  # try all possible drifts')
        print("\nArguments:")
        print("  encrypted_text  - The message to decrypt (required)")
        print("  drift          - Initial drift value (optional, 0-25)")
        print("\nIf drift is not provided, all possible drift values will be tried.")
        sys.exit(1)
    
    whisper = sys.argv[1]
    drift = None
    if len(sys.argv) == 3:
        try:
            drift = int(sys.argv[2])
            if not (0 <= drift <= 25):
                print("Warning: Drift value should typically be between 0-25")
        except ValueError:
            print("Error: Drift must be a valid integer")
            sys.exit(1)
    
    try:
        whisper_heard = listener(whisper, drift)
        if whisper_heard is not None:
            print("You received a whisper:", whisper_heard)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)