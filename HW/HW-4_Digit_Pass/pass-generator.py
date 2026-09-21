file = open("passlist.txt", "w")
counter=0

characters = ['0','1','2','3','4','5','6','7','8','9', 
  'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
  'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','p','Q','R','S','T','U','V','W','X','Y','Z',
  '!','@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','}','{','^','[',']',' ','+','-','_','&',';','"','?','`','\'','\\'
]

for i in characters:
  for j in characters:
    for k in characters:
      for l in characters:
        guess = str(i)+str(j)+str(k)+str(l)
        counter = counter + 1
        print(guess, end="")
        file.write(guess)
        file.write("\n")
        print("\b\b\b\b", end="")


print("Password list complete!")
file.close()