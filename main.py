#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is the main module that runs the intercom software on the RaPi in
fullscreen mode."""

from PySide2.QtWidgets import QMainWindow, QApplication
import time
import sys


class IntercomUI(QMainWindow):
    """The main UI"""
    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO do stuff

        # fullscreen
        self.showFullScreen()


def main():
    """Create and start the application"""
    app = QApplication(sys.argv)
    main_window = IntercomUI()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
