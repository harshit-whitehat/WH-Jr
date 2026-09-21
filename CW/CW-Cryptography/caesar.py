def main():
  choice = int(input("\n1. Encryption\n2. Decryption\nChoose(1, 2): "))
  if choice == 1:
    encryption()
  elif choice == 2:
    decryption()


def encryption():
  msg = input("Enter your message: ")
  key = int(input("Enter any key from 1-94: "))
  print("Encrypting...")
  encrypted_text = ""
  
  for i in range(len(msg)):
    temp = (ord(msg[i])+key)
    if temp > 126:
      temp = (temp % 126) + 31
    encrypted_text += chr(temp)
  
  print("The encrypted text is: "+encrypted_text)

def decryption():
  msg = input("Enter your cipher text: ")
  key = int(input("Enter any key from 1-94: "))
  decrypted_text = ""
  print("Decrypting")
  
  for i in range(len(msg)):
    temp = (ord(msg[i])-key)
    if temp < 32:
      temp = 95 + temp
    decrypted_text += chr(temp)
  
  print("The decrypted text is: "+decrypted_text)


if __name__ == "__main__":
  main()