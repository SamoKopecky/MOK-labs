def decode(numbers):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = ""
    for n in numbers:
        string += alphabet[n]
    return string


def encode(chars):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = []
    for c in chars:
        numbers.append(alphabet.index(c))
    return numbers


def encrypt(message, key):
    return list(map(lambda m: (m + key) % 26, message))


def decrypt(cipher_text, key):
    return list(map(lambda c: (c - key) % 26, cipher_text))


def check_homomorphism():
    key = 3
    m1 = 'hello'
    m2 = 'world'
    m1_enc = encode(m1)
    m2_enc = encode(m2)

    print(f'm1: {m1}')
    print(f'm2: {m2}')

    c1 = encrypt(m1_enc, key)
    c2 = encrypt(m2_enc, key)
    print(f'c1: {decode(c1)}')
    print(f'c2: {decode(c2)}')

    c3 = caesar_sum(c1, c2)
    m3 = decode(caesar_sum(m1_enc, m2_enc))
    first = decode(caesar_sum(decrypt(c1, key), decrypt(c2, key)))
    second = decode(decrypt(c3, 2 * key))
    print(f'{m3} (m1 + m2) == {first} (dec(c1) + dec(c2))')
    print(f'{m3} (m1 + m2) == {second} (dec(c1 + c2))')


def caesar_sum(a, b):
    c = []
    for i in range(len(a)):
        c.append((a[i] + b[i]) % 26)
    return c


def main():
    check_homomorphism()


if __name__ == '__main__':
    main()
