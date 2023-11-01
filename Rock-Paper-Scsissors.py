import random
class Game:
    def __init__(self):    
        self.Computer_score = 0
        self.Player_score = 0

    def Computer(self):
        return random.choice(["Rock", "Paper", "Scissor"])

    def Player(self):
        s=input("\nChoose between Rock, Paper, and Scissor: ")
        if s in ["Rock", "Paper", "Scissor"]:
            return s
        else:
            print("Invalid input, try again!")
            return self.Player()
    def Play(self):
        for _ in range(int(input("How many rounds would you like to play:"))):
            computer_choice = self.Computer()
            player_choice = self.Player()
            print(f"\n\4Player's Choice: {player_choice} \n\4Computer's Choice: {computer_choice}")
            if player_choice!=computer_choice:
                match player_choice:
                    case "Rock":
                        if (computer_choice== "Rock" and player_choice== "Scissor") :self.Computer_score+=1;print("\n\4Result:Computer Win!") 
                        elif (player_choice == "Rock" and computer_choice == "Scissor"):self.Player_score+=1; print ("\n\4Result:Player win!")
                        elif (computer_choice== "Paper" and player_choice== "Rock") :self.Computer_score+=1;print("\n\4Result:Computer Win!") 
                        elif (player_choice == "Paper" and computer_choice == "Rock"): self.Player_score+=1; print ("\n\4Result:Player win!")
                    case "Paper":
                        if (computer_choice== "Paper" and player_choice== "Rock"):self.Computer_score+=1;print("\n\4Result:Computer Win!") 
                        elif(player_choice == "Paper" and computer_choice == "Rock"): self.Player_score+=1; print ("\n\4Result:Player win!")
                        elif (computer_choice== "Scissor" and player_choice== "Paper"): self.Computer_score+=1;print("\n\4Result:Computer Win!")  
                        elif (player_choice == "Scissor" and computer_choice == "Paper"): self.Player_score+=1; print ("\n\4Result:Player win!")
                    case "Scissor":
                        if (computer_choice== "Rock" and player_choice== "Scissor"):self.Computer_score+=1;print("\n\4Result:Computer Win!")   
                        elif(player_choice == "Rock" and computer_choice == "Scissor"):self.Player_score+=1;print ("\n\4Result:Player win!")
                        elif (computer_choice== "Scissor" and player_choice== "Paper"):self.Computer_score+=1;print("\n\4Result:Computer Win!") 
                        elif(player_choice == "Scissor" and computer_choice == "Paper"):self.Player_score+=1; print ("\n\4Result:Player win!")
            else:print("\n\4Result:It's Tie!")
    def Score(self):print(f"Score: Player Score {self.Player_score} Computer Score:{self.Computer_score}")
    def play_again(self):
       while True:
         choice = input("\nWanna play again\nPress 1 for Yes\nPress 2 for No\n-->")
         if choice == "1":
            self.Play()
            self.Score()
         elif choice == "2":
            break  
         else:
            print("Invalid input, try again!")

            

G=Game()
G.Play()
G.Score()
G.play_again()



