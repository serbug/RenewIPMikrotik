import socket
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox



import paramiko

import sys

from Ui_Dialog import Ui_Dialog



class RenewIP(Ui_Dialog):
    def __init__(self):
        super(RenewIP).__init__()


    def start(self, Dialog):

        super(RenewIP, self).start(Dialog)

        self.pb.clicked.connect(self.button_click)
    # while True:
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
                 mt_username = "admin"
                 mt_password = "Windows0@"
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
                break
             try:
                ssh.connect(host, username=mt_username, password=mt_password, timeout=timeout)
                alert.setText("Succsessfully connected to the host. Executing commands...")
                alert.exec_()


             except paramiko.AuthenticationException:
                alert.setText("Wrong credentials.")
                alert.exec_()
                break

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
             break
       # break

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()

    ui = RenewIP()
    ui.start(window)

    window.show()

    sys.exit(app.exec_())
