class MenuEntry:
    def __init__(self):
        self.sub_entry=None
        self.parent_entry=None
        self.title=''

class MenuDisplay:
    def onSelection(self):
        pass

    def onNavigation(self):
        pass

    def draw(self):
        pass