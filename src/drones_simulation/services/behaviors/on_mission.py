from typing import Generator

import numpy as np

from ...models import Drone
from ...models.base import BaseBehavior


class OnMission(BaseBehavior):

    def _init_drone(self) -> None:
        self._drone = Drone(np.array([0, 0, 0]), np.array([1, 1, 1]))

    def steps(self) -> None:
        pass
