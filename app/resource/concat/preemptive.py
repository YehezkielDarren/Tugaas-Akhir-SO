from app.resource.cards.preemptive import preemptiveCardManager
from app.resource.groups.preemptive import preemptiveGroupManager


def preemptiveSetting(parent, groups_to_include=None):
    if groups_to_include is None:
        groups_to_include = ['preemptive']

    cardManager = preemptiveCardManager()
    groupManager = preemptiveGroupManager()

    group_dict = {}

    if 'preemptive' in groups_to_include:
        preemptiveGroup = groupManager.preemptiveGroup(parent)
        preemptiveGroup.addSettingCard(cardManager.preemptiveCards(
            preemptiveGroup))
        group_dict['preemptive'] = preemptiveGroup

    return group_dict
