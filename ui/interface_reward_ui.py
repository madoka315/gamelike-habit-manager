# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_reward.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

from qfluentwidgets import (ImageLabel, SmoothScrollArea, StrongBodyLabel)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(456, 401)
        Frame.setStyleSheet(u"QScrollArea{\n"
"	background: transparent; border: none\n"
"}\n"
"\n"
"#widget {\n"
"	background-color: rgb(243, 243, 243);\n"
"	border-radius: 8px;\n"
"}")
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rewardIconLabel = ImageLabel(self.frame)
        self.rewardIconLabel.setObjectName(u"rewardIconLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rewardIconLabel.sizePolicy().hasHeightForWidth())
        self.rewardIconLabel.setSizePolicy(sizePolicy)
        self.rewardIconLabel.setMinimumSize(QSize(36, 36))

        self.horizontalLayout.addWidget(self.rewardIconLabel)

        self.rewardLabel = StrongBodyLabel(self.frame)
        self.rewardLabel.setObjectName(u"rewardLabel")
        self.rewardLabel.setStyleSheet(u"color: rgb(170, 170, 0);")

        self.horizontalLayout.addWidget(self.rewardLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame)

        self.scrollArea = SmoothScrollArea(Frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 438, 321))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vlayout = QVBoxLayout()
        self.vlayout.setObjectName(u"vlayout")

        self.verticalLayout_3.addLayout(self.vlayout)

        self.scrollArea.setWidget(self.widget)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.rewardIconLabel.setText(QCoreApplication.translate("Frame", u"rewardIconLabel", None))
        self.rewardLabel.setText(QCoreApplication.translate("Frame", u"TextLabel", None))
    # retranslateUi

