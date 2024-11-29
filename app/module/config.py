import os
from qfluentwidgets import (qconfig, QConfig)

YEAR, AUTHOR, VERSION = 2024, 'Grup Gacor', '0.0.1'
config_path = os.path.join(os.getcwd(), 'config', 'config.json')
cfg = QConfig()
qconfig.load(config_path, cfg)
