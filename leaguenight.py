import sys
import json
import re
import time
import configparser
import requests

from PySide2.QtWidgets import QApplication, QMessageBox, QListWidgetItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QStandardItemModel
from riot import *


def decode_summonerdto_json(dct):
    return SummonerDTO(
        dct['profileIconId'],
        dct['name'],
        dct['puuid'],
        dct['summonerLevel'],
        dct['revisionDate'],
        dct['id'],
        dct['accountId'])


class LeagueNight:

    def __init__(self):
        super().__init__()

        config = configparser.ConfigParser()
        config.read('config.ini')

        self.api_key = config['DEFAULT']['RIOT_API_KEY']

        self.initUI()

    def initUI(self):
        app = QApplication(sys.argv)

        ui_file = QFile("UI/ui_mainwindow_v1.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        self.player_pool_model = (1, 5)

        ## self.window.playerPoolList() TODO: Start here

        self.window.usernameEdit.textEdited.connect(self.enable_add_player)
        self.window.usernameEdit.returnPressed.connect(self.add_player)

        self.window.addPlayerButton.clicked.connect(self.add_player)

        self.window.putTeam1Button.clicked.connect(self.add_player_team1)
        self.window.putTeam2Button.clicked.connect(self.add_player_team2)

        # self.window.removePlayerTeam1Button.clicked.connect(self.remove_player_team1)
        # self.window.removePlayerTeam2Button.clicked.connect(self.remove_player_team2)

        # Other Stuff
        self.start_time = time.time()

        self.window.show()
        sys.exit(app.exec_())

    def enable_add_player(self):
        if (self.window.usernameEdit.text() is not None and self.window.usernameEdit.text() != ""):
            self.window.addPlayerButton.setEnabled(True)
        else:
            QMessageBox.warning(
                self.window, "Error", "Enter Summoner Name", QMessageBox.Ok)

    def create_player(self, parent):
        loader = QUiLoader()

        file = QFile("UI/ui_playerpoolwidget.ui")
        file.open(QFile.ReadOnly)

        return loader.load(file, parent)

    def add_player(self):

        summoner = self.get_summoner(self.window.usernameEdit.text())

        if summoner is None:
            QMessageBox.warning(self.window, "League Night", "Invalid Summoner Name", QMessageBox.Ok, QMessageBox.NoButton)
            return

        item = QStandardItemModel()
        item = QListWidgetItem(self.window.playerPoolList)

        self.playerWidget = self.create_player(self.window.playerPoolList)
        self.playerWidget.playerLabel.setText(summoner.name)
        self.playerWidget.pointLabel.setText(str(summoner.points))

        item.setSizeHint(self.playerWidget.sizeHint())

        self.window.playerPoolList.addItem(item)
        self.window.playerPoolList.setItemWidget(item, self.playerWidget)

        self.window.usernameEdit.setText("")
        self.window.addPlayerButton.setEnabled(False)

    def remove_player_pool_widget(self):
        self.window.playerPoolList.removeItemWidget(self)

    def add_player_to_team(self, parent):
        file = QFile("UI/ui_playerteamwidget.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        PlayerTeamWidget = loader.load(file, parent)
        file.close()

        return PlayerTeamWidget

    # TODO: START HERE
    def add_player_team1(self):
        poolList = self.window.playerPoolList.count()
        item = self.window.playerPoolList.item(0)
        players = self.window.playerPoolList.selectedItems()
        for index in players:
            player = self.window.team1List.itemWidget(index)
            item = QListWidgetItem(self.window.team1List)

            team1Player = self.add_player_to_team(self.window.team1List)
            team1Player.playerLabel.setText(player.summoner.name)

            item.setSizeHint(team1Player.sizeHint())
            self.window.team1List.addItem(item)
            self.window.team1List.setItemWidget(item, team1Player)

    def add_player_team2(self):
        for player in self.window.playerPoolList.selectedItems():
            item = QListWidgetItem(self.window.team2List)

            team2Player = self.add_player_to_team(self.window.team2List)
            team2Player.playerLabel.setText(player.summoner.name)

            item.setSizeHint(team2Player.sizeHint())
            self.window.team2List.addItem(item)
            self.window.team2List.setItemWidget(item, team2Player)

    def get_summoner(self, username: str):
        summoner_regex = re.compile('^[0-9\w+ _\.]+$', re.UNICODE)
        summoner_name = username
        summoner = None

        url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name
        payload = {'api_key': self.api_key}

        if not summoner_regex.match(summoner_name) and len(summoner_name) <= 16:
            return None
        else:
            summoner_name_request = requests.get(url, params=payload)

            if summoner_name_request.status_code == 200:
                summoner = json.loads(
                    summoner_name_request.text, object_hook=decode_summonerdto_json)
                return summoner
            else:
                return None


if __name__ == '__main__':
    LeagueNight()
