from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic

from PyQt5.QtGui import QPixmap
import os                                                          
import sys
from stegano import lsb_1, extract_message_from_image

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		uic.loadUi(os.path.join(os.path.split(__file__)[0], "watermark_front.ui"), self)

		self.browse_button.clicked.connect(self.browse_image)
		self.watermark_button.clicked.connect(self.watermark_image)
		self.extract_message_button.clicked.connect(self.show_message)


	def browse_image(self):
		self.image_path, _ = QFileDialog.getOpenFileName(self, 'Select image', '', 'All Files (*)')
		pixmap = QPixmap(self.image_path)
		self.image_label.setPixmap(pixmap)
		if os.path.exists(self.image_path):
			self.watermark_button.setEnabled(True)
			self.extract_message_button.setEnabled(True)


	def watermark_image(self):
		message = self.message_text_edit.toPlainText()
		lsb_1(self.image_path, message)

	def show_message(self):
		message = extract_message_from_image(self.image_path)
		self.message_text_edit.setText(message)


