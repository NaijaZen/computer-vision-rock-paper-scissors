import random

def play():
	computer = get_computer_choice(['Rock','Papper','Scissors'])
	user = get_user_choice()
	get_winner(computer,user)

def get_computer_choice(computer):
	return random.choice(computer)

def get_user_choice ():
	while True:
		choice = input('please enter Rock, Papper or Scissors')
		if choice == 'Rock':
			return choice
		elif choice  == 'Papper':
			return choice
		elif choice == 'Scissors':
			return choice
			print('please enter Rock, Papper or Scissiors')

def get_winner(computer_choice,user_choice):
    if computer_choice == user_choice:
        print ('Its a draw')
    elif (computer_choice =='Rock' and user_choice == 'Scissors') or \
            (computer_choice =='Scissors' and user_choice == 'Papper') or \
            (computer_choice =='Papper' and user_choice == 'Rock'):
                print ('Computer wins')
    else:
        print ('user wins')
play()