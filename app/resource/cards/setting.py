from qfluentwidgets import (
    OptionsSettingCard, PrimaryPushSettingCard, FluentIcon as FIF)

from app.module.config import cfg, YEAR, AUTHOR, VERSION


class settingCardManager:
    def __init__(self):
        self.cards = {}

    def themeCards(self, parent):
        card = OptionsSettingCard(
            cfg.themeMode,
            FIF.BRUSH,
            'Apps Theme',
            'Change the appearance of your application',
            texts=['Light', 'Dark', 'Use system Setting'],
            parent=parent
        )

        self.cards['theme'] = card
        return card

    def aboutCard(self, parent):
        card = PrimaryPushSettingCard(
            'Check update',
            FIF.INFO,
            'About',
            f'© Copyright {YEAR}, {AUTHOR}. Version {VERSION}',
            parent
        )
        self.cards['about'] = card
        return card

    def getCard(self, cardName):
        return self.cards.get(cardName)
