from PIL import Image
import stepic

def XorCrypt(msg, key):
    input_msg = msg
    itr = len(input_msg)
    out = ""

    for i in range (itr):
        current_char = input_msg[i]
        current_key = key[i%len(key)]
        out += chr(ord(current_char) ^ ord(current_key))

    return out

def Encode():
    msg = input ("Please Enter the Message: ")

    enc_key = input("Enter the encryption key: ")

    msg = XorCrypt(msg, enc_key)
    
    msg = bytes(msg, 'utf-8')

    img = Image.open("Image.png")

    encoded_img = stepic.encode(img, msg)

    encoded_img.save("Encoded.png", 'PNG')

    print("Successfully Encoded!")

def Decode():
    img = Image.open("Encoded.png")

    dec_key = input("Enter the Decryption Key: ")
    
    msg = stepic.decode(img)

    decoded_msg = XorCrypt(msg, dec_key)

    print(decoded_msg)

print("Welcome to Image Stagonography")
print("1: Encode")
print("2: Decode")

choice = input("Please Select One: ")

if (choice == '1'):
    Encode()
elif(choice == '2'):
    Decode()
else:
    print("Invalid Choice")
