#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is the main module that runs the intercom software on the RaPi in
fullscreen mode."""

import sys
import time

from PySide2.QtCore import QTimer
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                               QMenuBar, QVBoxLayout, QWidget, QAction)

from image_widget import ImageWidget


class IntercomUI(QMainWindow):
    """The main UI."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("main")

        # TODO find out classes and create reasonably pretty css file
        with open("style/stylesheet.css", "r") as f:
            style_sheet = f.read()

        self.setStyleSheet(style_sheet)

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
        clear_widget = QWidget()
        self.setCentralWidget(clear_widget)

        menubar = self.setup_menu()
        self.statusBar()
        self.setMenuBar(menubar)

    def setup_menu(self) -> QMenuBar:
        """Create the menu of the main window"""
        menubar = QMenuBar(self)
        setting_menu = menubar.addMenu("Einstellungen")

        # bell sound selection
        bell_select_action = QAction("Klingelton", self)
        bell_select_action.setStatusTip("Wähle einen Klingelton")
        bell_select_action.triggered.connect(self.on_bell_select)
        setting_menu.addAction(bell_select_action)

        # volume settings
        volume_setting_action = QAction("Lautstärke", self)
        volume_setting_action.setStatusTip("Lautstärke ändern")
        volume_setting_action.triggered.connect(self.on_volume_setting)
        setting_menu.addAction(volume_setting_action)

        return menubar

    def on_bell_select(self):
        """Handle menu action for bell sound selection"""
        print("on_bell_select was triggered")

    def on_volume_setting(self):
        """Handle menu action for volume settings"""
        print("on_volume_setting was triggered")


def main():
    """Create and start the application."""
    app = QApplication(sys.argv)
    main_window = IntercomUI()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
