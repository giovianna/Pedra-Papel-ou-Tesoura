import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

escolha = [pedra, papel, tesoura]

computer_choice = random.choice(escolha)

computer_choice_index = random.randint(0, 2)
computer_choice = escolha[computer_choice_index]

player_choice = input('Vamos jogar pedra, papel, tesoura! Para escolher pedra digite 1, para papel 2 e para tesoura 3.\n').lower()

if player_choice in ['1', '2', '3']:
    player_choice_index = int(player_choice) - 1
    player_choice = escolha[player_choice_index]
    print(f'Você escolheu:\n{player_choice}')
else:
    print('Opção inválida!')
    exit()

print(f'Computador:\n{computer_choice}')    

if player_choice == computer_choice:
    print('Empate!')
elif (player_choice == pedra and computer_choice == tesoura) or \
     (player_choice == papel and computer_choice == pedra) or \
     (player_choice == tesoura and computer_choice == papel):
    print('Você venceu!')
else:
    print('Computador venceu!')











