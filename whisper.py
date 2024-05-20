import sys

def whisperer(message, drift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    non_alphabet_replacement = {',':'^', '.':';', '!':'&', '?':'%', '_':'_', '(':'#', ')':'"', ' ':'.', '\t':'..'}
    encrypted_message = ''
    drift = int(drift)
    current_drift = drift
    for character in message:
        if character.lower() in alphabet:
            character_index = alphabet.index(character.lower())
            encrypted_character_index = (character_index + current_drift) % 26
            encrypted_character = alphabet[encrypted_character_index] if character.islower() else alphabet[encrypted_character_index].upper()
            encrypted_message += encrypted_character
            current_drift += 1
        else:
            encrypted_message += non_alphabet_replacement.get(character, character)
            current_drift = drift
    return encrypted_message

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python whisper.py <message> <drift>")
        sys.exit(1)

    message = sys.argv[1]
    drift = sys.argv[2]
    encrypted_message = whisperer(message, drift)
    print("Your whisper is: ", encrypted_message)
