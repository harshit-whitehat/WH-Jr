import PyPDF2 as pd

filename = input('\nPath to the file: ')
file = open(filename, 'rb')
pdfReader = pd.PdfFileReader(file)

tried = 0

if not pdfReader.isEncrypted:
  print('The file is not password protected! You can successfully open it.')
else:
  wordListFile = open('test.txt', 'r', errors = 'ignore')
  body = wordListFile.read().lower()
  words = body.split('\n')
  for i in range(len(words)):
    word = words[i]
    print(f"Trying to decode password by: {word}")
    result = pdfReader.decrypt(word)
    if result == 1:
      print("Success. The password is : " + word)
      break
    elif result == 0:
      tried = tried + 1
      print("Password tried: " + str(tried))
      continue