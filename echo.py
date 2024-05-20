import sys

def listener(whisper, drift=None):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    non_alphabet_replacement = {'^':',', ';':'.', '&':'!', '%':'?', '_':'_', '#':'(', '"':')', '.':' ', '..':'\t'}
    
    if drift is not None:
        drift = int(drift)
        whisper_heard = ''
        current_drift = drift
        
        for character in whisper:
            if character.lower() in alphabet:
                character_index = alphabet.index(character.lower())
                decrypted_character_index = (character_index - current_drift) % 26
                decrypted_character = alphabet[decrypted_character_index] if character.islower() else alphabet[decrypted_character_index].upper()
                whisper_heard += decrypted_character 
                current_drift += 1
            else:
                whisper_heard += non_alphabet_replacement.get(character, character)
                current_drift = drift
        
        return whisper_heard
    else:
        for drift in range(26):
            whisper_heard = ''
            current_drift = drift
            
            for character in whisper:
                if character.lower() in alphabet:
                    character_index = alphabet.index(character.lower())
                    decrypted_character_index = (character_index - current_drift) % 26
                    decrypted_character = alphabet[decrypted_character_index] if character.islower() else alphabet[decrypted_character_index].upper()
                    whisper_heard += decrypted_character 
                    current_drift += 1
                else:
                    whisper_heard += non_alphabet_replacement.get(character, character)
                    current_drift = drift
            print(f"Decrypted text with a drift of {drift}: {whisper_heard}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python echo.py <encrypted_text> [drift]")
        sys.exit(1)
    
    whisper = sys.argv[1]
    drift = None
    if len(sys.argv) == 3:
        drift = sys.argv[2]
    whisper_heard = listener(whisper, drift)
    print("You received a whisper: ", whisper_heard)
    