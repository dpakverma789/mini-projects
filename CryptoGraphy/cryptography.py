
try:
    from passlib.hash import pbkdf2_sha256
except ModuleNotFoundError:
    import os
    os.system('pip install passlib')
    from passlib.hash import pbkdf2_sha256


if __name__ == '__main__':
    plain_text = input('Enter Your Text: ')
    encrypted_text = pbkdf2_sha256.hash(plain_text)
    # encrypted_text = pbkdf2_sha256.using(rounds=8000, salt_size=10).hash(plain_text)
    flag = pbkdf2_sha256.verify(plain_text, encrypted_text)
    print(encrypted_text, flag)
