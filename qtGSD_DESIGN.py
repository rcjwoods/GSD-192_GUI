# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtGSD_DESIGN.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(661, 728)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(100, 100))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 1000))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.MainVertLayout = QtGui.QVBoxLayout()
        self.MainVertLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.MainVertLayout.setContentsMargins(-1, 10, -1, -1)
        self.MainVertLayout.setSpacing(0)
        self.MainVertLayout.setObjectName(_fromUtf8("MainVertLayout"))
        self.gridLayout.addLayout(self.MainVertLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(100, 200))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setWhatsThis(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(17, 101, 594, 32))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_9.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_7 = QtGui.QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_9.addWidget(self.label_7)
        self.browserButton_7 = QtGui.QPushButton(self.horizontalLayoutWidget_6)
        self.browserButton_7.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browserButton_7.sizePolicy().hasHeightForWidth())
        self.browserButton_7.setSizePolicy(sizePolicy)
        self.browserButton_7.setMinimumSize(QtCore.QSize(80, 15))
        self.browserButton_7.setObjectName(_fromUtf8("browserButton_7"))
        self.horizontalLayout_9.addWidget(self.browserButton_7)
        self.filePathEdit_7 = QtGui.QLineEdit(self.horizontalLayoutWidget_6)
        self.filePathEdit_7.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePathEdit_7.sizePolicy().hasHeightForWidth())
        self.filePathEdit_7.setSizePolicy(sizePolicy)
        self.filePathEdit_7.setMinimumSize(QtCore.QSize(400, 30))
        self.filePathEdit_7.setObjectName(_fromUtf8("filePathEdit_7"))
        self.horizontalLayout_9.addWidget(self.filePathEdit_7)
        self.horizontalLayoutWidget_9 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(17, 25, 592, 32))
        self.horizontalLayoutWidget_9.setObjectName(_fromUtf8("horizontalLayoutWidget_9"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_10.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_11 = QtGui.QLabel(self.horizontalLayoutWidget_9)
        self.label_11.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_10.addWidget(self.label_11)
        self.browserButton = QtGui.QPushButton(self.horizontalLayoutWidget_9)
        self.browserButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browserButton.sizePolicy().hasHeightForWidth())
        self.browserButton.setSizePolicy(sizePolicy)
        self.browserButton.setMinimumSize(QtCore.QSize(80, 15))
        self.browserButton.setObjectName(_fromUtf8("browserButton"))
        self.horizontalLayout_10.addWidget(self.browserButton)
        self.filePathEdit_3 = QtGui.QLineEdit(self.horizontalLayoutWidget_9)
        self.filePathEdit_3.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePathEdit_3.sizePolicy().hasHeightForWidth())
        self.filePathEdit_3.setSizePolicy(sizePolicy)
        self.filePathEdit_3.setMinimumSize(QtCore.QSize(400, 30))
        self.filePathEdit_3.setObjectName(_fromUtf8("filePathEdit_3"))
        self.horizontalLayout_10.addWidget(self.filePathEdit_3)
        self.horizontalLayoutWidget_10 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(17, 63, 592, 32))
        self.horizontalLayoutWidget_10.setObjectName(_fromUtf8("horizontalLayoutWidget_10"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_11.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_12 = QtGui.QLabel(self.horizontalLayoutWidget_10)
        self.label_12.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_11.addWidget(self.label_12)
        self.browserButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget_10)
        self.browserButton_3.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browserButton_3.sizePolicy().hasHeightForWidth())
        self.browserButton_3.setSizePolicy(sizePolicy)
        self.browserButton_3.setMinimumSize(QtCore.QSize(80, 15))
        self.browserButton_3.setObjectName(_fromUtf8("browserButton_3"))
        self.horizontalLayout_11.addWidget(self.browserButton_3)
        self.filePathEdit_5 = QtGui.QLineEdit(self.horizontalLayoutWidget_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePathEdit_5.sizePolicy().hasHeightForWidth())
        self.filePathEdit_5.setSizePolicy(sizePolicy)
        self.filePathEdit_5.setMinimumSize(QtCore.QSize(400, 30))
        self.filePathEdit_5.setObjectName(_fromUtf8("filePathEdit_5"))
        self.horizontalLayout_11.addWidget(self.filePathEdit_5)
        self.runButton = QtGui.QPushButton(self.groupBox)
        self.runButton.setGeometry(QtCore.QRect(520, 140, 85, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        self.runButton.setMinimumSize(QtCore.QSize(80, 50))
        self.runButton.setIconSize(QtCore.QSize(24, 24))
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(100, 225))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(17, 25, 591, 32))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.browserButton_4 = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browserButton_4.sizePolicy().hasHeightForWidth())
        self.browserButton_4.setSizePolicy(sizePolicy)
        self.browserButton_4.setObjectName(_fromUtf8("browserButton_4"))
        self.horizontalLayout_6.addWidget(self.browserButton_4)
        self.loadButton = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadButton.sizePolicy().hasHeightForWidth())
        self.loadButton.setSizePolicy(sizePolicy)
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.horizontalLayout_6.addWidget(self.loadButton)
        self.filePathEdit_4 = QtGui.QLineEdit(self.horizontalLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePathEdit_4.sizePolicy().hasHeightForWidth())
        self.filePathEdit_4.setSizePolicy(sizePolicy)
        self.filePathEdit_4.setMinimumSize(QtCore.QSize(300, 30))
        self.filePathEdit_4.setObjectName(_fromUtf8("filePathEdit_4"))
        self.horizontalLayout_6.addWidget(self.filePathEdit_4)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(17, 63, 481, 29))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.plotButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotButton.sizePolicy().hasHeightForWidth())
        self.plotButton.setSizePolicy(sizePolicy)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.horizontalLayout_2.addWidget(self.plotButton)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(17, 100, 481, 29))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.comboBox_R1 = QtGui.QComboBox(self.horizontalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_R1.sizePolicy().hasHeightForWidth())
        self.comboBox_R1.setSizePolicy(sizePolicy)
        self.comboBox_R1.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_R1.setObjectName(_fromUtf8("comboBox_R1"))
        self.horizontalLayout_3.addWidget(self.comboBox_R1)
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(30, 0))
        self.label.setMaximumSize(QtCore.QSize(30, 29))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setLineWidth(5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.comboBox_R2 = QtGui.QComboBox(self.horizontalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_R2.sizePolicy().hasHeightForWidth())
        self.comboBox_R2.setSizePolicy(sizePolicy)
        self.comboBox_R2.setObjectName(_fromUtf8("comboBox_R2"))
        self.horizontalLayout_3.addWidget(self.comboBox_R2)
        self.plotRangeButton = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotRangeButton.sizePolicy().hasHeightForWidth())
        self.plotRangeButton.setSizePolicy(sizePolicy)
        self.plotRangeButton.setObjectName(_fromUtf8("plotRangeButton"))
        self.horizontalLayout_3.addWidget(self.plotRangeButton)
        self.horizontalLayoutWidget_7 = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(17, 140, 481, 29))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_5.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtGui.QLabel(self.horizontalLayoutWidget_7)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.comboBox_2 = QtGui.QComboBox(self.horizontalLayoutWidget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.horizontalLayout_5.addWidget(self.comboBox_2)
        self.checkBox = QtGui.QCheckBox(self.horizontalLayoutWidget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_5.addWidget(self.checkBox)
        self.plotImageButton = QtGui.QPushButton(self.horizontalLayoutWidget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotImageButton.sizePolicy().hasHeightForWidth())
        self.plotImageButton.setSizePolicy(sizePolicy)
        self.plotImageButton.setMinimumSize(QtCore.QSize(80, 15))
        self.plotImageButton.setObjectName(_fromUtf8("plotImageButton"))
        self.horizontalLayout_5.addWidget(self.plotImageButton)
        self.clearPlotButton = QtGui.QPushButton(self.groupBox_2)
        self.clearPlotButton.setGeometry(QtCore.QRect(520, 140, 85, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearPlotButton.sizePolicy().hasHeightForWidth())
        self.clearPlotButton.setSizePolicy(sizePolicy)
        self.clearPlotButton.setMinimumSize(QtCore.QSize(80, 50))
        self.clearPlotButton.setObjectName(_fromUtf8("clearPlotButton"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(17, 180, 481, 29))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_9 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout.addWidget(self.label_9)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 15))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.plotStripsButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotStripsButton.sizePolicy().hasHeightForWidth())
        self.plotStripsButton.setSizePolicy(sizePolicy)
        self.plotStripsButton.setMinimumSize(QtCore.QSize(80, 15))
        self.plotStripsButton.setObjectName(_fromUtf8("plotStripsButton"))
        self.horizontalLayout.addWidget(self.plotStripsButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 661, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setVisible(True)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "PLOT WINDOW", None))
        self.groupBox.setTitle(_translate("MainWindow", "  BINARY DATA CONVERSION", None))
        self.label_7.setText(_translate("MainWindow", " OUTPUT FILE   ", None))
        self.browserButton_7.setText(_translate("MainWindow", "Browse", None))
        self.filePathEdit_7.setText(_translate("MainWindow", "D:\\detdev\\maia\\python\\", None))
        self.label_11.setText(_translate("MainWindow", " DECODER FILE", None))
        self.browserButton.setText(_translate("MainWindow", "Browse", None))
        self.filePathEdit_3.setText(_translate("MainWindow", "D:\\detdev\\maia\\python\\qtGSD\\gsd_parse.out", None))
        self.label_12.setText(_translate("MainWindow", " INPUT FILE      ", None))
        self.browserButton_3.setText(_translate("MainWindow", "Browse", None))
        self.filePathEdit_5.setText(_translate("MainWindow", "D:\\detdev\\maia\\python\\", None))
        self.runButton.setText(_translate("MainWindow", "Run", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "  PLOT DATA", None))
        self.label_3.setText(_translate("MainWindow", " DATA FILE   ", None))
        self.browserButton_4.setText(_translate("MainWindow", "Browse", None))
        self.loadButton.setText(_translate("MainWindow", "Load", None))
        self.filePathEdit_4.setText(_translate("MainWindow", "D:\\detdev\\maia\\python\\", None))
        self.label_4.setText(_translate("MainWindow", " PLOT STRIP ", None))
        self.plotButton.setText(_translate("MainWindow", "Plot", None))
        self.label_5.setText(_translate("MainWindow", " PLOT SERIES", None))
        self.label.setText(_translate("MainWindow", "to", None))
        self.plotRangeButton.setText(_translate("MainWindow", "Plot", None))
        self.label_8.setText(_translate("MainWindow", " PLOT SPECTRA AS 2-D IMAGE", None))
        self.checkBox.setText(_translate("MainWindow", "Log", None))
        self.plotImageButton.setText(_translate("MainWindow", "Plot Image", None))
        self.clearPlotButton.setText(_translate("MainWindow", "Clear", None))
        self.label_9.setText(_translate("MainWindow", " PLOT TOTAL COUNTS vs STRIP", None))
        self.pushButton.setText(_translate("MainWindow", "Update", None))
        self.plotStripsButton.setText(_translate("MainWindow", "Plot Strips", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

