# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radar.ui'
#
# Created: Thu Feb 27 22:38:40 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_RadarWidget(object):
    def setupUi(self, RadarWidget):
        RadarWidget.setObjectName(_fromUtf8("RadarWidget"))
        RadarWidget.setWindowModality(QtCore.Qt.NonModal)
        RadarWidget.setEnabled(True)
        RadarWidget.resize(861, 655)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RadarWidget.sizePolicy().hasHeightForWidth())
        RadarWidget.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(RadarWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBoxPiste = QtGui.QGroupBox(RadarWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxPiste.sizePolicy().hasHeightForWidth())
        self.groupBoxPiste.setSizePolicy(sizePolicy)
        self.groupBoxPiste.setObjectName(_fromUtf8("groupBoxPiste"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxPiste)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.runwayLayout = QtGui.QVBoxLayout()
        self.runwayLayout.setObjectName(_fromUtf8("runwayLayout"))
        self.rwplane0 = QtGui.QLabel(self.groupBoxPiste)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rwplane0.sizePolicy().hasHeightForWidth())
        self.rwplane0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rwplane0.setFont(font)
        self.rwplane0.setObjectName(_fromUtf8("rwplane0"))
        self.runwayLayout.addWidget(self.rwplane0)
        self.runway0 = QtGui.QProgressBar(self.groupBoxPiste)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runway0.sizePolicy().hasHeightForWidth())
        self.runway0.setSizePolicy(sizePolicy)
        self.runway0.setProperty("value", 0)
        self.runway0.setInvertedAppearance(False)
        self.runway0.setObjectName(_fromUtf8("runway0"))
        self.runwayLayout.addWidget(self.runway0)
        self.rwplane1 = QtGui.QLabel(self.groupBoxPiste)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rwplane1.sizePolicy().hasHeightForWidth())
        self.rwplane1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rwplane1.setFont(font)
        self.rwplane1.setObjectName(_fromUtf8("rwplane1"))
        self.runwayLayout.addWidget(self.rwplane1)
        self.runway1 = QtGui.QProgressBar(self.groupBoxPiste)
        self.runway1.setProperty("value", 0)
        self.runway1.setInvertedAppearance(False)
        self.runway1.setObjectName(_fromUtf8("runway1"))
        self.runwayLayout.addWidget(self.runway1)
        self.rwplane2 = QtGui.QLabel(self.groupBoxPiste)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rwplane2.sizePolicy().hasHeightForWidth())
        self.rwplane2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rwplane2.setFont(font)
        self.rwplane2.setObjectName(_fromUtf8("rwplane2"))
        self.runwayLayout.addWidget(self.rwplane2)
        self.runway2 = QtGui.QProgressBar(self.groupBoxPiste)
        self.runway2.setProperty("value", 0)
        self.runway2.setObjectName(_fromUtf8("runway2"))
        self.runwayLayout.addWidget(self.runway2)
        self.rwplane3 = QtGui.QLabel(self.groupBoxPiste)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rwplane3.sizePolicy().hasHeightForWidth())
        self.rwplane3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rwplane3.setFont(font)
        self.rwplane3.setObjectName(_fromUtf8("rwplane3"))
        self.runwayLayout.addWidget(self.rwplane3)
        self.runway3 = QtGui.QProgressBar(self.groupBoxPiste)
        self.runway3.setProperty("value", 0)
        self.runway3.setObjectName(_fromUtf8("runway3"))
        self.runwayLayout.addWidget(self.runway3)
        self.label = QtGui.QLabel(self.groupBoxPiste)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.runwayLayout.addWidget(self.label)
        self.horizontalSlider = QtGui.QSlider(self.groupBoxPiste)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.runwayLayout.addWidget(self.horizontalSlider)
        self.gridLayout_2.addLayout(self.runwayLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxPiste)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabelSosiri = QtGui.QTableView(RadarWidget)
        self.tabelSosiri.setObjectName(_fromUtf8("tabelSosiri"))
        self.gridLayout_3.addWidget(self.tabelSosiri, 0, 0, 1, 1)
        self.labelSosiri = QtGui.QLabel(RadarWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSosiri.setFont(font)
        self.labelSosiri.setAutoFillBackground(False)
        self.labelSosiri.setObjectName(_fromUtf8("labelSosiri"))
        self.gridLayout_3.addWidget(self.labelSosiri, 1, 0, 1, 1)
        self.tabelPlecari = QtGui.QTableView(RadarWidget)
        self.tabelPlecari.setObjectName(_fromUtf8("tabelPlecari"))
        self.gridLayout_3.addWidget(self.tabelPlecari, 2, 0, 1, 1)
        self.labelPlecari = QtGui.QLabel(RadarWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPlecari.setFont(font)
        self.labelPlecari.setObjectName(_fromUtf8("labelPlecari"))
        self.gridLayout_3.addWidget(self.labelPlecari, 3, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonStart = QtGui.QPushButton(RadarWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStart.sizePolicy().hasHeightForWidth())
        self.buttonStart.setSizePolicy(sizePolicy)
        self.buttonStart.setObjectName(_fromUtf8("buttonStart"))
        self.horizontalLayout.addWidget(self.buttonStart)
        self.buttonStop = QtGui.QPushButton(RadarWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.buttonStop.sizePolicy().hasHeightForWidth())
        self.buttonStop.setSizePolicy(sizePolicy)
        self.buttonStop.setMinimumSize(QtCore.QSize(0, 9))
        self.buttonStop.setObjectName(_fromUtf8("buttonStop"))
        self.horizontalLayout.addWidget(self.buttonStop)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(RadarWidget)
        QtCore.QMetaObject.connectSlotsByName(RadarWidget)

    def retranslateUi(self, RadarWidget):
        RadarWidget.setWindowTitle(_translate("RadarWidget", "Form", None))
        self.groupBoxPiste.setTitle(_translate("RadarWidget", "Piste", None))
        self.rwplane0.setText(_translate("RadarWidget", "TextLabel", None))
        self.rwplane1.setText(_translate("RadarWidget", "TextLabel", None))
        self.rwplane2.setText(_translate("RadarWidget", "TextLabel", None))
        self.rwplane3.setText(_translate("RadarWidget", "TextLabel", None))
        self.label.setText(_translate("RadarWidget", "Viteza simularii", None))
        self.labelSosiri.setText(_translate("RadarWidget", "Sosiri", None))
        self.labelPlecari.setText(_translate("RadarWidget", "Plecari", None))
        self.buttonStart.setText(_translate("RadarWidget", "Start", None))
        self.buttonStop.setText(_translate("RadarWidget", "Stop", None))
