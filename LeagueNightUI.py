from PySide2.QtWidgets import QWidget, QVBoxLayout
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


class PlayerPoolWidget(QWidget):
    def __init__(self, parent, summoner=None):
        super().__init__(parent)


        #layout = QVBoxLayout()
        #layout.addWidget(PlayerPoolWidget)
        #self.setLayout(layout)


class PlayerTeamWidget(QWidget):
    def __init__(self, parent, summoner=None):
        file = QFile("UI/ui_playerteamwidget.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        PlayerTeamWidget = loader.load(file, self)
        file.close()
