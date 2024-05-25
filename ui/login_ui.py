# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, ImageLabel, LineEdit, PasswordLineEdit,
    PrimaryPushButton, PushButton, SubtitleLabel)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(409, 424)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI Variable"])
        font.setPointSize(11)
        Dialog.setFont(font)
        self.horizontalLayout_4 = QHBoxLayout(Dialog)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_label = ImageLabel(Dialog)
        self.logo_label.setObjectName(u"logo_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy1)
        self.logo_label.setMinimumSize(QSize(64, 64))
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.logo_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_4)

        self.label = SubtitleLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(5)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2 = BodyLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_usr = LineEdit(Dialog)
        self.lineEdit_usr.setObjectName(u"lineEdit_usr")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_usr)

        self.label_3 = BodyLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_pwd = PasswordLineEdit(Dialog)
        self.lineEdit_pwd.setObjectName(u"lineEdit_pwd")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_pwd)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalSpacer = QSpacerItem(60, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.login_button = PrimaryPushButton(Dialog)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout_3.addWidget(self.login_button)

        self.register_button = PushButton(Dialog)
        self.register_button.setObjectName(u"register_button")

        self.verticalLayout_3.addWidget(self.register_button)

        self.close_button = PushButton(Dialog)
        self.close_button.setObjectName(u"close_button")

        self.verticalLayout_3.addWidget(self.close_button)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)
        self.login_button.clicked.connect(Dialog.login)
        self.close_button.clicked.connect(Dialog.close)
        self.register_button.clicked.connect(Dialog.register)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.logo_label.setText(QCoreApplication.translate("Dialog", u"logo_label", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"tips", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801\uff1a", None))
        self.login_button.setText(QCoreApplication.translate("Dialog", u"\u767b\u5f55", None))
        self.register_button.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c\u7528\u6237", None))
        self.close_button.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

