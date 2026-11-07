import pyxel
from chef import Chef
from floor import Floor
from pan import Pan
from bin import Bin
from wall import Wall
from worktop import Worktop
from handover import Handover

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BOARD_HEIGHT, KITCHEN_LAYOUT, FPS, SERVICE_DURATION_FRAMES, MAX_FAILURES, SCORE_X, SCORE_Y, FAILURES_X, FAILURES_Y, TIMER_X, TIMER_Y, TEXT_COLOR, SPRITES

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Service Rush", display_scale=3)
        pyxel.load("assets/resources.pyxres")
        
        self.__chef1 = Chef(chef_id=1, start_col=5, start_row=2)  
        self.__chef2 = Chef(chef_id=2, start_col=5, start_row=6) 

        self.__score = 0
        self.__failures = 0
        self.__timer_frames = SERVICE_DURATION_FRAMES

        self.__floors = []
        self.__pan = None
        self.__bin = None
        self.__walls = []
        self.__worktops = []
        self.__handovers = []

        for row, row_items in enumerate(KITCHEN_LAYOUT):
            for col, item in enumerate(row_items):
                if item == "FREE":
                    self.__floors.append(Floor(col, row))
                elif item == "PAN":
                    self.__pan = Pan(col, row)
                elif item == "BIN":
                    self.__bin = Bin(col, row)
                elif item == "WALL":
                    self.__walls.append(Wall(col, row))
                elif item == "FREE_WORK":
                    self.__worktops.append(Worktop(col, row))
                elif item == "PASS":
                    self.__handovers.append(Handover(col, row))

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.__timer_frames > 0:
            self.__timer_frames -= 1

    def draw(self):
        # Clear the screen with a white color
        pyxel.cls(7)

        # Draw service board
        pyxel.rect(0, 0, SCREEN_WIDTH, BOARD_HEIGHT, 0) 

        # Draw floors
        for floor in self.__floors:
            floor.draw()


        # Draw kitchen layout 
        # Draw floor
        for floor in self.__floors:
            floor.draw()

        # Draw pan
        self.__pan.draw()

        # Draw bin
        self.__bin.draw()

        # Draw walls
        for wall in self.__walls:
            wall.draw()

        # Draw worktops
        for worktop in self.__worktops:
            worktop.draw()

        # Draw handover
        for handover in self.__handovers:
            handover.draw()

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