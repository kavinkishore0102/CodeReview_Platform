import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Demo UI")
        self.setGeometry(100, 100, 300, 200)

        # Create widgets
        self.label = QLabel("Hello, PySide6!")
        self.button = QPushButton("Click Me")

        # Connect button click to a function
        self.button.clicked.connect(self.on_button_click)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def on_button_click(self):
        self.label.setText("Button clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())
