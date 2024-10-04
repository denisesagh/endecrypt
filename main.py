import os


KEY=22 # Use any key you want to encrypt or decrypt the image

def encrypt(path, key):
    try:
        with open(path, 'rb') as fin:
            image = bytearray(fin.read())

        for index, values in enumerate(image):
            image[index] = values ^ key

        with open(path, 'wb') as fin:
            fin.write(image)



    except Exception as e:
        print('Error caught : ', str(e))

def decrypt(path, key):
    try:
        with open(path, 'rb') as fin:
            image = bytearray(fin.read())

        for index, values in enumerate(image):
            image[index] = values ^ key

        with open(path, 'wb') as fin:
            fin.write(image)

    except Exception as e:
        print('Error caught : ', str(e))


def filereader(mode):
    try:
        path = input(r'Enter path of Image or folder: ')
        if os.path.isdir(path):
            for image_file in os.listdir(path):
                image_path = os.path.join(path, image_file)
                print('--------------------------------------\n'
                      '|The path of file : ', image_path)
                if image_path.endswith('.jpg') or image_path.endswith('.png'): #remove this line if you want to encrypt any file
                    print('|Valid file format.')
                    if mode == 'encrypt':
                        encrypt(image_path, KEY)
                        print('|Encryption Done...')
                    elif mode == 'decrypt':
                        decrypt(image_path, KEY)
                        print('|Decryption Done...')
                    else:
                        print('|Invalid choice. Try again.')
            print('--------------------------------------')

        if os.path.isfile(path):
            if mode == 'encrypt':
                encrypt(path, KEY)
                print('--------------------------------------')
                print('Encryption from ', path, ' Done...')
                print('--------------------------------------')
            elif mode == 'decrypt':
                decrypt(path, KEY)
                print('--------------------------------------')
                print('Decryption from ', path, ' Done...')
                print('--------------------------------------')

        else:
            print('Invalid path. Try again.')

    except Exception as e:
        print('Error caught : ', str(e))

if __name__ == '__main__':
    while True:
        print('''
        1. Encrypt
        2. Decrypt
        3. Exit
        ''')
        choice = input('Enter your choice : ')
        if choice == '1':
            filereader('encrypt')
        elif choice == '2':
            filereader('decrypt')
        elif choice == '3':
            break
        else:
            print('Invalid choice. Try again.')
