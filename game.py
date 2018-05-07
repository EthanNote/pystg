from player import Player
from utility import Utility

if __name__ == '__main__':
    Utility.setup()
    Utility.add_to_group(Player(), 'player')
    Utility.gameloop()
