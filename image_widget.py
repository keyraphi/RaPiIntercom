"""A simple widget that holds nothing but an image."""

from PySide2.QtGui import QColor, QImage, QPixmap
from PySide2.QtWidgets import QLabel, QVBoxLayout, QWidget, QSizePolicy


class ImageWidget(QLabel):
    def __init__(self, image_path: str, parent=None):
        super().__init__(parent)
        self.pixmap = QPixmap(image_path)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.setPixmap(self.pixmap)
