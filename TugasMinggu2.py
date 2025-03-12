import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
    QFormLayout, QRadioButton, QComboBox, QGroupBox
)

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(100, 100, 400, 350)
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # 1. Identity Section
        identity_group = QGroupBox("Identitas")
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama  : Amir Hamzah "))
        identity_layout.addWidget(QLabel("Nim   : F1D021027"))
        identity_layout.addWidget(QLabel("Kelas : D"))
        identity_group.setLayout(identity_layout)
        main_layout.addWidget(identity_group)

        # 2. Navigation Section
        nav_group = QGroupBox("Navigation ")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)
        main_layout.addWidget(nav_group)

        # 3. Registration Form Section
        form_group = QGroupBox("User Registration (form layout)")
        form_layout = QFormLayout()

        self.full_name = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()

        self.gender_male = QRadioButton("Male")
        self.gender_female = QRadioButton("Female")

        self.country = QComboBox()
        self.country.addItems(["Select a Country", "USA", "UK", "Indonesia", "Germany"])

        form_layout.addRow("Full Name:", self.full_name)
        form_layout.addRow("Email:", self.email)
        form_layout.addRow("Phone:", self.phone)
        form_layout.addRow("Gender:", self.gender_male)
        form_layout.addRow("", self.gender_female)
        form_layout.addRow("Country:", self.country)

        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)

        # 4. Actions Section
        action_group = QGroupBox("Actions")
        action_layout = QHBoxLayout()
        submit_btn = QPushButton("Submit")
        cancel_btn = QPushButton("Cancel")
        action_layout.addWidget(submit_btn)
        action_layout.addWidget(cancel_btn)
        action_group.setLayout(action_layout)
        main_layout.addWidget(action_group)

        self.setLayout(main_layout)

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())
