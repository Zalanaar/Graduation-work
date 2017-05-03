#impiorting
import sys
import os
from os.path import expanduser
import subprocess
import osmapi
#from PyQt4 import QtGui*
from PySide.QtCore import *
from PySide.QtWebKit import *
from PySide.QtGui import *
from PySide import QtCore
from geopy.geocoders import Nominatim
import pandas as pd

class MainApp (QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        #title for window
        self.setWindowTitle(u'Pythia')
        #widdget setting
        self.left = 100
        self.top = 100
        self.width = 250
        self.height = 250
        self.setGeometry(self.left, self.top, self.width, self.height)

        #create menu
        self.fileMenu = self.menuBar().addMenu("&Menu")
        self.fileMenu.addAction("&Generate .csv...", self.generate_file)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction("&Open .csv...", self.on_load_file)
        self.fileMenu.addAction("&Save to .csv..", self.on_save_file)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction("&Exit", self.exit_action)

        ############################################    Option for Forecast     ############################################
        #create starting point widget
        self.lab_starting = QLabel("Starting Address", self)
        self.button_starting = QPushButton('Starting save', self)
        # connect
        self.text_starting = QLineEdit(self)
        self.lab_start_latitude = QLabel("latitude for Start Address")
        self.start_latitude = QDoubleSpinBox(self)
        self.start_latitude.setEnabled(False)
        self.lab_start_longitude = QLabel("longitude for Start Address")
        self.start_longitude = QDoubleSpinBox(self)
        self.start_longitude.setEnabled(False)

        #create waypoint widget
        self.lab_waypoint = QLabel("Waypoint Address", self)
        self.button_waypoint = QPushButton('Waypoint save',self)
        self.text_waypoint = QLineEdit(self)
        self.lab_waypoint_latitude = QLabel("latitude for Waypoint")
        self.waypoint_latitude = QDoubleSpinBox(self)
        self.waypoint_latitude.setEnabled(False)
        self.lab_waypoint_longitude = QLabel("longitude for Waypoint")
        self.waypoint_longitude = QDoubleSpinBox(self)
        self.waypoint_longitude.setEnabled(False)

        ############################################    Option Forecast     ############################################

        self.text_forecast = QLineEdit(self)


        #subprocess
        self.pipes = []
        self.determination_of_coordinates = os.path.join(os.path.dirname(__file__), "./determination.py")


        self.create_window()
        self.setup()
        #self.Browser = Browser(


    def on_load_file(self):
        file_open = "CSV (*csv)|* .csv"
        path = (QFileDialog.getOpenFileName(self, 'open file', file_open))
        self.op = pd.read_csv(path[0], ';', nrows=671) #make open


    def on_save_file(self):
        save_file = "CSV (*csv)|* .csv"
        path = (QFileDialog.getOpenFileName(self, 'Save file', save_file))

    def exit_action(self):
        self.close()

    def generate_file(self):
        print("generate")

    def create_window(self):
        self.main_frame = QWidget()
        #Group box for starting point
        starting_box = QGroupBox()
        starting_hbox = QHBoxLayout()
        starting_hbox.addWidget(self.lab_starting)
        starting_hbox.addWidget(self.text_starting)
        starting_hbox.addWidget(self.button_starting)
        starting_coordinate_hbox = QHBoxLayout()
        starting_coordinate_hbox.addWidget(self.lab_start_latitude)
        starting_coordinate_hbox.addWidget(self.start_latitude)
        starting_coordinate_hbox.addWidget(self.lab_start_longitude)
        starting_coordinate_hbox.addWidget(self.start_longitude)
        starting_vbox = QVBoxLayout()
        starting_vbox.addLayout(starting_hbox)
        starting_vbox.addLayout(starting_coordinate_hbox)
        starting_box.setLayout(starting_vbox)
        #Group box for waypoint widget
        waypoint_box = QGroupBox()
        waypoint_hbox = QHBoxLayout()
        waypoint_hbox.addWidget(self.lab_waypoint)
        waypoint_hbox.addWidget(self.text_waypoint)
        waypoint_hbox.addWidget(self.button_waypoint)
        waypoint_coordinate_hbox = QHBoxLayout()
        waypoint_coordinate_hbox.addWidget(self.lab_waypoint_latitude)
        waypoint_coordinate_hbox.addWidget(self.waypoint_latitude)
        waypoint_coordinate_hbox.addWidget(self.lab_waypoint_longitude)
        waypoint_coordinate_hbox.addWidget(self.waypoint_longitude)
        waypoint_vbox = QVBoxLayout()
        waypoint_vbox.addLayout(waypoint_hbox)
        waypoint_vbox.addLayout(waypoint_coordinate_hbox)
        waypoint_box.setLayout(waypoint_vbox)
        #layout for option forecast
        point_option_layout = QVBoxLayout()
        point_option_layout.addWidget(starting_box)
        point_option_layout.addWidget(waypoint_box)
        main_point_option_layout = QVBoxLayout()
        main_box = QGroupBox()
        main_label = QLabel('Option for forecast')
        main_point_option_layout.addWidget(main_label)
        main_point_option_layout.addLayout(point_option_layout)
        main_box.setLayout(main_point_option_layout)
        main = QVBoxLayout()
        main.addWidget(main_box)
        self.main_frame.setLayout(main)
        self.setCentralWidget(self.main_frame)

    def setup(self):
        self.button_starting.clicked.connect(self.save_starting_point)
        self.button_waypoint.clicked.connect(self.save_waypoint)

    def save_starting_point(self):
        star_point_text = self.text_starting.text()
        geolocator = Nominatim()
        start_location = geolocator.geocode(star_point_text)
        self.start_longitude.setValue(start_location.longitude)
        self.start_latitude.setValue(start_location.latitude)


    def save_waypoint(self):
        waypoint_text = self.text_waypoint.text()
        geolocator = Nominatim()
        waypoint_location = geolocator.geocode(waypoint_text)
        self.waypoint_longitude.setValue(waypoint_location.longitude)
        self.waypoint_latitude.setValue(waypoint_location.latitude)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())

