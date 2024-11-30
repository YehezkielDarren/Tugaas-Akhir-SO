from qfluentwidgets import SettingCardGroup


class preemptiveGroupManager:
    def __init__(self):
        self.groups = {}

    def preemptiveGroup(self, parent):
        group = SettingCardGroup('Shortest Job First', parent)
        self.groups['preemptive'] = group
        return group

    def resultPreemptiveGroup(self, parent):
        group = SettingCardGroup('Result', parent)
        self.groups['resultPreemptive'] = group
        return group

    def getGroup(self, groupName):
        return self.groups.get(groupName)
