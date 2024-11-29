from qfluentwidgets import SettingCardGroup


class settingGroupManager:
    def __init__(self):
        self.groups = {}

    def personalizationGroup(self, parent):
        group = SettingCardGroup('Personalization', parent)
        self.groups['personalization'] = group
        return group

    def aboutGroup(self, parent):
        group = SettingCardGroup('About', parent)
        self.groups['about'] = group
        return group

    def getGroup(self, groupName):
        return self.groups.get(groupName)
