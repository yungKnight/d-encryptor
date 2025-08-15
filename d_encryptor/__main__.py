"""
D-Encryptor Command Line Interface

A drift cipher encryption/decryption tool that uses progressive shifting.
"""

from .whisper import whisperer as say
from .echo import listener as listen
import sys

__all__ = ["listen", "say"]

def show_help():
    """Display detailed help information."""
    help_text = """
D-Encryptor - Progressive Drift Cipher Tool

DESCRIPTION:
    A python package that uses a progressive drift cipher.
    Each alphabetic character is shifted by an increasing amount based on position.

USAGE:
    d-encryptor <command> [arguments]
    python -m d_encryptor <command> [arguments]

COMMANDS:
    encrypt <message> <drift>
        Encrypts a message using the specified initial drift value.
        The drift increases by 1 for each alphabetic character.
        
        Example: d-encryptor encrypt "hello world" 5
    
    decrypt <encrypted_message> [drift]
        Decrypts a message. If drift is provided, uses that value.
        If no drift is provided, tries all possible drift values (0-25).
        
        Examples: 
            d-encryptor decrypt "mjqqt.btwqi" 5
            d-encryptor decrypt "mjqqt.btwqi"
    
    help, --help, -h
        Shows this help message.
    
    docs <function>
        Shows documentation for a specific function.
        Available functions: whisperer, listener
        
        Example: d-encryptor docs whisperer

SPECIAL CHARACTER MAPPING:
    During encryption:
        , → ^    . → ;    ! → &    ? → %
        ( → #    ) → "    space → .    tab → ..
    
    During decryption (reverse mapping):
        ^ → ,    ; → .    & → !    % → ?
        # → (    " → )    . → space    .. → tab

EXAMPLES:
    # Encrypt a simple message
    d-encryptor encrypt "hello" 1
    
    # Encrypt with spaces and punctuation
    d-encryptor encrypt "Hello, World!" 5
    
    # Decrypt with known drift
    d-encryptor decrypt "Igopt^.Ysuni&" 5
    
    # Decrypt without knowing drift (shows all possibilities)
    d-encryptor decrypt "Igopt^.Ysuni&"
    
    # View function documentation
    d-encryptor docs whisperer

ALGORITHM:
    The progressive drift cipher works by:
    1. Starting with an initial drift value
    2. For each alphabetic character, shift by current drift amount
    3. Increase drift by 1 after each alphabetic character
    4. Reset drift to initial value after non-alphabetic characters
    5. Preserve case (uppercase/lowercase) of original characters
"""
    print(help_text)

def show_function_docs(function_name):
    """Show documentation for a specific function."""
    if function_name.lower() == "whisperer":
        print("WHISPERER FUNCTION DOCUMENTATION:")
        print("=" * 40)
        print(say.__doc__)
    elif function_name.lower() == "listener":
        print("LISTENER FUNCTION DOCUMENTATION:")
        print("=" * 40)
        print(listen.__doc__)
    else:
        print(f"Unknown function: {function_name}")
        print("Available functions: whisperer, listener")

def main():
    """Main entry point for the d-encryptor package."""
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command in ["help", "--help", "-h"]:
        show_help()
        return
    
    elif command == "docs":
        if len(sys.argv) != 3:
            print("Usage: d-encryptor docs <function_name>")
            print("Available functions: whisperer, listener")
            sys.exit(1)
        show_function_docs(sys.argv[2])
        return
    
    elif command == "encrypt":
        if len(sys.argv) != 4:
            print("Usage: d-encryptor encrypt <message> <drift>")
            print("Example: d-encryptor encrypt \"hello world\" 5")
            sys.exit(1)
        message = sys.argv[2]
        drift = sys.argv[3]
        try:
            encrypted = say(message, drift)
            print(f"Encrypted message: {encrypted}")
        except ValueError:
            print("Error: Drift must be a valid integer")
            sys.exit(1)
         
    elif command == "decrypt":
        if len(sys.argv) < 3 or len(sys.argv) > 4:
            print("Usage: d-encryptor decrypt <encrypted_message> [drift]")
            print("Examples:")
            print("  d-encryptor decrypt \"mjqqt.btwqi\" 5")
            print("  d-encryptor decrypt \"mjqqt.btwqi\"  # tries all drifts")
            sys.exit(1)
        encrypted_message = sys.argv[2]
        drift = sys.argv[3] if len(sys.argv) == 4 else None
        decrypted = listen(encrypted_message, drift)
        if decrypted:
            print(f"Decrypted message: {decrypted}")
    
    else:
        print(f"Unknown command: {command}")
        print("Available commands: encrypt, decrypt, help, docs")
        print("Use 'd-encryptor help' for detailed usage information")
        sys.exit(1)

if __name__ == "__main__":
    main()