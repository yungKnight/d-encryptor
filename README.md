# D-Encryptor

A simple encryption/decryption tool using a drift cipher algorithm.

## Installation

```bash
pip install -e .
```

## Usage

### As a command line tool:
```bash
# Encrypt a message
d-encryptor encrypt "hello world" 5

# Decrypt a message with known drift
d-encryptor decrypt "mjqqt.btwqi" 5

# Decrypt without knowing the drift (tries all possibilities)
d-encryptor decrypt "mjqqt.btwqi"
```

### As a Python module:
```bash
# Encrypt
python -m d_encryptor encrypt "hello world" 5

# Decrypt
python -m d_encryptor decrypt "mjqqt.btwqi" 5
```

### In Python code:
```python
from d_encryptor import say, listen

# Encrypt
encrypted = say("hello world", 5)
print(encrypted)  # mjqqt.btwqi

# Decrypt
decrypted = listen("mjqqt.btwqi", 5)
print(decrypted)  # hello world
```

## How it works

The drift cipher shifts each letter by an increasing amount based on its position and the initial drift value.
=======
# d-encryptor
This is a combination of python programs that encrypts normal messages and decrypts whisper format all of which are <br> executable from the WindowsOS, MacOS and Linux command terminal

## INSTALLATION
This is a batch of simple python programs with the only requirements being to have ```python``` installed on your local machine.

1. Download ```python``` from the official page (skip if you have ```python``` installed on your machine)
  
2. Clone the repository
 
## USAGE
1. Open your computer terminal <br>

2. Check into the host directory where you cloned the repository into <br>
```C:\your\host\directory```

3. Check into the cloned repository <br>
```cd d-encryptor``` on ```windows```(check for alternate commands in other OS)

4. Run the command(s): <br>
## For encryption of messages:
 ```python whisper.py "your_message" (drift_value)``` <br>
## For decryption of whisper(s):
 ```python echo.py "your_whisper" (drift_value)``` <br>
## Note: 
```drift_value``` is optional and can range from 1-25 with no need for the parentheses
