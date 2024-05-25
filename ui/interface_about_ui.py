# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_about.ui'
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

from qfluentwidgets import (BodyLabel, ImageLabel, StrongBodyLabel, SubtitleLabel)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(640, 480)
        self.verticalLayout_2 = QVBoxLayout(Frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logoLabel = ImageLabel(self.frame)
        self.logoLabel.setObjectName(u"logoLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoLabel.sizePolicy().hasHeightForWidth())
        self.logoLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.logoLabel)

        self.titleLabel = SubtitleLabel(self.frame)
        self.titleLabel.setObjectName(u"titleLabel")

        self.horizontalLayout_2.addWidget(self.titleLabel)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.signLabel = StrongBodyLabel(Frame)
        self.signLabel.setObjectName(u"signLabel")
        self.signLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.signLabel)

        self.descLabel = BodyLabel(Frame)
        self.descLabel.setObjectName(u"descLabel")
        self.descLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.descLabel)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.logoLabel.setText(QCoreApplication.translate("Frame", u"TextLabel", None))
        self.titleLabel.setText(QCoreApplication.translate("Frame", u"\u57fa\u4e8ePython\u7684\u6e38\u620f\u578b\u81ea\u5f8b\u4e60\u60ef\u6570\u636e\u7ba1\u7406\u7cfb\u7edf", None))
        self.signLabel.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p><br/></p><p>2024\u5e745\u6708</p></body></html>", None))
        self.descLabel.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p>\u8bbe\u8ba1\u7406\u5ff5\uff1a</p><p>\u6dfb\u52a0\u81ea\u5f8b\u4e60\u60ef\uff0c\u8bbe\u5b9a\u76ee\u6807;</p><p>\u901a\u8fc7\u575a\u6301\u5b8c\u6210\u81ea\u5f8b\u76ee\u6807\uff0c\u6512\u591f\u5956\u676f\uff0c\u5151\u6362\u5fc3\u4eea\u7684\u76ee\u6807\uff1b</p><p>\u5b9e\u73b0\u81ea\u6211\u6fc0\u52b1\uff0c\u7528\u5956\u52b1\u9a71\u52a8\u81ea\u5df1\u3002</p></body></html>", None))
    # retranslateUi

