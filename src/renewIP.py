import socket
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import paramiko

import sys


class RenewIp(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(524, 360)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-image: url(back.jpg);")

        self.pb = QtWidgets.QPushButton(Dialog)
        self.pb.setGeometry(QtCore.QRect(185, 220, 111, 41))
        self.pb.setObjectName("pb")
        self.pb.setStyleSheet("background: cornflowerBlue; border-style: outset; border-width: 2px; border-radius: "
                              "10px; "
                              "border-color: beige;font: bold 14px; min-width: 8em;padding: 10px;")
        self.pb.clicked.connect(self.button_click)

        self.le = QtWidgets.QLineEdit(Dialog)
        self.le.setGeometry(QtCore.QRect(170, 140, 191, 41))
        self.le.setAlignment(QtCore.Qt.AlignCenter)
        self.le.setObjectName("le")
        self.le.setStyleSheet("background:lightSteelBlue;font: bold 14px;")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Renew Mikrotik"))
        self.pb.setText(_translate("Dialog", "Renew IP"))
        self.le.setPlaceholderText(_translate("Dialog", "Ip Mikrotik"))


    def button_click(self):
        while True:
            global ssh, host, mt_username, mt_password, timeout
            alert = QMessageBox()
            alert.setWindowTitle("Alert")
            alert.setStyleSheet("width: 600px;background: cornflowerBlue;border-style: outset; border-width: 2px; "
                                "border-radius: "
                                "10px; "
                                "border-color: beige;font: bold 14px; min-width: 8em;padding: 10px;")

            shost = self.le.text()
            try:
                socket.inet_aton(shost)
                mt_username = "username"
                mt_password = "password"
                timeout = 5
                host = shost
                ssh = paramiko.SSHClient()

                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                x = "Connecting to " + host
                alert.setText(x)
                alert.exec_()

            except socket.error:
                alert.setText("Check your ip my friend")

                alert.exec_()

            try:
                ssh.connect(host, username=mt_username, password=mt_password, timeout=timeout)
                alert.setText("Succsessfully connected to the host. Executing commands...")
                alert.exec_()

            except paramiko.AuthenticationException:
                alert.setText("Wrong credentials.")
                alert.exec_()

            except:
                alert.setText("Error connecting to the device. Retry Again...")

                alert.exec_()
                break

            mt_command = '/ip dhcp-client renew 0'
            time.sleep(.3)
            ssh.exec_command(mt_command)
            print(mt_command)
            alert.setText(mt_command + '\nExternal commands are executed successfully.\n')
            alert.exec_()
            ssh.get_transport().close()
            ssh.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()

    ui = RenewIp()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())
