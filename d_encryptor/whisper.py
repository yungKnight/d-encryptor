"""
D-Encryptor Whisper Module

This module provides encryption functionality using a progressive drift cipher algorithm.
The cipher applies an incrementally increasing shift to each alphabetic character in the message.

Author: Eniola Ajayi
Version: 0.1.0
"""

import sys


def whisperer(message, drift):
    """
    Encrypts a message using a progressive drift cipher algorithm.
    
    The function applies a Caesar cipher with an incrementally increasing shift value.
    Each alphabetic character is shifted by (initial_drift + position) positions in the alphabet.
    Non-alphabetic characters are replaced according to a predefined mapping or left unchanged.
    
    Args:
        message (str): The plaintext message to encrypt. Can contain any characters.
        drift (int): The initial shift value. Will be converted to integer.
                           This value increases by 1 for each alphabetic character processed.
    
    Returns:
        str: The encrypted message with:
             - Alphabetic characters shifted by progressive drift amounts
             - Special characters replaced according to the mapping
             - Case preservation (uppercase/lowercase maintained)
    
    Example:
        >>> whisperer("hello", 1)
        'igopt'
        
        >>> whisperer("Hello, World!", 2)
        'Jgopt^.Ysuni&'
    
    Algorithm Details:
        - Alphabetic characters: Shifted by (drift + character_position) mod 26
        - Case is preserved (uppercase remains uppercase)
        - After each alphabetic character, drift increases by 1
        - Non-alphabetic characters reset drift to original value
        - Special character mappings: , → ^, . → ;, ! → &, etc.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Mapping for non-alphabetic character replacement
    non_alphabet_replacement = {
        ',': '^',   
        '.': ';',   
        '!': '&',   
        '?': '%',   
        '_': '_',   
        '(': '#',   
        ')': '"',   
        ' ': '.',   
        '\t': '..' 
    }
    
    encrypted_message = ''
    drift = int(drift)
    current_drift = drift  
    
    # Process each character in the message
    for character in message:
        if character.lower() in alphabet:
            # Handle alphabetic characters with progressive shift
            character_index = alphabet.index(character.lower())
            encrypted_character_index = (character_index + current_drift) % 26
            
            # Preserve original case
            if character.islower():
                encrypted_character = alphabet[encrypted_character_index]
            else:
                encrypted_character = alphabet[encrypted_character_index].upper()
            
            encrypted_message += encrypted_character
            current_drift += 1  # Increment drift for next alphabetic character
        else:
            # Handle non-alphabetic characters
            encrypted_message += non_alphabet_replacement.get(character, character)
            current_drift = drift  # Reset drift to original value
    
    return encrypted_message


if __name__ == "__main__":
    """
    Command-line interface for the whisperer function.
    
    Usage:
        python whisper.py <message> <drift>
    
    Arguments:
        message: The text message to encrypt (wrap in quotes if it contains spaces)
        drift: The initial drift/shift value (integer)
    
    Example:
        python whisper.py "Hello World" 5
        python whisper.py "secret message" 10
    """
    if len(sys.argv) != 3:
        print("Usage: python whisper.py <message> <drift>")
        print("\nExamples:")
        print('  python whisper.py "Hello World" 5')
        print('  python whisper.py "secret" 3')
        sys.exit(1)
    
    message = sys.argv[1]
    drift = sys.argv[2]
    
    try:
        encrypted_message = whisperer(message, drift)
        print("You sent a whisper: ", encrypted_message)
    except ValueError:
        print("Error: Drift must be a valid integer")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)