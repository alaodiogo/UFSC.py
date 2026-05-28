palavra_1 = input()
palavra_2 = input()

if palavra_1 == palavra_2:
    eh_anagrama = False
else:
    eh_anagrama = sorted(palavra_1) == sorted(palavra_2)
    
print (eh_anagrama)