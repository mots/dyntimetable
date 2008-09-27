# coding: utf-8
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
import stunden
import sys
 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 
 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 
        
        stundenpl = stunden.StundenPlan('8bi')
        tablemodel = MyTableModel(stundenpl.getLessons(), self)
        suppllist = stundenpl.getCurrentSups()
        entflist = []
        for i in suppllist:
            if i[4] == u'entf\xe4llt':
                suppllist.remove(i)
                entflist.append(i)
        entfpos = []
        for i in entflist:
            entfpos.append(i[:2])
        supplpos = []
        for i in suppllist:
            supplpos.append(i[:2])
        tablemodel.setentfallpos(entfpos)
        tablemodel.setsupplpos(supplpos)
        tableview = MyTableView(self, suppllist, entflist, supplpos, entfpos)
        tableview.setModel(tablemodel) 
 
        layout = QVBoxLayout(self) 
        layout.addWidget(tableview) 
        self.setLayout(layout)
       # print tableview.horizontalHeader().size().width()
        self.resize(640, 400)
        tableview.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        tableview.verticalHeader().setResizeMode(QHeaderView.Stretch)
       # tableview.horizontalHeader().setHeaderData(0, Qt.Horizontal, QVariant('Dongs'))


class MyTableView(QTableView):
    def __init__(self, parent, suppllist, entflist, supplpos, entfpos):
        self.suppllist = suppllist
        self.entflist = entflist
        self.supplpos = supplpos
        self.entfpos = entfpos
        QTableView.__init__(self, parent)

    def mouseDoubleClickEvent(self, ev):
        cell = self.selectionModel().selection().indexes()[0]
        if [cell.column(), cell.row()] in self.supplpos:
            for i in self.suppllist:
                if i[:2] == [cell.column(), cell.row()]:
                    suppl = i
            QMessageBox.information(self, 'Details', 'Lehrer(in) $Lehrername ist abwesend und wird von <b>'+ suppl[2] + '</b> vertreten. Klassenraum: ' + suppl[3], QMessageBox.Ok)
        elif [cell.column(), cell.row()] in self.entfpos:
            QMessageBox.information(self, 'Details', u'Lehrer(in) $Lehrername ist abwesend, die Stunde entfällt...')


#            QMessageBox.information(self.parent, 'Details', 
        #        QMessageBox.information(self, 'dongs', str(cell.column())+str(cell.row()), QMessageBox.Ok)

class MyTableModel(QAbstractTableModel): 
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args) 
        self.arraydata = datain
        self.entfallpos = []
        self.supplpos = []

    def setentfallpos(self, entfallpos):
        self.entfallpos = entfallpos

    def setsupplpos(self, supplpos):
        self.supplpos = supplpos

    def rowCount(self, parent):
        rowcount = max([len(x) for x in self.arraydata])
        for x in self.arraydata:
            while len(x) < rowcount:
                x.append('')
        return rowcount 
 
    def columnCount(self, parent): 
        return len(self.arraydata) 
 
    def data(self, index, role):
        if role == Qt.BackgroundRole and [index.column(), index.row()] in self.entfallpos:
            return QVariant(QBrush(QColor(239, 41, 41)))
        if role == Qt.BackgroundRole and [index.column(), index.row()] in self.supplpos:
            return QVariant(QBrush(QColor(252, 233, 79)))
        elif not index.isValid(): 
            return QVariant() 
        elif role != Qt.DisplayRole: 
            return QVariant() 
        return QVariant(self.arraydata[index.column()][index.row()]) 

    def headerData(self,section,orientation,role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return QVariant(int(Qt.AlignHCenter|Qt.AlignVCenter))
            return QVariant(int(Qt.AlignRight|Qt.AlignVCenter))
        if role != Qt.DisplayRole:
            return QVariant()
        if orientation == Qt.Horizontal:
            if section == 0:
                return QVariant('Montag')
            elif section == 1:
                return QVariant('Dienstag')
            elif section == 2:
                return QVariant('Mittwoch')
            elif section == 3:
                return QVariant('Donnerstag')
            elif section == 4:
                return QVariant('Freitag')
        return QVariant(int(section+1)) 

if __name__ == "__main__": 
    main()
