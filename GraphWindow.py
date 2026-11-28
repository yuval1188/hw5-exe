import os
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QComboBox,
                               QFrame, QHBoxLayout, QVBoxLayout)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class GraphWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Graph Window")
        self.resize(820, 520)

        self.figure = Figure(dpi=100, facecolor="#FFFFFF")
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axes = self.figure.add_subplot()
        self.axes.set_xlabel("Time (s)", color="#5B647A", fontsize=10)
        self.axes.set_ylabel("Temperature (°C)", color="#5B647A", fontsize=10)
        self.axes.grid(True, color="#E4E8F1")
        self.axes.tick_params(colors="#8A93A8", labelsize=9)
        self.axes.spines["top"].set_visible(False)
        self.axes.spines["right"].set_visible(False)
        self.axes.spines["left"].set_color("#C9CEDB")
        self.axes.spines["bottom"].set_color("#C9CEDB")
        self.figure.subplots_adjust(left=0.13, right=0.97, top=0.95, bottom=0.13)

        graph_card = QFrame()
        graph_card.setObjectName("card")
        graph_layout = QVBoxLayout()
        graph_layout.setContentsMargins(16, 16, 16, 16)
        graph_layout.addWidget(self.canvas)
        graph_card.setLayout(graph_layout)

        title = QLabel("Graphs")
        title.setObjectName("graphTitle")
        subtitle = QLabel("Temperature over time")
        subtitle.setObjectName("subtitle")

        body_label = QLabel("Body")
        self.body_box = QComboBox()
        self.body_box.addItem("Body 1")
        self.body_box.addItem("Body 2")
        self.body_box.addItem("Both bodies")

        self.draw_button = QPushButton("Draw")
        self.draw_button.setObjectName("drawButton")

        self.clear_button = QPushButton("Clear")
        self.clear_button.setObjectName("clearButton")

        self.export_button = QPushButton("Export to CSV")
        self.export_button.setObjectName("exportButton")

        side_layout = QVBoxLayout()
        side_layout.setSpacing(12)
        side_layout.addWidget(title)
        side_layout.addWidget(subtitle)
        side_layout.addSpacing(16)
        side_layout.addWidget(body_label)
        side_layout.addWidget(self.body_box)
        side_layout.addSpacing(10)
        side_layout.addWidget(self.draw_button)
        side_layout.addWidget(self.clear_button)
        side_layout.addStretch()
        side_layout.addWidget(self.export_button)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(24, 24, 24, 24)
        main_layout.setSpacing(24)
        main_layout.addWidget(graph_card, 1)
        main_layout.addLayout(side_layout)
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    folder = os.path.dirname(__file__)
    file = open(os.path.join(folder, "style.qss"), "r")
    app.setStyleSheet(file.read())
    file.close()

    window = GraphWindow(None)
    window.show()
    sys.exit(app.exec())