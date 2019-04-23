# secret_number = 6
# i = 0
# while i < 5:
#     x = int(input("CHUTE:\n"))
#     if x == secret_number:
#         print("Parabéns, você acertou!")
#         break
#     else:
#         chances = 4 - i
#         print("Errou. Você possui " + str(chances) + " chances.")
#         i = i + 1
# print("itssss over...........")

#-----------------------------------

numbers = [1, 4, 6, 6, 9, 345, 23 ,101]
lista = []
for x in numbers:
    if x not in lista:
        lista.append(x)
print(lista)