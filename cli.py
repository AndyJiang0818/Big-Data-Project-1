import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout


def cli():
    for currentItem in tableWidget.selectedItems():
        print("Row : " + str(currentItem.row()) + " Column : " + str(currentItem.column()) + " " + currentItem.text())


app = QApplication(sys.argv)

qwidget = QWidget()

qwidget.setWindowTitle("HetioNet")
qwidget.resize(800, 1120)

layout = QVBoxLayout()
tableWidget = QTableWidget()
tableWidget.setColumnCount(5)
tableWidget.setRowCount(10)
tableWidget.setColumnWidth(0, 200)
tableWidget.setColumnWidth(1, 200)
tableWidget.setColumnWidth(2, 200)
tableWidget.setColumnWidth(3, 200)
tableWidget.setColumnWidth(4, 250)

# adding item in table
tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("DiseaseName"))
tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Drug_Name"))
tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Gene_Name"))
tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Occur_Location"))

tableWidget.setItem(0, 0, QTableWidgetItem("Anatomy::UBERON:0000002"))
tableWidget.setItem(0, 1, QTableWidgetItem("Anatomy::UBERON:0000002"))
tableWidget.setItem(0, 2, QTableWidgetItem("uterine cervix"))
tableWidget.setItem(0, 3, QTableWidgetItem("Gene::1"))
tableWidget.setItem(0, 4, QTableWidgetItem("Anatomy"))

tableWidget.setItem(1, 0, QTableWidgetItem("Disease::DOID:0050156"))
tableWidget.setItem(1, 1, QTableWidgetItem("Disease::DOID:0050156"))
tableWidget.setItem(1, 2, QTableWidgetItem("idiopathic pulmonary fibrosis"))
tableWidget.setItem(1, 3, QTableWidgetItem(""))
tableWidget.setItem(1, 4, QTableWidgetItem("Anatomy::UBERON:0000002"))

tableWidget.setItem(1, 0, QTableWidgetItem("Gene::1"))
tableWidget.setItem(1, 1, QTableWidgetItem("Gene::1"))
tableWidget.setItem(1, 2, QTableWidgetItem("A1BG"))
tableWidget.setItem(1, 3, QTableWidgetItem("Gene"))
tableWidget.setItem(1, 4, QTableWidgetItem("Anatomy::UBERON:0000002"))

tableWidget.setItem(2, 0, QTableWidgetItem("Gene::1"))
tableWidget.setItem(2, 1, QTableWidgetItem("Compound::DB00014"))
tableWidget.setItem(2, 2, QTableWidgetItem("Goserelin"))
tableWidget.setItem(1, 3, QTableWidgetItem("Disease::DOID:0050156"))
tableWidget.setItem(1, 4, QTableWidgetItem("Gene::1"))

tableWidget.setItem(3, 0, QTableWidgetItem(""))
tableWidget.setItem(3, 1, QTableWidgetItem("Desmopressin"))
tableWidget.setItem(3, 2, QTableWidgetItem("Compound::DB00035"))
tableWidget.setItem(1, 3, QTableWidgetItem("Compound"))
tableWidget.setItem(1, 4, QTableWidgetItem("Anatomy::UBERON:0000002"))

tableWidget.doubleClicked.connect(cli)
layout.addWidget(tableWidget)
qwidget.setLayout(layout)
qwidget.show()

sys.exit(app.exec_())
