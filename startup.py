import sys
import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainFrame(QtGui.QWidget):

    def __init__(self):
        super(MainFrame, self).__init__()

        self.initUI()

    def initUI(self):

        #Maak items aan
        opd1 = QtGui.QPushButton('Image', self)
        opd2 = QtGui.QPushButton('Index + livesearch', self)

        '''
        textEdit is een variable in de scope van initUI()
        self.textEdit maakt een attribuut in MainFrame beschikbaar voor andere functies
        '''
        #set GridLayout
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        #Toevoegen van de items (item, row, column, spawn row, spawn column)
        grid.addWidget(opd1, 0, 0, 1, 1)
        grid.addWidget(opd2, 0, 1, 1, 1)

        opd1.clicked.connect(self.image)
        opd2.clicked.connect(self.index)


        #Standaard intialiseer dingen
        self.setLayout(grid)
        self.setGeometry(350, 350, 350, 300)
        self.setWindowTitle('IPFIT5')
        self.resize(200, 10)
        self.show()

    def image(self):
        source, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Source disk bijv: /dev/sdb1')
        if os.getuid() == 0:
            os.system("python /home/jasper/SuperAwesomeSearch/scripts/getImage.py " + str(source))
        else:
            QMessageBox.about(self, "Kan niet worden uitgevoerd", "Je bent geen root")
    def index(self):
        source = str(QtGui.QFileDialog.getExistingDirectory(self, 'Select a destination', '/'))
        command = '"python /home/jasper/SuperAwesomeSearch/run_search.py '+ source + '" '
        command2 = '"python /home/jasper/SuperAwesomeSearch/scripts/Livesearch.py ' + source + '" '
        os.system('parallel -j 2 -- ' + command2 + command)



def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainFrame()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
