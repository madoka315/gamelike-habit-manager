# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reward_card_widget.ui'
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

from qfluentwidgets import (BodyLabel, ElevatedCardWidget, ImageLabel, PrimaryPushButton,
    StrongBodyLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 125))
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = ElevatedCardWidget(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.imageLabel_2 = ImageLabel(self.frame_2)
        self.imageLabel_2.setObjectName(u"imageLabel_2")
        self.imageLabel_2.setMaximumSize(QSize(64, 64))

        self.horizontalLayout.addWidget(self.imageLabel_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.descLabel = StrongBodyLabel(self.frame_2)
        self.descLabel.setObjectName(u"descLabel")
        self.descLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.descLabel)

        self.completionLabel = BodyLabel(self.frame_2)
        self.completionLabel.setObjectName(u"completionLabel")
        self.completionLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.completionLabel)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = PrimaryPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton, 0, Qt.AlignRight|Qt.AlignBottom)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rewardIconLabel = ImageLabel(self.frame)
        self.rewardIconLabel.setObjectName(u"rewardIconLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.rewardIconLabel.sizePolicy().hasHeightForWidth())
        self.rewardIconLabel.setSizePolicy(sizePolicy1)
        self.rewardIconLabel.setMinimumSize(QSize(32, 32))
        self.rewardIconLabel.setMaximumSize(QSize(32, 32))
        self.rewardIconLabel.setSizeIncrement(QSize(32, 32))
        self.rewardIconLabel.setBaseSize(QSize(32, 32))
        self.rewardIconLabel.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.rewardIconLabel)

        self.consumeLabel = StrongBodyLabel(self.frame)
        self.consumeLabel.setObjectName(u"consumeLabel")
        self.consumeLabel.setStyleSheet(u"color: rgb(170, 170, 0);")
        self.consumeLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.consumeLabel)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.reward_complete)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.imageLabel_2.setText(QCoreApplication.translate("Form", u"ImageLabel", None))
        self.descLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.completionLabel.setText(QCoreApplication.translate("Form", u"\u8fd8\u6ca1\u6709\u5151\u6362\u8fc7\u8fd9\u4e2a\u5956\u52b1", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5151\u6362\u5956\u52b1", None))
        self.rewardIconLabel.setText(QCoreApplication.translate("Form", u"rewardIconLabel", None))
        self.consumeLabel.setText(QCoreApplication.translate("Form", u"rewardtLabel", None))
    # retranslateUi

