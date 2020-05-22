import time

import pytest
from pylenium import Pylenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from models.game import Trex, Obstacle


class TrexRunner:
    def __init__(self, py: Pylenium):
        self.py = py
        self.is_first_jump = True

    DEFAULT_DISTANCE = 110
    FLYING_OBSTACLE_WIDTH = 46
    CACTUS_SMALL_WIDTH = 17
    CACTUS_LARGE_WIDTH = 25
    TREX_HEIGHT = 51

    @property
    def trex(self) -> Trex:
        dino = self.py.execute_script('return Runner.instance_.tRex')
        return Trex(**dino)

    @property
    def trex_position(self) -> float:
        return self.trex.xPos

    @property
    def current_speed(self) -> float:
        return self.py.execute_script('return Runner.instance_.currentSpeed')

    @property
    def has_crashed(self) -> bool:
        return self.py.execute_script('return Runner.instance_.crashed')

    def setup(self) -> 'TrexRunner':
        self.py.visit('chrome://dino')
        self.py.get('canvas').should().be_visible()
        return self

    def start(self) -> 'TrexRunner':
        time.sleep(1)  # Add delay to avoid race condition
        self.jump()
        return self

    def jump(self):
        """ Hit the Space Bar to make Tiny Tim jump! """
        ActionChains(self.py.webdriver).send_keys(Keys.SPACE).perform()

    def is_obstacle_present(self) -> bool:
        obs = self.py.execute_script(
            'return Runner.instance_.horizon.obstacles.filter(o => (o.xPos > 25))[0] || {}')
        obstacle = Obstacle(**obs)
        distance_to_start_jump = self.DEFAULT_DISTANCE + 40 if self.is_first_jump else self.DEFAULT_DISTANCE

        # Calculate the distance difference to initiate the space bar press event based on current game speed
        if self.current_speed >= 10:
            distance_to_start_jump = round(distance_to_start_jump + (20 * (self.current_speed % 10))) + 40

        # If the game speed is > 13, space bar needs to be pressed in advance
        if self.current_speed > 13:
            distance_to_start_jump += 50

        # Check if there is an obstacle present in the current view
        if obstacle is not None and obstacle.xPos is not None:
            # If the obstacle is flying, we need to jump only if the height of Trex >= vertical position of the obstacle
            if ['width'] == self.FLYING_OBSTACLE_WIDTH and obstacle.yPos < self.TREX_HEIGHT:
                return False

            current_distance = obstacle.xPos - self.trex_position

            if obstacle.xPos > self.trex_position and current_distance <= distance_to_start_jump:
                if self.is_first_jump:
                    self.is_first_jump = False
                print(f'Identified Obstacle at {current_distance}')
                return True
        return False

    def get_score(self) -> str:
        return self.py.execute_script('return Runner.instance_.distanceMeter.highScore.join(\"\").substring(4)')


@pytest.fixture
def trex(py):
    return TrexRunner(py)


def test_trex_game(py, trex):
    trex.setup().start()
    while not trex.has_crashed:
        if trex.is_obstacle_present():
            trex.jump()
    py.screenshot('tiny_tim.png')
    print(f'\nYour score is: {trex.get_score()}')
