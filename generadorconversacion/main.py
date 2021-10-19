################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import json

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.borrar_conversation.clicked.connect(self.remove_theme)
        self.ui.add_subline.clicked.connect(self.add_subline)
        self.ui.add_line.clicked.connect(self.add_line)
        self.ui.generate_conversation.clicked.connect(self.generate_conversation)
        self.ui.remove_element.clicked.connect(self.remove_element)
        self.ui.conversation_tree.selectedItems

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def add_subline(self):
        new_item = QTreeWidgetItem()
        getSelected = self.ui.conversation_tree.currentItem()
        new_item.setText(0, self.ui.line_phrase.text())
        new_item.setText(2, self.ui.line_keywords.text())
        # print(self.ui.needs_a_response.isChecked())
        
        if self.ui.needs_a_response.isChecked() == True:
            new_item.setText(4, "1")
        else:
            new_item.setText(4, "0")

        if self.ui.yes_or_no.isChecked() == True:
            new_item.setText(3, "1")
        else:
            new_item.setText(3, "0")     

        if self.ui.returns_to_start.isChecked() == True:
            new_item.setText(5, "1")
        else:
            new_item.setText(5, "0")  

        if getSelected:
            getSelected.addChild(new_item)
        else:
            print("no está seleccionado")

    def add_line(self):
        new_item = QTreeWidgetItem()
        new_item.setText(0, self.ui.line_phrase.text())
        
        if self.ui.needs_a_response.isChecked() == True:
            new_item.setText(4, "1")
        else:
            new_item.setText(4, "0")

        if self.ui.yes_or_no.isChecked() == True:
            new_item.setText(3, "1")
        else:
            new_item.setText(3, "0")     

        if self.ui.returns_to_start.isChecked() == True:
            new_item.setText(5, "1")
        else:
            new_item.setText(5, "0") 

        self.ui.conversation_tree.addTopLevelItem(new_item)

    def remove_theme(self):
        self.ui.conversation_tree.clear() 
        # new_item = QTreeWidgetItem()
        # new_item.setText(0, self.ui.conversation_name.text())
        # self.ui.conversation_tree.addTopLevelItem(new_item)

    def remove_element(self):
        print(self.ui.conversation_tree.currentItem())
        self.ui.conversation_tree.currentItem().removeChild(self.ui.conversation_tree.currentItem())

    def generate_conversation(self):
        main_json= {}

        main_lines_vector = []
        lines_vector = []

        item_vector = []
        name_vector = []

        conversation_name = self.ui.conversation_name.text()
        iterator = QTreeWidgetItemIterator(self.ui.conversation_tree)

        while iterator.value():
            item = iterator.value()

            print("")  
            print("Nueva linea")  
            print("")  

            index = self.ui.conversation_tree.indexFromItem(item, 0)

            if item.parent() == None:
                line_name = conversation_name+"_"+str(index.row())
                main_lines_vector.append(line_name)
            else:
                indice_nombre = item_vector.index(item.parent())
                line_name = name_vector[indice_nombre]+"_"+str(index.row())                

            next_possible_lines = []
            phrase = item.text(0)

            if item.text(2) == "si":
                keywords = ["okey", "vale", "perfe", "si", "guay","claro"]
            elif item.text(2) == "no":
                keywords = ["no", "que va", "para nada", "en absoluto"]
            else:
                keywords = item.text(2).split(",")

            binary = (item.text(3))
            to_start = (item.text(5))
            needs_response = (item.text(4))
            if item.childCount() > 0:                     
                print("Número de childs: ",item.childCount())                 
                for i in range(0,item.childCount()):
                    next_possible_lines.append(line_name+"_"+str(i))

            if not item in item_vector:
                item_vector.append(item)
                name_vector.append(line_name)

            # print("nombre de linea",line_name)
            # print("posibles lineas siguientes",next_possible_lines)
            # print("frase",phrase)
            # print("palabras clave",keywords)
            # print("es binario",binary)
            # print("al inicio",to_start)
            # print("necesita respuesta",needs_response)  

            item_json =  {
                    "line_name" : line_name,
                    "next_possible_lines" : next_possible_lines,     
                    "phrase" : phrase,
                    "emotion" : 0,
                    "keywords" : keywords,
                    "binary" : int(binary),
                    "to_start" : int(to_start),
                    "needs_response" : int(needs_response)
                }
            
            lines_vector.append(item_json)

            print(item_json)

            iterator+=1
        main_json["main_lines"] = main_lines_vector
        main_json["lines"] = lines_vector

        print("")
        print("Lineas: ",main_json["lines"])
        print("")
        print("Lineas principales: ",main_json["main_lines"])

        with open("conversaciones/"+conversation_name+".json", "w+") as f:
            json.dump(main_json, f)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
