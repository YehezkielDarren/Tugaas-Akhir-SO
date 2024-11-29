# TODO: Gantt chart module
class GanttChart:
    def __init__(self, data):
        self.data = data

    def render(self):
        return f'Gantt chart with data: {self.data}'