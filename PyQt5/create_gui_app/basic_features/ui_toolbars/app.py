import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QToolBar,
    QAction,
    QStatusBar,
    QCheckBox,
    QWidget
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("bug.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        # You can enter keyboard shortcuts using key names (e.g. Ctrl+p)
        # Qt.namespace identifiers (e.g. Qt.CTRL + Qt.Key_P)
        # or system agnostic identifiers (e.g. QKeySequence.Print)
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)
    
    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
