import zipfile
import time

path = input("\nEnter zipfile path: ")

try:
  zipf = zipfile.ZipFile(path)
  if not zipf:
    print("Folder is not encrypted, can be successfully opened")

  else:
    success = False
    tries = 0
    startTime = time.time()
    endTime = 0

    passList = open("passlist.txt", "r", errors="ignore").read().split("\n")
    for guess in passList:
      print(f"Tries: {tries}", end="")
      tries=tries+1
      try: 
        with zipfile.ZipFile(path, "r") as zf:
          zf.read(pwd=guess)
          endTime = time.time()
          success = True
          break
      except:
        print("\b"*15, end="")

    if success:
      print(f"Success! The password is: {guess}. Decoded in {endTime-startTime}s.")
    else:
      print("Password could not be found.")

except:
  print("Error, recheck zipfile path")