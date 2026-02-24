import pygame


class PygameView:

    def __init__(self, controller):
        self.controller = controller

        self.width = 900
        self.height = 550
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Math Escape Room")

        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 32)

        self.clock = pygame.time.Clock()
        self.user_input = ""

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        self.controller.submit(self.user_input)
                        self.user_input = ""

                    elif event.key == pygame.K_BACKSPACE:
                        self.user_input = self.user_input[:-1]

                    elif event.key == pygame.K_r:
                        self.controller.reset()
                        self.user_input = ""

                    else:
                        if event.unicode.isdigit():
                            self.user_input += event.unicode

            self.screen.fill((20, 20, 20))

            # כותרת
            title = self.font.render("Math Escape Room", True, (255, 255, 255))
            self.screen.blit(title, (260, 40))

            # סטטוס
            status_text = f"Room {min(self.controller.room_index + 1, self.controller.rooms_total)}/{self.controller.rooms_total}  |  Mistakes {self.controller.mistakes}/{self.controller.mistakes_allowed}"
            status = self.small_font.render(status_text, True, (180, 180, 180))
            self.screen.blit(status, (160, 120))

            # שאלה (התיקון החשוב נמצא כאן)
            if not self.controller.game_over and not self.controller.game_won:
                question_text = self.controller.current_question()
                question = self.font.render(question_text, True, (255, 255, 255))
                self.screen.blit(question, (250, 220))

                input_surface = self.font.render(self.user_input, True, (0, 255, 0))
                self.screen.blit(input_surface, (420, 300))

                instruction = self.small_font.render("Type answer and press ENTER", True, (150, 150, 150))
                self.screen.blit(instruction, (270, 350))

            # הודעה
            message = self.font.render(self.controller.message, True, (255, 200, 0))
            self.screen.blit(message, (300, 420))

            restart_text = self.small_font.render("Press R to restart", True, (120, 120, 120))
            self.screen.blit(restart_text, (330, 480))

            pygame.display.flip()
            self.clock.tick(60)
            