alphabetToDigit = {}
digitToAlphabet = {}
num = 0
for i in range(65, 123):
    if chr(i).isalpha():
        alphabetToDigit[chr(i)] = num
        digitToAlphabet[num] = chr(i)
        num += 1


def encrypt(mess, encryptionKey):
    encryptedText = []
    for letter in mess:
        if letter in alphabetToDigit:
            newLetter = (alphabetToDigit[letter] + encryptionKey) % len(alphabetToDigit)
            encryptedText.append(digitToAlphabet[newLetter])
        else:
            encryptedText.append(letter)
    return ''.join(encryptedText)


def decrypt(mess, encryptionKey):
    decryptedText = []
    for letter in mess:
        if letter in alphabetToDigit:
            num  = alphabetToDigit[letter] - encryptionKey
            if num > 0:
                num %= len(digitToAlphabet)
            else:
                num = -(-num % len(digitToAlphabet))
            if num >= 0:
                decryptedText.append(digitToAlphabet[num])
            else:
                decryptedText.append(digitToAlphabet[len(alphabetToDigit) + num]) # +(-digit) = -digit
        else:
            decryptedText.append(letter)
    return ''.join(decryptedText)


def brute_force_hack(mess, rang = (-100, 100)):
    res = []
    for i in range(rang[0],rang[1]):
        res.append(decrypt(mess, i))
    return res


if __name__ == '__main__':
    print('ABCXYZaz ->',encrypt('ABCXYZaz', 1), 'key = 1')
    print(decrypt(encrypt('ABCXYZaz', 1), 1), ' <- Decrypt , key = 1')
    print('The secret password is Rosebud ->', encrypt('The secret password is Rosebud', 8), 'key = 8')
    print(decrypt(encrypt('The secret password is Rosebud', 8), 8), ' <- Decrypt , key = 8')
    hacked_text = brute_force_hack(encrypt('The secret password is Rosebud', 8))
    print(hacked_text)