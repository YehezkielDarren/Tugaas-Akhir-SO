from app.resource.cards.setting import settingCardManager
from app.resource.groups.setting import settingGroupManager


def concatSetting(parent, groups_to_include=None):
    if groups_to_include is None:
        groups_to_include = ['personal', 'about']

    cardManager = settingCardManager()
    groupManager = settingGroupManager()

    group_dict = {}

    if 'personal' in groups_to_include:
        personalGroup = groupManager.personalizationGroup(parent)
        personalGroup.addSettingCard(cardManager.themeCards(personalGroup))
        group_dict['personal'] = personalGroup

    if 'about' in groups_to_include:
        aboutGroup = groupManager.aboutGroup(parent)
        aboutGroup.addSettingCard(cardManager.aboutCard(aboutGroup))
        group_dict['about'] = aboutGroup

    return group_dict
