# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fiber2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 346)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.Kmfiber = QtWidgets.QLineEdit(Dialog)
        self.Kmfiber.setGeometry(QtCore.QRect(180, 50, 113, 20))
        self.Kmfiber.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.Kmfiber.setText("")
        self.Kmfiber.setClearButtonEnabled(True)
        self.Kmfiber.setObjectName("Kmfiber")

        self.Splidsninger = QtWidgets.QLineEdit(Dialog)
        self.Splidsninger.setGeometry(QtCore.QRect(180, 80, 113, 20))
        self.Splidsninger.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.Splidsninger.setObjectName("Splidsninger")

        self.Konnektor = QtWidgets.QLineEdit(Dialog)
        self.Konnektor.setGeometry(QtCore.QRect(180, 110, 113, 20))
        self.Konnektor.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.Konnektor.setObjectName("Konnektor")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)

        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 140, 111, 23))
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")

        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(180, 170, 111, 23))
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.lcdNumber_3 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_3.setGeometry(QtCore.QRect(180, 200, 111, 23))
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setObjectName("lcdNumber_3")

        self.lcdNumber_4 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_4.setGeometry(QtCore.QRect(180, 230, 111, 23))
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.setObjectName("lcdNumber_4")

        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 125, 211))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(300, 210, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(300, 180, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(300, 150, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(300, 240, 47, 13))
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Beregn"))
        self.label.setText(_translate("Dialog", "Indtast antal Km fiber"))
        self.label_2.setText(_translate("Dialog", "Indtast antal spildsninger"))
        self.label_3.setText(_translate("Dialog", "Indtast antal konnektorer"))
        self.label_4.setText(_translate("Dialog", "MM 850 nm dæmpning"))
        self.label_5.setText(_translate("Dialog", "MM 1300 nm dæmpning"))
        self.label_6.setText(_translate("Dialog", "SM 1310 nm dæmpning"))
        self.label_7.setText(_translate("Dialog", "SM 1550 nm dæmpning"))
        self.label_8.setText(_translate("Dialog", "[dB]"))
        self.label_9.setText(_translate("Dialog", "[dB]"))
        self.label_10.setText(_translate("Dialog", "[dB]"))
        self.label_11.setText(_translate("Dialog", "[dB]"))

#Nedenstående def skal indeholde koden der beregner fiberbugdettet
#mm850 er variablen for dæmpningen ved MM 850 nm o.s.v

    def on_click(self):
        KonValue = int(self.Konnektor.text())
        spiValue = int(self.Splidsninger.text())
        kmfib = int(self.Kmfiber.text())
        mm850=KonValue*0.5+spiValue*0.1+kmfib*2.5
        mm1300=KonValue*0.5+spiValue*0.1+kmfib*0.6
        sm1310=KonValue*0.5+spiValue*0.1+kmfib*0.35
        sm1550=KonValue*0.5+spiValue*0.1+kmfib*0.2

        self.lcdNumber.display(mm850)
        self.lcdNumber_2.display(mm1300)
        self.lcdNumber_3.display(sm1310)
        self.lcdNumber_4.display(sm1550)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

