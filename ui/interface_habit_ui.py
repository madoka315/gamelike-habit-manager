# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_habit.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import (CommandBar, SmoothScrollArea)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(490, 419)
        Frame.setStyleSheet(u"QScrollArea{\n"
"	background: transparent; border: none\n"
"}\n"
"\n"
"#widget {\n"
"	background-color: rgb(243, 243, 243);\n"
"	border-radius: 8px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.commandbar = CommandBar(Frame)
        self.commandbar.setObjectName(u"commandbar")
        self.commandbar.setMinimumSize(QSize(0, 10))

        self.verticalLayout_2.addWidget(self.commandbar, 0, Qt.AlignRight|Qt.AlignTop)

        self.scrollArea = SmoothScrollArea(Frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 472, 385))
        self.scrollArea.setWidget(self.widget)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
    # retranslateUi

