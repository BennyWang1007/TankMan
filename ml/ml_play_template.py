import random


class MLPlay:
    def __init__(self):
        self.game_info = []
        self.player_2P_info = []
        self.player_1P_info = []
        print("Initial ml script")
        self.time = 0

    def update(self, scene_info: dict):
        """
        Generate the command according to the received scene information
        """
        # print(scene_info)
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        command = []
        self.time += 1
        if self.time % 30 == 0:
            act = random.randrange(5)
        else:
            act = None
        if act == 1:
            command.append("TURN_RIGHT")
        elif act == 2:
            command.append("TURN_LEFT")
        elif act == 3:
            command.append("FORWARD")
        elif act == 4:
            command.append("BACKWARD")
        if act == 0:
            command.append("SHOOT")

        return command

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")

