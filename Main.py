import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QSlider,
                             QDoubleSpinBox, QFrame, QHBoxLayout, QVBoxLayout, QGridLayout)
from PySide6.QtCore import Qt
from AboutWindow import AboutWindow
from GraphWindow import GraphWindow

class HeatTransfer(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Heat Transfer")
        self.resize(820, 560)

        title = QLabel("Heat Transfer")
        title.setObjectName("title")
        subtitle = QLabel("Simulation of heat flow between two bodies")
        subtitle.setObjectName("subtitle")

        title_layout = QVBoxLayout()
        title_layout.addWidget(title)
        title_layout.addWidget(subtitle)

        self.about_button = QPushButton("About")
        self.about_button.setObjectName("aboutButton")

        header_layout = QHBoxLayout()
        header_layout.addLayout(title_layout)
        header_layout.addStretch()
        header_layout.addWidget(self.about_button)

        self.slider1 = QSlider(Qt.Orientation.Vertical)
        self.slider1.setObjectName("hotSlider")
        self.slider1.setRange(0, 500)
        self.slider1.setValue(200)

        self.body1 = QFrame()
        self.body1.setObjectName("hotBody")
        self.body1.setFixedSize(130, 170)

        body1_layout = QHBoxLayout()
        body1_layout.addWidget(self.slider1)
        body1_layout.addWidget(self.body1)

        self.body2 = QFrame()
        self.body2.setObjectName("coldBody")
        self.body2.setFixedSize(130, 170)

        self.slider2 = QSlider(Qt.Orientation.Vertical)
        self.slider2.setObjectName("coldSlider")
        self.slider2.setRange(0, 500)
        self.slider2.setValue(0)

        body2_layout = QHBoxLayout()
        body2_layout.addWidget(self.body2)
        body2_layout.addWidget(self.slider2)

        conductivity_label = QLabel("Conductivity")
        conductivity_label.setObjectName("fieldTitle")
        conductivity_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.conductivity_box = QDoubleSpinBox()
        self.conductivity_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.conductivity_box.setRange(0.01, 100)
        self.conductivity_box.setValue(1.00)
        self.conductivity_box.setSuffix(" J/s°C")

        self.bridge = QFrame()
        self.bridge.setObjectName("bridge")
        self.bridge.setFixedHeight(22)

        middle_layout = QVBoxLayout()
        middle_layout.addStretch()
        middle_layout.addWidget(conductivity_label)
        middle_layout.addWidget(self.conductivity_box)
        middle_layout.addSpacing(10)
        middle_layout.addWidget(self.bridge)
        middle_layout.addStretch()

        top_layout = QHBoxLayout()
        top_layout.addLayout(body1_layout)
        top_layout.addLayout(middle_layout)
        top_layout.addLayout(body2_layout)

        self.temp1_box = QDoubleSpinBox()
        self.temp1_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp1_box.setRange(0, 500)
        self.temp1_box.setValue(200)
        self.temp1_box.setSuffix(" °C")
        self.temp1_box.setReadOnly(True)

        self.mass1_box = QDoubleSpinBox()
        self.mass1_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mass1_box.setRange(0.01, 1000)
        self.mass1_box.setValue(10)
        self.mass1_box.setSuffix(" kg")

        self.cap1_box = QDoubleSpinBox()
        self.cap1_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cap1_box.setRange(0.01, 10000)
        self.cap1_box.setValue(0.4)
        self.cap1_box.setSuffix(" J/kg°C")

        data1_layout = QGridLayout()
        data1_layout.addWidget(QLabel("Temp."), 0, 0)
        data1_layout.addWidget(self.temp1_box, 0, 1)
        data1_layout.addWidget(QLabel("Mass"), 1, 0)
        data1_layout.addWidget(self.mass1_box, 1, 1)
        data1_layout.addWidget(QLabel("H. Cap."), 2, 0)
        data1_layout.addWidget(self.cap1_box, 2, 1)

        self.temp2_box = QDoubleSpinBox()
        self.temp2_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp2_box.setRange(0, 500)
        self.temp2_box.setValue(0)
        self.temp2_box.setSuffix(" °C")
        self.temp2_box.setReadOnly(True)

        self.mass2_box = QDoubleSpinBox()
        self.mass2_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mass2_box.setRange(0.01, 1000)
        self.mass2_box.setValue(10)
        self.mass2_box.setSuffix(" kg")

        self.cap2_box = QDoubleSpinBox()
        self.cap2_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cap2_box.setRange(0.01, 10000)
        self.cap2_box.setValue(0.4)
        self.cap2_box.setSuffix(" J/kg°C")

        data2_layout = QGridLayout()
        data2_layout.addWidget(self.temp2_box, 0, 0)
        data2_layout.addWidget(QLabel("Temp."), 0, 1)
        data2_layout.addWidget(self.mass2_box, 1, 0)
        data2_layout.addWidget(QLabel("Mass"), 1, 1)
        data2_layout.addWidget(self.cap2_box, 2, 0)
        data2_layout.addWidget(QLabel("H. Cap."), 2, 1)

        self.start_button = QPushButton("Start")
        self.start_button.setObjectName("startButton")
        self.start_button.setCheckable(True)

        self.graphs_button = QPushButton("Graphs")
        self.graphs_button.setObjectName("graphsButton")

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.start_button)
        buttons_layout.addWidget(self.graphs_button)

        bottom_layout = QHBoxLayout()
        bottom_layout.addLayout(data1_layout)
        bottom_layout.addStretch()
        bottom_layout.addLayout(buttons_layout)
        bottom_layout.addStretch()
        bottom_layout.addLayout(data2_layout)


        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(28, 28, 28, 28)
        card_layout.setSpacing(28)
        card_layout.addLayout(top_layout)
        card_layout.addLayout(bottom_layout)
        card.setLayout(card_layout)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(28, 24, 28, 28)
        main_layout.setSpacing(18)
        main_layout.addLayout(header_layout)
        main_layout.addWidget(card)
        self.setLayout(main_layout)
        self.about_button.clicked.connect(self.open_about)
        self.graphs_button.clicked.connect(self.open_graphs)

    def open_about(self):
        self.about_window = AboutWindow("https://github.com/yuval1188/hw-exe2")
        self.about_window.show()

    def open_graphs(self):
        self.graph_window = GraphWindow(self)
        self.graph_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    file = open("style.qss", "r")
    app.setStyleSheet(file.read())
    file.close()

    window = HeatTransfer()
    window.show()
    sys.exit(app.exec())