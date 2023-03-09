def reverse(word): 
  str = "" 
  for i in word: 
    str = i + str
  return str
  
palavra=input("Insira a palavra para inverter: ")
  
print ("Original: ",palavra) 
  
print ("Invertida: ",reverse(palavra))