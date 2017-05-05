#impiorting
import sys
import os
import osmapi
from PySide.QtCore import *
from PySide.QtWebKit import *
from PySide.QtGui import *
from PySide import QtCore
from geopy.geocoders import Nominatim
import pandas as pd
import datetime
import random

import generation

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
        generate = self.fileMenu.addMenu("&Generate .csv")
        generate.addAction("&Generate Way One", self.generate_way_one)
        generate.addAction("&Generate Way Two", self.generate_way_two)
        generate.addAction("&Generate Way Three", self.generate_way_three)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction("&Open .csv...", self.on_load_file)
        self.fileMenu.addAction("&Save to .csv..", self.on_save_file)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction("&Exit", self.exit_action)

        ############################################    Option for Forecast     ############################################
        #create starting point widget
        self.lab_starting = QLabel("Starting Address", self)
        self.button_starting = QPushButton('Starting save', self)
        self.text_starting = QLineEdit(self)
        self.lab_start_latitude = QLabel("latitude for Start Address")
        self.start_latitude = QDoubleSpinBox(self)
        self.start_latitude.setDecimals(5)
        self.start_latitude.setEnabled(False)
        self.lab_start_longitude = QLabel("longitude for Start Address")
        self.start_longitude = QDoubleSpinBox(self)
        self.start_longitude.setDecimals(5)
        self.start_longitude.setEnabled(False)
        self.lab_start_time = QLabel("Time for Starting")
        self.start_time = QTimeEdit()
        self.start_time.setTime(datetime.datetime.time(datetime.datetime.now()))

        #create waypoint widget
        self.lab_waypoint = QLabel("Waypoint Address", self)
        self.button_waypoint = QPushButton('Waypoint save',self)
        self.text_waypoint = QLineEdit(self)
        self.lab_waypoint_latitude = QLabel("latitude for Waypoint")
        self.waypoint_latitude = QDoubleSpinBox(self)
        self.waypoint_latitude.setDecimals(5)
        self.waypoint_latitude.setEnabled(False)
        self.lab_waypoint_longitude = QLabel("longitude for Waypoint")
        self.waypoint_longitude = QDoubleSpinBox(self)
        self.waypoint_longitude.setDecimals(5)
        self.waypoint_longitude.setEnabled(False)
        self.lab_waypoint_time = QLabel("Time for Waypoint")
        self.waypoint_time = QTimeEdit()
        self.waypoint_time.setTime(datetime.datetime.time(datetime.datetime.now() + datetime.timedelta(minutes=30)))

        self.lab_time = QLabel("Time for Forecast")
        self.time_for_forc = QTimeEdit()

        ############################################    Option Forecast     ############################################

        self.lab_text_forecast = QLabel("Forecast Address")
        self.text_forecast = QLineEdit(self)
        #self.text_forecast.setEnabled(False)
        self.lab_forecast_latitude = QLabel("Forecast latitude Address")
        self.forecast_latitude =QDoubleSpinBox(self)
        self.forecast_latitude.setDecimals(5)
        self.forecast_latitude.setEnabled(False)
        self.lab_forecast_longitude = QLabel("Forecast longitude Address")
        self.forecast_longitude = QDoubleSpinBox(self)
        self.forecast_longitude.setDecimals(5)
        self.forecast_longitude.setEnabled(False)
        self.lab_forecast_time = QLabel("Forecast Time")
        self.forecast_time = QTimeEdit()
        self.forecast_time.setEnabled(False)


        self.forecast_button = QPushButton('Forecast!', self)

        self.create_window()
        self.setup()


    def on_load_file(self):
        print("load file")
        try:
            file_open = "CSV (*csv)|* .csv"
            path = (QFileDialog.getOpenFileName(self, 'open file', file_open))
        except Exception:
            print("fuck")


    def on_save_file(self):
        save_file = "CSV (*csv)|* .csv"
        path = (QFileDialog.getOpenFileName(self, 'Save file', save_file))

    def exit_action(self):
        self.close()

    def generate_way_one(self):
        generation.way_one()

    def generate_way_two(self):
        generation.way_two()

    def generate_way_three(self):
        generation.way_three()

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
        starting_time = QHBoxLayout()
        starting_time.addWidget(self.lab_start_time)
        starting_time.addWidget(self.start_time)
        starting_vbox = QVBoxLayout()
        starting_vbox.addLayout(starting_hbox)
        starting_vbox.addLayout(starting_coordinate_hbox)
        starting_vbox.addLayout(starting_time)
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
        waypoint_time = QHBoxLayout()
        waypoint_time.addWidget(self.lab_waypoint_time)
        waypoint_time.addWidget(self.waypoint_time)
        waypoint_vbox = QVBoxLayout()
        waypoint_vbox.addLayout(waypoint_hbox)
        waypoint_vbox.addLayout(waypoint_coordinate_hbox)
        waypoint_vbox.addLayout(waypoint_time)
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
        #layout for forecast
        forecast_box = QGroupBox()
        forecast_vbox = QVBoxLayout()
        forecast_text_hbox = QHBoxLayout()
        forecast_text_hbox.addWidget(self.lab_text_forecast)
        forecast_text_hbox.addWidget(self.text_forecast)
        forecast_coordinate_hbox = QHBoxLayout()
        forecast_coordinate_hbox.addWidget(self.lab_forecast_latitude)
        forecast_coordinate_hbox.addWidget(self.forecast_latitude)
        forecast_coordinate_hbox.addWidget(self.lab_forecast_longitude)
        forecast_coordinate_hbox.addWidget(self.forecast_longitude)
        forecast_time = QHBoxLayout()
        forecast_time.addWidget(self.lab_forecast_time)
        forecast_time.addWidget(self.forecast_time)
        option_forc = QHBoxLayout()
        option_forc.addWidget(self.lab_time)
        option_forc.addWidget(self.time_for_forc)
        forecast_label = QLabel("Forecast")
        forecast_vbox.addWidget(forecast_label)
        #forecast_vbox.addLayout(option_forc)
        forecast_vbox.addLayout(forecast_text_hbox)
        forecast_vbox.addLayout(forecast_coordinate_hbox)
        forecast_vbox.addLayout(forecast_time)
        forecast_box.setLayout(forecast_vbox)
        main = QHBoxLayout()
        main.addWidget(main_box)
        main.addWidget(forecast_box)
        main_vbox = QVBoxLayout()
        main_vbox.addLayout(main)
        main_vbox.addWidget(self.forecast_button)
        self.main_frame.setLayout(main_vbox)
        self.setCentralWidget(self.main_frame)
        self.forecast_button.setEnabled(False)


    def setup(self):
        self.button_starting.clicked.connect(self.save_starting_point)
        self.button_waypoint.clicked.connect(self.save_waypoint)
        self.forecast_button.clicked.connect(self.forecast_data)

    def save_starting_point(self):
        star_point_text = self.text_starting.text()
        geolocator = Nominatim()
        if len(star_point_text) == 0:
            self.error_message = QMessageBox.information(self, 'Error', 'Starting adress is empty. Please, check correctness of input', QMessageBox.Ok)
        else:
            start_location = geolocator.geocode(star_point_text)
            self.start_longitude.setValue(start_location.longitude)
            self.start_latitude.setValue(start_location.latitude)
            self.start_longitude.setEnabled(False)
            self.start_latitude.setEnabled(False)
            self.text_starting.setEnabled(False)
            self.start_time.setEnabled(False)
        if self.start_longitude is not None and self.waypoint_longitude is not None: #check this
            self.forecast_button.setEnabled(True)



    def save_waypoint(self):
        waypoint_text = self.text_waypoint.text()
        geolocator = Nominatim()
        waypoint_location = geolocator.geocode(waypoint_text)
        #waypoint_location.longitude = None
        #waypoint_location.latitude = None

        ##I don't fucking know how check wrong address
        if len(waypoint_text) == 0:
            self.error_message = QMessageBox.information(self, 'Error', 'Waypoint address is empty. Please, check correctness of input ', QMessageBox.Ok)
        else:
            self.waypoint_longitude.setValue(waypoint_location.longitude)
            self.waypoint_latitude.setValue(waypoint_location.latitude)
            self.waypoint_longitude.setEnabled(False)
            self.waypoint_latitude.setEnabled(False)
            self.text_waypoint.setEnabled(False)
            self.waypoint_time.setEnabled(False)

    def forecast_data(self): #plug
        ##unlock option for forecast
        self.text_starting.setEnabled(True)
        self.start_time.setEnabled(True)
        self.start_latitude.setEnabled(True)
        self.start_longitude.setEnabled(True)

        self.text_waypoint.setEnabled(True)
        self.waypoint_latitude.setEnabled(True)
        self.waypoint_longitude.setEnabled(True)
        self.waypoint_time.setEnabled(True)

        geolocator = Nominatim()
        random_forecast_longitude = random.uniform(48.69300, 48.71397)
        random_forecast_latitude = random.uniform(44.50172, 44.52881)
        self.forecast_longitude.setValue(random_forecast_longitude)
        self.forecast_latitude.setValue(random_forecast_latitude)
        forecast_location = geolocator.reverse(str(random_forecast_latitude), str(random_forecast_longitude)) #fix this
        #print(forecast_location)
        self.text_forecast.setText(forecast_location.address)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())

