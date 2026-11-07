import pyxel
from chef import Chef

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BOARD_HEIGHT, KITCHEN_LAYOUT, FPS, SERVICE_DURATION_FRAMES, MAX_FAILURES, SCORE_X, SCORE_Y, FAILURES_X, FAILURES_Y, TIMER_X, TIMER_Y, TEXT_COLOR

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Service Rush", display_scale=3)
        pyxel.load("assets/resources.pyxres")
        
        self.__chef1 = Chef(chef_id=1, start_col=5, start_row=2)  
        self.__chef2 = Chef(chef_id=2, start_col=5, start_row=6) 

        self.__score = 0
        self.__failures = 0
        self.__timer_frames = SERVICE_DURATION_FRAMES

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.__timer_frames > 0:
            self.__timer_frames -= 1

    def draw(self):
        # Clear the screen with a white color
        pyxel.cls(7)

        # Draw service board
        pyxel.rect(0, 0, SCREEN_WIDTH, BOARD_HEIGHT, 0) 

        # Draw kitchen layout
        for row, row_item in enumerate(KITCHEN_LAYOUT):
            for col, item in enumerate(row_item):
                x = col * 16
                y = row * 16 + BOARD_HEIGHT
                if item == "FREE":
                    pyxel.rect(x, y, 16, 16, 7)  # White for free space
                elif item == "WALL":
                    pyxel.rect(x, y, 16, 16, 13)  # Grey for walls
                elif item == "PASS":
                    pyxel.rect(x, y, 16, 16, 10)  # Yellow for pass-through areas
                elif item == "BIN":
                    pyxel.rect(x, y, 16, 16, 8)  # Red gray for bin
                elif item == "FREE_WORK":
                    pyxel.rect(x, y, 16, 16, 4)  # Brown for free work areas
                else:
                    pyxel.rect(x, y, 16, 16, 11)  # Green for items

        # Draw chefs
        self.__chef1.draw()
        self.__chef2.draw()

        # Draw score, failures, and timer
        total_sec = self.__timer_frames // FPS
        minutos = total_sec // 60
        segundos = total_sec % 60
        time_str = f"{minutos:02d}:{segundos:02d}"

        pyxel.text(SCORE_X, SCORE_Y, f"SCORE: {self.__score}", TEXT_COLOR)        
        pyxel.text(FAILURES_X, FAILURES_Y, f"FAILURES: {self.__failures}/{MAX_FAILURES}", TEXT_COLOR)
        pyxel.text(TIMER_X, TIMER_Y, f"TIME: {time_str}", TEXT_COLOR)