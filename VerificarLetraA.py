def verificar_letra_a(texto):
    texto_lower = texto.lower()
    count_a = texto_lower.count('a')
    if count_a > 0:
        print(f"A letra 'a' aparece {count_a} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

def main():
    texto = input("Informe uma string: ")
    verificar_letra_a(texto)

if __name__ == "__main__":
    main()