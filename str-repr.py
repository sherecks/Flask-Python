class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def __str__(self):
    return f"{self.nome}, {self.idade} anos de idade."

  def __repr__(self):
    return f"<('{self.nome}', {self.idade})>"


Pietra = Pessoa("Pietra", 19)
print(Pietra)
