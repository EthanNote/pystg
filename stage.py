class Phase:
    def __init__(self):
        self.firing_list = []
        self.boss = None
        self.frame_count = 0
        self.firing_index = 1

    def update(self):
        while self.firing_index < len(self.firing_list) and \
                self.frame_count > self.firing_list[self.firing_index].triger_time:
            self.firing_list[self.firing_index].fire()
            self.firing_index += 1

    @property
    def finished(self):
        return self.firing_index >= len(self.firing_list)


class Stage:
    def __init__(self, phase_list):
        self.phase_list = phase_list
        self.phase_index = 0

    def update(self):
        while self.phase_list < len(self.phase_list) and not self.phase_list[self.phase_index].finished:
            self.phase_list[self.phase_index].update()
