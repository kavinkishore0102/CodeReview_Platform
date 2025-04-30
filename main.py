from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QStackedWidget, QFileDialog
)
from PySide6.QtGui import QPalette, QLinearGradient, QColor, QBrush
from PySide6.QtCore import Qt
import sys


class HomePage(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()
        self.switch_page_callback = switch_page_callback
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title = QLabel("Welcome to the Code Review Assistant")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        title.setAlignment(Qt.AlignCenter)

        start_button = QPushButton("Start Review")
        start_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px;
                border-radius: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        start_button.clicked.connect(self.switch_page_callback)

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(start_button)
        layout.addStretch()
        self.setLayout(layout)


class ReviewPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        label = QLabel("This is the Review Page.")
        label.setStyleSheet("font-size: 18px; color: white;")
        label.setAlignment(Qt.AlignCenter)

        upload_btn = QPushButton("Upload Code File")
        upload_btn.setStyleSheet("""
            QPushButton {
                background-color: #64B5F6;
                color: black;
                padding: 10px;
                border-radius: 10px;
            }
        """)
        upload_btn.clicked.connect(self.upload_file)

        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(upload_btn)
        layout.addStretch()
        self.setLayout(layout)

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Code File", "", "C Files (*.c);;Python Files (*.py);;All Files (*)")
        if file_path:
            print("Selected file:", file_path)  # You can later add analysis here


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Code Review Assistant")
        self.setGeometry(300, 200, 600, 400)

        self.stack = QStackedWidget()
        self.home_page = HomePage(self.go_to_review_page)
        self.review_page = ReviewPage()

        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.review_page)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack)
        self.setLayout(main_layout)

        self.set_gradient_background()

    def set_gradient_background(self):
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#0F0F0F"))
        gradient.setColorAt(1.0, QColor("#1E88E5"))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

    def go_to_review_page(self):
        self.stack.setCurrentWidget(self.review_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
