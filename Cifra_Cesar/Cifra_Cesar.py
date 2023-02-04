"""PROGRAMA AINDA NÃO ESTÁ PRONTO, AINDA PRECISA TRATAR ALGUMAS EXCEÇÕES QUE PODEM-
- OCORRER EM TEMPO DE EXECUÇÃO.
"""
import os

def criptografar(texto, num):
    os.system("cls") if os.name in "nt" else os.system("clear")
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "Z"]
    encrypt = list()
    for char in texto:
        pos = alpha.index(char)
        encrypt.append(alpha[pos+num])
    print(f"Mensagem criptografada: {encrypt}")

try:
    print("\n\n")
    print("*"*60)
    print("Seja bem vindo(a) ao programa de criptografia!")
    print("*"*60)
    print("\n\n")
    texto = str(input("Digite o texto a ser criptografado: ").upper())
    num = int(input("Digite o número de pulos: "))
    criptografar(texto, num)
except KeyboardInterrupt:
    os.system("cls") if os.name in "nt" else os.system("clear")
    print("\n\n")
    print("*"*60)
    print("Programa finalizado pelo usuário..")
    print("*"*60)