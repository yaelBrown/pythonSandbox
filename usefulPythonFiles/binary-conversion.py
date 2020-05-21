#Binary Converter - www.101computing.net/binary-converter-using-python/  
  
#Binary to denary conversion  
binary = input("Input a number in binary:")  
denary = 0  
for digit in binary:  
  #A left shift in binary means x2  
  denary = denary*2 + int(digit)  
print("Your denary number is: " + str(denary))  
  
#Denary to binary conversion  
denary = int(input("Input a denary number:"))  
binary=""  
while denary>0:  
  #A left shift in binary means /2  
  binary = str(denary%2) + binary  
  denary = denary//2  
print("Your binary number is: " + binary)  