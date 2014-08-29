import sys
from PyQt4 import QtGui, QtCore


class MainFrame(QtGui.QWidget):

    def __init__(self):
        super(MainFrame, self).__init__()

        self.initUI()

    def initUI(self):
        #Maak items aan
        self.dirLbl = QtGui.QLabel(self.filepath)

        #file Dir
        self.pathRoot = QtCore.QDir.rootPath()
        self.model = QtGui.QFileSystemModel(self)
        self.model.setRootPath(self.filepath)
        self.indexRoot = self.model.index(self.model.rootPath())
        self.treeView = QtGui.QTreeView(self)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.indexRoot)
        self.treeView.clicked.connect(self.on_treeView_clicked)

        '''
        textEdit is een variable in de scope van initUI()
        self.textEdit maakt een attribuut in MainFrame beschikbaar voor andere functies
        '''


        #set GridLayout
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        #Toevoegen van de items (item, row, column, spawn row, spawn column)


        grid.addWidget(self.dirLbl, 0, 0, 1, 3)

        grid.addWidget(self.treeView,1, 0, 1, 3)


        #Wat moet de item uitvoeren bij een actie


        #Standaard intialiseer dingen
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Live search')
        self.resize(800,600)
        self.show()


    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent()) #Get label
        filename = self.model.fileName(indexItem) #laatste gedeelte
        filepath = self.model.filePath(indexItem) #alles
        self.dirLbl.setText(filepath)


def main(filepath):
    MainFrame.filepath = filepath
    app = QtGui.QApplication(sys.argv)
    ex = MainFrame()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main(sys.argv[1])
