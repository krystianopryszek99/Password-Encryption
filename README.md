# Password-Generator

<a href="https://pypi.org/project/cryptography/"><img src="https://img.shields.io/badge/pypi-36.0.1-green.svg"></a>
<a href="https://cryptography.io/en/latest/"><img src="https://img.shields.io/badge/docs-cryptography-blue.svg"></a>

## Table Of Content
- [Overview](#Overview)
- [Installation](#Installation)
- [References](#Refrences)

## Overview

`Cryptography` is a Python module that provides cryptographic techniques and methods.

```
>>> from cryptography.fernet import Fernet
>>> # Put this somewhere safe!
>>> key = Fernet.generate_key()
>>> f = Fernet(key)
>>> token = f.encrypt(b"A really secret message. Not for prying eyes.")
>>> token
b'...'
>>> f.decrypt(token)
'A really secret message. Not for prying eyes.'
```

## Installation

In order to install `cryptography` you will be required to have `pip`. When installing Python, tick the `pip` and you will have the ability to install libraries using `pip`.

```
$ pip install cryptography
```

## How to run

Follow the below steps to run this program on your machine.

1. Clone this repository onto your machine.
  ```
  $ git clone https://github.com/krystianopryszek99/Password-Generator.git
  ```
2. Navigate to the folder `Password-Generator`.
3. Open cmd and enter:
 ```
  $ python passwordGenerator.py
  ```

## References
- [Cryptography Docs](https://pypi.org/project/cryptography/)
- [Cryptography](https://cryptography.io/en/latest/)
