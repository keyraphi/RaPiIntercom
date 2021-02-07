#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is the main module that runs the intercom software on the RaPi in
fullscreen mode."""

import sys
import time

from PySide2.QtCore import QTimer
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout

from image_widget import ImageWidget


class IntercomUI(QMainWindow):
    """The main UI."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.title = "Load image in PySide2"
        self.setWindowTitle(self.title)

        self.setStyleSheet("background-color:gray")
        self.show_start_screen(2000)

        # fullscreen
        self.showFullScreen()

    def show_start_screen(self, time_ms: int) -> None:
        """Show start-splashscreen for the given time. The regular UI is shown
        afterwards.

        Args:
            time_ms:
                Number of miliseconds to actually show the splash-screen
        """
        # TODO show start screen
        print("Trace: Start-screen start", time.time())
        # label = QLabel(self)
        # pixmap = QPixmap('images/splash_screen.png')
        # label.setPixmap(pixmap)
        image_widget = ImageWidget("images/splash_screen.png")
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        h_layout.addWidget(image_widget)
        v_layout.addLayout(h_layout)
        widget = QWidget()
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)

        timer = QTimer(self)
        timer.singleShot(time_ms, self.on_start_screen_end)

    def on_start_screen_end(self) -> None:
        print("Trace: Start-screen end", time.time())
        clear_widget = QWidget()
        self.setCentralWidget(clear_widget)
        # TODO construct actual Ui


def main():
    """Create and start the application."""
    app = QApplication(sys.argv)
    main_window = IntercomUI()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
