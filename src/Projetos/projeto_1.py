name = input("Digite seu primeiro nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
print(f"Seu nome é {name}, sua idade é {idade} e sua altura é {altura:.2f}")
print(f"{name} é idoso") if idade >= 60 else print(f"{name} é jovem")
nome: str = "Rubens"
