vocal=0
consonante=['a']
for x in range(10):
    
    letras = str(input("Ingrese su letra "))
    if (letras == 'a' or letras == 'e' or letras == 'i' or letras == 'o' or letras == 'u'):
        vocal= vocal + 1
        print("vocal")
    else:
         consonante= consonante + 1
         print("consonante")
print(f"Usted tiene: {vocal} vocales y {consonante} consonantes")