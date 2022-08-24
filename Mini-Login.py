users = [
  (0, "Pips", "haole"),
  (1, "Joao", "caramela"),
  (2, "Branca", "franguinho"),
]


user_mapping = {user[1]: user for user in users}

name_input = input("Digite seu nome: ")
senha_input = input("Digite sua senha: ")

_, name, senha = user_mapping[name_input]

if senha_input == senha:
  print("Suas informações estão corretas!!!")
else:
  print("Seus detalhes estão incorretos!!!")  