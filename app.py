import pyxel
import random

from chef import Chef
from floor import Floor
from pan import Pan
from bin import Bin
from wall import Wall
from worktop import Worktop
from handover import Handover
from board import Board
from sink import Sink
from blender import Blender
from plates import Plates
from return_ import Return
from serve import Serve
from ingredient import Ingredient
from order import Order

from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, BOARD_HEIGHT, KITCHEN_LAYOUT, FPS,
    SERVICE_DURATION_FRAMES, MAX_FAILURES, SCORE_Y, FAILURES_Y, TIMER_Y, TEXT_COLOR, RECIPES,
    FIRST_ORDER_DELAY_SEC, ORDER_SPAWN_INTERVAL_SEC, MAX_WAITING_ORDERS, BOARD_MARGIN_RIGHT,
    ORDER_SPACING, ORDER_X, ORDER_Y
)

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Service Rush", display_scale=3)
        pyxel.load("assets/resources.pyxres")
        
        self.__chef1 = Chef(chef_id=1, col=5, row=2)  
        self.__chef2 = Chef(chef_id=2, col=5, row=6) 

        self.__score = 0
        self.__failures = 0
        self.__timer_frames = SERVICE_DURATION_FRAMES

        self.__floors = []
        self.__pan = None
        self.__bin = None
        self.__walls = []
        self.__worktops = []
        self.__handovers = []
        self.__boards = []
        self.__sink = None
        self.__blender = None
        self.__plates = None
        self.__return = None
        self.__serve = None
        self.__ingredients = []

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
                elif item == "BOARD":
                    self.__boards.append(Board(col, row))
                elif item == "SINK":
                    self.__sink = Sink(col, row)
                elif item == "BLENDER":
                    self.__blender = Blender(col, row)
                elif item == "PLATES":
                    self.__plates = Plates(col, row)
                elif item == "RETURN":
                    self.__return = Return(col, row)
                elif item == "SERVE":
                    self.__serve = Serve(col, row)
                elif item in ("ONION", "EGG", "CHORIZO", "TOMATO", "POTATO"):
                    item_lower = item.lower()
                    self.__ingredients.append(Ingredient(col, row, item_lower))

        self.__orders = []
        self.__spawn_timer_frames = FIRST_ORDER_DELAY_SEC * FPS
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.__timer_frames > 0:
            self.__timer_frames -= 1

        if self.__spawn_timer_frames > 0:
            self.__spawn_timer_frames -= 1
        else:
            if len(self.__orders) < MAX_WAITING_ORDERS:
                random_recipe = random.choice(list(RECIPES.keys()))
                self.__orders.append(Order(random_recipe))
                self.__spawn_timer_frames = ORDER_SPAWN_INTERVAL_SEC * FPS

        for order in self.__orders:
            order.update()

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

        # Draw boards
        for board in self.__boards:
            board.draw()

        # Draw sink
        self.__sink.draw()

        # Draw blender
        self.__blender.draw()

        # Draw plates  
        self.__plates.draw()

        # Draw return
        self.__return.draw()

        # Draw serve
        self.__serve.draw()

        # Draw ingredients
        for ingredient in self.__ingredients:
            ingredient.draw()

        # Draw chefs
        self.__chef1.draw()
        self.__chef2.draw()

        # Draw score, failures, and timer
        score_str = f"{self.__score}"
        failures_str = f"{self.__failures}/{MAX_FAILURES}"
        total_sec = self.__timer_frames // FPS
        minutes = total_sec // 60
        seconds = total_sec % 60
        time_str = f"{minutes:02d}:{seconds:02d}"

        score_x = SCREEN_WIDTH - (len(score_str) * 4) - BOARD_MARGIN_RIGHT
        failures_x = SCREEN_WIDTH - (len(failures_str) * 4) - BOARD_MARGIN_RIGHT
        timer_x = SCREEN_WIDTH - (len(time_str) * 4) - BOARD_MARGIN_RIGHT

        pyxel.text(score_x, SCORE_Y, score_str, TEXT_COLOR)
        pyxel.text(failures_x, FAILURES_Y, failures_str, TEXT_COLOR)
        pyxel.text(timer_x, TIMER_Y, time_str, TEXT_COLOR)

        # Draw orders
        for i, order in enumerate(self.__orders):
            order.draw(x=ORDER_X + (i * ORDER_SPACING), y=ORDER_Y)