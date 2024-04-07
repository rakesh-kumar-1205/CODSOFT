import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")
        self.master.geometry("300x250")  # Set initial window size

        self.user_choice_label = tk.Label(master, text="Choose Rock, Paper, or Scissors:")
        self.user_choice_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("Rock")
        self.user_choice_menu = tk.OptionMenu(master, self.user_choice_var, "Rock", "Paper", "Scissors")
        self.user_choice_menu.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        self.play_button = tk.Button(master, text="Play", command=self.play_game, bg="green", fg="white", relief="raised")
        self.play_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        self.result_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.score_label = tk.Label(master, text="Score: User - 0 | Computer - 0", font=("Helvetica", 10))
        self.score_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game, state=tk.DISABLED, bg="blue", fg="white", relief="raised")
        self.play_again_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        self.user_score = 0
        self.computer_score = 0

    def play_game(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        
        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

        self.update_score(result)

        self.score_label.config(text=f"Score: User - {self.user_score} | Computer - {self.computer_score}")

        self.play_again_button.config(state=tk.NORMAL)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            return "You win!"
        else:
            return "Computer wins!"

    def update_score(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1

    def reset_game(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score: User - 0 | Computer - 0")
        self.play_again_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
