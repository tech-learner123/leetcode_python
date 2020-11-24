class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        After at most 4 cycles,
        the limit cycle trajectory returns to the initial point.
        We do not need to run 4 cycles to identify the limit cycle trajectory. One cycle is enough. There could be two situations here.

            First, if the robot returns to the initial point after one cycle, that's the limit cycle trajectory.

            Second, if the robot doesn't face north at the end of the first cycle, that's the limit cycle trajectory. Once again, that's the consequence of the plane symmetry for the repeated cycles [proof].
        """
        # north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position is in the center
        x = y = 0
        # facing north
        idx = 0

        for i in instructions:
            if i == "L":
                idx = (idx + 3) % 4
            elif i == "R":
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]

        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        return (x == 0 and y == 0) or idx != 0