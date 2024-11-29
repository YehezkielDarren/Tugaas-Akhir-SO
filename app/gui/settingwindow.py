from app.gui.base.interface import BaseInterface
from app.resource.concat.setting import concatSetting


class SettingInterface(BaseInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent, objectName='settingWindow',
                         layoutType='expand', layoutFunction=self.__initLayout)

    def __initLayout(self):
        groups = concatSetting(self.scrollWidget)

        self.layout.setSpacing(28)
        self.layout.setContentsMargins(60, 10, 60, 0)

        for group in groups.values():
            self.layout.addWidget(group)
