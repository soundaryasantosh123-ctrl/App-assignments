class Player:
    def __init__(self, name, jersey_number, runs):
        self.name = name
        self.jersey_number = jersey_number
        self.runs = runs

    def category(self):
        if self.runs >= 1000:
            return "Excellent"
        elif self.runs >= 500:
            return "Good"
        else:
            return "Average"

    def display(self):
        print("Player Name   :", self.name)
        print("Jersey Number :", self.jersey_number)
        print("Runs          :", self.runs)
        print("Category      :", self.category())
        print("-" * 30)


class Team:
    def __init__(self):
        self.players = []

    def add_player(self):
        name = input("Enter Player Name: ")
        jersey_number = int(input("Enter Jersey Number: "))
        runs = int(input("Enter Runs: "))

        player = Player(name, jersey_number, runs)
        self.players.append(player)

        print("Player added successfully!\n")

    def display_players(self):
        if not self.players:
            print("No players found.")
        else:
            print("\n--- Cricket Team Players ---")
            for player in self.players:
                player.display()


team = Team()

while True:
    print("\n===== Cricket Team Management System =====")
    print("1. Add Player")
    print("2. Display Players")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        team.add_player()

    elif choice == "2":
        team.display_players()

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
