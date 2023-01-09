# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 21:22:35 2023

@author: Supreeth
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy, QStyleFactory
import sys

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        self.setWindowTitle("Clinical Diagonizer")
        self.setWindowState(self.windowState()|QtCore.Qt.WindowMaximized)
# =============================================================================
#         self.MAIN_VBOX = QtWidgets.QVBoxLayout()
#         self.MAIN_VBOX.setContentsMargins(0, 0, 0, 0)
#         self.MAIN_VBOX.setSpacing(0)
#         self.setLayout(self.MAIN_VBOX)
# =============================================================================
        self.setContentsMargins(0, 0, 0, 0)
        self.show()
    
    
if __name__ == "__main__":
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    app.setStyle(QStyleFactory.create('Fusion'))
    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass