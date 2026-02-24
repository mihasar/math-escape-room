from models.puzzle import new_puzzle
from database.db import DBManager
from views.cli_view import CLIView

class MainController:

    def __init__(self):
        self.rooms_total = 5
        self.mistakes_allowed = 3
        self.db = DBManager()
        self.view = CLIView()
        self.player_name = "Player"
        self.reset()

    def reset(self):
        self.puzzles = []
        for _ in range(self.rooms_total):
            self.puzzles.append(new_puzzle())

        self.room_index = 0
        self.__mistakes = 0
        self.message = ""
        self.game_over = False
        self.game_won = False

    def set_player_name(self, name):
        self.player_name = name if name.strip() != "" else "Player"

    def current_question(self):
        return self.puzzles[self.room_index].question()
    
    @property
    def mistakes(self):
        return self.__mistakes
    
    def submit(self, user_input):

        if self.game_over or self.game_won:
            return

        if self.puzzles[self.room_index].check(user_input):

            self.room_index += 1
            self.message = "Correct!"

            if self.room_index >= self.rooms_total:
                self.game_won = True
                self.message = "YOU ESCAPED!"
                self.db.save_score(self.player_name, self.room_index, self.mistakes)

        else:
            self.__mistakes += 1
            self.message = "Wrong!"

            if self.mistakes >= self.mistakes_allowed:
                self.game_over = True
                self.message = "GAME OVER!"
                self.db.save_score(self.player_name, self.room_index, self.mistakes)

    def run(self):
        name = self.view.ask("Enter player name: ")
        self.set_player_name(name)
        
        while True:
            self.view.show_menu(self.player_name)
            choice = self.view.get_choice()

            if choice == "1":
                self.play_cli()

            elif choice == "2":
                # ✅ Pygame mode
                import pygame
                from views.pygameview import PygameView

                pygame.init()
                self.reset()
                view = PygameView(self)
                view.run()
                pygame.quit()

            elif choice == "3":
                self.view.show(self.get_stats_text())

            elif choice == "4":
                name = self.view.ask("Enter new player name: ")
                self.set_player_name(name)
                self.view.show(f"Player set to: {self.player_name}\n")

            elif choice == "5":
                self.reset_stats()
                self.view.show("Scores cleared.\n")

            elif choice == "6":
                self.view.show("Bye!\n")
                break

            else:
                self.view.show("Invalid choice.\n")
    
    def play_cli(self):
        self.reset()

        while not self.game_over and not self.game_won:
            self.view.show_separator()
            self.view.show_question(self.current_question())

            user_input = self.view.ask("Your answer: ")
            self.submit(user_input)

            self.view.show_status(self.message, self.mistakes, self.mistakes_allowed)

        # הודעת סיום
        self.view.show(self.message + "\n")

    def get_scores(self):
        return self.db.fetch_scores()

    def get_stats_text(self):

        rows = self.get_scores()

        if len(rows) == 0:
            return "\nNo scores yet.\n"

        text = "\nplayer | rooms | mistakes\n"
        text += "-------------------------\n"

        for r in rows:
            text += f"{r[0]}  | {r[1]}     | {r[2]}\n"

        return text

    def reset_stats(self):
        self.db.clear_scores()