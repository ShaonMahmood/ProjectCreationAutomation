#!/usr/bin/env python3

# Filename: new_gui.py

"""PyCalc is a simple calculator built using Python and PyQt5."""

import sys

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit, QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QFormLayout, QHBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

__version__ = '2.0'
__author__ = 'Md Mahmood Bin Habib'



# Create a subclass of QMainWindow to setup the calculator's GUI
class PyProjectUi(QMainWindow):
    """PyProject's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Project Automator')
        self.setFixedSize(800, 600)

        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        # self.generalLayout.addSpacing(30)

        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self._centralWidget.setLayout(self.generalLayout)

        # Create the display and the buttons
        self._createDisplay()
        # self._createButtons()

    # Snip
    def _createDisplay(self):
        """Create the display."""

        # Layout 1(Horizontal Layout)
        # Project Title

        self.project_title_label = QLabel()
        self.project_title_label.setText("A Simple Desktop App For Creating New Python Projects")
        self.project_title_label.setAlignment(Qt.AlignTop)


        # Layout 2(Grid Layout)
        # Github Credentials


        # Layout 3(Grid Layout)
        # Project Name
        layout2 = QFormLayout()
        layout2.addRow('Name:', QLineEdit())
        layout2.addRow('Age:', QLineEdit())
        layout2.addRow('Job:', QLineEdit())
        layout2.addRow('Hobbies:', QLineEdit())
        # self.display.setReadOnly(True)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.project_title_label)
        self.generalLayout.addLayout(layout2)


# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyProjectUi()
    view.show()
    # Execute the project's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()

