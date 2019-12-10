from PyQt5 import QtWidgets
from automation_gui import Ui_MainWindow  # importing our generated file
from core.common import create_project

def show_message(text):
    alert = QtWidgets.QMessageBox()
    alert.setText(text)
    alert.exec_()

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.create_button.clicked.connect(self.on_button_clicked)
        self.ui.create_button.setToolTip("Click Here to Create Project")
        self.ui.password_text.setEchoMode(QtWidgets.QLineEdit.Password)



    def on_button_clicked(self):
        buttonReply = QtWidgets.QMessageBox.question(self,
                                                     'Confirmation',
                                                     "Do you want to create a new project?",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            username = self.ui.username_text.text()
            password = self.ui.password_text.text()
            project_directory = self.ui.project_directory_text.text()
            project_name = self.ui.project_name_text.text()
            venv_name = self.ui.venv_text.text()
            response = create_project(username,password,project_directory,project_name,venv_name)

            if response == 1:
                show_message("project created successfully")
                self.ui.project_directory_text.setText("")
                self.ui.project_name_text.setText("")
                self.ui.venv_text.setText("")
            elif response == 0:
                show_message("wrong username and password")

            else:
                show_message("project with the same name is already created")
                self.ui.project_name_text.setText("")
        else:
            print("Nah")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())

