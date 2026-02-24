class CLIView:
    def show_menu(self, player_name):
        print("\n=== Math Escape Room ===")
        print(f"Current player: {player_name}")
        print("1) Play (CLI)")
        print("2) Play (Pygame)")
        print("3) Show Scores")
        print("4) Change Player Name")
        print("5) Reset Scores")
        print("6) Exit")

    def get_choice(self):
        return input("Choose (1-6): ").strip()

    def ask(self, text):
        return input(text).strip()

    def show(self, text):
        print(text)

    def show_separator(self):
        print("\n-------------------")

    def show_question(self, question):
        print(question)

    def show_status(self, message, mistakes, mistakes_allowed):
        print(message)
        print(f"Mistakes: {mistakes}/{mistakes_allowed}")