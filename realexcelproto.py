# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jeffr\Desktop\PCCWExcel\new_excelproto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from pandasmodel import *
from sheetclass import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 447)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sheet = simp()
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.file_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.file_entry.setObjectName("file_entry")
        self.verticalLayout.addWidget(self.file_entry)
        self.file_button = QtWidgets.QPushButton(self.centralwidget)
        self.file_button.setObjectName("file_button")
        self.file_button.clicked.connect(self.format_excel)
        self.verticalLayout.addWidget(self.file_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.a_end = QtWidgets.QLineEdit(self.centralwidget)
        self.a_end.setObjectName("a_end")
        self.verticalLayout_2.addWidget(self.a_end)
        self.label_a_end = QtWidgets.QLabel(self.centralwidget)
        self.label_a_end.setObjectName("label_a_end")
        self.verticalLayout_2.addWidget(self.label_a_end)
        # self.a_end_button = QtWidgets.QPushButton(self.centralwidget)
        # self.a_end_button.setObjectName("a_end_button")
        # self.a_end_button.clicked.connect(self.a_end_func)
        # self.a_end_button.clicked.connect(self.btn_clk)
        # self.verticalLayout_2.addWidget(self.a_end_button)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.z_end = QtWidgets.QLineEdit(self.centralwidget)
        self.z_end.setObjectName("z_end")
        self.label_z_end = QtWidgets.QLabel(self.centralwidget)
        self.label_z_end.setObjectName("label_z_end")
        self.verticalLayout_3.addWidget(self.z_end)
        self.verticalLayout_3.addWidget(self.label_z_end)
        # self.z_end_button = QtWidgets.QPushButton(self.centralwidget)
        # self.z_end_button.setObjectName("z_end_button")
        # self.z_end_button.clicked.connect(self.z_end_func)
        # self.z_end_button.clicked.connect(self.btn_clk)
        # self.verticalLayout_3.addWidget(self.z_end_button)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.a_pop = QtWidgets.QLineEdit(self.centralwidget)
        self.a_pop.setObjectName("a_pop")
        self.label_a_pop = QtWidgets.QLabel(self.centralwidget)
        self.label_a_pop.setObjectName("label_a_pop")
        self.verticalLayout_4.addWidget(self.a_pop)
        self.verticalLayout_4.addWidget(self.label_a_pop)
        # self.a_pop_button = QtWidgets.QPushButton(self.centralwidget)
        # self.a_pop_button.setObjectName("a_pop_button")
        # self.a_pop_button.clicked.connect(self.pop_a)
        # self.a_pop_button.clicked.connect(self.btn_clk)
        # self.verticalLayout_4.addWidget(self.a_pop_button)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.z_pop = QtWidgets.QLineEdit(self.centralwidget)
        self.z_pop.setObjectName("z_pop")
        self.label_z_pop = QtWidgets.QLabel(self.centralwidget)
        self.label_z_pop.setObjectName("label_z_pop")
        self.verticalLayout_5.addWidget(self.z_pop)
        self.verticalLayout_5.addWidget(self.label_z_pop)
        # self.z_pop_button = QtWidgets.QPushButton(self.centralwidget)
        # self.z_pop_button.setObjectName("z_pop_button")
        # self.z_pop_button.clicked.connect(self.pop_z)
        # self.z_pop_button.clicked.connect(self.btn_clk)
        # self.verticalLayout_5.addWidget(self.z_pop_button)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cable = QtWidgets.QLineEdit(self.centralwidget)
        self.cable.setObjectName("cable")
        self.label_cable = QtWidgets.QLabel(self.centralwidget)
        self.label_cable.setObjectName("label_cable")
        self.verticalLayout_6.addWidget(self.cable)
        self.verticalLayout_6.addWidget(self.label_cable)
        # self.cable_button = QtWidgets.QPushButton(self.centralwidget)
        # self.cable_button.setObjectName("cable_button")
        # self.cable_button.clicked.connect(self.cable_func)
        # self.cable_button.clicked.connect(self.btn_clk)
        # self.verticalLayout_6.addWidget(self.cable_button)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.searchbutton.setObjectName("searchbutton")
        self.searchbutton.clicked.connect(self.a_end_func)
        self.searchbutton.clicked.connect(self.z_end_func)
        self.searchbutton.clicked.connect(self.pop_z)
        self.searchbutton.clicked.connect(self.pop_a)
        self.searchbutton.clicked.connect(self.cable_func)
        self.searchbutton.clicked.connect(self.btn_clk)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setObjectName("create_button")
        self.create_button.clicked.connect(self.reset_button)
        #self.verticalLayout_7.addWidget(self.create_button)
        self.verticalLayout_7.addWidget(self.searchbutton)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_8.addWidget(self.tableView)
        self.verticalLayout_8.addWidget(self.create_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file_button.setText(_translate("MainWindow", "Enter File"))
        # self.a_end_button.setText(_translate("MainWindow", "add a_end"))
        # self.z_end_button.setText(_translate("MainWindow", "add z_end"))
        # self.a_pop_button.setText(_translate("MainWindow", "add a_pop"))
        # self.z_pop_button.setText(_translate("MainWindow", "add z_pop"))
        # self.cable_button.setText(_translate("MainWindow", "add cable"))
        self.create_button.setText(_translate("MainWindow", "Reset"))
        self.searchbutton.setText(_translate("MainWindow", "Search"))
        self.label_a_end.setText(_translate("MainWindow", "Enter in a end"))
        self.label_z_end.setText(_translate("MainWindow", "Enter in z end"))
        self.label_cable.setText(_translate("MainWindow", "Enter in cable"))
        self.label_a_pop.setText(_translate("MainWindow", "Enter in a pop"))
        self.label_z_pop.setText(_translate("MainWindow", "Enter in z pop"))
    

    def format_excel(self):
        self.sheet.read_in(self.file_entry.text())
        model = PandasModel(self.sheet.show())
        self.tableView.setModel(model)
        

    def a_end_func(self):
    	if self.a_end.text() is '':
    		pass
    	else:
	        bigger_list = []
	        list_thing = ['A_end']
	        list_thing.append(self.a_end.text())
	        bigger_list.append(list_thing)
	        self.sheet.simplifier(bigger_list)
	        self.a_end.clear()

    def z_end_func(self):
    	if self.z_end.text() is '':
    		pass
    	else:
	        bigger_list = []
	        list_thing = ['Z_end']
	        list_thing.append(self.z_end.text())
	        bigger_list.append(list_thing)
	        self.sheet.simplifier(bigger_list)
	        self.z_end.clear()
	    


    def pop_z(self):
    	if self.z_pop.text() is '':
    		pass
    	else:
	        self.sheet.POP_exception_Z_end(self.z_pop.text())
	        self.z_pop.clear()

    def pop_a(self):

    	if self.a_pop.text() is '':
    		pass
    	else:
	        self.sheet.POP_exception_A_end(self.a_pop.text())
	        self.a_pop.clear()

    def cable_func(self):

    	if self.cable.text() is '':
    		pass
    	else:
	        self.sheet.cable_exception(self.cable.text()) 
	        self.cable.clear()

    def btn_clk(self):
        # path = self.file_entry.text()
        # df = self.sheet.read_in(path)
        model = PandasModel(self.sheet.show())
        self.tableView.setModel(model)
    
    def reset_button(self):
    	self.format_excel()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

