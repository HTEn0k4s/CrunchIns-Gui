import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from crunch import Ui_Form
import itertools
class affiche(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.liste = QTreeWidget()
        self.liste.setColumnCount(1);
        self.liste.show()
class crunchins(QWidget):
    def genere(self):
        l = 0
        bb =0
        self.aa = self.ui.aa.value()
        f = self.ui.filename.text()
        openy = open(f,"w")
        while l<self.ui.nbcaractere.value():
            b = map(''.join,itertools.product(str(self.ui.caractere.text()),repeat=self.aa))
            for it in b:
                bb+=1
                print it,str(bb)
                openy.write(it+"\n")
                item = QTreeWidgetItem(af.liste)
                item.setText(0,str(it))
                if bb == self.ui.nbcaractere.value():
                    break
                QApplication.processEvents()
            l = l+bb
    def __init__(self, parent = None):
        super(crunchins, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect(self.ui.generate,SIGNAL('clicked()'),self.genere)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = crunchins()
    d.setWindowTitle("CrunchInS ")
    af = affiche()
    af.start()
    d.show()
    app.exec_()
