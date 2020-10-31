import os


import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon




class Ui_Dialog(object):

    def start(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(524, 360)

        Dialog.setWindowTitle("Renew IP")

        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-image: url(main/resources/image/back.jpg);")
        Dialog.setWindowIcon(QIcon('main/resources/image/iconapp.png'))
        # Dialog.setWindowFlags(Qt.FramelessWindowHint)

        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(169, 40, 191, 41))

        self.graphicsView.setStyleSheet("border-image: url(main/resources/image/logo-bianco-azzurro.png)")
        self.graphicsView.setObjectName("graphicsView")
        self.pb = QtWidgets.QPushButton(Dialog)
        self.pb.setGeometry(QtCore.QRect(185, 220, 111, 41))
        self.pb.setObjectName("pb")
        self.pb.setStyleSheet("background: cornflowerBlue; border-style: outset; border-width: 2px; border-radius: "
                              "10px; "
                              "border-color: beige;font: bold 14px; min-width: 8em;padding: 10px;")

        self.le = QtWidgets.QLineEdit(Dialog)
        self.le.setGeometry(QtCore.QRect(170, 140, 191, 41))
        self.le.setAlignment(QtCore.Qt.AlignCenter)
        self.le.setObjectName("le")
        self.le.setStyleSheet("background:lightSteelBlue;font: bold 14px;")

        # self.lb = QtWidgets.QLabel(Dialog)
        # self.lb.setGeometry(QtCore.QRect(185, 280, 111, 41))
        # self.lb.setObjectName("lb")
        # self.lb.setStyleSheet("color: red;")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        self.pb.setText(_translate("Dialog", "Renew IP"))
        self.le.setPlaceholderText(_translate("Dialog", "Ip Mikrotik"))
        # self.lb.setText(_translate("Dialog", "HELLO"))



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = QtWidgets.QMainWindow()

    ui = Ui_Dialog()
    ui.start(window)

    window.show()
    sys.exit(app.exec_())
