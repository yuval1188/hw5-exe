from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QFrame,
                               QVBoxLayout)
from PySide6.QtCore import Qt


class AboutWindow(QWidget):

    def __init__(self, github_url):
        super().__init__()
        self.github_url = github_url
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("אודות")
        self.setFixedWidth(440)
        self.setObjectName("aboutWindow")

        self.image_label = QLabel()
        self.image_label.setFixedSize(150, 150)
        self.image_label.setScaledContents(True)
        image = QPixmap("11.jpeg")
        self.image_label.setPixmap(image)

        photo_frame = QFrame()
        photo_frame.setObjectName("photoFrame")
        photo_frame.setFixedSize(176, 176)
        photo_layout = QVBoxLayout()
        photo_layout.setContentsMargins(10, 10, 10, 10)
        photo_layout.addWidget(self.image_label)
        photo_frame.setLayout(photo_layout)

        self.label_name = QLabel("יובל נסים")
        self.label_name.setObjectName("name")
        self.label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_project = QLabel("Heat Transfer  ·  Version 1.0")
        self.label_project.setObjectName("projectName")
        self.label_project.setAlignment(Qt.AlignmentFlag.AlignCenter)

        about_title = QLabel("♡ על הפרויקט")
        about_title.setObjectName("cardTitle")

        about_text = QLabel("הסימולציה מראה איך חום עובר בין שני גופים "
                            "בטמפרטורות שונות, עד שהם מגיעים לאותה טמפרטורה.\n\n"
                            "א. בוחרים טמפרטורה לכל גוף בעזרת הסליידר\n"
                            "ב. מזינים מסה וקיבול חום לכל גוף\n"
                            "ג. לוחצים Start וצופים בשינוי\n"
                            "ד. לוחצים Graphs כדי לראות את הגרף")
        about_text.setObjectName("cardText")
        about_text.setWordWrap(True)

        about_card = QFrame()
        about_card.setObjectName("card")
        about_layout = QVBoxLayout()
        about_layout.addWidget(about_title)
        about_layout.addWidget(about_text)
        about_card.setLayout(about_layout)

        formulas_title = QLabel("♡ הנוסחאות")
        formulas_title.setObjectName("cardTitle")

        formulas_text = QLabel("I = σ · (T₂ − T₁)\n"
                               "ΔQ = I · Δt\n"
                               "ΔT = ΔQ / (m · c)\n"
                               "New T = T + ΔT")
        formulas_text.setObjectName("formulas")
        formulas_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        formulas_card = QFrame()
        formulas_card.setObjectName("card")
        formulas_layout = QVBoxLayout()
        formulas_layout.addWidget(formulas_title)
        formulas_layout.addWidget(formulas_text)
        formulas_card.setLayout(formulas_layout)

        link_style = 'style="color:#D6336C; text-decoration:none; font-weight:600;"'

        self.label_email = QLabel("✉  yuval6891@gmail.com")
        self.label_email.setObjectName("contact")
        self.label_email.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_linkedin = QLabel('<a href="https://www.linkedin.com/in/yuval-nissim-832457397/" '
                                     + link_style + '>העמוד שלי ב-LinkedIn</a>')
        self.label_linkedin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_linkedin.setOpenExternalLinks(True)

        self.label_github = QLabel('<a href="' + self.github_url + '" '
                                   + link_style + '>לצפייה בקוד הפרויקט ב-GitHub ←</a>')
        self.label_github.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_github.setOpenExternalLinks(True)

        self.close_button = QPushButton("סגירה")
        self.close_button.setObjectName("closeButton")
        self.close_button.clicked.connect(self.close)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 28, 30, 24)
        main_layout.setSpacing(10)
        main_layout.addWidget(photo_frame, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addSpacing(4)
        main_layout.addWidget(self.label_name)
        main_layout.addWidget(self.label_project)
        main_layout.addSpacing(6)
        main_layout.addWidget(about_card)
        main_layout.addWidget(formulas_card)
        main_layout.addSpacing(6)
        main_layout.addWidget(self.label_email)
        main_layout.addWidget(self.label_linkedin)
        main_layout.addWidget(self.label_github)
        main_layout.addSpacing(8)
        main_layout.addWidget(self.close_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(main_layout)

        self.setStyleSheet("""
            QWidget {
                font-family: "Segoe UI";
                font-size: 10pt;
                color: #6B2D4A;
                background: transparent;
            }
            #aboutWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #FFD6E7, stop:1 #FFF4F8);
            }
            #photoFrame {
                background-color: #FFFFFF;
                border: 3px solid #F7A8C4;
                border-radius: 20px;
            }
            #name {
                font-size: 20pt;
                font-weight: 700;
                color: #C2185B;
            }
            #projectName {
                font-size: 10pt;
                color: #B5838D;
                letter-spacing: 1px;
            }
            #card {
                background-color: #FFFFFF;
                border: 1px solid #F8C8DC;
                border-radius: 16px;
            }
            #cardTitle {
                font-size: 11pt;
                font-weight: 700;
                color: #D6336C;
            }
            #cardText {
                color: #7A4A5E;
            }
            #formulas {
                font-family: "Cambria Math";
                font-size: 11pt;
                color: #6B2D4A;
                background-color: #FFF0F6;
                border-radius: 10px;
                padding: 8px;
            }
            #contact {
                color: #7A4A5E;
            }
            #closeButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #F78FB3, stop:1 #E75480);
                color: #FFFFFF;
                border: none;
                border-radius: 16px;
                padding: 8px 40px;
                font-size: 11pt;
                font-weight: 700;
            }
            #closeButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #F06A9B, stop:1 #D6336C);
            }
        """)


if __name__ == "__main__":
    app = QApplication([])
    window = AboutWindow("https://github.com/yuval1188/hw-exe2")
    window.show()
    app.exec()