# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'habit_card_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CommandBar, ElevatedCardWidget, ImageLabel,
    ProgressBar, StrongBodyLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(265, 280)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(250, 280))
        Form.setMaximumSize(QSize(265, 280))
        Form.setStyleSheet(u"ElevatedCardWidget{\n"
"	border: 1px solid rgb(234, 234, 234);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"BodyLabel, #rewardFrame{\n"
"	border-radius: 8px;\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = ElevatedCardWidget(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.imageLabel = ImageLabel(self.frame)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setMaximumSize(QSize(64, 64))
        self.imageLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.imageLabel)

        self.verticalSpacer = QSpacerItem(10, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.rewardFrame = QFrame(self.frame)
        self.rewardFrame.setObjectName(u"rewardFrame")
        self.rewardFrame.setFrameShape(QFrame.StyledPanel)
        self.rewardFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.rewardFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rewardIconLabel = ImageLabel(self.rewardFrame)
        self.rewardIconLabel.setObjectName(u"rewardIconLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.rewardIconLabel.sizePolicy().hasHeightForWidth())
        self.rewardIconLabel.setSizePolicy(sizePolicy1)
        self.rewardIconLabel.setMinimumSize(QSize(32, 32))
        self.rewardIconLabel.setMaximumSize(QSize(32, 32))
        self.rewardIconLabel.setSizeIncrement(QSize(32, 32))
        self.rewardIconLabel.setBaseSize(QSize(32, 32))
        self.rewardIconLabel.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.rewardIconLabel)

        self.rewardLabel = StrongBodyLabel(self.rewardFrame)
        self.rewardLabel.setObjectName(u"rewardLabel")
        self.rewardLabel.setStyleSheet(u"color: rgb(170, 170, 0);")
        self.rewardLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.rewardLabel)


        self.horizontalLayout.addWidget(self.rewardFrame)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.contentLabel = BodyLabel(self.frame)
        self.contentLabel.setObjectName(u"contentLabel")
        self.contentLabel.setWordWrap(True)
        self.contentLabel.setMargin(10)

        self.verticalLayout.addWidget(self.contentLabel)

        self.progressLabel = BodyLabel(self.frame)
        self.progressLabel.setObjectName(u"progressLabel")
        self.progressLabel.setMargin(10)

        self.verticalLayout.addWidget(self.progressLabel)

        self.progressBar = ProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.commandBar = CommandBar(self.frame)
        self.commandBar.setObjectName(u"commandBar")
        self.commandBar.setMinimumSize(QSize(225, 0))

        self.verticalLayout.addWidget(self.commandBar, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.imageLabel.setText(QCoreApplication.translate("Form", u"imageLabel", None))
        self.rewardIconLabel.setText(QCoreApplication.translate("Form", u"rewardIconLabel", None))
        self.rewardLabel.setText(QCoreApplication.translate("Form", u"rewardtLabel", None))
        self.contentLabel.setText(QCoreApplication.translate("Form", u"contentLabel", None))
        self.progressLabel.setText(QCoreApplication.translate("Form", u"progressLbel", None))
    # retranslateUi

