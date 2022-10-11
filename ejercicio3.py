perro = ['Puppy', '12/12/2012' , 'Macho', '123']
for ejem in range(len(perro)):
    if perro[ejem] == '12/12/2012':
        perro[ejem] = '13/12/2012'
for ejem in range(len(perro)):
    if perro[ejem] == '123':
        perro[ejem] = '28957346'
        print(perro) 