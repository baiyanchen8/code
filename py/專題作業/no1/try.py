import cv2
print("OpenCV version:", cv2.__version__)

from PyQt5.QtWidgets import QApplication, QLabel
app = QApplication([])
label = QLabel('Hello, Qt!')
label.show()
app.exec_()
