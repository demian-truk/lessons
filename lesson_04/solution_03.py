"""
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования.
Функция возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
"""

input_string = input("Enter string to encryption: ")
encryption_key = input("Enter encryption key: ")


def get_key_symbol(key, index):
    """
    if length of our key is less than initial string we get next character from very beginning in loop
    """
    if index > len(key) - 1:
        return key[index % len(key)]
    return key[index]


def xor_cipher(string, key):
    result = []
    for index, symbol in enumerate(string):
        result.append(chr(ord(symbol) ^ ord(get_key_symbol(key, index))))
    return "".join(result)


def xor_uncipher(encrypted_string, key):
    result = []
    for index, symbol in enumerate(encrypted_string):
        result.append(chr(ord(symbol) ^ ord(get_key_symbol(key, index))))
    return "".join(result)


# encryption
encrypted_string = xor_cipher(input_string, encryption_key)
print(f"Encrypted string: {encrypted_string}")

# decryption
decrypted_string = xor_uncipher(encrypted_string, encryption_key)
print(f"Decrypted string: {decrypted_string}")
