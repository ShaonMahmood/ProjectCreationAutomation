# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'automation_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.github_heading = QtWidgets.QLabel(self.centralwidget)
        self.github_heading.setGeometry(QtCore.QRect(320, 80, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.github_heading.setFont(font)
        self.github_heading.setObjectName("github_heading")
        self.usertoken_label = QtWidgets.QLabel(self.centralwidget)
        self.usertoken_label.setGeometry(QtCore.QRect(210, 200, 101, 41))
        self.usertoken_label.setObjectName("usertoken_label")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(210, 140, 101, 41))
        self.username_label.setObjectName("username_label")
        self.usertoken_text = QtWidgets.QLineEdit(self.centralwidget)
        self.usertoken_text.setGeometry(QtCore.QRect(341, 200, 350, 41))
        self.usertoken_text.setObjectName("usertoken_text")
        self.username_text = QtWidgets.QLineEdit(self.centralwidget)
        self.username_text.setGeometry(QtCore.QRect(341, 140, 201, 41))
        self.username_text.setObjectName("username_text")
        self.project_heading = QtWidgets.QLabel(self.centralwidget)
        self.project_heading.setGeometry(QtCore.QRect(320, 270, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.project_heading.setFont(font)
        self.project_heading.setObjectName("project_heading")
        self.project_directory_label = QtWidgets.QLabel(self.centralwidget)
        self.project_directory_label.setGeometry(QtCore.QRect(210, 340, 120, 20))
        self.project_directory_label.setObjectName("project_directory_label")
        self.project_directory_text = QtWidgets.QLineEdit(self.centralwidget)
        self.project_directory_text.setGeometry(QtCore.QRect(341, 330, 201, 41))
        self.project_directory_text.setText("")
        self.project_directory_text.setObjectName("project_directory_text")
        self.project_name_label = QtWidgets.QLabel(self.centralwidget)
        self.project_name_label.setGeometry(QtCore.QRect(210, 400, 101, 20))
        self.project_name_label.setObjectName("project_name_label")
        self.project_name_text = QtWidgets.QLineEdit(self.centralwidget)
        self.project_name_text.setGeometry(QtCore.QRect(341, 390, 201, 41))
        self.project_name_text.setObjectName("project_name_text")
        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setGeometry(QtCore.QRect(512, 510, 161, 51))
        self.create_button.setObjectName("create_button")
        self.app_heading = QtWidgets.QLabel(self.centralwidget)
        self.app_heading.setGeometry(QtCore.QRect(100, 20, 650, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.app_heading.setFont(font)
        self.app_heading.setObjectName("app_heading")
        self.venv_label = QtWidgets.QLabel(self.centralwidget)
        self.venv_label.setGeometry(QtCore.QRect(210, 460, 120, 16))
        self.venv_label.setObjectName("venv_label")
        self.venv_text = QtWidgets.QLineEdit(self.centralwidget)
        self.venv_text.setGeometry(QtCore.QRect(341, 450, 201, 41))
        self.venv_text.setObjectName("venv_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project Creation Window"))
        self.github_heading.setText(_translate("MainWindow", "Github Credentials"))
        self.usertoken_label.setText(_translate("MainWindow", "Github Token"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.project_heading.setText(_translate("MainWindow", "Project Settings"))
        self.project_directory_label.setText(_translate("MainWindow", "Project Directory"))
        self.project_name_label.setText(_translate("MainWindow", "Project Name"))
        self.create_button.setText(_translate("MainWindow", "Create New Project"))
        self.app_heading.setText(_translate("MainWindow", "A Simple Desktop App For Creating New Python Projects"))
        self.venv_label.setText(_translate("MainWindow", "Virtual Env Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
