import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QSlider
from PyQt5.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QWidget,QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
import sys
def calculate_mach(speed, altitude):
    sos = 1235.6
    g = 9.81  # Acceleration due to gravity (m/s^2)
    M = 0.0289644  # Molar mass of air (kg/mol)
    R = 8.31432  # Universal gas constant (N·m/(mol·K))
    mach = speed / sos
    m = (altitude-15.01) * 0.00648
    temp_h = 15.01 - m
    press = 101.259 *math.exp(-g * M * altitude / ((R * (temp_h+273.15))))
    return mach, temp_h, press

def draw_polygon():
    polygon1 = [[3.59, 7.47], [3.15, 7.47], [2.9, 7.39], [2.02, 7.39], [1.83, 7.25], [1.81, 7], [2.02, 6.85],
                [2.28, 6.85], [3, 7], [3.23, 7.14], [3.59, 7.15], [3.59, 7.44]]
    polygon2 = [[3.59, 2.51], [3.31, 2.58], [2.92, 2.68], [2.43, 2.77], [1.83, 2.77], [1.80, 2.44], [2.05, 2.35],
                [2.45, 2.27], [3.59, 2.27], [3.59, 2.51]]
    ##
    polygon3 = [[3.59, 7.47], [7.51, 7.47], [7.51, 6.81], [7.14, 6.78], [5.79, 6.97], [4.51, 7.13], [3.59, 7.15],
                [3.59, 7.47]]
    polygon4 = [[7.51, 5.95], [4.01, 5.51], [3.68, 5.11], [3.55, 4.82], [3.77, 4.42], [4.05, 4.24], [7.51, 3.74],
                [7.51, 5.95]]
    polygon5 = [[7.51, 2.94], [4.88, 2.54], [3.59, 2.51], [3.59, 2.27], [7.51, 2.27], [7.51, 2.94]]
    ##
    polygon6 = [[7.51, 2.94], [7.96, 2.69], [9.46, 2.69], [9.69, 2.85], [9.92, 2.85], [9.92, 2.27], [9.93, 2.27],
                [7.51, 2.27], [7.51, 2.94]]
    polygon7 = [[7.51, 5.43], [7.51, 4.32], [9.37, 4.32], [9.92, 3.74], [9.92, 5.85], [9.43, 5.49], [7.51, 5.43]]
    polygon8 = [[7.51, 7.47], [7.51, 6.81], [7.87, 6.92], [8.78, 7.08], [9.41, 7.07], [9.42, 6.95], [9.78, 6.79],
                [9.92, 6.79], [9.92, 7.47], [7.51, 7.47]]
    ##
    polygon9 = [[9.92, 7.47], [9.92, 6.8], [10.38, 6.77], [11.04, 7.07], [11.04, 7.47], [9.92, 7.47]]
    polygon10 = [[9.92, 5.92], [13.34, 4.84], [9.92, 3.72], [9.92, 5.92]]
    polygon11 = [[9.92, 2.27], [11.04, 2.27], [11.04, 2.64], [10.38, 2.84], [9.94, 2.87], [9.92, 2.27]]
    ##
    polygon12 = [[11.04, 7.07], [11.04, 7.48], [13.47, 7.51], [15.94, 6.5], [13.47, 7.07], [11.04, 7.07]]
    polygon13 = [[11.04, 2.67], [11.04, 2.27], [13.47, 2.27], [15.94, 3.35], [13.47, 2.7], [11.04, 2.67]]
    ##
    line1 = [[4.37, 7.10], [7.47, 6.7], [7.47, 5.97], [4.35, 5.56], [4.37, 7.1]]
    line2 = [[4.37, 4.16], [7.47, 3.74], [7.47, 2.99], [4.37, 2.57], [4.37, 4.16]]
    line3 = [[9.92, 3.71], [9.92, 2.9], [10.41, 2.85], [11.04, 2.68], [11.04, 4.05], [9.92, 3.71]]
    line4 = [[9.92, 6.75], [9.92, 5.93], [11.04, 5.6], [11.04, 7.05], [10.38, 6.75], [9.92, 6.75]]
    line5 = [[2, 3], [2.2, 3]]

    ##4

    xs, ys = zip(*polygon1)
    xa, ya = zip(*polygon2)
    xb, yb = zip(*polygon3)
    xc, yc = zip(*polygon4)
    xd, yd = zip(*polygon5)
    xe, ye = zip(*polygon6)
    xf, yf = zip(*polygon7)
    xz, yz = zip(*polygon8)
    xq, yq = zip(*polygon9)
    xw, yw = zip(*polygon10)
    xr, yr = zip(*polygon11)
    xt, yt = zip(*polygon12)
    xu, yu = zip(*polygon13)
    xl1, yl1 = zip(*line1)
    xl2, yl2 = zip(*line2)
    xl3, yl3 = zip(*line3)
    xl4, yl4 = zip(*line4)
    xl5, yl5 = zip(*line5)

    plt.style.use('dark_background')
    plt.figure()

    plt.plot(xl5, yl5, color='blue')
    plt.fill(xl3, yl3, color='white')
    plt.plot(xl3, yl3, color='white')
    plt.fill(xl4, yl4, color='white')
    plt.plot(xl4, yl4, color='white')
    plt.fill(xl1, yl1, color='white')
    plt.plot(xl1, yl1, color='white')
    plt.fill(xl2, yl2, color='white')
    plt.plot(xl2, yl2, color='white')
    plt.fill(xl2, yl2, color='white')
    plt.plot(xl2, yl2, color='white')
    plt.fill(xa, ya, color='yellow')
    plt.plot(xa, ya, color='yellow')
    plt.fill(xs, ys, color='yellow')
    plt.plot(xs, ys, color='yellow')
    plt.fill(xb, yb, color='blue')
    plt.plot(xb, yb, color='blue')
    plt.fill(xc, yc, color='blue')
    plt.plot(xc, yc, color='blue')
    plt.fill(xd, yd, color='blue')
    plt.plot(xd, yd, color='blue')
    plt.fill(xe, ye, color='violet')
    plt.plot(xe, ye, color='violet')
    plt.fill(xf, yf, color='violet')
    plt.plot(xf, yf, color='violet')
    plt.fill(xz, yz, color='violet')
    plt.plot(xz, yz, color='violet')
    plt.fill(xq, yq, color='green')
    plt.plot(xq, yq, color='green')
    plt.fill(xw, yw, color='green')
    plt.plot(xw, yw, color='green')
    plt.fill(xr, yr, color='green')
    plt.plot(xr, yr, color='green')
    plt.fill(xt, yt, color='pink')
    plt.plot(xt, yt, color='pink')
    plt.fill(xu, yu, color='pink')
    plt.plot(xu, yu, color='pink')

    plt.show()

def calculate_pres_temp(mach,throttle,altitude):
    temp_start = [288, 288, 521,416 , 188 , 188, 188, 188]
    press_start =[101.2,101.2,810.0,810.0,429.6,429.6,429.6,429.6]
    result_temp =[]
    result_press =[]

    for i in range(len(temp_start)):
        s = temp_start[i]*(1+0.2*mach**2) - (altitude*0.00648)
        result_temp.append(s)
    result_temp[3] = throttle * 13.88
    result_temp[4] = temp_start[4]*(1+0.2*mach**2) - (altitude*0.00648) + ((throttle-30)/10)*145
    result_temp[5] = temp_start[5]*(1+0.2*mach**2) - (altitude*0.00648) + ((throttle-30)/10)*145
    result_temp[6] = temp_start[6]*(1+0.2*mach**2) - (altitude*0.00648) + ((throttle-30)/10)*145
    result_temp[7] = temp_start[7]*(1+0.2*mach**2) - (altitude*0.00648) + ((throttle-30)/10)*145
    for i in range(len(temp_start)):
        s = press_start[i]*(1 + 0.2*mach**2)**(1.4/(1.4-1))
        result_press.append(s)
    return result_press,result_temp


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")
        self.setGeometry(0, 0, 1200, 1200)


        ##
        slider_speed = QSlider(self)
        slider_speed.setOrientation(Qt.Horizontal)  # Đặt hướng dọc
        slider_speed.setMinimum(0)
        slider_speed.setMaximum(2415)
        slider_speed.setValue(0)
        slider_speed.move(650, 745)
        slider_speed.resize(160, 30)
        slider_speed.valueChanged.connect(self.update_speed)


        slider_altitude = QSlider(self)
        slider_altitude.setOrientation(Qt.Horizontal)  # Đặt hướng dọc
        slider_altitude.setMinimum(0)
        slider_altitude.setMaximum(13000)
        slider_altitude.setValue(0)
        slider_altitude.move(650, 795)
        slider_altitude.resize(160, 30)
        slider_altitude.valueChanged.connect(self.update_altitude)

        slider_throtle = QSlider(self)
        slider_throtle.setOrientation(Qt.Horizontal)  # Đặt hướng dọc
        slider_throtle.setMinimum(30)
        slider_throtle.setMaximum(100)
        slider_throtle.setValue(30)
        slider_throtle.move(650, 845)
        slider_throtle.resize(160, 30)
        slider_throtle.valueChanged.connect(self.update_throtle)


        # Calculate Mach, static temperature, and pressure
        self.speed_value = slider_speed.value()
        self.altitude_value = slider_altitude.value()
        self.throtle_value = slider_throtle.value()
        self.s = [470, 470, 833, 1388, 1388, 1388, 1388, 1388]

        self.mach, self.temp_h, self.press = calculate_mach(self.speed_value, self.altitude_value)
        self.mach = round(self.mach,2)
        self.press = round(self.press,2)
        self.temp_h = round(self.temp_h,2)
        self.a, self.b = calculate_pres_temp(self.mach, self.throtle_value, self.altitude_value)
        for i in range(len(self.a)):
            self.a[i] = round(self.a[i], 2)

        for i in range(len(self.b)):
            self.b[i] = round(self.b[i], 2)
        ####Bieu Do

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.plot(self.b, marker='o', label='temptrain')
        self.ax.plot(self.s, marker='o', label='line-limit')
        self.canvas.get_width_height()

        # Set title and axis labels
        self.ax.set_xlabel('Train')
        self.ax.set_ylabel('Nhiệt độ')
        self.ax.set_title('Biểu đồ Nhiệt độ')
        self.ax.legend()
        if any(self.b[i] > self.s[i] for i in range(len(self.s))):
            for i in range(len(self.s)):
                if self.b[i] > self.s[i]:
                    plt.text(i, self.b[i], "Overheat", ha='center', va='bottom', color="red")
        # Create a QVBoxLayout instance
        self.canvas.setFixedSize(1900, 500)
        self.canvas.move(0, 50)
        self.setCentralWidget(self.canvas)  # Set the layout as the central widget








        label_input = QLabel("Input",self)
        label_input.move(600,550)


        label_mach = QLabel("Mach", self)
        label_mach.move(375, 600)
        label_press = QLabel("Press", self)
        label_press.move(375, 650)
        label_temp = QLabel("Temp", self)
        label_temp.move(375, 700)
        label_speed = QLabel("Speed (Km)", self)
        label_speed.move(375, 750)
        label_altitude = QLabel("Altitude (M)", self)
        label_altitude.move(375, 800)
        label_throttle = QLabel("Throttle", self)
        label_throttle.move(375, 850)
        self.line_mach = QLineEdit(self)
        self.line_mach.setText(str(self.mach))
        self.line_mach.setReadOnly(True)
        self.line_mach.move(500,595)
        self.line_mach.resize(100,30)
        self.line_press = QLineEdit(self)
        self.line_press.setText(str(self.press))
        self.line_press.setReadOnly(True)
        self.line_press.move(500, 645)
        self.line_press.resize(100, 30)
        self.line_temp = QLineEdit(self)
        self.line_temp.setText(str(self.temp_h))
        self.line_temp.setReadOnly(True)
        self.line_temp.move(500, 695)
        self.line_temp.resize(100, 30)
        self.line_speed = QLineEdit(self)
        self.line_speed.setText(str(slider_speed.value()))
        self.line_speed.setReadOnly(True)
        self.line_speed.move(500, 745)
        self.line_speed.resize(100, 30)
        self.line_altitude = QLineEdit(self)
        self.line_altitude.setText(str(self.altitude_value))
        self.line_altitude.setReadOnly(True)
        self.line_altitude.move(500, 795)
        self.line_altitude.resize(100, 30)
        self.line_throtle = QLineEdit(self)
        self.line_throtle.setText(str(self.throtle_value))
        self.line_throtle.setReadOnly(True)
        self.line_throtle.move(500, 845)
        self.line_throtle.resize(100, 30)
        input_combo = QComboBox(self)
        input_combo.addItem("Input: Speed + Altitude")
        input_combo.move(650,595)
        input_combo.resize(180,30)
        unit_press = QLabel("k Pa",self)
        unit_press.resize(100,30)
        unit_press.move(650,645)
        unit_temp = QLabel("C",self)
        unit_temp.move(650,695)
        unit_temp.resize(100, 30)


        #OUTPUT
        label_output = QLabel("Output",self)
        label_output.move(1250,550)
        label_bstation1 = QLabel("Station",self)
        label_bstation1.move(1000,595)
        label_bstation2 = QLabel("Station",self)
        label_bstation2.move(1300,595)
        label_bpress1 = QLabel("Pres-kPa",self)
        label_bpress1.move(1100,595)
        label_bpress2 = QLabel("Pres-kPa", self)
        label_bpress2.move(1400, 595)

        label_btemp1 = QLabel("Temp-K",self)
        label_btemp1.move(1200,595)
        label_btemp2 = QLabel("Temp-K", self)
        label_btemp2.move(1500, 595)

        label_station1 = QLabel("1",self)
        label_station1.move(1000, 645)
        label_station2 = QLabel("2", self)
        label_station2.move(1000, 695)
        label_station3 = QLabel("3", self)
        label_station3.move(1000, 745)
        label_station4 = QLabel("4", self)
        label_station4.move(1000, 795)
        label_station5 = QLabel("5", self)
        label_station5.move(1300, 645)
        label_station6 = QLabel("6", self)
        label_station6.move(1300, 695)
        label_station7 = QLabel("7", self)
        label_station7.move(1300, 745)
        label_station8 = QLabel("8", self)
        label_station8.move(1300, 795)
        self.line_press1 = QLineEdit(self)
        self.line_press1.setText(str(self.a[0]))
        self.line_press1.setReadOnly(True)
        self.line_press1.move(1100, 645)
        self.line_press1.resize(70,30)
        self.line_press2 = QLineEdit(self)
        self.line_press2.setText(str(self.a[1]))
        self.line_press2.setReadOnly(True)
        self.line_press2.move(1100, 695)
        self.line_press2.resize(70, 30)
        self.line_press3 = QLineEdit(self)
        self.line_press3.setText(str(self.a[2]))
        self.line_press3.setReadOnly(True)
        self.line_press3.move(1100, 745)
        self.line_press3.resize(70, 30)
        self.line_press4 = QLineEdit(self)
        self.line_press4.setText(str(self.a[3]))
        self.line_press4.setReadOnly(True)
        self.line_press4.move(1100, 795)
        self.line_press4.resize(70, 30)
        self.line_press5 = QLineEdit(self)
        self.line_press5.setText(str(self.a[4]))
        self.line_press5.setReadOnly(True)
        self.line_press5.move(1400, 645)
        self.line_press5.resize(70, 30)
        self.line_press6 = QLineEdit(self)
        self.line_press6.setText(str(self.a[5]))
        self.line_press6.setReadOnly(True)
        self.line_press6.move(1400, 695)
        self.line_press6.resize(70, 30)
        self.line_press7 = QLineEdit(self)
        self.line_press7.setText(str(self.a[6]))
        self.line_press7.setReadOnly(True)
        self.line_press7.move(1400, 745)
        self.line_press7.resize(70, 30)
        self.line_press8 = QLineEdit(self)
        self.line_press8.setText(str(self.a[7]))
        self.line_press8.setReadOnly(True)
        self.line_press8.move(1400, 795)
        self.line_press8.resize(70, 30)
        ###
        self.line_temp1 = QLineEdit(self)
        self.line_temp1.setText(str(self.b[0]))
        self.line_temp1.setReadOnly(True)
        self.line_temp1.move(1200, 645)
        self.line_temp1.resize(70, 30)
        self.line_temp2 = QLineEdit(self)
        self.line_temp2.setText(str(self.b[1]))
        self.line_temp2.setReadOnly(True)
        self.line_temp2.move(1200, 695)
        self.line_temp2.resize(70, 30)
        self.line_temp3 = QLineEdit(self)
        self.line_temp3.setText(str(self.b[2]))
        self.line_temp3.setReadOnly(True)
        self.line_temp3.move(1200, 745)
        self.line_temp3.resize(70, 30)
        self.line_temp4 = QLineEdit(self)
        self.line_temp4.setText(str(self.b[3]))
        self.line_temp4.setReadOnly(True)
        self.line_temp4.move(1200, 795)
        self.line_temp4.resize(70, 30)
        self.line_temp5 = QLineEdit(self)
        self.line_temp5.setText(str(self.b[4]))
        self.line_temp5.setReadOnly(True)
        self.line_temp5.move(1500, 645)
        self.line_temp5.resize(70, 30)
        self.line_temp6 = QLineEdit(self)
        self.line_temp6.setText(str(self.b[5]))
        self.line_temp6.setReadOnly(True)
        self.line_temp6.move(1500, 695)
        self.line_temp6.resize(70, 30)
        self.line_temp7 = QLineEdit(self)
        self.line_temp7.setText(str(self.b[6]))
        self.line_temp7.setReadOnly(True)
        self.line_temp7.move(1500, 745)
        self.line_temp7.resize(70, 30)
        self.line_temp8 = QLineEdit(self)
        self.line_temp8.setText(str(self.b[7]))
        self.line_temp8.setReadOnly(True)
        self.line_temp8.move(1500, 795)
        self.line_temp8.resize(70, 30)

        # User input widgets

    def update_speed(self, value):
        # Phương thức xử lý khi giá trị slider thay đổi
        self.line_speed.setText(str(value))
        self.speed_value =value

        self.mach , self.press, self.temp_h = calculate_mach(value,self.altitude_value)
        self.mach = round(self.mach, 2)
        self.press = round(self.press, 2)
        self.temp_h = round(self.temp_h, 2)
        self.line_mach.setText(str(self.mach))
        self.line_press.setText(str(self.press))
        self.line_temp.setText(str(self.temp_h))
        self.a, self.b = calculate_pres_temp(self.mach,self.throtle_value,self.altitude_value)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.plot(self.b, marker='o', label='temptrain')
        self.ax.plot(self.s, marker='o', label='line-limit')
        self.canvas.get_width_height()

        # Set title and axis labels
        self.ax.set_xlabel('Train')
        self.ax.set_ylabel('Nhiệt độ')
        self.ax.set_title('Biểu đồ Nhiệt độ')
        self.ax.legend()
        if any(self.b[i] > self.s[i] for i in range(len(self.s))):
            for i in range(len(self.s)):
                if self.b[i] > self.s[i]:
                    plt.text(i, self.b[i], "Overheat", ha='center', va='bottom', color="red")

        # Create a QVBoxLayout instance
        self.canvas.setFixedSize(1900, 500)
        self.canvas.move(500, 50)
        self.setCentralWidget(self.canvas)  # Set the layout as the central widget
        for i in range(len(self.a)):
            self.a[i] = round(self.a[i], 2)

        for i in range(len(self.b)):
            self.b[i] = round(self.b[i], 2)
        self.line_press8.setText(str(self.a[0]))
        self.line_press8.setText(str(self.a[1]))
        self.line_press8.setText(str(self.a[2]))
        self.line_press8.setText(str(self.a[3]))
        self.line_press8.setText(str(self.a[4]))
        self.line_press8.setText(str(self.a[5]))
        self.line_press8.setText(str(self.a[6]))
        self.line_press8.setText(str(self.a[7]))
        self.line_temp1.setText(str(self.b[0]))
        self.line_temp2.setText(str(self.b[1]))
        self.line_temp3.setText(str(self.b[2]))
        self.line_temp4.setText(str(self.b[3]))
        self.line_temp5.setText(str(self.b[4]))
        self.line_temp6.setText(str(self.b[5]))
        self.line_temp7.setText(str(self.b[6]))
        self.line_temp8.setText(str(self.b[7]))




    def update_altitude(self,value):
        self.line_altitude.setText(str(value))
        self.altitude_value = value
        self.mach , self.press,self.temp_h = calculate_mach(self.speed_value,value)
        self.mach = round(self.mach, 2)
        self.press = round(self.press, 2)
        self.temp_h = round(self.temp_h, 2)
        self.line_mach.setText(str(self.mach))
        self.line_press.setText(str(self.press))
        self.line_temp.setText(str(self.temp_h))
        self.a, self.b = calculate_pres_temp(self.mach, self.throtle_value, value)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.plot(self.b, marker='o', label='temptrain')
        self.ax.plot(self.s, marker='o', label='line-limit')
        self.canvas.get_width_height()

        # Set title and axis labels
        self.ax.set_xlabel('Train')
        self.ax.set_ylabel('Nhiệt độ')
        self.ax.set_title('Biểu đồ Nhiệt độ')
        self.ax.legend()
        if any(self.b[i] > self.s[i] for i in range(len(self.s))):
            for i in range(len(self.s)):
                if self.b[i] > self.s[i]:
                    plt.text(i, self.b[i], "Overheat", ha='center', va='bottom', color="red")

        # Create a QVBoxLayout instance
        self.canvas.setFixedSize(1900, 500)
        self.canvas.move(500, 50)
        self.setCentralWidget(self.canvas)  # Set the layout as the central widget
        for i in range(len(self.a)):
            self.a[i] = round(self.a[i], 2)

        for i in range(len(self.b)):
            self.b[i] = round(self.b[i], 2)
        self.line_press1.setText(str(self.a[0]))
        self.line_press1.setText(str(self.a[1]))
        self.line_press1.setText(str(self.a[2]))
        self.line_press1.setText(str(self.a[3]))
        self.line_press1.setText(str(self.a[4]))
        self.line_press1.setText(str(self.a[5]))
        self.line_press1.setText(str(self.a[6]))
        self.line_press1.setText(str(self.a[7]))
        self.line_temp1.setText(str(self.b[0]))
        self.line_temp2.setText(str(self.b[1]))
        self.line_temp3.setText(str(self.b[2]))
        self.line_temp4.setText(str(self.b[3]))
        self.line_temp5.setText(str(self.b[4]))
        self.line_temp6.setText(str(self.b[5]))
        self.line_temp7.setText(str(self.b[6]))
        self.line_temp8.setText(str(self.b[7]))

    def update_throtle(self,value):
        self.line_throtle.setText(str(value))
        self.throtle_value = value
        self.a, self.b = calculate_pres_temp(self.mach, value,self.altitude_value)
        self.mach = round(self.mach, 2)
        self.press = round(self.press, 2)
        self.temp_h = round(self.temp_h, 2)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.plot(self.b, marker='o', label='temptrain')
        self.ax.plot(self.s, marker='o', label='line-limit')

        # Set title and axis labels
        self.ax.set_xlabel('Train')
        self.ax.set_ylabel('Nhiệt độ')
        self.ax.set_title('Biểu đồ Nhiệt độ')
        self.ax.legend()
        if any(self.b[i] > self.s[i] for i in range(len(self.s))):
            for i in range(len(self.s)):
                if self.b[i] > self.s[i]:
                    plt.text(i, self.b[i], "Overheat", ha='center', va='bottom', color="red")

        # Create a QVBoxLayout instance
        self.canvas.setFixedSize(1900, 500)
        self.canvas.move(500, 50)
        self.setCentralWidget(self.canvas)  # Set the layout as the central widget
        for i in range(len(self.a)):
            self.a[i] = round(self.a[i], 2)

        for i in range(len(self.b)):
            self.b[i] = round(self.b[i], 2)
        self.line_press1.setText(str(self.a[0]))
        self.line_press1.setText(str(self.a[1]))
        self.line_press1.setText(str(self.a[2]))
        self.line_press1.setText(str(self.a[3]))
        self.line_press1.setText(str(self.a[4]))
        self.line_press1.setText(str(self.a[5]))
        self.line_press1.setText(str(self.a[6]))
        self.line_press1.setText(str(self.a[7]))
        self.line_temp1.setText(str(self.b[0]))
        self.line_temp2.setText(str(self.b[1]))
        self.line_temp3.setText(str(self.b[2]))
        self.line_temp4.setText(str(self.b[3]))
        self.line_temp5.setText(str(self.b[4]))
        self.line_temp6.setText(str(self.b[5]))
        self.line_temp7.setText(str(self.b[6]))
        self.line_temp8.setText(str(self.b[7]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
