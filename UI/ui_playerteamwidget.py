# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\ui_playerteamwidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlayerTeamWidget(object):
    def setupUi(self, PlayerTeamWidget):
        PlayerTeamWidget.setObjectName("PlayerTeamWidget")
        PlayerTeamWidget.resize(394, 35)
        self.horizontalLayout = QtWidgets.QHBoxLayout(PlayerTeamWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playerLabel = QtWidgets.QLabel(PlayerTeamWidget)
        self.playerLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.playerLabel.setObjectName("playerLabel")
        self.horizontalLayout.addWidget(self.playerLabel)
        self.checkFirstGame = QtWidgets.QCheckBox(PlayerTeamWidget)
        self.checkFirstGame.setObjectName("checkFirstGame")
        self.horizontalLayout.addWidget(self.checkFirstGame)
        self.checkSupport = QtWidgets.QCheckBox(PlayerTeamWidget)
        self.checkSupport.setObjectName("checkSupport")
        self.horizontalLayout.addWidget(self.checkSupport)
        self.checkHonor = QtWidgets.QCheckBox(PlayerTeamWidget)
        self.checkHonor.setObjectName("checkHonor")
        self.horizontalLayout.addWidget(self.checkHonor)

        self.retranslateUi(PlayerTeamWidget)
        QtCore.QMetaObject.connectSlotsByName(PlayerTeamWidget)

    def retranslateUi(self, PlayerTeamWidget):
        _translate = QtCore.QCoreApplication.translate
        PlayerTeamWidget.setWindowTitle(_translate("PlayerTeamWidget", "Form"))
        self.playerLabel.setText(_translate("PlayerTeamWidget", "TextLabel"))
        self.checkFirstGame.setText(_translate("PlayerTeamWidget", "First Game"))
        self.checkSupport.setText(_translate("PlayerTeamWidget", "Support"))
        self.checkHonor.setText(_translate("PlayerTeamWidget", "Honorable Opponent"))

