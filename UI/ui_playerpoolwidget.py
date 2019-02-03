# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\ui_playerpoolwidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlayerPoolWidget(object):
    def setupUi(self, PlayerPoolWidget):
        PlayerPoolWidget.setObjectName("PlayerPoolWidget")
        PlayerPoolWidget.resize(171, 31)
        self.horizontalLayout = QtWidgets.QHBoxLayout(PlayerPoolWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playerLabel = QtWidgets.QLabel(PlayerPoolWidget)
        self.playerLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.playerLabel.setObjectName("playerLabel")
        self.horizontalLayout.addWidget(self.playerLabel)
        self.pointLabel = QtWidgets.QLabel(PlayerPoolWidget)
        self.pointLabel.setObjectName("pointLabel")
        self.horizontalLayout.addWidget(self.pointLabel)

        self.retranslateUi(PlayerPoolWidget)
        QtCore.QMetaObject.connectSlotsByName(PlayerPoolWidget)

    def retranslateUi(self, PlayerPoolWidget):
        _translate = QtCore.QCoreApplication.translate
        PlayerPoolWidget.setWindowTitle(_translate("PlayerPoolWidget", "Form"))
        self.playerLabel.setText(_translate("PlayerPoolWidget", "TextLabel"))
        self.pointLabel.setText(_translate("PlayerPoolWidget", "TextLabel"))

