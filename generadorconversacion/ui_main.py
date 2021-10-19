# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1075, 644)
        MainWindow.setMinimumSize(QSize(880, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Roboto Condensed Light")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(60, 231, 195);")

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.conversation_tree = QTreeWidget(self.content_bar)
        self.conversation_tree.setObjectName(u"conversation_tree")
        self.conversation_tree.setGeometry(QRect(10, 100, 781, 431))
        self.label_title_2 = QLabel(self.content_bar)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setGeometry(QRect(20, 30, 231, 31))
        self.label_title_2.setFont(font1)
        self.label_title_2.setStyleSheet(u"color: rgb(60, 231, 195);")
        self.conversation_name = QLineEdit(self.content_bar)
        self.conversation_name.setObjectName(u"conversation_name")
        self.conversation_name.setGeometry(QRect(260, 30, 231, 25))
        self.label_title_3 = QLabel(self.content_bar)
        self.label_title_3.setObjectName(u"label_title_3")
        self.label_title_3.setGeometry(QRect(860, 70, 121, 31))
        self.label_title_3.setFont(font1)
        self.label_title_3.setStyleSheet(u"color: rgb(60, 231, 195);")
        self.line_phrase = QLineEdit(self.content_bar)
        self.line_phrase.setObjectName(u"line_phrase")
        self.line_phrase.setGeometry(QRect(810, 100, 231, 25))
        self.label_title_4 = QLabel(self.content_bar)
        self.label_title_4.setObjectName(u"label_title_4")
        self.label_title_4.setGeometry(QRect(880, 130, 81, 31))
        self.label_title_4.setFont(font1)
        self.label_title_4.setStyleSheet(u"color: rgb(60, 231, 195);")
        self.line_keywords = QLineEdit(self.content_bar)
        self.line_keywords.setObjectName(u"line_keywords")
        self.line_keywords.setGeometry(QRect(810, 160, 231, 25))
        self.generate_conversation = QPushButton(self.content_bar)
        self.generate_conversation.setObjectName(u"generate_conversation")
        self.generate_conversation.setGeometry(QRect(840, 480, 171, 41))
        self.generate_conversation.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.add_subline = QPushButton(self.content_bar)
        self.add_subline.setObjectName(u"add_subline")
        self.add_subline.setGeometry(QRect(840, 370, 171, 31))
        self.add_subline.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.borrar_conversation = QPushButton(self.content_bar)
        self.borrar_conversation.setObjectName(u"borrar_conversation")
        self.borrar_conversation.setGeometry(QRect(40, 70, 171, 21))
        self.borrar_conversation.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.label_title_5 = QLabel(self.content_bar)
        self.label_title_5.setObjectName(u"label_title_5")
        self.label_title_5.setGeometry(QRect(870, 30, 101, 31))
        self.label_title_5.setFont(font1)
        self.label_title_5.setStyleSheet(u"color: rgb(60, 231, 195);")
        self.add_line = QPushButton(self.content_bar)
        self.add_line.setObjectName(u"add_line")
        self.add_line.setGeometry(QRect(840, 320, 171, 31))
        self.add_line.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.remove_element = QPushButton(self.content_bar)
        self.remove_element.setObjectName(u"remove_element")
        self.remove_element.setGeometry(QRect(840, 420, 171, 31))
        self.remove_element.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.frame = QFrame(self.content_bar)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(820, 200, 211, 101))
        self.frame.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.returns_to_start = QCheckBox(self.frame)
        self.returns_to_start.setObjectName(u"returns_to_start")
        self.returns_to_start.setGeometry(QRect(10, 70, 201, 23))
        self.returns_to_start.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.yes_or_no = QCheckBox(self.frame)
        self.yes_or_no.setObjectName(u"yes_or_no")
        self.yes_or_no.setGeometry(QRect(10, 10, 201, 23))
        self.yes_or_no.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.yes_or_no.setChecked(False)
        self.needs_a_response = QCheckBox(self.frame)
        self.needs_a_response.setObjectName(u"needs_a_response")
        self.needs_a_response.setGeometry(QRect(10, 40, 201, 23))
        self.needs_a_response.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: rgb(33, 33, 75);")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font2 = QFont()
        font2.setFamily(u"Roboto")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(128, 102, 168);")

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_2.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Conversation designer", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        ___qtreewidgetitem = self.conversation_tree.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"to_start", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"needs_response", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"binary", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"keywords", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"emotion", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"phrase", None));
        self.label_title_2.setText(QCoreApplication.translate("MainWindow", u"Nombre de la conversaci\u00f3n", None))
        self.label_title_3.setText(QCoreApplication.translate("MainWindow", u"Frase de linea", None))
        self.label_title_4.setText(QCoreApplication.translate("MainWindow", u"Keywords", None))
        self.line_keywords.setText("")
        self.generate_conversation.setText(QCoreApplication.translate("MainWindow", u"Generar conversaci\u00f3n", None))
        self.add_subline.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir subl\u00ednea", None))
        self.borrar_conversation.setText(QCoreApplication.translate("MainWindow", u"Borrar conversaci\u00f3n", None))
        self.label_title_5.setText(QCoreApplication.translate("MainWindow", u"Nueva linea", None))
        self.add_line.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir l\u00ednea", None))
        self.remove_element.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionadas", None))
        self.returns_to_start.setText(QCoreApplication.translate("MainWindow", u"\u00bfVuelve a la rama inicial?", None))
        self.yes_or_no.setText(QCoreApplication.translate("MainWindow", u"\u00bfSe responde con si o no?", None))
        self.needs_a_response.setText(QCoreApplication.translate("MainWindow", u"\u00bfNecesita una respuesta?", None))
        self.label_credits.setText("")
    # retranslateUi

