# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_data.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (ImageLabel, SmoothScrollArea, StrongBodyLabel, SubtitleLabel)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(508, 312)
        Frame.setStyleSheet(u"SmoothScrollArea {\n"
"	border: none; \n"
"	background: transparent;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents {\n"
"	border-radius: 8px;\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"")
        self.verticalLayout_9 = QVBoxLayout(Frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.totalrewardLabel = SubtitleLabel(Frame)
        self.totalrewardLabel.setObjectName(u"totalrewardLabel")

        self.verticalLayout_2.addWidget(self.totalrewardLabel)

        self.rewardLabel = StrongBodyLabel(Frame)
        self.rewardLabel.setObjectName(u"rewardLabel")
        self.rewardLabel.setStyleSheet(u"color: rgb(170, 170, 0);")

        self.verticalLayout_2.addWidget(self.rewardLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line = QFrame(Frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.totalhabitcplLabel = SubtitleLabel(Frame)
        self.totalhabitcplLabel.setObjectName(u"totalhabitcplLabel")

        self.verticalLayout_3.addWidget(self.totalhabitcplLabel)

        self.habitcplLabel = StrongBodyLabel(Frame)
        self.habitcplLabel.setObjectName(u"habitcplLabel")
        self.habitcplLabel.setStyleSheet(u"color: rgb(32, 81, 127);")

        self.verticalLayout_3.addWidget(self.habitcplLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.line_2 = QFrame(Frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.totalrewardcplLabel = SubtitleLabel(Frame)
        self.totalrewardcplLabel.setObjectName(u"totalrewardcplLabel")

        self.verticalLayout_4.addWidget(self.totalrewardcplLabel)

        self.rewardcplLabel = StrongBodyLabel(Frame)
        self.rewardcplLabel.setObjectName(u"rewardcplLabel")
        self.rewardcplLabel.setStyleSheet(u"color: rgb(15, 117, 88);")

        self.verticalLayout_4.addWidget(self.rewardcplLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = SmoothScrollArea(Frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 486, 233))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.habiticonLabel = ImageLabel(self.frame)
        self.habiticonLabel.setObjectName(u"habiticonLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.habiticonLabel.sizePolicy().hasHeightForWidth())
        self.habiticonLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.habiticonLabel, 0, Qt.AlignVCenter)

        self.label_8 = SubtitleLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(32, 81, 127);")

        self.horizontalLayout_4.addWidget(self.label_8, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_6.addLayout(self.gridLayout)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 42))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.rewardiconLabel = ImageLabel(self.frame_2)
        self.rewardiconLabel.setObjectName(u"rewardiconLabel")
        sizePolicy1.setHeightForWidth(self.rewardiconLabel.sizePolicy().hasHeightForWidth())
        self.rewardiconLabel.setSizePolicy(sizePolicy1)
        self.rewardiconLabel.setMinimumSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.rewardiconLabel)

        self.label_9 = SubtitleLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(15, 117, 88);")

        self.horizontalLayout_2.addWidget(self.label_9)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_7.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(0, 43))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.detailiconLabel = ImageLabel(self.frame_3)
        self.detailiconLabel.setObjectName(u"detailiconLabel")
        sizePolicy1.setHeightForWidth(self.detailiconLabel.sizePolicy().hasHeightForWidth())
        self.detailiconLabel.setSizePolicy(sizePolicy1)
        self.detailiconLabel.setMinimumSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.detailiconLabel)

        self.label_10 = SubtitleLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.vlayout = QVBoxLayout()
        self.vlayout.setObjectName(u"vlayout")

        self.verticalLayout_8.addLayout(self.vlayout)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.verticalLayout_9.addLayout(self.verticalLayout)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.totalrewardLabel.setText(QCoreApplication.translate("Frame", u"\u603b\u5956\u676f\u503c", None))
        self.rewardLabel.setText(QCoreApplication.translate("Frame", u"TextLabel", None))
        self.totalhabitcplLabel.setText(QCoreApplication.translate("Frame", u"\u603b\u4e60\u60ef\u6253\u5361\u6b21\u6570", None))
        self.habitcplLabel.setText(QCoreApplication.translate("Frame", u"TextLabel", None))
        self.totalrewardcplLabel.setText(QCoreApplication.translate("Frame", u"\u603b\u5956\u52b1\u5b9e\u73b0\u6b21\u6570", None))
        self.rewardcplLabel.setText(QCoreApplication.translate("Frame", u"TextLabel", None))
        self.habiticonLabel.setText(QCoreApplication.translate("Frame", u"habiticon", None))
        self.label_8.setText(QCoreApplication.translate("Frame", u"\u6570\u636e-\u81ea\u5f8b\u4e60\u60ef", None))
        self.rewardiconLabel.setText(QCoreApplication.translate("Frame", u"rewardicon", None))
        self.label_9.setText(QCoreApplication.translate("Frame", u"\u6570\u636e-\u5956\u52b1\u5151\u6362", None))
        self.detailiconLabel.setText(QCoreApplication.translate("Frame", u"detailicon", None))
        self.label_10.setText(QCoreApplication.translate("Frame", u"\u8be6\u7ec6\u8bb0\u5f55", None))
    # retranslateUi

