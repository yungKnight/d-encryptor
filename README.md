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