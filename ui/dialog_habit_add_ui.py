# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_habit_add.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, ComboBox, LineEdit, SmoothScrollArea,
    SpinBox, StrongBodyLabel, SwitchButton)

class Ui_dialog_habit_add(object):
    def setupUi(self, dialog_habit_add):
        if not dialog_habit_add.objectName():
            dialog_habit_add.setObjectName(u"dialog_habit_add")
        dialog_habit_add.resize(480, 640)
        dialog_habit_add.setStyleSheet(u"SmoothScrollArea{\n"
"	background: transparent; \n"
"	border: none;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents{\n"
"	border-radius: 6px;\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(dialog_habit_add)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_10 = StrongBodyLabel(dialog_habit_add)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.scrollArea = SmoothScrollArea(dialog_habit_add)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 100))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 458, 98))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_5)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_9 = BodyLabel(dialog_habit_add)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)

        self.label = StrongBodyLabel(dialog_habit_add)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_content = LineEdit(dialog_habit_add)
        self.lineEdit_content.setObjectName(u"lineEdit_content")

        self.gridLayout_3.addWidget(self.lineEdit_content, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = BodyLabel(dialog_habit_add)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.switchButton = SwitchButton(dialog_habit_add)
        self.switchButton.setObjectName(u"switchButton")

        self.gridLayout.addWidget(self.switchButton, 3, 1, 1, 1)

        self.label_2 = BodyLabel(dialog_habit_add)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_4 = StrongBodyLabel(dialog_habit_add)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_reward = LineEdit(dialog_habit_add)
        self.lineEdit_reward.setObjectName(u"lineEdit_reward")

        self.gridLayout.addWidget(self.lineEdit_reward, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = BodyLabel(dialog_habit_add)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.spinBox_times = SpinBox(dialog_habit_add)
        self.spinBox_times.setObjectName(u"spinBox_times")
        self.spinBox_times.setMaximum(999)

        self.gridLayout_2.addWidget(self.spinBox_times, 3, 2, 1, 1)

        self.label_5 = StrongBodyLabel(dialog_habit_add)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_7 = BodyLabel(dialog_habit_add)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_6 = BodyLabel(dialog_habit_add)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.spinBox_days = SpinBox(dialog_habit_add)
        self.spinBox_days.setObjectName(u"spinBox_days")
        self.spinBox_days.setMaximum(999)

        self.gridLayout_2.addWidget(self.spinBox_days, 3, 1, 1, 1)

        self.comboBox = ComboBox(dialog_habit_add)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 3, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.retranslateUi(dialog_habit_add)

        QMetaObject.connectSlotsByName(dialog_habit_add)
    # setupUi

    def retranslateUi(self, dialog_habit_add):
        dialog_habit_add.setWindowTitle(QCoreApplication.translate("dialog_habit_add", u"Dialog", None))
        self.label_10.setText(QCoreApplication.translate("dialog_habit_add", u"\u56fe\u6807", None))
        self.label_9.setText(QCoreApplication.translate("dialog_habit_add", u"\uff08\u5c0f\u4e8e64\u5b57\uff09", None))
        self.label.setText(QCoreApplication.translate("dialog_habit_add", u"\u4e60\u60ef\u5185\u5bb9", None))
        self.lineEdit_content.setPlaceholderText(QCoreApplication.translate("dialog_habit_add", u"\u793a\u4f8b\uff1a\u65e9\u7761\u65e9\u8d77", None))
        self.label_3.setText(QCoreApplication.translate("dialog_habit_add", u"\u662f\u5426\u5f00\u542f\u968f\u673a\u6d6e\u52a8", None))
        self.switchButton.setText(QCoreApplication.translate("dialog_habit_add", u"...", None))
        self.label_2.setText(QCoreApplication.translate("dialog_habit_add", u"\u83b7\u5f97\u5956\u676f\u503c", None))
        self.label_4.setText(QCoreApplication.translate("dialog_habit_add", u"\u5956\u52b1\u9009\u9879", None))
        self.lineEdit_reward.setPlaceholderText(QCoreApplication.translate("dialog_habit_add", u"\u793a\u4f8b\uff1a666", None))
        self.label_8.setText(QCoreApplication.translate("dialog_habit_add", u"\u53ef\u5b8c\u6210\u51e0\u6b21", None))
        self.label_5.setText(QCoreApplication.translate("dialog_habit_add", u"\u5468\u671f\u9009\u9879", None))
        self.label_7.setText(QCoreApplication.translate("dialog_habit_add", u"\u6bcf\u51e0\u5929", None))
        self.label_6.setText(QCoreApplication.translate("dialog_habit_add", u"\u9884\u8bbe", None))
        self.comboBox.setText(QCoreApplication.translate("dialog_habit_add", u"PushButton", None))
    # retranslateUi

