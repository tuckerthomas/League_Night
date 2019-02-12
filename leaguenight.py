import sys
import json
import re
import time
import configparser
import requests

from PySide2.QtWidgets import QApplication, QMessageBox, QListWidgetItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from riot import *


def decode_summoner_dto_json(dct):
    return SummonerDTO(
        dct['profileIconId'],
        dct['name'],
        dct['puuid'],
        dct['summonerLevel'],
        dct['revisionDate'],
        dct['id'],
        dct['accountId'])


class LeagueNight:

    # before_main() but not actually main() ¯\_(ツ)_/¯
    def __init__(self):
        super().__init__()

        config = configparser.ConfigParser()
        config.read('config.ini')

        self.api_key = config['DEFAULT']['RIOT_API_KEY']

        self.initUI()

    # main()
    def initUI(self):
        app = QApplication(sys.argv)

        ui_file = QFile("UI/ui_mainwindow.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        self.window.usernameEdit.textEdited.connect(self.enable_add_player)
        self.window.usernameEdit.returnPressed.connect(self.add_player)

        self.window.addPlayerButton.clicked.connect(self.add_player)

        self.window.putTeam1Button.clicked.connect(self.add_player_team1)
        self.window.putTeam2Button.clicked.connect(self.add_player_team2)

        self.window.removePlayerTeam1Button.clicked.connect(self.remove_player_team1)
        self.window.removePlayerTeam2Button.clicked.connect(self.remove_player_team2)

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

    # Creates player widget for player pool list
    def create_player(self, parent, summoner):
        loader = QUiLoader()

        file = QFile("UI/ui_playerpoolwidget.ui")
        file.open(QFile.ReadOnly)

        new_player = loader.load(file, parent)
        file.close()

        # Set the QWidget's summoner
        new_player.summoner = summoner

        return new_player

    # Adds a new player to the player pool list
    def add_player(self):
        summoner = self.get_summoner(self.window.usernameEdit.text())

        if summoner is None:
            QMessageBox.warning(self.window, "League Night", "Invalid Summoner Name", QMessageBox.Ok, QMessageBox.NoButton)
            return

        item = QListWidgetItem(self.window.playerPoolList)

        playerWidget = self.create_player(self.window.playerPoolList, summoner)
        playerWidget.playerLabel.setText(summoner.name)
        playerWidget.pointLabel.setText(str(summoner.points))

        item.setSizeHint(playerWidget.sizeHint())

        self.window.playerPoolList.addItem(item)
        self.window.playerPoolList.setItemWidget(item, playerWidget)

        self.window.usernameEdit.setText("")
        self.window.addPlayerButton.setEnabled(False)

    # Creates player widget for team lists
    def add_player_to_team(self, parent, summoner):
        file = QFile("UI/ui_playerteamwidget.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()

        PlayerTeamWidget = loader.load(file, parent)
        PlayerTeamWidget.summoner = summoner
        file.close()

        return PlayerTeamWidget

    def check_player_exists(self, list, summoner):
        for i in range(list.count()):
            player_widget = list.itemWidget(list.item(i))

            if player_widget.summoner.name == summoner.name:
                return True

        return False

    # Adds a player from the Player Pool to the Team 1 List
    def add_player_team1(self):
        team1List = self.window.team1List
        playerPoolList = self.window.playerPoolList

        players = playerPoolList.selectedItems()

        for index in players:
            player = playerPoolList.itemWidget(index)

            if self.check_player_exists(self.window.team2List, player.summoner):
                QMessageBox.warning(self.window, "League Night", "Player is already on the other Team", QMessageBox.Ok,
                                    QMessageBox.NoButton)
            elif self.check_player_exists(self.window.team1List, player.summoner):
                QMessageBox.warning(self.window, "League Night", "Player is already on this Team", QMessageBox.Ok,
                                    QMessageBox.NoButton)
            else:
                item = QListWidgetItem(team1List)

                team1Player = self.add_player_to_team(team1List, player.summoner)
                team1Player.playerLabel.setText(player.summoner.name)

                item.setSizeHint(team1Player.sizeHint())
                team1List.addItem(item)
                team1List.setItemWidget(item, team1Player)

    # Adds a player from the Player Pool to the Team 2 List
    def add_player_team2(self):
        team2List = self.window.team2List
        playerPoolList = self.window.playerPoolList

        players = playerPoolList.selectedItems()

        for index in players:
            player = playerPoolList.itemWidget(index)

            if self.check_player_exists(self.window.team1List, player.summoner):
                QMessageBox.warning(self.window, "League Night", "Player is already on the other Team", QMessageBox.Ok,
                                    QMessageBox.NoButton)
            elif self.check_player_exists(self.window.team2List, player.summoner):
                QMessageBox.warning(self.window, "League Night", "Player is already on this Team", QMessageBox.Ok,
                                    QMessageBox.NoButton)
            else:
                item = QListWidgetItem(team2List)

                team2Player = self.add_player_to_team(team2List, player.summoner)
                team2Player.playerLabel.setText(player.summoner.name)

                item.setSizeHint(team2Player.sizeHint())
                team2List.addItem(item)
                team2List.setItemWidget(item, team2Player)

    # Removes a player from the Team 1 List
    def remove_player_team1(self):
        team1List = self.window.team1List

        for item in team1List.selectedItems():
            team1List.takeItem(team1List.row(item))

    # Removes a player from the Team 2 List
    def remove_player_team2(self):
        team2List = self.window.team2List

        for item in team2List.selectedItems():
            team2List.takeItem(team2List.row(item))

    def get_summoner(self, username: str):
        summoner_regex = re.compile('^[0-9\w+ _\.]+$', re.UNICODE)
        summoner_name = username

        url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name
        payload = {'api_key': self.api_key}

        if not summoner_regex.match(summoner_name) and len(summoner_name) <= 16:
            return None
        else:
            summoner_name_request = requests.get(url, params=payload)

            if summoner_name_request.status_code == 200:
                summoner = json.loads(
                    summoner_name_request.text, object_hook=decode_summoner_dto_json)
                return summoner
            else:
                return None


if __name__ == '__main__':
    LeagueNight()
