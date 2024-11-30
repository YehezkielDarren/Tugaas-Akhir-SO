from app.resource.cards.preemptive import preemptiveCardManager
from app.resource.groups.preemptive import preemptiveGroupManager


def preemptiveSetting(parent, groups_to_include=None):
    if groups_to_include is None:
        groups_to_include = ['preemptive', 'resultPreemptive']

    cardManager = preemptiveCardManager()
    groupManager = preemptiveGroupManager()

    group_dict = {}

    if 'preemptive' in groups_to_include:
        preemptiveGroup = groupManager.preemptiveGroup(parent)
        preemptiveGroup.addSettingCard(cardManager.preemptiveCards(
            preemptiveGroup))
        group_dict['preemptive'] = preemptiveGroup

    if 'resultPreemptive' in groups_to_include:
        resultPreemptiveGroup = groupManager.resultPreemptiveGroup(parent)
        resultPreemptiveGroup.addSettingCard(cardManager.resultPreemptiveCards(
            resultPreemptiveGroup))
        group_dict['resultPreemptive'] = resultPreemptiveGroup

    return group_dict
