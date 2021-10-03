from Crypto.Cipher import AES
from hybrid import decrypt, decryptAES, getNonce

pri=input("Enter the Private Key: ")
pri = [int(i) for i in pri.split()]
cipherKey=input("Enter the AES Symmetric Key: ")
cipherKey = [int (i) for i in cipherKey.split(", ")]
filePath=input("Enter cipher file path: ")


decriptedKey=''.join(decrypt(pri,cipherKey))
print()
print("Decrypting the AES Symmetric Key...")

decriptedKey=decriptedKey.encode('utf-8')
cipherAESd = AES.new(decriptedKey, AES.MODE_GCM, nonce=getNonce())
with open(filePath, 'rb') as f:
    cipherText = f.read()
    print(cipherText)
    decrypted=decryptAES(cipherAESd,cipherText.decode('utf-8', errors='ignore'))
    print()
    print("Decrypting the message using the AES symmetric key.....")
    print("decrypted message: ", decrypted)
