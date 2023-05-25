game zapas
class Developer(Person):
    def __init__(self, name, contact):
        super().__init__(name, contact)
        self.games = []

    def create_game(self, title, genre, date, game_type):
        # implementation omitted for brevity

    def manage_game(self):
        while True:
            print("\n=== Game Management Menu ===")
            print("1. View all games")
            print("2. Edit game attributes")
            print("3. Delete a game")
            print("4. Exit game management")

            choice = input("Enter choice (1-4): ")
            if choice == "1":
                # View all games
                print("=== All Games ===")
                for game in self.games:
                    print(f"{game.get_title()} ({game.get_genre()}, {game.get_date()})")

            elif choice == "2":
                # Edit game attributes
                print("=== Edit Game ===")
                game_title = input("Enter title of game to edit: ")
                for game in self.games:
                    if game.get_title() == game_title:
                        print(f"Editing attributes for {game_title}")
                        new_title = input("Enter new title (leave blank to keep current title): ")
                        if new_title:
                            game.set_title(new_title)
                        new_genre = input("Enter new genre (leave blank to keep current genre): ")
                        if new_genre:
                            game.set_genre(new_genre)
                        if isinstance(game, ActionGame):
                            new_levels = input("Enter new number of levels (leave blank to keep current levels): ")
                            if new_levels:
                                game.set_levels(new_levels)
                        elif isinstance(game, StrategyGame):
                            new_mission = input("Enter new mission (leave blank to keep current mission): ")
                            if new_mission:
                                game.set_mission(new_mission)

                        print(f"{game_title} updated successfully.")
                        break
                else:
                    print(f"Game '{game_title}' not found.")

            elif choice == "3":
                # Delete a game
                print("=== Delete Game ===")
                game_title = input("Enter title of game to delete: ")
                for game in self.games:
                    if game.get_title() == game_title:
                        self.games.remove(game)
                        print(f"{game_title} deleted successfully.")
                        break
                else:
                    print(f"Game '{game_title}' not found.")

            elif choice == "4":
                # Exit game management
                print("Exiting game management.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
