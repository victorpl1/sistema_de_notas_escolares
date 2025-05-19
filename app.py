#digite seu nome para comerçarmos o codigo
nome =(input("digite seu nome:"))
#local onde o aluno coloca as notas
Nota_1 = int(input("nota do primeiro bimestre:"))

Nota_2 = int(input("nota do segundo bimestre:"))

Nota_3 = int(input("nota do terceiro bimestre:"))

Nota_4 = int(input("nota do quarto bimestre:"));

#soma as notas e divide por 4.
media = (Nota_1+Nota_2+Nota_3+Nota_4)/4
#se a media for maior ou igual a 7 o aluno será aprovado.
if media >= 6:

  print(f'{nome} você foi aprovado na disciplina y')
  print(f"{Nota_1,Nota_2,Nota_3,Nota_4}")

  #mostra todas as notas do aluno incluindo nome e nota final, para um melhor entendimento!
  print("nota final")
  print(media);

#se nao for irá mostrar que o aluno foi reprovado na disciplina
else:

  print(f"{nome} você foi reprovado na disciplina Y")
  print(f"{Nota_1,Nota_2,Nota_3,Nota_4}")

   #mostra todas as notas do aluno incluindo nome e nota final, para um melhor entendimento!
  print("nota final"f"{media}")

input("Pressione Enter para sair...");