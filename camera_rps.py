import cv2
from keras.models import load_model
import numpy as np
import random
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
choices = ["Rock","Papper","Scissors","nothing"]
print ("welcome to the computer vision Rock, Papper and Scissors game \
       please display Rock, Papper and Scissors to camera")
class Computer_Vision:
    def __init__(self,computer_wins=0,user_wins=0):
        self.computer_wins = 0
        self.user_wins = 0

    def play_game(self):
        start_time = time.time()
        print_winner = False
        while True:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time > 4.9 and  elapsed_time < 5:
                print("please show Rock,Papper,or Scissors at the camera")
                user_choice = self.get_prediction()
                print (f'you chose {user_choice}')
                computer_choice = self.get_computer_choice()
            elif elapsed_time > 5 and elapsed_time < 7:
                if print_winner is False:
                   winner = self.get_winner(computer_choice,user_choice)
                   print (winner)
                   print ("get ready for the next round. Please display Rock, Papper or Scissors to the camera.")
                   if winner == 'Computer wins':
                       self.computer_wins += 1
                   elif winner == 'user wins':
                       self.user_wins +=1
                   print_winner = True
                   print ("computer score:",self.computer_wins)
                   print ("user score:", self.user_wins)
                   if self.computer_wins == 3:
                       print ("Computer has won 3 rounds. Computer wins. Game over")
                       return
                   elif self.user_wins == 3:
                       print ("User has won 3 rounds. User wins. Game over")
                       return
            elif elapsed_time > 7:
                print_winner = False
                start_time = time.time()

    def get_prediction(self):
        prediction = model.predict(data)
        highest_index = np.argmax(prediction[0])
        user_choice = choices[highest_index]
        return user_choice

    def get_computer_choice(self):
        computer_choice = random.choice(choices[0:3])
        return computer_choice

    def get_winner(self,computer_choice,user_choice):
        if user_choice == "nothing":
                return("please put your hand to the camera")
        elif user_choice == computer_choice:
                return("its a draw")
        elif (computer_choice =='Rock' and user_choice == 'Scissors') or \
            (computer_choice =='Scissors' and user_choice == 'Papper') or \
            (computer_choice =='Papper' and user_choice == 'Rock'):
                return ('Computer wins')
        else:
            return ('user wins')
def game_loop():
        game =Computer_Vision(computer_wins=0,user_wins=0)
        game.play_game()

game_loop()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()