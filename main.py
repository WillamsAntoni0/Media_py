def main():
    # Entrada de dados
    Aprovados = 0
    Reprovados = 0
    
    Alunos = int(input("Informe quantos alunos serao avaliados: "))
    
    for i in range(1, Alunos + 1):
        materia1 = float(input("\nInforme a nota da materia 1: "))
        materia2 = float(input("\nInforme a nota da materia 2: "))
        materia3 = float(input("\nInforme a nota da materia 3: "))
        materia4 = float(input("\nInforme a nota da materia 4: "))
        materia5 = float(input("\nInforme a nota da materia 5: "))

        Soma = materia1 + materia2 + materia3 + materia4 + materia5
        Media = Soma / 5
        print(f"\nResultado da media: {Media:.2f}")

        if materia1 >= 6 and materia2 >= 6 and materia3 >= 6 and materia4 >= 6 and materia5 >= 6:
            print("\nAluno aprovado")
            Aprovados += 1
        else:
            print("\nAluno reprovado")
            Reprovados += 1

    print(f"\nTotal de alunos aprovados: {Aprovados}")
    print(f"Total de alunos reprovados: {Reprovados}")

if __name__ == "__main__":
    main()
