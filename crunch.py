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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(366, 416)
        Form.setMaximumSize(QtCore.QSize(366, 416))
        Form.setStyleSheet(_fromUtf8("QWidget{\n"
"  background:black;\n"
"}"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../escudo.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(136, 111, 20);\n"
"font: 75 14pt \"Birch Std\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setStyleSheet(_fromUtf8("color:white;\n"
""))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.generate = QtGui.QPushButton(self.frame_2)
        self.generate.setMaximumSize(QtCore.QSize(100, 16777215))
        self.generate.setStyleSheet(_fromUtf8("QPushButton{\n"
"  background:rgb(158, 114, 11);\n"
"  color:black;\n"
"}\n"
"QPushButton:hover{\n"
"  background: black;\n"
"  color:white;\n"
"  border:1px solid white;\n"
"}"))
        self.generate.setObjectName(_fromUtf8("generate"))
        self.gridLayout_3.addWidget(self.generate, 7, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.filename = QtGui.QLineEdit(self.frame_2)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.gridLayout_3.addWidget(self.filename, 0, 1, 1, 3)
        self.caractere = QtGui.QLineEdit(self.frame_2)
        self.caractere.setObjectName(_fromUtf8("caractere"))
        self.gridLayout_3.addWidget(self.caractere, 4, 1, 1, 3)
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)
        self.nbcaractere = QtGui.QSpinBox(self.frame_2)
        self.nbcaractere.setMaximum(899999999)
        self.nbcaractere.setObjectName(_fromUtf8("nbcaractere"))
        self.gridLayout_3.addWidget(self.nbcaractere, 1, 1, 1, 3)
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.aa = QtGui.QSpinBox(self.frame_2)
        self.aa.setMaximumSize(QtCore.QSize(2222222, 16777215))
        self.aa.setMinimum(2)
        self.aa.setMaximum(222222222)
        self.aa.setObjectName(_fromUtf8("aa"))
        self.gridLayout_3.addWidget(self.aa, 2, 1, 1, 3)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">CrunchInS - Gui</span></p></body></html>", None))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#70540e;\">♦♦♦♦♦♦[H4ckT3ur]♦♦♦♦♦</span></p></body></html>", None))
        self.generate.setText(_translate("Form", "Generate", None))
        self.label_8.setText(_translate("Form", "Nombre de caractere :", None))
        self.label_3.setText(_translate("Form", "Nom du fichier de sorti :", None))
        self.label_6.setText(_translate("Form", "Caractere :", None))
        self.label_4.setText(_translate("Form", "Nombre de ligne a generere :", None))

