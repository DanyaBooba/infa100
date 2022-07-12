from functools import total_ordering
import sys
import os
import shutil
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap, QFont

from task_chooser import Task_Chooser
from data_parser import Localization, Config


class UI_VarWindow(object):
    "Окно решения варианта."

    def __init__(self):
        self.getTasksData()

    def getTasksData(self):
        self.tasks_data = dict()
        for number in range(1, 28):
            self.tasks_data[number] = Task_Chooser.choose_task(number)
        self.user_answers = [None for _ in range(28)]

    def setupUi(self, BaseWindow):
        BaseWindow.resize(1000, 600)
        BaseWindow.move(300, 300)
        self.setWindowTitle(Localization.VAR_WIN_TITLE)
        self.setWindowIcon(QIcon('icons/icon.png'))

        self.exitAction_var = QAction(QIcon('icons/exit.png'), '&' + Localization.EXIT, self)
        self.exitAction_var.setShortcut(Localization.EXIT_SHORTCUT)
        self.exitAction_var.setStatusTip(Localization.EXIT_STATUS_TIP)
        self.exitAction_var.triggered.connect(qApp.quit)
        self.statusBar()

        self.menubar_var = self.menuBar()
        self.fileMenu_var = self.menubar_var.addMenu('&' + Localization.FILE)
        self.fileMenu_var.addAction(self.exitAction_var)

        self.centralWidget = QWidget()
        self.centralLayout = QGridLayout()

        self.contents_nums = QWidget()
        self.nums_widget_layout = QGridLayout()
        self.buttons_list = [None] + [QPushButton(str(number), self) for number in range(1, 28)]
        self.placing_x = 0
        for button in self.buttons_list[1:]:
            self.nums_widget_layout.addWidget(button, self.placing_x, 0)
            self.placing_x = self.placing_x + 1
        self.contents_nums.setLayout(self.nums_widget_layout)

        self.contents_tasks = QStackedWidget()
        self.contents_default = QWidget()
        self.tasks_widget_layout_default = QGridLayout()
        self.default_text = QLabel(Localization.VAR_DEFAULT_TEXT)
        self.tasks_widget_layout_default.addWidget(self.default_text)
        self.contents_default.setLayout(self.tasks_widget_layout_default)


        # 111111111
        self.task_1_widget = QWidget()
        task_1_data = self.tasks_data[1]
        self.task_1_text = QLabel(task_1_data['text'])
        self.task_1_text.setWordWrap(True)
        self.task_1_text.setAlignment(Qt.AlignCenter)
        self.task_1_answer = task_1_data['answer']
        self.task_1_widget_clicked_grid = QGridLayout()

        self.task_1_picture_path = 'data/tasks_data/1/' + task_1_data['id'] + '.png'
        self.task_1_picture_exists = True if os.path.exists(self.task_1_picture_path) else False
        if self.task_1_picture_exists:
            self.task_1_picture = QPixmap(self.task_1_picture_path)
            self.task_1_picture_lbl = QLabel(self)
            self.task_1_picture_lbl.setPixmap(self.task_1_picture)

        self.task_1_blank = QLineEdit()
        self.task_1_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_1():
            self.user_answers[1] = self.task_1_blank.text()
            self.task_1_blank.setEnabled(False)
            self.task_1_save_button.setParent(None)
            self.task_1_widget_clicked_grid.addWidget(self.task_1_edit_button, 28, 0, 29, 0)
        def edit_task_1():
            self.task_1_blank.setEnabled(True)
            self.task_1_edit_button.setParent(None)
            self.task_1_widget_clicked_grid.addWidget(self.task_1_save_button, 28, 0, 29, 0)
        self.task_1_save_button = QPushButton(Localization.SAVE)
        self.task_1_save_button.clicked.connect(save_task_1)
        self.task_1_edit_button = QPushButton(Localization.EDIT)
        self.task_1_edit_button.clicked.connect(edit_task_1)
        
        self.task_1_widget_clicked_grid.addWidget(self.task_1_text, 1, 0, 7, 0)
        if self.task_1_picture_exists:
            self.task_1_widget_clicked_grid.addWidget(self.task_1_picture_lbl, 8, 0, 15, 0, alignment=Qt.AlignCenter)
        self.task_1_widget_clicked_grid.addWidget(self.task_1_blank, 25, 0, 26, 0)
        self.task_1_widget_clicked_grid.addWidget(self.task_1_save_button, 28, 0, 29, 0)
        self.task_1_widget.setLayout(self.task_1_widget_clicked_grid)


        # 222222222
        self.task_2_widget = QWidget()
        task_2_data = self.tasks_data[2]
        self.task_2_text = QLabel(task_2_data['text'])
        self.task_2_text.setWordWrap(True)
        self.task_2_text.setAlignment(Qt.AlignCenter)
        self.task_2_answer = task_2_data['answer']
        self.task_2_widget_clicked_grid = QGridLayout()

        self.task_2_picture_path = 'data/tasks_data/2/' + task_2_data['id'] + '.png'
        self.task_2_picture_exists = True if os.path.exists(self.task_2_picture_path) else False
        if self.task_2_picture_exists:
            self.task_2_picture = QPixmap(self.task_2_picture_path)
            self.task_2_picture_lbl = QLabel(self)
            self.task_2_picture_lbl.setPixmap(self.task_2_picture)

        self.task_2_blank = QLineEdit()
        self.task_2_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_2():
            self.user_answers[2] = self.task_2_blank.text()
            self.task_2_blank.setEnabled(False)
            self.task_2_save_button.setParent(None)
            self.task_2_widget_clicked_grid.addWidget(self.task_2_edit_button, 28, 0, 29, 0)
        def edit_task_2():
            self.task_2_blank.setEnabled(True)
            self.task_2_edit_button.setParent(None)
            self.task_2_widget_clicked_grid.addWidget(self.task_2_save_button, 28, 0, 29, 0)
        self.task_2_save_button = QPushButton(Localization.SAVE)
        self.task_2_save_button.clicked.connect(save_task_2)
        self.task_2_edit_button = QPushButton(Localization.EDIT)
        self.task_2_edit_button.clicked.connect(edit_task_2)
        
        self.task_2_widget_clicked_grid.addWidget(self.task_2_text, 1, 0, 7, 0)
        if self.task_2_picture_exists:
            self.task_2_widget_clicked_grid.addWidget(self.task_2_picture_lbl, 8, 0, 25, 0, alignment=Qt.AlignCenter)
        self.task_2_widget_clicked_grid.addWidget(self.task_2_blank, 25, 0, 26, 0)
        self.task_2_widget_clicked_grid.addWidget(self.task_2_save_button, 28, 0, 29, 0)
        self.task_2_widget.setLayout(self.task_2_widget_clicked_grid)


        #333333333
        self.task_3_widget = QWidget()
        task_3_data = self.tasks_data[3]

        self.task_3_text1 = QLabel(task_3_data['text1'])
        self.task_3_text1.setWordWrap(True)
        self.task_3_text1.setAlignment(Qt.AlignCenter)
        self.task_3_text2 = QLabel(task_3_data['text2'])
        self.task_3_text2.setWordWrap(True)
        self.task_3_text2.setAlignment(Qt.AlignCenter)
        self.task_3_text3 = QLabel(task_3_data['text3'])
        self.task_3_text3.setAlignment(Qt.AlignCenter)
        self.task_3_text4 = QLabel(task_3_data['text4'])
        self.task_3_text3.setWordWrap(True)
        self.task_3_text4.setWordWrap(True)
        self.task_3_text4.setAlignment(Qt.AlignCenter)
        self.task_3_text5 = QLabel(task_3_data['text5'])
        self.task_3_text5.setWordWrap(True)
        self.task_3_text5.setAlignment(Qt.AlignCenter)
        self.task_3_text6 = QLabel(task_3_data['text6'])
        self.task_3_text6.setWordWrap(True)
        self.task_3_text6.setAlignment(Qt.AlignCenter)

        self.task_3_answer = task_3_data['answer']
        self.task_3_widget_clicked_grid = QGridLayout()

        self.task_3_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_3_file_path = 'data/tasks_data/3/' + task_3_data['id'] + '.xlsx'

        self.task_3_picture_2to3_path = 'data/tasks_data/3/' + task_3_data['id'] + '_2to3.png'
        self.task_3_picture_2to3 = QPixmap(self.task_3_picture_2to3_path)
        self.task_3_picture_2to3_lbl = QLabel(self)
        self.task_3_picture_2to3_lbl.setPixmap(self.task_3_picture_2to3)
        self.task_3_picture_3to4_path = 'data/tasks_data/3/' + task_3_data['id'] + '_3to4.png'
        self.task_3_picture_3to4 = QPixmap(self.task_3_picture_3to4_path)
        self.task_3_picture_3to4_lbl = QLabel(self)
        self.task_3_picture_3to4_lbl.setPixmap(self.task_3_picture_3to4)
        self.task_3_picture_4to5_path = 'data/tasks_data/3/' + task_3_data['id'] + '_4to5.png'
        self.task_3_picture_4to5 = QPixmap(self.task_3_picture_4to5_path)
        self.task_3_picture_4to5_lbl = QLabel(self)
        self.task_3_picture_4to5_lbl.setPixmap(self.task_3_picture_4to5)
        self.task_3_picture_5to6_path = 'data/tasks_data/3/' + task_3_data['id'] + '_5to6.png'
        self.task_3_picture_5to6 = QPixmap(self.task_3_picture_5to6_path)
        self.task_3_picture_5to6_lbl = QLabel(self)
        self.task_3_picture_5to6_lbl.setPixmap(self.task_3_picture_5to6)

        self.task_3_blank = QLineEdit()
        self.task_3_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_3():
            self.user_answers[3] = self.task_3_blank.text()
            self.task_3_blank.setEnabled(False)
            self.task_3_save_button.setParent(None)
            self.task_3_widget_clicked_grid.addWidget(self.task_3_edit_button, 1400, 0, 1407, 0)
        def edit_task_3():
            self.task_3_blank.setEnabled(True)
            self.task_3_edit_button.setParent(None)
            self.task_3_widget_clicked_grid.addWidget(self.task_3_save_button, 1400, 0, 1407, 0)
        self.task_3_save_button = QPushButton(Localization.SAVE)
        self.task_3_save_button.clicked.connect(save_task_3)
        self.task_3_edit_button = QPushButton(Localization.EDIT)
        self.task_3_edit_button.clicked.connect(edit_task_3)
        
        self.task_3_widget_clicked_grid.addWidget(self.task_3_text1, 0, 0, 1, 0)
        self.task_3_widget_clicked_grid.addWidget(self.task_3_get_file_btn, 2, 0, 3, 0)
        self.task_3_widget_clicked_grid.addWidget(self.task_3_text2, 4, 0, 6, 0)
        self.task_3_widget_clicked_grid.addWidget(self.task_3_picture_2to3_lbl, 9, 0, 11, 0, alignment=Qt.AlignCenter)
        self.task_3_widget_clicked_grid.addWidget(self.task_3_text3, 15, 0, 16, 0)
        self.task_3_widget_clicked_grid.addWidget(self.task_3_picture_3to4_lbl, 25, 0, 27, 0, alignment=Qt.AlignCenter)
        self.task_3_widget_clicked_grid.addWidget(self.task_3_text4, 39, 0, 41, 0)
        self.task_3_widget_clicked_grid.addWidget(self.task_3_picture_4to5_lbl, 62, 0, 64, 0, alignment=Qt.AlignCenter)
        self.task_3_widget_clicked_grid.addWidget(self.task_3_text5, 86, 0, 87, 0)
        self.task_3_widget_clicked_grid.addWidget(self.task_3_picture_5to6_lbl, 166, 0, 168, 0, alignment=Qt.AlignCenter)
        self.task_3_widget_clicked_grid.addWidget(self.task_3_text6, 330, 0, 332, 0)
        self.task_3_widget_clicked_grid.addWidget(self.task_3_blank, 650, 0, 652, 0)
        self.task_3_widget_clicked_grid.addWidget(self.task_3_save_button, 1400, 0, 1407, 0)
        self.task_3_widget.setLayout(self.task_3_widget_clicked_grid)

        def task_3_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_3_file_path, destination_path)
            except FileNotFoundError:
                pass

        self.task_3_get_file_btn.clicked.connect(task_3_get_file_button_clicked)


        #444444444
        self.task_4_widget = QWidget()
        task_4_data = self.tasks_data[4]
        self.task_4_text = QLabel(task_4_data['text'])
        self.task_4_text.setWordWrap(True)
        self.task_4_text.setAlignment(Qt.AlignCenter)
        self.task_4_answer = task_4_data['answer']
        self.task_4_widget_clicked_grid = QGridLayout()

        self.task_4_blank = QLineEdit()
        self.task_4_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_4():
            self.user_answers[4] = self.task_4_blank.text()
            self.task_4_blank.setEnabled(False)
            self.task_4_save_button.setParent(None)
            self.task_4_widget_clicked_grid.addWidget(self.task_4_edit_button, 9, 0, 10, 0)
        def edit_task_4():
            self.task_4_blank.setEnabled(True)
            self.task_4_edit_button.setParent(None)
            self.task_4_widget_clicked_grid.addWidget(self.task_4_save_button, 9, 0, 10, 0)
        self.task_4_save_button = QPushButton(Localization.SAVE)
        self.task_4_save_button.clicked.connect(save_task_4)
        self.task_4_edit_button = QPushButton(Localization.EDIT)
        self.task_4_edit_button.clicked.connect(edit_task_4)
        
        self.task_4_widget_clicked_grid.addWidget(self.task_4_text, 1, 0, 7, 0)
        self.task_4_widget_clicked_grid.addWidget(self.task_4_blank, 8, 0, 9, 0)
        self.task_4_widget_clicked_grid.addWidget(self.task_4_save_button, 9, 0, 10, 0)
        self.task_4_widget.setLayout(self.task_4_widget_clicked_grid)


        #555555555
        self.task_5_widget = QWidget()
        task_5_data = self.tasks_data[5]
        self.task_5_text = QLabel(task_5_data['text'])
        self.task_5_text.setWordWrap(True)
        self.task_5_text.setAlignment(Qt.AlignCenter)
        self.task_5_answer = task_5_data['answer']
        self.task_5_widget_clicked_grid = QGridLayout()

        self.task_5_blank = QLineEdit()
        self.task_5_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_5():
            self.user_answers[5] = self.task_5_blank.text()
            self.task_5_blank.setEnabled(False)
            self.task_5_save_button.setParent(None)
            self.task_5_widget_clicked_grid.addWidget(self.task_5_edit_button, 9, 0, 10, 0)
        def edit_task_5():
            self.task_5_blank.setEnabled(True)
            self.task_5_edit_button.setParent(None)
            self.task_5_widget_clicked_grid.addWidget(self.task_5_save_button, 9, 0, 10, 0)
        self.task_5_save_button = QPushButton(Localization.SAVE)
        self.task_5_save_button.clicked.connect(save_task_5)
        self.task_5_edit_button = QPushButton(Localization.EDIT)
        self.task_5_edit_button.clicked.connect(edit_task_5)
        
        self.task_5_widget_clicked_grid.addWidget(self.task_5_text, 1, 0, 7, 0)
        self.task_5_widget_clicked_grid.addWidget(self.task_5_blank, 8, 0, 9, 0)
        self.task_5_widget_clicked_grid.addWidget(self.task_5_save_button, 9, 0, 10, 0)
        self.task_5_widget.setLayout(self.task_5_widget_clicked_grid)


        #666666666
        self.task_6_widget = QWidget()
        task_6_data = self.tasks_data[6]
        self.task_6_text = QLabel(task_6_data['text'] + '\n\n' + task_6_data['program'])
        self.task_6_text.setWordWrap(True)
        self.task_6_answer = task_6_data['answer']
        self.task_6_widget_clicked_grid = QGridLayout()

        self.task_6_blank = QLineEdit()
        self.task_6_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_6():
            self.user_answers[6] = self.task_6_blank.text()
            self.task_6_blank.setEnabled(False)
            self.task_6_save_button.setParent(None)
            self.task_6_widget_clicked_grid.addWidget(self.task_6_edit_button, 9, 0, 10, 0)
        def edit_task_6():
            self.task_6_blank.setEnabled(True)
            self.task_6_edit_button.setParent(None)
            self.task_6_widget_clicked_grid.addWidget(self.task_6_save_button, 9, 0, 10, 0)
        self.task_6_save_button = QPushButton(Localization.SAVE)
        self.task_6_save_button.clicked.connect(save_task_6)
        self.task_6_edit_button = QPushButton(Localization.EDIT)
        self.task_6_edit_button.clicked.connect(edit_task_6)
        
        self.task_6_widget_clicked_grid.addWidget(self.task_6_text, 1, 0, 7, 0, alignment=Qt.AlignCenter)
        self.task_6_widget_clicked_grid.addWidget(self.task_6_blank, 8, 0, 9, 0)
        self.task_6_widget_clicked_grid.addWidget(self.task_6_save_button, 9, 0, 10, 0)
        self.task_6_widget.setLayout(self.task_6_widget_clicked_grid)


        #777777777
        self.task_7_widget = QWidget()
        task_7_data = self.tasks_data[7]
        self.task_7_text = QLabel(task_7_data['text'])
        self.task_7_text.setWordWrap(True)
        self.task_5_text.setAlignment(Qt.AlignCenter)
        self.task_7_answer = task_7_data['answer']
        self.task_7_widget_clicked_grid = QGridLayout()

        self.task_7_blank = QLineEdit()
        self.task_7_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_7():
            self.user_answers[7] = self.task_7_blank.text()
            self.task_7_blank.setEnabled(False)
            self.task_7_save_button.setParent(None)
            self.task_7_widget_clicked_grid.addWidget(self.task_7_edit_button, 9, 0, 10, 0)
        def edit_task_7():
            self.task_7_blank.setEnabled(True)
            self.task_7_edit_button.setParent(None)
            self.task_7_widget_clicked_grid.addWidget(self.task_7_save_button, 9, 0, 10, 0)
        self.task_7_save_button = QPushButton(Localization.SAVE)
        self.task_7_save_button.clicked.connect(save_task_7)
        self.task_7_edit_button = QPushButton(Localization.EDIT)
        self.task_7_edit_button.clicked.connect(edit_task_7)
        
        self.task_7_widget_clicked_grid.addWidget(self.task_7_text, 1, 0, 7, 0)
        self.task_7_widget_clicked_grid.addWidget(self.task_7_blank, 8, 0, 9, 0)
        self.task_7_widget_clicked_grid.addWidget(self.task_7_save_button, 9, 0, 10, 0)
        self.task_7_widget.setLayout(self.task_7_widget_clicked_grid)


        #888888888
        self.task_8_widget = QWidget()
        task_8_data = self.tasks_data[8]
        self.task_8_text = QLabel(task_8_data['text'])
        self.task_8_text.setWordWrap(True)
        self.task_8_text.setAlignment(Qt.AlignCenter)
        self.task_8_answer = task_8_data['answer']
        self.task_8_widget_clicked_grid = QGridLayout()

        self.task_8_blank = QLineEdit()
        self.task_8_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_8():
            self.user_answers[8] = self.task_8_blank.text()
            self.task_8_blank.setEnabled(False)
            self.task_8_save_button.setParent(None)
            self.task_8_widget_clicked_grid.addWidget(self.task_8_edit_button, 9, 0, 10, 0)
        def edit_task_8():
            self.task_8_blank.setEnabled(True)
            self.task_8_edit_button.setParent(None)
            self.task_8_widget_clicked_grid.addWidget(self.task_8_save_button, 9, 0, 10, 0)
        self.task_8_save_button = QPushButton(Localization.SAVE)
        self.task_8_save_button.clicked.connect(save_task_8)
        self.task_8_edit_button = QPushButton(Localization.EDIT)
        self.task_8_edit_button.clicked.connect(edit_task_8)
        
        self.task_8_widget_clicked_grid.addWidget(self.task_8_text, 1, 0, 7, 0)
        self.task_8_widget_clicked_grid.addWidget(self.task_8_blank, 8, 0, 9, 0)
        self.task_8_widget_clicked_grid.addWidget(self.task_8_save_button, 9, 0, 10, 0)
        self.task_8_widget.setLayout(self.task_8_widget_clicked_grid)


        #999999999
        self.task_9_widget = QWidget()
        task_9_data = self.tasks_data[9]
        self.task_9_text = QLabel(task_9_data['text'])
        self.task_9_text.setWordWrap(True)
        self.task_9_text.setAlignment(Qt.AlignCenter)
        self.task_9_answer = task_9_data['answer']
        self.task_9_widget_clicked_grid = QGridLayout()

        self.task_9_blank = QLineEdit()
        self.task_9_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_9():
            self.user_answers[9] = self.task_9_blank.text()
            self.task_9_blank.setEnabled(False)
            self.task_9_save_button.setParent(None)
            self.task_9_widget_clicked_grid.addWidget(self.task_9_edit_button, 11, 0, 12, 0)
        def edit_task_9():
            self.task_9_blank.setEnabled(True)
            self.task_9_edit_button.setParent(None)
            self.task_9_widget_clicked_grid.addWidget(self.task_9_save_button, 11, 0, 12, 0)
        self.task_9_save_button = QPushButton(Localization.SAVE)
        self.task_9_save_button.clicked.connect(save_task_9)
        self.task_9_edit_button = QPushButton(Localization.EDIT)
        self.task_9_edit_button.clicked.connect(edit_task_9)

        self.task_9_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_9_file_path = 'data/tasks_data/9/' + task_9_data['id'] + '.xlsx'
        def task_9_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_9_file_path, destination_path)
            except FileNotFoundError:
                pass
            self.task_9_get_file_btn.clicked.connect(task_9_get_file_button_clicked)
        
        self.task_9_widget_clicked_grid.addWidget(self.task_9_text, 1, 0, 7, 0)
        self.task_9_widget_clicked_grid.addWidget(self.task_9_get_file_btn, 8, 0, 9, 0)
        self.task_9_widget_clicked_grid.addWidget(self.task_9_blank, 10, 0, 11, 0)
        self.task_9_widget_clicked_grid.addWidget(self.task_9_save_button, 11, 0, 12, 0)
        self.task_9_widget.setLayout(self.task_9_widget_clicked_grid)



        #101010101010101010
        self.task_10_widget = QWidget()
        task_10_data = self.tasks_data[10]
        self.task_10_text = QLabel(task_10_data['text'])
        self.task_10_text.setWordWrap(True)
        self.task_10_text.setAlignment(Qt.AlignCenter)
        self.task_10_answer = task_10_data['answer']
        self.task_10_widget_clicked_grid = QGridLayout()

        self.task_10_blank = QLineEdit()
        self.task_10_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_10():
            self.user_answers[10] = self.task_10_blank.text()
            self.task_10_blank.setEnabled(False)
            self.task_10_save_button.setParent(None)
            self.task_10_widget_clicked_grid.addWidget(self.task_10_edit_button, 11, 0, 12, 0)
        def edit_task_10():
            self.task_10_blank.setEnabled(True)
            self.task_10_edit_button.setParent(None)
            self.task_10_widget_clicked_grid.addWidget(self.task_10_save_button, 11, 0, 12, 0)
        self.task_10_save_button = QPushButton(Localization.SAVE)
        self.task_10_save_button.clicked.connect(save_task_10)
        self.task_10_edit_button = QPushButton(Localization.EDIT)
        self.task_10_edit_button.clicked.connect(edit_task_10)

        self.task_10_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_10_file_path = 'data/tasks_data/10/' + task_10_data['id'] + '.docx'
        def task_10_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_10_file_path, destination_path)
            except FileNotFoundError:
                pass
            self.task_10_get_file_btn.clicked.connect(task_10_get_file_button_clicked)
        
        self.task_10_widget_clicked_grid.addWidget(self.task_10_text, 1, 0, 7, 0)
        self.task_10_widget_clicked_grid.addWidget(self.task_10_get_file_btn, 8, 0, 10, 0)
        self.task_10_widget_clicked_grid.addWidget(self.task_10_blank, 9, 0, 11, 0)
        self.task_10_widget_clicked_grid.addWidget(self.task_10_save_button, 11, 0, 12, 0)
        self.task_10_widget.setLayout(self.task_10_widget_clicked_grid)


        #111111111111111111
        self.task_11_widget = QWidget()
        task_11_data = self.tasks_data[11]
        self.task_11_text = QLabel(task_11_data['text'])
        self.task_11_text.setWordWrap(True)
        self.task_11_text.setAlignment(Qt.AlignCenter)
        self.task_11_answer = task_11_data['answer']
        self.task_11_widget_clicked_grid = QGridLayout()

        self.task_11_blank = QLineEdit()
        self.task_11_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_11():
            self.user_answers[11] = self.task_11_blank.text()
            self.task_11_blank.setEnabled(False)
            self.task_11_save_button.setParent(None)
            self.task_11_widget_clicked_grid.addWidget(self.task_11_edit_button, 9, 0, 10, 0)
        def edit_task_11():
            self.task_11_blank.setEnabled(True)
            self.task_11_edit_button.setParent(None)
            self.task_11_widget_clicked_grid.addWidget(self.task_11_save_button, 9, 0, 10, 0)
        self.task_11_save_button = QPushButton(Localization.SAVE)
        self.task_11_save_button.clicked.connect(save_task_11)
        self.task_11_edit_button = QPushButton(Localization.EDIT)
        self.task_11_edit_button.clicked.connect(edit_task_11)
        
        self.task_11_widget_clicked_grid.addWidget(self.task_11_text, 1, 0, 7, 0)
        self.task_11_widget_clicked_grid.addWidget(self.task_11_blank, 8, 0, 9, 0)
        self.task_11_widget_clicked_grid.addWidget(self.task_11_save_button, 9, 0, 10, 0)
        self.task_11_widget.setLayout(self.task_11_widget_clicked_grid)


        # 12121212121212121212
        self.task_12_widget = QWidget()
        task_12_data = self.tasks_data[12]
        self.task_12_text = QLabel(task_12_data['text'])
        self.task_12_text.setWordWrap(True)
        self.task_12_answer = task_12_data['answer']
        self.task_12_widget_clicked_grid = QGridLayout()

        if task_12_data['hasPictures'] == True:
            self.task_12_picture_path = 'data/tasks_data/12/' + task_12_data['id'] + '.png'
            self.task_12_picture_exists = True if os.path.exists(self.task_12_picture_path) else False
            if self.task_12_picture_exists:
                self.task_12_picture = QPixmap(self.task_12_picture_path)
                self.task_12_picture_lbl = QLabel(self)
                self.task_12_picture_lbl.setPixmap(self.task_12_picture)

        self.task_12_blank = QLineEdit()
        self.task_12_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_12():
            self.user_answers[12] = self.task_12_blank.text()
            self.task_12_blank.setEnabled(False)
            self.task_12_save_button.setParent(None)
            self.task_12_widget_clicked_grid.addWidget(self.task_12_edit_button, 21, 0, 22, 0)
        def edit_task_12():
            self.task_12_blank.setEnabled(True)
            self.task_12_edit_button.setParent(None)
            self.task_12_widget_clicked_grid.addWidget(self.task_12_save_button, 21, 0, 22, 0)
        self.task_12_save_button = QPushButton(Localization.SAVE)
        self.task_12_save_button.clicked.connect(save_task_12)
        self.task_12_edit_button = QPushButton(Localization.EDIT)
        self.task_12_edit_button.clicked.connect(edit_task_12)

        if task_12_data['hasPictures'] == False:
            self.task_12_widget_clicked_grid.addWidget(self.task_12_text, 1, 0, 15, 0)
            self.task_12_widget_clicked_grid.addWidget(self.task_12_blank, 18, 0, 20, 0)
            self.task_12_widget_clicked_grid.addWidget(self.task_12_save_button, 21, 0, 22, 0)
            self.task_12_widget.setLayout(self.task_12_widget_clicked_grid)
        elif task_12_data['hasPictures'] == True:
            self.task_12_widget_clicked_grid.addWidget(self.task_12_picture_lbl, 1, 0, 15, 1)
            self.task_12_widget_clicked_grid.addWidget(self.task_12_text, 1, 2, 15, 9)
            self.task_12_widget_clicked_grid.addWidget(self.task_12_blank, 18, 0, 20, 0)
            self.task_12_widget_clicked_grid.addWidget(self.task_12_save_button, 21, 0, 22, 0)
            self.task_12_widget.setLayout(self.task_12_widget_clicked_grid)


        # 131313131313131313
        self.task_13_widget = QWidget()
        task_13_data = self.tasks_data[13]
        self.task_13_text = QLabel(task_13_data['text'])
        self.task_13_text.setWordWrap(True)
        self.task_13_text.setAlignment(Qt.AlignCenter)
        self.task_13_answer = task_13_data['answer']
        self.task_13_widget_clicked_grid = QGridLayout()

        self.task_13_text_widgth = self.task_13_text.frameGeometry().width()
        self.task_13_text_height = self.task_13_text.frameGeometry().height()

        self.task_13_picture_path = 'data/tasks_data/13/' + task_13_data['id'] + '.png'
        self.task_13_picture_exists = True if os.path.exists(self.task_13_picture_path) else False
        if self.task_13_picture_exists:
            self.task_13_picture = QPixmap(self.task_13_picture_path)
            self.task_13_picture = self.task_13_picture.scaled(self.task_13_text_widgth, self.task_13_text_height, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.task_13_picture_lbl = QLabel(self)
            self.task_13_picture_lbl.setPixmap(self.task_13_picture)

        self.task_13_blank = QLineEdit()
        self.task_13_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_13():
            self.user_answers[13] = self.task_13_blank.text()
            self.task_13_blank.setEnabled(False)
            self.task_13_save_button.setParent(None)
            self.task_13_widget_clicked_grid.addWidget(self.task_13_edit_button, 30, 0, 31, 0)
        def edit_task_13():
            self.task_13_blank.setEnabled(True)
            self.task_13_edit_button.setParent(None)
            self.task_13_widget_clicked_grid.addWidget(self.task_13_save_button, 30, 0, 31, 0)
        self.task_13_save_button = QPushButton(Localization.SAVE)
        self.task_13_save_button.clicked.connect(save_task_13)
        self.task_13_edit_button = QPushButton(Localization.EDIT)
        self.task_13_edit_button.clicked.connect(edit_task_13)
        
        self.task_13_widget_clicked_grid.addWidget(self.task_13_text, 1, 0, 7, 0)
        if self.task_13_picture_exists:
            self.task_13_widget_clicked_grid.addWidget(self.task_13_picture_lbl, 8, 0, 15, 0, alignment=Qt.AlignCenter)
        self.task_13_widget_clicked_grid.addWidget(self.task_13_blank, 25, 0, 26, 0)
        self.task_13_widget_clicked_grid.addWidget(self.task_13_save_button, 30, 0, 31, 0)
        self.task_13_widget.setLayout(self.task_13_widget_clicked_grid)


        #141414141414141414
        self.task_14_widget = QWidget()
        task_14_data = self.tasks_data[14]
        self.task_14_text = QLabel(task_14_data['text'])
        self.task_14_text.setWordWrap(True)
        self.task_14_text.setAlignment(Qt.AlignCenter)
        self.task_14_answer = task_14_data['answer']
        self.task_14_widget_clicked_grid = QGridLayout()

        self.task_14_blank = QLineEdit()
        self.task_14_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_14():
            self.user_answers[14] = self.task_14_blank.text()
            self.task_14_blank.setEnabled(False)
            self.task_14_save_button.setParent(None)
            self.task_14_widget_clicked_grid.addWidget(self.task_14_edit_button, 9, 0, 10, 0)
        def edit_task_14():
            self.task_14_blank.setEnabled(True)
            self.task_14_edit_button.setParent(None)
            self.task_14_widget_clicked_grid.addWidget(self.task_14_save_button, 9, 0, 10, 0)
        self.task_14_save_button = QPushButton(Localization.SAVE)
        self.task_14_save_button.clicked.connect(save_task_14)
        self.task_14_edit_button = QPushButton(Localization.EDIT)
        self.task_14_edit_button.clicked.connect(edit_task_14)
        
        self.task_14_widget_clicked_grid.addWidget(self.task_14_text, 1, 0, 7, 0)
        self.task_14_widget_clicked_grid.addWidget(self.task_14_blank, 8, 0, 9, 0)
        self.task_14_widget_clicked_grid.addWidget(self.task_14_save_button, 9, 0, 10, 0)
        self.task_14_widget.setLayout(self.task_14_widget_clicked_grid)


        #151515151515151515
        self.task_15_widget = QWidget()
        task_15_data = self.tasks_data[15]
        self.task_15_text = QLabel(task_15_data['text'])
        self.task_15_text.setWordWrap(True)
        self.task_15_text.setAlignment(Qt.AlignCenter)
        self.task_15_answer = task_15_data['answer']
        self.task_15_widget_clicked_grid = QGridLayout()

        self.task_15_blank = QLineEdit()
        self.task_15_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_15():
            self.user_answers[15] = self.task_15_blank.text()
            self.task_15_blank.setEnabled(False)
            self.task_15_save_button.setParent(None)
            self.task_15_widget_clicked_grid.addWidget(self.task_15_edit_button, 9, 0, 10, 0)
        def edit_task_15():
            self.task_15_blank.setEnabled(True)
            self.task_15_edit_button.setParent(None)
            self.task_15_widget_clicked_grid.addWidget(self.task_15_save_button, 9, 0, 10, 0)
        self.task_15_save_button = QPushButton(Localization.SAVE)
        self.task_15_save_button.clicked.connect(save_task_15)
        self.task_15_edit_button = QPushButton(Localization.EDIT)
        self.task_15_edit_button.clicked.connect(edit_task_15)
        
        self.task_15_widget_clicked_grid.addWidget(self.task_15_text, 1, 0, 7, 0)
        self.task_15_widget_clicked_grid.addWidget(self.task_15_blank, 8, 0, 9, 0)
        self.task_15_widget_clicked_grid.addWidget(self.task_15_save_button, 9, 0, 10, 0)
        self.task_15_widget.setLayout(self.task_15_widget_clicked_grid)


        #161616161616161616
        self.task_16_widget = QWidget()
        task_16_data = self.tasks_data[16]
        self.task_16_text_for_lbl = task_16_data['text']
        if task_16_data['program'].strip() != 'нет':
            self.task_16_text_for_lbl = self.task_16_text_for_lbl + '\n\n' + task_16_data['program']
        self.task_16_text = QLabel(self.task_16_text_for_lbl)
        self.task_16_text.setWordWrap(True)
        self.task_16_answer = task_16_data['answer']
        self.task_16_widget_clicked_grid = QGridLayout()

        self.task_16_blank = QLineEdit()
        self.task_16_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_16():
            self.user_answers[16] = self.task_16_blank.text()
            self.task_16_blank.setEnabled(False)
            self.task_16_save_button.setParent(None)
            self.task_16_widget_clicked_grid.addWidget(self.task_16_edit_button, 9, 0, 10, 0)
        def edit_task_16():
            self.task_16_blank.setEnabled(True)
            self.task_16_edit_button.setParent(None)
            self.task_16_widget_clicked_grid.addWidget(self.task_16_save_button, 9, 0, 10, 0)
        self.task_16_save_button = QPushButton(Localization.SAVE)
        self.task_16_save_button.clicked.connect(save_task_16)
        self.task_16_edit_button = QPushButton(Localization.EDIT)
        self.task_16_edit_button.clicked.connect(edit_task_16)
        
        self.task_16_widget_clicked_grid.addWidget(self.task_16_text, 1, 0, 7, 0, alignment=Qt.AlignCenter)
        self.task_16_widget_clicked_grid.addWidget(self.task_16_blank, 8, 0, 9, 0)
        self.task_16_widget_clicked_grid.addWidget(self.task_16_save_button, 9, 0, 10, 0)
        self.task_16_widget.setLayout(self.task_16_widget_clicked_grid)


        #171717171717171717
        self.task_17_widget = QWidget()
        task_17_data = self.tasks_data[17]
        self.task_17_text = QLabel(task_17_data['text'])
        self.task_17_text.setWordWrap(True)
        self.task_17_text.setAlignment(Qt.AlignCenter)
        self.task_17_answer = task_17_data['answer']
        self.task_17_widget_clicked_grid = QGridLayout()

        self.task_17_blank = QLineEdit()
        self.task_17_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_17():
            self.user_answers[17] = self.task_17_blank.text()
            self.task_17_blank.setEnabled(False)
            self.task_17_save_button.setParent(None)
            self.task_17_widget_clicked_grid.addWidget(self.task_17_edit_button, 11, 0, 12, 0)
        def edit_task_17():
            self.task_17_blank.setEnabled(True)
            self.task_17_edit_button.setParent(None)
            self.task_17_widget_clicked_grid.addWidget(self.task_17_save_button, 11, 0, 12, 0)
        self.task_17_save_button = QPushButton(Localization.SAVE)
        self.task_17_save_button.clicked.connect(save_task_17)
        self.task_17_edit_button = QPushButton(Localization.EDIT)
        self.task_17_edit_button.clicked.connect(edit_task_17)

        self.task_17_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_17_file_path = 'data/tasks_data/17/' + task_17_data['fileName']
        def task_17_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_17_file_path, destination_path)
            except FileNotFoundError:
                pass
        self.task_17_get_file_btn.clicked.connect(task_17_get_file_button_clicked)
        
        self.task_17_widget_clicked_grid.addWidget(self.task_17_text, 1, 0, 7, 0)
        self.task_17_widget_clicked_grid.addWidget(self.task_17_get_file_btn, 8, 0, 10, 0)
        self.task_17_widget_clicked_grid.addWidget(self.task_17_blank, 9, 0, 11, 0)
        self.task_17_widget_clicked_grid.addWidget(self.task_17_save_button, 11, 0, 12, 0)
        self.task_17_widget.setLayout(self.task_17_widget_clicked_grid)


        #181818181818181818
        self.task_18_widget = QWidget()
        task_18_data = self.tasks_data[18]
        self.task_18_text = QLabel(task_18_data['text'])
        self.task_18_text.setWordWrap(True)
        self.task_18_text.setAlignment(Qt.AlignCenter)
        self.task_18_answer = task_18_data['answer']
        self.task_18_widget_clicked_grid = QGridLayout()

        self.task_18_blank = QLineEdit()
        self.task_18_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_18():
            self.user_answers[18] = self.task_18_blank.text()
            self.task_18_blank.setEnabled(False)
            self.task_18_save_button.setParent(None)
            self.task_18_widget_clicked_grid.addWidget(self.task_18_edit_button,14, 0, 15, 0)
        def edit_task_18():
            self.task_18_blank.setEnabled(True)
            self.task_18_edit_button.setParent(None)
            self.task_18_widget_clicked_grid.addWidget(self.task_18_save_button, 14, 0, 15, 0)
        self.task_18_save_button = QPushButton(Localization.SAVE)
        self.task_18_save_button.clicked.connect(save_task_18)
        self.task_18_edit_button = QPushButton(Localization.EDIT)
        self.task_18_edit_button.clicked.connect(edit_task_18)

        self.task_18_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_18_file_path = 'data/tasks_data/18/' + task_18_data['id'] + '.xlsx'
        def task_18_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_18_file_path, destination_path)
            except FileNotFoundError:
                pass
        self.task_18_get_file_btn.clicked.connect(task_18_get_file_button_clicked)

        self.task_18_picture_path = 'data/tasks_data/18/example.png'
        self.task_18_picture = QPixmap(self.task_18_picture_path)
        self.task_18_picture_lbl = QLabel(self)
        self.task_18_picture_lbl.setPixmap(self.task_18_picture)
        
        self.task_18_widget_clicked_grid.addWidget(self.task_18_text, 1, 0, 5, 0)
        self.task_18_widget_clicked_grid.addWidget(self.task_18_picture_lbl, 5, 0, 9, 0, alignment=Qt.AlignCenter)
        self.task_18_widget_clicked_grid.addWidget(self.task_18_get_file_btn, 10, 0, 11, 0)
        self.task_18_widget_clicked_grid.addWidget(self.task_18_blank, 12, 0, 13, 0)
        self.task_18_widget_clicked_grid.addWidget(self.task_18_save_button, 14, 0, 15, 0)
        self.task_18_widget.setLayout(self.task_18_widget_clicked_grid)


        #191919191919191919
        self.task_19_widget = QWidget()
        task_19_data = self.tasks_data[19]
        self.task_19_text = QLabel(task_19_data['text'])
        self.task_19_text.setWordWrap(True)
        self.task_19_text.setAlignment(Qt.AlignCenter)
        self.task_19_answer = task_19_data['answer']
        self.task_19_widget_clicked_grid = QGridLayout()

        self.task_19_blank = QLineEdit()
        self.task_19_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_19():
            self.user_answers[19] = self.task_19_blank.text()
            self.task_19_blank.setEnabled(False)
            self.task_19_save_button.setParent(None)
            self.task_19_widget_clicked_grid.addWidget(self.task_19_edit_button, 9, 0, 10, 0)
        def edit_task_19():
            self.task_19_blank.setEnabled(True)
            self.task_19_edit_button.setParent(None)
            self.task_19_widget_clicked_grid.addWidget(self.task_19_save_button, 9, 0, 10, 0)
        self.task_19_save_button = QPushButton(Localization.SAVE)
        self.task_19_save_button.clicked.connect(save_task_19)
        self.task_19_edit_button = QPushButton(Localization.EDIT)
        self.task_19_edit_button.clicked.connect(edit_task_19)
        
        self.task_19_widget_clicked_grid.addWidget(self.task_19_text, 1, 0, 7, 0)
        self.task_19_widget_clicked_grid.addWidget(self.task_19_blank, 8, 0, 9, 0)
        self.task_19_widget_clicked_grid.addWidget(self.task_19_save_button, 9, 0, 10, 0)
        self.task_19_widget.setLayout(self.task_19_widget_clicked_grid)


        #202020202020202020
        self.task_20_widget = QWidget()
        task_20_data = self.tasks_data[20]
        self.task_20_text = QLabel(task_20_data['text'])
        self.task_20_text.setWordWrap(True)
        self.task_20_text.setAlignment(Qt.AlignCenter)
        self.task_20_answer = task_20_data['answer']
        self.task_20_widget_clicked_grid = QGridLayout()

        self.task_20_blank = QLineEdit()
        self.task_20_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_20():
            self.user_answers[20] = self.task_20_blank.text()
            self.task_20_blank.setEnabled(False)
            self.task_20_save_button.setParent(None)
            self.task_20_widget_clicked_grid.addWidget(self.task_20_edit_button, 9, 0, 10, 0)
        def edit_task_20():
            self.task_20_blank.setEnabled(True)
            self.task_20_edit_button.setParent(None)
            self.task_20_widget_clicked_grid.addWidget(self.task_20_save_button, 9, 0, 10, 0)
        self.task_20_save_button = QPushButton(Localization.SAVE)
        self.task_20_save_button.clicked.connect(save_task_20)
        self.task_20_edit_button = QPushButton(Localization.EDIT)
        self.task_20_edit_button.clicked.connect(edit_task_20)
        
        self.task_20_widget_clicked_grid.addWidget(self.task_20_text, 1, 0, 7, 0)
        self.task_20_widget_clicked_grid.addWidget(self.task_20_blank, 8, 0, 9, 0)
        self.task_20_widget_clicked_grid.addWidget(self.task_20_save_button, 9, 0, 10, 0)
        self.task_20_widget.setLayout(self.task_20_widget_clicked_grid)


        #212121212121212121
        self.task_21_widget = QWidget()
        task_21_data = self.tasks_data[21]
        self.task_21_text = QLabel(task_21_data['text'])
        self.task_21_text.setWordWrap(True)
        self.task_21_text.setAlignment(Qt.AlignCenter)
        self.task_21_answer = task_21_data['answer']
        self.task_21_widget_clicked_grid = QGridLayout()

        self.task_21_blank = QLineEdit()
        self.task_21_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_21():
            self.user_answers[21] = self.task_21_blank.text()
            self.task_21_blank.setEnabled(False)
            self.task_21_save_button.setParent(None)
            self.task_21_widget_clicked_grid.addWidget(self.task_21_edit_button, 9, 0, 10, 0)
        def edit_task_21():
            self.task_21_blank.setEnabled(True)
            self.task_21_edit_button.setParent(None)
            self.task_21_widget_clicked_grid.addWidget(self.task_21_save_button, 9, 0, 10, 0)
        self.task_21_save_button = QPushButton(Localization.SAVE)
        self.task_21_save_button.clicked.connect(save_task_21)
        self.task_21_edit_button = QPushButton(Localization.EDIT)
        self.task_21_edit_button.clicked.connect(edit_task_21)
        
        self.task_21_widget_clicked_grid.addWidget(self.task_21_text, 1, 0, 7, 0)
        self.task_21_widget_clicked_grid.addWidget(self.task_21_blank, 8, 0, 9, 0)
        self.task_21_widget_clicked_grid.addWidget(self.task_21_save_button, 9, 0, 10, 0)
        self.task_21_widget.setLayout(self.task_21_widget_clicked_grid)


        #222222222222222222
        self.task_22_widget = QWidget()
        task_22_data = self.tasks_data[22]
        self.task_22_text_for_lbl = task_22_data['text']
        if task_22_data['program'].strip() != 'нет':
            self.task_22_text_for_lbl = self.task_22_text_for_lbl + '\n\n' + task_22_data['program']
        self.task_22_text = QLabel(self.task_22_text_for_lbl)
        self.task_22_text.setWordWrap(True)
        self.task_22_answer = task_22_data['answer']
        self.task_22_widget_clicked_grid = QGridLayout()

        self.task_22_blank = QLineEdit()
        self.task_22_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_22():
            self.user_answers[22] = self.task_22_blank.text()
            self.task_22_blank.setEnabled(False)
            self.task_22_save_button.setParent(None)
            self.task_22_widget_clicked_grid.addWidget(self.task_22_edit_button, 9, 0, 10, 0)
        def edit_task_22():
            self.task_22_blank.setEnabled(True)
            self.task_22_edit_button.setParent(None)
            self.task_22_widget_clicked_grid.addWidget(self.task_22_save_button, 9, 0, 10, 0)
        self.task_22_save_button = QPushButton(Localization.SAVE)
        self.task_22_save_button.clicked.connect(save_task_22)
        self.task_22_edit_button = QPushButton(Localization.EDIT)
        self.task_22_edit_button.clicked.connect(edit_task_22)
        
        self.task_22_widget_clicked_grid.addWidget(self.task_22_text, 1, 0, 7, 0, alignment=Qt.AlignCenter)
        self.task_22_widget_clicked_grid.addWidget(self.task_22_blank, 8, 0, 9, 0)
        self.task_22_widget_clicked_grid.addWidget(self.task_22_save_button, 9, 0, 10, 0)
        self.task_22_widget.setLayout(self.task_22_widget_clicked_grid)


        #232323232323232323
        self.task_23_widget = QWidget()
        task_23_data = self.tasks_data[23]
        self.task_23_text = QLabel(task_23_data['text'])
        self.task_23_text.setWordWrap(True)
        self.task_23_text.setAlignment(Qt.AlignCenter)
        self.task_23_answer = task_23_data['answer']
        self.task_23_widget_clicked_grid = QGridLayout()

        self.task_23_blank = QLineEdit()
        self.task_23_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_23():
            self.user_answers[23] = self.task_23_blank.text()
            self.task_23_blank.setEnabled(False)
            self.task_23_save_button.setParent(None)
            self.task_23_widget_clicked_grid.addWidget(self.task_23_edit_button, 9, 0, 10, 0)
        def edit_task_23():
            self.task_23_blank.setEnabled(True)
            self.task_23_edit_button.setParent(None)
            self.task_23_widget_clicked_grid.addWidget(self.task_23_save_button, 9, 0, 10, 0)
        self.task_23_save_button = QPushButton(Localization.SAVE)
        self.task_23_save_button.clicked.connect(save_task_23)
        self.task_23_edit_button = QPushButton(Localization.EDIT)
        self.task_23_edit_button.clicked.connect(edit_task_23)
        
        self.task_23_widget_clicked_grid.addWidget(self.task_23_text, 1, 0, 7, 0)
        self.task_23_widget_clicked_grid.addWidget(self.task_23_blank, 8, 0, 9, 0)
        self.task_23_widget_clicked_grid.addWidget(self.task_23_save_button, 9, 0, 10, 0)
        self.task_23_widget.setLayout(self.task_23_widget_clicked_grid)


        #242424242424242424
        self.task_24_widget = QWidget()
        task_24_data = self.tasks_data[24]
        self.task_24_text = QLabel(task_24_data['text'])
        self.task_24_text.setWordWrap(True)
        self.task_24_text.setAlignment(Qt.AlignCenter)
        self.task_24_answer = task_24_data['answer']
        self.task_24_widget_clicked_grid = QGridLayout()

        self.task_24_blank = QLineEdit()
        self.task_24_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_24():
            self.user_answers[24] = self.task_24_blank.text()
            self.task_24_blank.setEnabled(False)
            self.task_24_save_button.setParent(None)
            self.task_24_widget_clicked_grid.addWidget(self.task_24_edit_button, 11, 0, 12, 0)
        def edit_task_24():
            self.task_24_blank.setEnabled(True)
            self.task_24_edit_button.setParent(None)
            self.task_24_widget_clicked_grid.addWidget(self.task_24_save_button, 11, 0, 12, 0)
        self.task_24_save_button = QPushButton(Localization.SAVE)
        self.task_24_save_button.clicked.connect(save_task_24)
        self.task_24_edit_button = QPushButton(Localization.EDIT)
        self.task_24_edit_button.clicked.connect(edit_task_24)

        self.task_24_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_24_file_path = 'data/tasks_data/24/' + task_24_data['id'] + '.txt'
        def task_24_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_24_file_path, destination_path)
            except FileNotFoundError:
                pass
        self.task_24_get_file_btn.clicked.connect(task_24_get_file_button_clicked)
        
        self.task_24_widget_clicked_grid.addWidget(self.task_24_text, 1, 0, 7, 0)
        self.task_24_widget_clicked_grid.addWidget(self.task_24_get_file_btn, 8, 0, 10, 0)
        self.task_24_widget_clicked_grid.addWidget(self.task_24_blank, 9, 0, 11, 0)
        self.task_24_widget_clicked_grid.addWidget(self.task_24_save_button, 11, 0, 12, 0)
        self.task_24_widget.setLayout(self.task_24_widget_clicked_grid)


        #252525252525252525
        self.task_25_widget = QWidget()
        task_25_data = self.tasks_data[25]
        self.task_25_text = QLabel(task_25_data['text'])
        self.task_25_text.setWordWrap(True)
        self.task_25_text.setAlignment(Qt.AlignCenter)
        self.task_25_answer = task_25_data['answer']
        self.task_25_widget_clicked_grid = QGridLayout()

        self.task_25_blank = QLineEdit()
        self.task_25_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_25():
            self.user_answers[25] = self.task_25_blank.text()
            self.task_25_blank.setEnabled(False)
            self.task_25_save_button.setParent(None)
            self.task_25_widget_clicked_grid.addWidget(self.task_25_edit_button, 9, 0, 10, 0)
        def edit_task_25():
            self.task_25_blank.setEnabled(True)
            self.task_25_edit_button.setParent(None)
            self.task_25_widget_clicked_grid.addWidget(self.task_25_save_button, 9, 0, 10, 0)
        self.task_25_save_button = QPushButton(Localization.SAVE)
        self.task_25_save_button.clicked.connect(save_task_25)
        self.task_25_edit_button = QPushButton(Localization.EDIT)
        self.task_25_edit_button.clicked.connect(edit_task_25)
        
        self.task_25_widget_clicked_grid.addWidget(self.task_25_text, 1, 0, 7, 0)
        self.task_25_widget_clicked_grid.addWidget(self.task_25_blank, 8, 0, 9, 0)
        self.task_25_widget_clicked_grid.addWidget(self.task_25_save_button, 9, 0, 10, 0)
        self.task_25_widget.setLayout(self.task_25_widget_clicked_grid)


        #262626262626262626
        self.task_26_widget = QWidget()
        task_26_data = self.tasks_data[26]
        self.task_26_text = QLabel(task_26_data['text'])
        self.task_26_text.setWordWrap(True)
        self.task_26_text.setAlignment(Qt.AlignCenter)
        self.task_26_answer = task_26_data['answer']
        self.task_26_widget_clicked_grid = QGridLayout()

        self.task_26_blank = QLineEdit()
        self.task_26_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_26():
            self.user_answers[26] = self.task_26_blank.text()
            self.task_26_blank.setEnabled(False)
            self.task_26_save_button.setParent(None)
            self.task_26_widget_clicked_grid.addWidget(self.task_26_edit_button, 11, 0, 12, 0)
        def edit_task_26():
            self.task_26_blank.setEnabled(True)
            self.task_26_edit_button.setParent(None)
            self.task_26_widget_clicked_grid.addWidget(self.task_26_save_button, 11, 0, 12, 0)
        self.task_26_save_button = QPushButton(Localization.SAVE)
        self.task_26_save_button.clicked.connect(save_task_26)
        self.task_26_edit_button = QPushButton(Localization.EDIT)
        self.task_26_edit_button.clicked.connect(edit_task_26)

        self.task_26_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_26_file_path = 'data/tasks_data/26/' + task_26_data['id'] + '.txt'
        def task_26_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_26_file_path, destination_path)
            except FileNotFoundError:
                pass
        self.task_26_get_file_btn.clicked.connect(task_26_get_file_button_clicked)
        
        self.task_26_widget_clicked_grid.addWidget(self.task_26_text, 1, 0, 7, 0)
        self.task_26_widget_clicked_grid.addWidget(self.task_26_get_file_btn, 8, 0, 10, 0)
        self.task_26_widget_clicked_grid.addWidget(self.task_26_blank, 9, 0, 11, 0)
        self.task_26_widget_clicked_grid.addWidget(self.task_26_save_button, 11, 0, 12, 0)
        self.task_26_widget.setLayout(self.task_26_widget_clicked_grid)


        #272727272727272727
        self.task_27_widget = QWidget()
        task_27_data = self.tasks_data[27]
        self.task_27_text = QLabel(task_27_data['text'])
        self.task_27_text.setWordWrap(True)
        self.task_27_text.setAlignment(Qt.AlignCenter)
        self.task_27_answer = task_27_data['answer']
        self.task_27_widget_clicked_grid = QGridLayout()

        self.task_27_blank = QLineEdit()
        self.task_27_blank.setPlaceholderText(Localization.BLANK_PLACEHOLDER)
        def save_task_27():
            self.user_answers[27] = self.task_27_blank.text()
            self.task_27_blank.setEnabled(False)
            self.task_27_save_button.setParent(None)
            self.task_27_widget_clicked_grid.addWidget(self.task_27_edit_button, 11, 0, 12, 0)
        def edit_task_27():
            self.task_27_blank.setEnabled(True)
            self.task_27_edit_button.setParent(None)
            self.task_27_widget_clicked_grid.addWidget(self.task_27_save_button, 11, 0, 12, 0)
        self.task_27_save_button = QPushButton(Localization.SAVE)
        self.task_27_save_button.clicked.connect(save_task_27)
        self.task_27_edit_button = QPushButton(Localization.EDIT)
        self.task_27_edit_button.clicked.connect(edit_task_27)

        self.task_27_get_file_a_btn = QPushButton(Localization.GET_FILE_A, self)
        self.task_27_get_file_b_btn = QPushButton(Localization.GET_FILE_B, self)
        self.task_27_file_a_path = 'data/tasks_data/27/' + task_27_data['id'] + '_A.txt'
        self.task_27_file_b_path = 'data/tasks_data/27/' + task_27_data['id'] + '_B.txt'

        def task_27_get_file_a_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_27_file_a_path, destination_path)
            except FileNotFoundError:
                pass
        self.task_27_get_file_a_btn.clicked.connect(task_27_get_file_a_button_clicked)

        def task_27_get_file_b_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_27_file_b_path, destination_path)
            except FileNotFoundError:
                pass
        self.task_27_get_file_b_btn.clicked.connect(task_27_get_file_b_button_clicked)
        
        self.task_27_widget_clicked_grid.addWidget(self.task_27_text, 1, 0, 7, 0)
        self.task_27_widget_clicked_grid.addWidget(self.task_27_get_file_a_btn, 8, 0, 9, 0)
        self.task_27_widget_clicked_grid.addWidget(self.task_27_get_file_b_btn, 9, 0, 10, 0)
        self.task_27_widget_clicked_grid.addWidget(self.task_27_blank, 10, 0, 11, 0)
        self.task_27_widget_clicked_grid.addWidget(self.task_27_save_button, 11, 0, 12, 0)
        self.task_27_widget.setLayout(self.task_27_widget_clicked_grid)

        #aft
        self.widgets_list = {
            0: self.contents_default,
            1: self.task_1_widget,
            2: self.task_2_widget,
            3: self.task_3_widget,
            4: self.task_4_widget,
            5: self.task_5_widget,
            6: self.task_6_widget,
            7: self.task_7_widget,
            8: self.task_8_widget,
            9: self.task_9_widget,
            10: self.task_10_widget,
            11: self.task_11_widget,
            12: self.task_12_widget,
            13: self.task_13_widget,
            14: self.task_14_widget,
            15: self.task_15_widget,
            16: self.task_16_widget,
            17: self.task_17_widget,
            18: self.task_18_widget,
            19: self.task_19_widget,
            20: self.task_20_widget,
            21: self.task_21_widget,
            22: self.task_22_widget,
            23: self.task_23_widget,
            24: self.task_24_widget,
            25: self.task_25_widget,
            26: self.task_26_widget,
            27: self.task_27_widget
        }
        for key in self.widgets_list:
            self.contents_tasks.addWidget(self.widgets_list[key])

        def btn_clicked(button_num):
            try:
                self.contents_tasks.setCurrentIndex(button_num)
            except KeyError:
                pass

        def buttons_set(num):
            self.buttons_list[num].clicked.connect(lambda: btn_clicked(num))
        for num in range(1, 28):
            buttons_set(num)

        self.contents_tasks.setCurrentIndex(0)
        self.scrollArea_nums = QScrollArea()
        self.scrollArea_nums.setWidgetResizable(True)
        self.scrollArea_nums.setWidget(self.contents_nums)

        self.scrollArea_tasks = QScrollArea()
        self.scrollArea_tasks.setWidgetResizable(True)
        self.scrollArea_tasks.setWidget(self.contents_tasks)

        self.finish_btn = QPushButton(Localization.FINISH)
        self.finish_btn.clicked.connect(self.finish)

        self.centralLayout.addWidget(self.scrollArea_tasks, 0, 0, 1, 1)
        self.centralLayout.addWidget(self.scrollArea_nums, 0, 2, 1, 12)
        self.centralLayout.addWidget(self.finish_btn, 1, 0, 2, 12)
        self.centralWidget.setLayout(self.centralLayout)
        self.setCentralWidget(self.centralWidget)
        

    def finish(self):
        for task in range(1, 28):
            self.finish_btn.setText(Localization.SHOW_RESULTS)
            button_name_1 = 'task_' + str(task) + '_save_button'
            button_name_2 = 'task_' + str(task) + '_edit_button'
            blank_name = 'task_' + str(task) + '_blank'
            self.__dict__[button_name_1].setParent(None)
            self.__dict__[button_name_2].setParent(None)
            self.__dict__[blank_name].setEnabled(False)

        self.results_contents = QWidget()
        self.widgets_list[28] = self.results_contents
        self.contents_tasks.addWidget(self.widgets_list[28])
        self.results_grid_clicked = QGridLayout()

        task_num = 1
        for column in range(1, 4):
            for task in range(task_num, task_num + 9):
                correct_text = Localization.CORRECT if self.user_answers[task] == self.tasks_data[task]['answer'] else Localization.INCORRECT
                header_text = Localization.RESULTS_HEADER_TEXT % (task, correct_text)
                user_text = Localization.YOUR_ANSWER % self.user_answers[task] if not self.user_answers[task] is None else Localization.NO_ANSWER
                descr_text = Localization.CORRECT_ANSWER % self.tasks_data[task]['answer']
                lbl = QLabel(header_text + '\n' + user_text + '\n' + descr_text)
                row = task
                if 10 <= row <= 18:
                    row = row - 9
                elif row >= 19:
                    row = row - 18
                row = row - 1
                self.results_grid_clicked.addWidget(lbl, row, column)
            task_num = task_num + 9

        self.user_results = [None]
        for task in range(1, 28):
            if self.user_answers[task] == self.tasks_data[task]['answer']:
                self.user_results.append(True)
            else:
                self.user_results.append(False)
        self.number_of_completed_tasks = self.user_results.count(True)
        self.result_text = Localization.RESULT % self.number_of_completed_tasks

        self.first_points = 0
        for ind in range(1, 28):
            if self.user_results[ind] and ind < 26:
                self.first_points = self.first_points + 1
            elif self.user_results[ind] and 26 <= ind <= 27:
                self.first_points = self.first_points + 2
        self.total_points = int(Config.POINTS[str(self.first_points)])
        self.result_points_text = Localization.RESULT_IN_POINTS % (self.first_points, self.total_points)
        self.result_text = self.result_text + '\n' + self.result_points_text

        self.res_lbl = QLabel(self.result_text)
        self.results_grid_clicked.addWidget(self.res_lbl, 9, 1, alignment=Qt.AlignCenter)
        
        self.results_contents.setLayout(self.results_grid_clicked)
        self.contents_tasks.setCurrentIndex(28)


class UI_BaseWindow(object):
    "Окно базы заданий."
    def back_btn_clicked(self):
        self.menubar_var.clear()
        self.setupUi_continue()

    def setupUi_continue(self):
        self.setWindowTitle(Localization.BASE_WIN_TITLE)
        self.setWindowIcon(QIcon('icons/icon.png'))

        self.exitAction_var = QAction(QIcon('icons/exit.png'), '&' + Localization.EXIT, self)
        self.exitAction_var.setShortcut(Localization.EXIT_SHORTCUT)
        self.exitAction_var.setStatusTip(Localization.EXIT_STATUS_TIP)
        self.exitAction_var.triggered.connect(qApp.quit)
        self.statusBar()

        self.menubar_var = self.menuBar()
        self.fileMenu_var = self.menubar_var.addMenu('&' + Localization.FILE)
        self.fileMenu_var.addAction(self.exitAction_var)

        self.lbl = QLabel(Localization.CHOOSE_TASK, self)
        self.show_btn = QPushButton(Localization.SHOW, self)
        self.show_btn.clicked.connect(self.show_btn_clicked)

        self.centralWidget = QWidget()
        self.combo = QComboBox()
        self.list_of_items = [Localization.TASK + str(num) for num in range(1, 28)]
        self.combo.addItems(self.list_of_items)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.lbl, 1, 0, alignment=Qt.AlignCenter)
        grid.addWidget(self.combo, 2, 0, 4, 0)
        grid.addWidget(self.show_btn, 3, 0, 5, 0)
        
        self.centralWidget.setLayout(grid)
        self.setCentralWidget(self.centralWidget)

    def show_btn_clicked(self):
        task_num = self.combo.currentText().replace(Localization.TASK, '')

        self.lbl2 = QLabel(Localization.TASK_HEADER % task_num, self)
        self.back_btn = QPushButton(Localization.BACK, self)
        self.back_btn.clicked.connect(self.back_btn_clicked)

        # 1111111111
        self.task_1_widget = QWidget()
        task_1_data = Task_Chooser.choose_task_1()
        self.task_1_text = QLabel(task_1_data['text'])
        self.task_1_text.setWordWrap(True)
        self.task_1_text.setAlignment(Qt.AlignCenter)
        self.task_1_answer = QLabel(Localization.ANSWER + task_1_data['answer'])
        self.task_1_answer.setWordWrap(True)
        self.task_1_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_1_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_1_description = task_1_data['description']
        self.task_1_description_widget = QLabel(self.task_1_description)
        self.task_1_description_widget.setWordWrap(True)
        task_1_widget_clicked_grid = QGridLayout()

        self.task_1_picture_path = 'data/tasks_data/1/' + task_1_data['id'] + '.png'
        self.task_1_picture_exists = True if os.path.exists(self.task_1_picture_path) else False
        if self.task_1_picture_exists:
            self.task_1_picture = QPixmap(self.task_1_picture_path)
            self.task_1_picture_lbl = QLabel(self)
            self.task_1_picture_lbl.setPixmap(self.task_1_picture)
        
        task_1_widget_clicked_grid.addWidget(self.task_1_text, 1, 0, 7, 0)
        if self.task_1_picture_exists:
            task_1_widget_clicked_grid.addWidget(self.task_1_picture_lbl, 10, 0, 12, 0, alignment=Qt.AlignCenter)
        task_1_widget_clicked_grid.addWidget(self.task_1_show_ans_btn, 25, 0, 27, 0)
        task_1_widget_clicked_grid.addWidget(self.task_1_show_descr_btn, 55, 0, 63, 0)
        self.task_1_widget.setLayout(task_1_widget_clicked_grid)

        def task_1_ans_button_clicked():
            self.task_1_show_ans_btn.setParent(None)
            task_1_widget_clicked_grid.addWidget(self.task_1_answer, 25, 0, 27, 0)
        def task_1_descr_button_clicked():
            self.task_1_show_descr_btn.setParent(None)
            task_1_widget_clicked_grid.addWidget(self.task_1_description_widget, 55, 0, 63, 0)

        self.task_1_show_ans_btn.clicked.connect(task_1_ans_button_clicked)
        self.task_1_show_descr_btn.clicked.connect(task_1_descr_button_clicked)


        # 222222222
        self.task_2_widget = QWidget()
        task_2_data = Task_Chooser.choose_task_2()
        self.task_2_text = QLabel(task_2_data['text'])
        self.task_2_text.setWordWrap(True)
        self.task_2_text.setAlignment(Qt.AlignCenter)
        self.task_2_answer = QLabel('Ответ: ' + task_2_data['answer'])
        self.task_2_answer.setWordWrap(True)
        self.task_2_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_2_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_2_description = task_2_data['description']
        self.task_2_description_widget = QLabel(self.task_2_description)
        self.task_2_description_widget.setWordWrap(True)
        task_2_widget_clicked_grid = QGridLayout()

        self.task_2_picture_path = 'data/tasks_data/2/' + task_2_data['id'] + '.png'
        self.task_2_picture_exists = True if os.path.exists(self.task_2_picture_path) else False
        if self.task_2_picture_exists:
            self.task_2_picture = QPixmap(self.task_2_picture_path)
            self.task_2_picture_lbl = QLabel(self)
            self.task_2_picture_lbl.setPixmap(self.task_2_picture)
        
        task_2_widget_clicked_grid.addWidget(self.task_2_text, 1, 0, 7, 0)
        if self.task_2_picture_exists:
            task_2_widget_clicked_grid.addWidget(self.task_2_picture_lbl, 10, 0, 12, 0, alignment=Qt.AlignCenter)
        task_2_widget_clicked_grid.addWidget(self.task_2_show_ans_btn, 25, 0, 27, 0)
        task_2_widget_clicked_grid.addWidget(self.task_2_show_descr_btn, 55, 0, 63, 0)
        self.task_2_widget.setLayout(task_2_widget_clicked_grid)

        def task_2_ans_button_clicked():
            self.task_2_show_ans_btn.setParent(None)
            task_2_widget_clicked_grid.addWidget(self.task_2_answer, 25, 0, 27, 0)
        def task_2_descr_button_clicked():
            self.task_2_show_descr_btn.setParent(None)
            task_2_widget_clicked_grid.addWidget(self.task_2_description_widget, 55, 0, 63, 0)

        self.task_2_show_ans_btn.clicked.connect(task_2_ans_button_clicked)
        self.task_2_show_descr_btn.clicked.connect(task_2_descr_button_clicked)


        # 3333333333333333
        self.task_3_widget = QWidget()
        task_3_data = Task_Chooser.choose_task_3()

        self.task_3_text1 = QLabel(task_3_data['text1'])
        self.task_3_text1.setWordWrap(True)
        self.task_3_text1.setAlignment(Qt.AlignCenter)
        self.task_3_text2 = QLabel(task_3_data['text2'])
        self.task_3_text2.setWordWrap(True)
        self.task_3_text2.setAlignment(Qt.AlignCenter)
        self.task_3_text3 = QLabel(task_3_data['text3'])
        self.task_3_text3.setAlignment(Qt.AlignCenter)
        self.task_3_text4 = QLabel(task_3_data['text4'])
        self.task_3_text3.setWordWrap(True)
        self.task_3_text4.setWordWrap(True)
        self.task_3_text4.setAlignment(Qt.AlignCenter)
        self.task_3_text5 = QLabel(task_3_data['text5'])
        self.task_3_text5.setWordWrap(True)
        self.task_3_text5.setAlignment(Qt.AlignCenter)
        self.task_3_text6 = QLabel(task_3_data['text6'])
        self.task_3_text6.setWordWrap(True)
        self.task_3_text6.setAlignment(Qt.AlignCenter)

        self.task_3_answer = QLabel('Ответ: ' + task_3_data['answer'])
        self.task_3_answer.setWordWrap(True)
        self.task_3_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_3_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_3_description = task_3_data['description']
        self.task_3_description_widget = QLabel(self.task_3_description)
        self.task_3_description_widget.setWordWrap(True)
        task_3_widget_clicked_grid = QGridLayout()

        self.task_3_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_3_file_path = 'data/tasks_data/3/' + task_3_data['id'] + '.xlsx'

        self.task_3_picture_2to3_path = 'data/tasks_data/3/' + task_3_data['id'] + '_2to3.png'
        self.task_3_picture_2to3 = QPixmap(self.task_3_picture_2to3_path)
        self.task_3_picture_2to3_lbl = QLabel(self)
        self.task_3_picture_2to3_lbl.setPixmap(self.task_3_picture_2to3)
        self.task_3_picture_3to4_path = 'data/tasks_data/3/' + task_3_data['id'] + '_3to4.png'
        self.task_3_picture_3to4 = QPixmap(self.task_3_picture_3to4_path)
        self.task_3_picture_3to4_lbl = QLabel(self)
        self.task_3_picture_3to4_lbl.setPixmap(self.task_3_picture_3to4)
        self.task_3_picture_4to5_path = 'data/tasks_data/3/' + task_3_data['id'] + '_4to5.png'
        self.task_3_picture_4to5 = QPixmap(self.task_3_picture_4to5_path)
        self.task_3_picture_4to5_lbl = QLabel(self)
        self.task_3_picture_4to5_lbl.setPixmap(self.task_3_picture_4to5)
        self.task_3_picture_5to6_path = 'data/tasks_data/3/' + task_3_data['id'] + '_5to6.png'
        self.task_3_picture_5to6 = QPixmap(self.task_3_picture_5to6_path)
        self.task_3_picture_5to6_lbl = QLabel(self)
        self.task_3_picture_5to6_lbl.setPixmap(self.task_3_picture_5to6)
        
        task_3_widget_clicked_grid.addWidget(self.task_3_text1, 0, 0, 1, 0)
        task_3_widget_clicked_grid.addWidget(self.task_3_get_file_btn, 2, 0, 3, 0)
        task_3_widget_clicked_grid.addWidget(self.task_3_text2, 4, 0, 6, 0)
        task_3_widget_clicked_grid.addWidget(self.task_3_picture_2to3_lbl, 9, 0, 11, 0, alignment=Qt.AlignCenter)
        task_3_widget_clicked_grid.addWidget(self.task_3_text3, 15, 0, 16, 0)
        task_3_widget_clicked_grid.addWidget(self.task_3_picture_3to4_lbl, 25, 0, 27, 0, alignment=Qt.AlignCenter)
        task_3_widget_clicked_grid.addWidget(self.task_3_text4, 39, 0, 41, 0)
        task_3_widget_clicked_grid.addWidget(self.task_3_picture_4to5_lbl, 62, 0, 64, 0, alignment=Qt.AlignCenter)
        task_3_widget_clicked_grid.addWidget(self.task_3_text5, 86, 0, 87, 0)
        task_3_widget_clicked_grid.addWidget(self.task_3_picture_5to6_lbl, 166, 0, 168, 0, alignment=Qt.AlignCenter)
        task_3_widget_clicked_grid.addWidget(self.task_3_text6, 330, 0, 332, 0)
        task_3_widget_clicked_grid.addWidget(self.task_3_show_ans_btn, 650, 0, 652, 0)
        task_3_widget_clicked_grid.addWidget(self.task_3_show_descr_btn, 1400, 0, 1407, 0)
        self.task_3_widget.setLayout(task_3_widget_clicked_grid)

        def task_3_ans_button_clicked():
            self.task_3_show_ans_btn.setParent(None)
            task_3_widget_clicked_grid.addWidget(self.task_3_answer, 650, 0, 652, 0)
        def task_3_descr_button_clicked():
            self.task_3_show_descr_btn.setParent(None)
            task_3_widget_clicked_grid.addWidget(self.task_3_description_widget, 1400, 0, 1407, 0)
        def task_3_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_3_file_path, destination_path)
            except FileNotFoundError:
                pass

        self.task_3_show_ans_btn.clicked.connect(task_3_ans_button_clicked)
        self.task_3_show_descr_btn.clicked.connect(task_3_descr_button_clicked)
        self.task_3_get_file_btn.clicked.connect(task_3_get_file_button_clicked)


        # 4444444444
        self.task_4_widget = QWidget()
        task_4_data = Task_Chooser.choose_task_4()
        self.task_4_text = QLabel(task_4_data['text'])
        self.task_4_text.setWordWrap(True)
        self.task_4_text.setAlignment(Qt.AlignCenter)
        self.task_4_answer = QLabel('Ответ: ' + task_4_data['answer'])
        self.task_4_answer.setWordWrap(True)
        self.task_4_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_4_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_4_description = task_4_data['description']
        self.task_4_description_widget = QLabel(self.task_4_description)
        self.task_4_description_widget.setWordWrap(True)
        task_4_widget_clicked_grid = QGridLayout()
        
        task_4_widget_clicked_grid.addWidget(self.task_4_text, 1, 0, 7, 0)
        task_4_widget_clicked_grid.addWidget(self.task_4_show_ans_btn, 10, 0, 12, 0)
        task_4_widget_clicked_grid.addWidget(self.task_4_show_descr_btn, 25, 0, 33, 0)
        self.task_4_widget.setLayout(task_4_widget_clicked_grid)

        def task_4_ans_button_clicked():
            self.task_4_show_ans_btn.setParent(None)
            task_4_widget_clicked_grid.addWidget(self.task_4_answer, 10, 0, 12, 0)
        def task_4_descr_button_clicked():
            self.task_4_show_descr_btn.setParent(None)
            task_4_widget_clicked_grid.addWidget(self.task_4_description_widget, 25, 0, 33, 0)

        self.task_4_show_ans_btn.clicked.connect(task_4_ans_button_clicked)
        self.task_4_show_descr_btn.clicked.connect(task_4_descr_button_clicked)


        # 5555555555
        self.task_5_widget = QWidget()
        task_5_data = Task_Chooser.choose_task_5()
        self.task_5_text = QLabel(task_5_data['text'])
        self.task_5_text.setWordWrap(True)
        self.task_5_text.setAlignment(Qt.AlignCenter)
        self.task_5_answer = QLabel('Ответ: ' + task_5_data['answer'])
        self.task_5_answer.setWordWrap(True)
        self.task_5_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_5_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_5_description = task_5_data['description']
        self.task_5_description_widget = QLabel(self.task_5_description)
        self.task_5_description_widget.setWordWrap(True)
        task_5_widget_clicked_grid = QGridLayout()
        
        task_5_widget_clicked_grid.addWidget(self.task_5_text, 1, 0, 7, 0)
        task_5_widget_clicked_grid.addWidget(self.task_5_show_ans_btn, 10, 0, 12, 0)
        task_5_widget_clicked_grid.addWidget(self.task_5_show_descr_btn, 25, 0, 33, 0)
        self.task_5_widget.setLayout(task_5_widget_clicked_grid)

        def task_5_ans_button_clicked():
            self.task_5_show_ans_btn.setParent(None)
            task_5_widget_clicked_grid.addWidget(self.task_5_answer, 10, 0, 12, 0)
        def task_5_descr_button_clicked():
            self.task_5_show_descr_btn.setParent(None)
            task_5_widget_clicked_grid.addWidget(self.task_5_description_widget, 25, 0, 33, 0)

        self.task_5_show_ans_btn.clicked.connect(task_5_ans_button_clicked)
        self.task_5_show_descr_btn.clicked.connect(task_5_descr_button_clicked)


        # 66666666
        self.task_6_widget = QWidget()
        task_6_data = Task_Chooser.choose_task_6()
        self.task_6_text = QLabel(task_6_data['text'] + '\n\n' + task_6_data['program'])
        self.task_6_text.setWordWrap(True)
        self.task_6_answer = QLabel('Ответ: ' + task_6_data['answer'])
        self.task_6_answer.setWordWrap(True)
        self.task_6_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_6_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_6_description = task_6_data['description']
        if task_6_data['python'].strip() != 'нет':
            self.task_6_description = self.task_6_description + '\n\n' + task_6_data['python']
        self.task_6_description_widget = QLabel(self.task_6_description)
        self.task_6_description_widget.setWordWrap(True)
        task_6_widget_clicked_grid = QGridLayout()
        
        task_6_widget_clicked_grid.addWidget(self.task_6_text, 1, 0, 7, 0, alignment=Qt.AlignCenter)
        task_6_widget_clicked_grid.addWidget(self.task_6_show_ans_btn, 10, 0, 12, 0)
        task_6_widget_clicked_grid.addWidget(self.task_6_show_descr_btn, 25, 0, 33, 0)
        self.task_6_widget.setLayout(task_6_widget_clicked_grid)

        def task_6_ans_button_clicked():
            self.task_6_show_ans_btn.setParent(None)
            task_6_widget_clicked_grid.addWidget(self.task_6_answer, 10, 0, 12, 0)
        def task_6_descr_button_clicked():
            self.task_6_show_descr_btn.setParent(None)
            task_6_widget_clicked_grid.addWidget(self.task_6_description_widget, 25, 0, 33, 0)

        self.task_6_show_ans_btn.clicked.connect(task_6_ans_button_clicked)
        self.task_6_show_descr_btn.clicked.connect(task_6_descr_button_clicked)


        # 7777777777
        self.task_7_widget = QWidget()
        task_7_data = Task_Chooser.choose_task_7()
        self.task_7_text = QLabel(task_7_data['text'])
        self.task_7_text.setWordWrap(True)
        self.task_7_text.setAlignment(Qt.AlignCenter)
        self.task_7_answer = QLabel('Ответ: ' + task_7_data['answer'])
        self.task_7_answer.setWordWrap(True)
        self.task_7_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_7_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_7_description = task_7_data['description']
        self.task_7_description_widget = QLabel(self.task_7_description)
        self.task_7_description_widget.setWordWrap(True)
        task_7_widget_clicked_grid = QGridLayout()
        
        task_7_widget_clicked_grid.addWidget(self.task_7_text, 1, 0, 7, 0)
        task_7_widget_clicked_grid.addWidget(self.task_7_show_ans_btn, 10, 0, 12, 0)
        task_7_widget_clicked_grid.addWidget(self.task_7_show_descr_btn, 27, 0, 33, 0)
        self.task_7_widget.setLayout(task_7_widget_clicked_grid)

        def task_7_ans_button_clicked():
            self.task_7_show_ans_btn.setParent(None)
            task_7_widget_clicked_grid.addWidget(self.task_7_answer, 10, 0, 12, 0)
        def task_7_descr_button_clicked():
            self.task_7_show_descr_btn.setParent(None)
            task_7_widget_clicked_grid.addWidget(self.task_7_description_widget, 27, 0, 33, 0)

        self.task_7_show_ans_btn.clicked.connect(task_7_ans_button_clicked)
        self.task_7_show_descr_btn.clicked.connect(task_7_descr_button_clicked)


        # 88888888888888
        self.task_8_widget = QWidget()
        task_8_data = Task_Chooser.choose_task_8()
        self.task_8_text = QLabel(task_8_data['text'])
        self.task_8_text.setWordWrap(True)
        self.task_8_text.setAlignment(Qt.AlignCenter)
        self.task_8_answer = QLabel('Ответ: ' + task_8_data['answer'])
        self.task_8_answer.setWordWrap(True)
        self.task_8_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_8_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_8_description = task_8_data['description']
        if task_8_data['python'].strip() != 'нет':
            self.task_8_description = self.task_8_description + '\n\n' + task_8_data['python']
        self.task_8_description_widget = QLabel(self.task_8_description)
        self.task_8_description_widget.setWordWrap(True)
        task_8_widget_clicked_grid = QGridLayout()
        
        task_8_widget_clicked_grid.addWidget(self.task_8_text, 1, 0, 7, 0)
        task_8_widget_clicked_grid.addWidget(self.task_8_show_ans_btn, 10, 0, 12, 0)
        task_8_widget_clicked_grid.addWidget(self.task_8_show_descr_btn, 25, 0, 33, 0)
        self.task_8_widget.setLayout(task_8_widget_clicked_grid)

        def task_8_ans_button_clicked():
            self.task_8_show_ans_btn.setParent(None)
            task_8_widget_clicked_grid.addWidget(self.task_8_answer, 10, 0, 12, 0)
        def task_8_descr_button_clicked():
            self.task_8_show_descr_btn.setParent(None)
            task_8_widget_clicked_grid.addWidget(self.task_8_description_widget, 25, 0, 33, 0)

        self.task_8_show_ans_btn.clicked.connect(task_8_ans_button_clicked)
        self.task_8_show_descr_btn.clicked.connect(task_8_descr_button_clicked)


        # 9999999999
        self.task_9_widget = QWidget()
        task_9_data = Task_Chooser.choose_task_9()
        self.task_9_text = QLabel(task_9_data['text'])
        self.task_9_text.setWordWrap(True)
        self.task_9_text.setAlignment(Qt.AlignCenter)
        self.task_9_answer = QLabel('Ответ: ' + task_9_data['answer'])
        self.task_9_answer.setWordWrap(True)
        self.task_9_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_9_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_9_description = task_9_data['description']
        self.task_9_description_widget = QLabel(self.task_9_description)
        self.task_9_description_widget.setWordWrap(True)
        task_9_widget_clicked_grid = QGridLayout()

        self.task_9_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_9_file_path = 'data/tasks_data/9/' + task_9_data['id'] + '.xlsx'
        
        task_9_widget_clicked_grid.addWidget(self.task_9_text, 1, 0, 9, 0)
        task_9_widget_clicked_grid.addWidget(self.task_9_get_file_btn, 10, 0, 12, 0)
        task_9_widget_clicked_grid.addWidget(self.task_9_show_ans_btn, 29, 0, 33, 0)
        task_9_widget_clicked_grid.addWidget(self.task_9_show_descr_btn, 70, 0, 74, 0)
        self.task_9_widget.setLayout(task_9_widget_clicked_grid)

        def task_9_ans_button_clicked():
            self.task_9_show_ans_btn.setParent(None)
            task_9_widget_clicked_grid.addWidget(self.task_9_answer, 29, 0, 33, 0)
        def task_9_descr_button_clicked():
            self.task_9_show_descr_btn.setParent(None)
            task_9_widget_clicked_grid.addWidget(self.task_9_description_widget, 70, 0, 74, 0)
        def task_9_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_9_file_path, destination_path)
            except FileNotFoundError:
                pass

        self.task_9_show_ans_btn.clicked.connect(task_9_ans_button_clicked)
        self.task_9_show_descr_btn.clicked.connect(task_9_descr_button_clicked)
        self.task_9_get_file_btn.clicked.connect(task_9_get_file_button_clicked)


        # 10101010101010101010
        self.task_10_widget = QWidget()
        task_10_data = Task_Chooser.choose_task_10()
        self.task_10_text = QLabel(task_10_data['text'])
        self.task_10_text.setWordWrap(True)
        self.task_10_text.setAlignment(Qt.AlignCenter)
        self.task_10_answer = QLabel('Ответ: ' + task_10_data['answer'])
        self.task_10_answer.setWordWrap(True)
        self.task_10_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_10_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_10_description = task_10_data['description']
        self.task_10_description_widget = QLabel(self.task_10_description)
        self.task_10_description_widget.setWordWrap(True)
        task_10_widget_clicked_grid = QGridLayout()

        self.task_10_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_10_file_path = 'data/tasks_data/10/' + task_10_data['id'] + '.docx'
        
        task_10_widget_clicked_grid.addWidget(self.task_10_text, 1, 0, 9, 0)
        task_10_widget_clicked_grid.addWidget(self.task_10_get_file_btn, 10, 0, 12, 0)
        task_10_widget_clicked_grid.addWidget(self.task_10_show_ans_btn, 29, 0, 33, 0)
        task_10_widget_clicked_grid.addWidget(self.task_10_show_descr_btn, 60, 0, 64, 0)
        self.task_10_widget.setLayout(task_10_widget_clicked_grid)

        def task_10_ans_button_clicked():
            self.task_10_show_ans_btn.setParent(None)
            task_10_widget_clicked_grid.addWidget(self.task_10_answer, 29, 0, 33, 0)
        def task_10_descr_button_clicked():
            self.task_10_show_descr_btn.setParent(None)
            task_10_widget_clicked_grid.addWidget(self.task_10_description_widget, 60, 0, 64, 0)
        def task_10_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_10_file_path, destination_path)
            except FileNotFoundError:
                pass

        self.task_10_show_ans_btn.clicked.connect(task_10_ans_button_clicked)
        self.task_10_show_descr_btn.clicked.connect(task_10_descr_button_clicked)
        self.task_10_get_file_btn.clicked.connect(task_10_get_file_button_clicked)


        # 11111111111111111111
        self.task_11_widget = QWidget()
        task_11_data = Task_Chooser.choose_task_11()
        self.task_11_text = QLabel(task_11_data['text'])
        self.task_11_text.setWordWrap(True)
        self.task_11_text.setAlignment(Qt.AlignCenter)
        self.task_11_answer = QLabel('Ответ: ' + task_11_data['answer'])
        self.task_11_answer.setWordWrap(True)
        self.task_11_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_11_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_11_description = task_11_data['description']
        self.task_11_description_widget = QLabel(self.task_11_description)
        self.task_11_description_widget.setWordWrap(True)
        task_11_widget_clicked_grid = QGridLayout()
        
        task_11_widget_clicked_grid.addWidget(self.task_11_text, 1, 0, 7, 0)
        task_11_widget_clicked_grid.addWidget(self.task_11_show_ans_btn, 10, 0, 12, 0)
        task_11_widget_clicked_grid.addWidget(self.task_11_show_descr_btn, 27, 0, 33, 0)
        self.task_11_widget.setLayout(task_11_widget_clicked_grid)

        def task_11_ans_button_clicked():
            self.task_11_show_ans_btn.setParent(None)
            task_11_widget_clicked_grid.addWidget(self.task_11_answer, 10, 0, 12, 0)
        def task_11_descr_button_clicked():
            self.task_11_show_descr_btn.setParent(None)
            task_11_widget_clicked_grid.addWidget(self.task_11_description_widget, 27, 0, 33, 0)

        self.task_11_show_ans_btn.clicked.connect(task_11_ans_button_clicked)
        self.task_11_show_descr_btn.clicked.connect(task_11_descr_button_clicked)


        # 12121212121212121212
        self.task_12_widget = QWidget()
        task_12_data = Task_Chooser.choose_task_12()
        self.task_12_text = QLabel(task_12_data['text'])
        self.task_12_text.setWordWrap(True)
        self.task_12_answer = QLabel('Ответ: ' + task_12_data['answer'])
        self.task_12_answer.setWordWrap(True)
        self.task_12_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_12_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_12_description = task_12_data['description']
        if task_12_data['python'].strip() != 'нет':
            self.task_12_description = self.task_12_description + '\n\n' + task_12_data['python']
        self.task_12_description_widget = QLabel(self.task_12_description)
        self.task_12_description_widget.setWordWrap(True)
        task_12_widget_clicked_grid = QGridLayout()

        if task_12_data['hasPictures'] == True:
            self.task_12_picture_path = 'data/tasks_data/12/' + task_12_data['id'] + '.png'
            self.task_12_picture_exists = True if os.path.exists(self.task_12_picture_path) else False
            if self.task_12_picture_exists:
                self.task_12_picture = QPixmap(self.task_12_picture_path)
                self.task_12_picture_lbl = QLabel(self)
                self.task_12_picture_lbl.setPixmap(self.task_12_picture)

            self.task_12_ans_picture_path = 'data/tasks_data/12/' + task_12_data['id'] + '_ans.png'
            self.task_12_ans_picture_exists = True if os.path.exists(self.task_12_ans_picture_path) else False
            if self.task_12_ans_picture_exists:
                self.task_12_ans_picture = QPixmap(self.task_12_ans_picture_path)
                self.task_12_ans_picture_lbl = QLabel(self)
                self.task_12_ans_picture_lbl.setPixmap(self.task_12_ans_picture)

        def task_12_ans_button_clicked():
            self.task_12_show_ans_btn.setParent(None)
            task_12_widget_clicked_grid.addWidget(self.task_12_answer, 18, 0, 20, 0)
        def task_12_descr_button_clicked_has_pictures_false():
            self.task_12_show_descr_btn.setParent(None)
            task_12_widget_clicked_grid.addWidget(self.task_12_description_widget, 40, 0, 46, 0)
        def task_12_descr_button_clicked_has_pictures_true():
            self.task_12_show_descr_btn.setParent(None)
            task_12_widget_clicked_grid.addWidget(self.task_12_ans_picture_lbl, 25, 0, 46, 1)
            task_12_widget_clicked_grid.addWidget(self.task_12_description_widget, 25, 2, 46, 9)

        if task_12_data['hasPictures'] == False:
            task_12_widget_clicked_grid.addWidget(self.task_12_text, 1, 0, 15, 0)
            task_12_widget_clicked_grid.addWidget(self.task_12_show_ans_btn, 18, 0, 20, 0)
            task_12_widget_clicked_grid.addWidget(self.task_12_show_descr_btn, 40, 0, 46, 0)
            self.task_12_widget.setLayout(task_12_widget_clicked_grid)
            self.task_12_show_ans_btn.clicked.connect(task_12_ans_button_clicked)
            self.task_12_show_descr_btn.clicked.connect(task_12_descr_button_clicked_has_pictures_false)
        elif task_12_data['hasPictures'] == True:
            task_12_widget_clicked_grid.addWidget(self.task_12_picture_lbl, 1, 0, 15, 1)
            task_12_widget_clicked_grid.addWidget(self.task_12_text, 1, 2, 15, 9)
            task_12_widget_clicked_grid.addWidget(self.task_12_show_ans_btn, 18, 0, 20, 0)
            task_12_widget_clicked_grid.addWidget(self.task_12_show_descr_btn, 40, 0, 46, 0)
            self.task_12_widget.setLayout(task_12_widget_clicked_grid)
            self.task_12_show_ans_btn.clicked.connect(task_12_ans_button_clicked)
            self.task_12_show_descr_btn.clicked.connect(task_12_descr_button_clicked_has_pictures_true)


        # 13131313131313131313
        self.task_13_widget = QWidget()
        task_13_data = Task_Chooser.choose_task_13()
        self.task_13_text = QLabel(task_13_data['text'])
        self.task_13_text.setWordWrap(True)
        self.task_13_text.setAlignment(Qt.AlignCenter)
        self.task_13_answer = QLabel('Ответ: ' + task_13_data['answer'])
        self.task_13_answer.setWordWrap(True)
        self.task_13_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_13_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_13_description = task_13_data['description']
        self.task_13_description_widget = QLabel(self.task_13_description)
        self.task_13_description_widget.setWordWrap(True)
        task_13_widget_clicked_grid = QGridLayout()

        self.task_13_text_widgth = self.task_13_text.frameGeometry().width()
        self.task_13_text_height = self.task_13_text.frameGeometry().height()

        self.task_13_picture_path = 'data/tasks_data/13/' + task_13_data['id'] + '.png'
        self.task_13_picture_exists = True if os.path.exists(self.task_13_picture_path) else False
        if self.task_13_picture_exists:
            self.task_13_picture = QPixmap(self.task_13_picture_path)
            self.task_13_picture = self.task_13_picture.scaled(self.task_13_text_widgth, self.task_13_text_height, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.task_13_picture_lbl = QLabel(self)
            self.task_13_picture_lbl.setPixmap(self.task_13_picture)
        
        task_13_widget_clicked_grid.addWidget(self.task_13_text, 1, 0, 7, 0)
        if self.task_13_picture_exists:
            task_13_widget_clicked_grid.addWidget(self.task_13_picture_lbl, 10, 0, 12, 0, alignment=Qt.AlignCenter)
        task_13_widget_clicked_grid.addWidget(self.task_13_show_ans_btn, 25, 0, 27, 0)
        task_13_widget_clicked_grid.addWidget(self.task_13_show_descr_btn, 55, 0, 63, 0)
        self.task_13_widget.setLayout(task_13_widget_clicked_grid)

        def task_13_ans_button_clicked():
            self.task_13_show_ans_btn.setParent(None)
            task_13_widget_clicked_grid.addWidget(self.task_13_answer, 25, 0, 27, 0)
        def task_13_descr_button_clicked():
            self.task_13_show_descr_btn.setParent(None)
            task_13_widget_clicked_grid.addWidget(self.task_13_description_widget, 55, 0, 63, 0)

        self.task_13_show_ans_btn.clicked.connect(task_13_ans_button_clicked)
        self.task_13_show_descr_btn.clicked.connect(task_13_descr_button_clicked)


        # 1414141414141414141414141414
        self.task_14_widget = QWidget()
        task_14_data = Task_Chooser.choose_task_14()
        self.task_14_text = QLabel(task_14_data['text'])
        self.task_14_text.setWordWrap(True)
        self.task_14_text.setAlignment(Qt.AlignCenter)
        self.task_14_answer = QLabel('Ответ: ' + task_14_data['answer'])
        self.task_14_answer.setWordWrap(True)
        self.task_14_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_14_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_14_description = task_14_data['description']
        if task_14_data['python'].strip() != 'нет':
            self.task_14_description = self.task_14_description + '\n\n' + task_14_data['python']
        self.task_14_description_widget = QLabel(self.task_14_description)
        self.task_14_description_widget.setWordWrap(True)
        task_14_widget_clicked_grid = QGridLayout()
        
        task_14_widget_clicked_grid.addWidget(self.task_14_text, 1, 0, 7, 0)
        task_14_widget_clicked_grid.addWidget(self.task_14_show_ans_btn, 10, 0, 12, 0)
        task_14_widget_clicked_grid.addWidget(self.task_14_show_descr_btn, 25, 0, 33, 0)
        self.task_14_widget.setLayout(task_14_widget_clicked_grid)

        def task_14_ans_button_clicked():
            self.task_14_show_ans_btn.setParent(None)
            task_14_widget_clicked_grid.addWidget(self.task_14_answer, 10, 0, 12, 0)
        def task_14_descr_button_clicked():
            self.task_14_show_descr_btn.setParent(None)
            task_14_widget_clicked_grid.addWidget(self.task_14_description_widget, 25, 0, 33, 0)

        self.task_14_show_ans_btn.clicked.connect(task_14_ans_button_clicked)
        self.task_14_show_descr_btn.clicked.connect(task_14_descr_button_clicked)


        # 1515151515151515151515151515
        self.task_15_widget = QWidget()
        task_15_data = Task_Chooser.choose_task_15()
        self.task_15_text = QLabel(task_15_data['text'])
        self.task_15_text.setWordWrap(True)
        self.task_15_text.setAlignment(Qt.AlignCenter)
        self.task_15_answer = QLabel('Ответ: ' + task_15_data['answer'])
        self.task_15_answer.setWordWrap(True)
        self.task_15_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_15_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_15_description = task_15_data['description']
        if task_15_data['python'].strip() != 'нет':
            self.task_15_description = self.task_15_description + '\n\n' + task_15_data['python']
        self.task_15_description_widget = QLabel(self.task_15_description)
        self.task_15_description_widget.setWordWrap(True)
        task_15_widget_clicked_grid = QGridLayout()
        
        task_15_widget_clicked_grid.addWidget(self.task_15_text, 1, 0, 7, 0)
        task_15_widget_clicked_grid.addWidget(self.task_15_show_ans_btn, 10, 0, 12, 0)
        task_15_widget_clicked_grid.addWidget(self.task_15_show_descr_btn, 25, 0, 33, 0)
        self.task_15_widget.setLayout(task_15_widget_clicked_grid)

        def task_15_ans_button_clicked():
            self.task_15_show_ans_btn.setParent(None)
            task_15_widget_clicked_grid.addWidget(self.task_15_answer, 10, 0, 12, 0)
        def task_15_descr_button_clicked():
            self.task_15_show_descr_btn.setParent(None)
            task_15_widget_clicked_grid.addWidget(self.task_15_description_widget, 25, 0, 33, 0)

        self.task_15_show_ans_btn.clicked.connect(task_15_ans_button_clicked)
        self.task_15_show_descr_btn.clicked.connect(task_15_descr_button_clicked)


        # 1616161616161616
        self.task_16_widget = QWidget()
        task_16_data = Task_Chooser.choose_task_16()
        self.task_16_text_for_lbl = task_16_data['text']
        if task_16_data['program'].strip() != 'нет':
            self.task_16_text_for_lbl = self.task_16_text_for_lbl + '\n\n' + task_16_data['program']
        self.task_16_text = QLabel(self.task_16_text_for_lbl)
        self.task_16_text.setWordWrap(True)
        self.task_16_answer = QLabel('Ответ: ' + task_16_data['answer'])
        self.task_16_answer.setWordWrap(True)
        self.task_16_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_16_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_16_description = task_16_data['description']
        self.task_16_description_widget = QLabel(self.task_16_description)
        self.task_16_description_widget.setWordWrap(True)
        task_16_widget_clicked_grid = QGridLayout()
        
        task_16_widget_clicked_grid.addWidget(self.task_16_text, 1, 0, 7, 0, alignment=Qt.AlignCenter)
        task_16_widget_clicked_grid.addWidget(self.task_16_show_ans_btn, 10, 0, 12, 0)
        task_16_widget_clicked_grid.addWidget(self.task_16_show_descr_btn, 25, 0, 33, 0)
        self.task_16_widget.setLayout(task_16_widget_clicked_grid)

        def task_16_ans_button_clicked():
            self.task_16_show_ans_btn.setParent(None)
            task_16_widget_clicked_grid.addWidget(self.task_16_answer, 10, 0, 12, 0)
        def task_16_descr_button_clicked():
            self.task_16_show_descr_btn.setParent(None)
            task_16_widget_clicked_grid.addWidget(self.task_16_description_widget, 25, 0, 33, 0)

        self.task_16_show_ans_btn.clicked.connect(task_16_ans_button_clicked)
        self.task_16_show_descr_btn.clicked.connect(task_16_descr_button_clicked)


        # 1717171717171717171717171717
        self.task_17_widget = QWidget()
        task_17_data = Task_Chooser.choose_task_17()
        self.task_17_text = QLabel(task_17_data['text'])
        self.task_17_text.setWordWrap(True)
        self.task_17_text.setAlignment(Qt.AlignCenter)
        self.task_17_answer = QLabel('Ответ: ' + task_17_data['answer'])
        self.task_17_answer.setWordWrap(True)
        self.task_17_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_17_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_17_description = task_17_data['description']
        if task_17_data['python'].strip() != 'нет':
            self.task_17_description = self.task_17_description + '\n\n' + task_17_data['python']
        self.task_17_description_widget = QLabel(self.task_17_description)
        self.task_17_description_widget.setWordWrap(True)
        task_17_widget_clicked_grid = QGridLayout()

        self.task_17_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_17_file_path = 'data/tasks_data/17/' + task_17_data['fileName']
        
        task_17_widget_clicked_grid.addWidget(self.task_17_text, 1, 0, 7, 0)
        task_17_widget_clicked_grid.addWidget(self.task_17_get_file_btn, 5, 0, 9, 0)
        task_17_widget_clicked_grid.addWidget(self.task_17_show_ans_btn, 10, 0, 12, 0)
        task_17_widget_clicked_grid.addWidget(self.task_17_show_descr_btn, 25, 0, 33, 0)
        self.task_17_widget.setLayout(task_17_widget_clicked_grid)

        def task_17_ans_button_clicked():
            self.task_17_show_ans_btn.setParent(None)
            task_17_widget_clicked_grid.addWidget(self.task_17_answer, 10, 0, 12, 0)
        def task_17_descr_button_clicked():
            self.task_17_show_descr_btn.setParent(None)
            task_17_widget_clicked_grid.addWidget(self.task_17_description_widget, 25, 0, 33, 0)

        self.task_17_show_ans_btn.clicked.connect(task_17_ans_button_clicked)
        self.task_17_show_descr_btn.clicked.connect(task_17_descr_button_clicked)

        def task_17_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_17_file_path, destination_path)
            except FileNotFoundError:
                pass
        self.task_17_get_file_btn.clicked.connect(task_17_get_file_button_clicked)


        # 1818181818181818181818181818
        self.task_18_widget = QWidget()
        task_18_data = Task_Chooser.choose_task_18()
        self.task_18_text = QLabel(task_18_data['text'])
        self.task_18_text.setWordWrap(True)
        self.task_18_text.setAlignment(Qt.AlignCenter)
        self.task_18_answer = QLabel('Ответ: ' + task_18_data['answer'])
        self.task_18_answer.setWordWrap(True)
        self.task_18_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_18_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_18_description = task_18_data['description']
        self.task_18_description_widget = QLabel(self.task_18_description)
        self.task_18_description_widget.setWordWrap(True)
        task_18_widget_clicked_grid = QGridLayout()

        self.task_18_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_18_file_path = 'data/tasks_data/18/' + task_18_data['id'] + '.xlsx'

        self.task_18_picture_path = 'data/tasks_data/18/example.png'
        self.task_18_picture = QPixmap(self.task_18_picture_path)
        self.task_18_picture_lbl = QLabel(self)
        self.task_18_picture_lbl.setPixmap(self.task_18_picture)
        
        task_18_widget_clicked_grid.addWidget(self.task_18_text, 1, 0, 5, 0)
        task_18_widget_clicked_grid.addWidget(self.task_18_picture_lbl, 5, 0, 9, 0, alignment=Qt.AlignCenter)
        task_18_widget_clicked_grid.addWidget(self.task_18_get_file_btn, 15, 0, 17, 0)
        task_18_widget_clicked_grid.addWidget(self.task_18_show_ans_btn, 40, 0, 42, 0)
        task_18_widget_clicked_grid.addWidget(self.task_18_show_descr_btn, 95, 0, 97, 0)
        self.task_18_widget.setLayout(task_18_widget_clicked_grid)

        def task_18_ans_button_clicked():
            self.task_18_show_ans_btn.setParent(None)
            task_18_widget_clicked_grid.addWidget(self.task_18_answer, 40, 0, 42, 0)
        def task_18_descr_button_clicked():
            self.task_18_show_descr_btn.setParent(None)
            task_18_widget_clicked_grid.addWidget(self.task_18_description_widget, 95, 0, 103, 0)

        self.task_18_show_ans_btn.clicked.connect(task_18_ans_button_clicked)
        self.task_18_show_descr_btn.clicked.connect(task_18_descr_button_clicked)

        def task_18_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_18_file_path, destination_path)
            except FileNotFoundError:
                pass
        self.task_18_get_file_btn.clicked.connect(task_18_get_file_button_clicked)


        # 19191919191919191919
        self.task_19_widget = QWidget()
        task_19_data = Task_Chooser.choose_task_19()
        self.task_19_text = QLabel(task_19_data['text'])
        self.task_19_text.setWordWrap(True)
        self.task_19_text.setAlignment(Qt.AlignCenter)
        self.task_19_answer = QLabel('Ответ: ' + task_19_data['answer'])
        self.task_19_answer.setWordWrap(True)
        self.task_19_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_19_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_19_description = task_19_data['description']
        self.task_19_description_widget = QLabel(self.task_19_description)
        self.task_19_description_widget.setWordWrap(True)
        task_19_widget_clicked_grid = QGridLayout()
        
        task_19_widget_clicked_grid.addWidget(self.task_19_text, 1, 0, 7, 0)
        task_19_widget_clicked_grid.addWidget(self.task_19_show_ans_btn, 10, 0, 12, 0)
        task_19_widget_clicked_grid.addWidget(self.task_19_show_descr_btn, 27, 0, 33, 0)
        self.task_19_widget.setLayout(task_19_widget_clicked_grid)

        def task_19_ans_button_clicked():
            self.task_19_show_ans_btn.setParent(None)
            task_19_widget_clicked_grid.addWidget(self.task_19_answer, 10, 0, 12, 0)
        def task_19_descr_button_clicked():
            self.task_19_show_descr_btn.setParent(None)
            task_19_widget_clicked_grid.addWidget(self.task_19_description_widget, 27, 0, 33, 0)

        self.task_19_show_ans_btn.clicked.connect(task_19_ans_button_clicked)
        self.task_19_show_descr_btn.clicked.connect(task_19_descr_button_clicked)


        # 20202020202020202020
        self.task_20_widget = QWidget()
        task_20_data = Task_Chooser.choose_task_20()
        self.task_20_text = QLabel(task_20_data['text'])
        self.task_20_text.setWordWrap(True)
        self.task_20_text.setAlignment(Qt.AlignCenter)
        self.task_20_answer = QLabel('Ответ: ' + task_20_data['answer'])
        self.task_20_answer.setWordWrap(True)
        self.task_20_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_20_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_20_description = task_20_data['description']
        self.task_20_description_widget = QLabel(self.task_20_description)
        self.task_20_description_widget.setWordWrap(True)
        task_20_widget_clicked_grid = QGridLayout()
        
        task_20_widget_clicked_grid.addWidget(self.task_20_text, 1, 0, 7, 0)
        task_20_widget_clicked_grid.addWidget(self.task_20_show_ans_btn, 10, 0, 12, 0)
        task_20_widget_clicked_grid.addWidget(self.task_20_show_descr_btn, 27, 0, 33, 0)
        self.task_20_widget.setLayout(task_20_widget_clicked_grid)

        def task_20_ans_button_clicked():
            self.task_20_show_ans_btn.setParent(None)
            task_20_widget_clicked_grid.addWidget(self.task_20_answer, 10, 0, 12, 0)
        def task_20_descr_button_clicked():
            self.task_20_show_descr_btn.setParent(None)
            task_20_widget_clicked_grid.addWidget(self.task_20_description_widget, 27, 0, 33, 0)

        self.task_20_show_ans_btn.clicked.connect(task_20_ans_button_clicked)
        self.task_20_show_descr_btn.clicked.connect(task_20_descr_button_clicked)


        # 21212121212121212121
        self.task_21_widget = QWidget()
        task_21_data = Task_Chooser.choose_task_21()
        self.task_21_text = QLabel(task_21_data['text'])
        self.task_21_text.setWordWrap(True)
        self.task_21_text.setAlignment(Qt.AlignCenter)
        self.task_21_answer = QLabel('Ответ: ' + task_21_data['answer'])
        self.task_21_answer.setWordWrap(True)
        self.task_21_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_21_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_21_description = task_21_data['description']
        self.task_21_description_widget = QLabel(self.task_21_description)
        self.task_21_description_widget.setWordWrap(True)
        task_21_widget_clicked_grid = QGridLayout()
        
        task_21_widget_clicked_grid.addWidget(self.task_21_text, 1, 0, 7, 0)
        task_21_widget_clicked_grid.addWidget(self.task_21_show_ans_btn, 10, 0, 12, 0)
        task_21_widget_clicked_grid.addWidget(self.task_21_show_descr_btn, 27, 0, 33, 0)
        self.task_21_widget.setLayout(task_21_widget_clicked_grid)

        def task_21_ans_button_clicked():
            self.task_21_show_ans_btn.setParent(None)
            task_21_widget_clicked_grid.addWidget(self.task_21_answer, 10, 0, 12, 0)
        def task_21_descr_button_clicked():
            self.task_21_show_descr_btn.setParent(None)
            task_21_widget_clicked_grid.addWidget(self.task_21_description_widget, 27, 0, 33, 0)

        self.task_21_show_ans_btn.clicked.connect(task_21_ans_button_clicked)
        self.task_21_show_descr_btn.clicked.connect(task_21_descr_button_clicked)


        # 2222222222222222
        self.task_22_widget = QWidget()
        task_22_data = Task_Chooser.choose_task_22()
        self.task_22_text = QLabel(task_22_data['text'] + '\n\n' + task_22_data['program'])
        self.task_22_text.setWordWrap(True)
        self.task_22_answer = QLabel('Ответ: ' + task_22_data['answer'])
        self.task_22_answer.setWordWrap(True)
        self.task_22_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_22_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_22_description = task_22_data['description']
        if task_22_data['python'].strip() != 'нет':
            self.task_22_description = self.task_22_description + '\n\n' + task_22_data['python']
        self.task_22_description_widget = QLabel(self.task_22_description)
        self.task_22_description_widget.setWordWrap(True)
        task_22_widget_clicked_grid = QGridLayout()
        
        task_22_widget_clicked_grid.addWidget(self.task_22_text, 1, 0, 7, 0, alignment=Qt.AlignCenter)
        task_22_widget_clicked_grid.addWidget(self.task_22_show_ans_btn, 10, 0, 12, 0)
        task_22_widget_clicked_grid.addWidget(self.task_22_show_descr_btn, 25, 0, 33, 0)
        self.task_22_widget.setLayout(task_22_widget_clicked_grid)

        def task_22_ans_button_clicked():
            self.task_22_show_ans_btn.setParent(None)
            task_22_widget_clicked_grid.addWidget(self.task_22_answer, 10, 0, 12, 0)
        def task_22_descr_button_clicked():
            self.task_22_show_descr_btn.setParent(None)
            task_22_widget_clicked_grid.addWidget(self.task_22_description_widget, 25, 0, 33, 0)

        self.task_22_show_ans_btn.clicked.connect(task_22_ans_button_clicked)
        self.task_22_show_descr_btn.clicked.connect(task_22_descr_button_clicked)


        # 23232323232323232323
        self.task_23_widget = QWidget()
        task_23_data = Task_Chooser.choose_task_23()
        self.task_23_text = QLabel(task_23_data['text'])
        self.task_23_text.setWordWrap(True)
        self.task_23_text.setAlignment(Qt.AlignCenter)
        self.task_23_answer = QLabel('Ответ: ' + task_23_data['answer'])
        self.task_23_answer.setWordWrap(True)
        self.task_23_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_23_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_23_description = task_23_data['description']
        self.task_23_description_widget = QLabel(self.task_23_description)
        self.task_23_description_widget.setWordWrap(True)
        task_23_widget_clicked_grid = QGridLayout()
        
        task_23_widget_clicked_grid.addWidget(self.task_23_text, 1, 0, 7, 0)
        task_23_widget_clicked_grid.addWidget(self.task_23_show_ans_btn, 10, 0, 12, 0)
        task_23_widget_clicked_grid.addWidget(self.task_23_show_descr_btn, 27, 0, 33, 0)
        self.task_23_widget.setLayout(task_23_widget_clicked_grid)

        def task_23_ans_button_clicked():
            self.task_23_show_ans_btn.setParent(None)
            task_23_widget_clicked_grid.addWidget(self.task_23_answer, 10, 0, 12, 0)
        def task_23_descr_button_clicked():
            self.task_23_show_descr_btn.setParent(None)
            task_23_widget_clicked_grid.addWidget(self.task_23_description_widget, 27, 0, 33, 0)

        self.task_23_show_ans_btn.clicked.connect(task_23_ans_button_clicked)
        self.task_23_show_descr_btn.clicked.connect(task_23_descr_button_clicked)


        # 2424242424242424242424242424
        self.task_24_widget = QWidget()
        task_24_data = Task_Chooser.choose_task_24()
        self.task_24_text = QLabel(task_24_data['text'])
        self.task_24_text.setWordWrap(True)
        self.task_24_text.setAlignment(Qt.AlignCenter)
        self.task_24_answer = QLabel('Ответ: ' + task_24_data['answer'])
        self.task_24_answer.setWordWrap(True)
        self.task_24_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_24_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_24_description = task_24_data['description']
        if task_24_data['python'].strip() != 'нет':
            self.task_24_description = self.task_24_description + '\n\n' + task_24_data['python']
        self.task_24_description_widget = QLabel(self.task_24_description)
        self.task_24_description_widget.setWordWrap(True)
        task_24_widget_clicked_grid = QGridLayout()

        self.task_24_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_24_file_path = 'data/tasks_data/24/' + task_24_data['id'] + '.txt'
        
        task_24_widget_clicked_grid.addWidget(self.task_24_text, 1, 0, 7, 0)
        task_24_widget_clicked_grid.addWidget(self.task_24_get_file_btn, 10, 0, 12, 0)
        task_24_widget_clicked_grid.addWidget(self.task_24_show_ans_btn, 25, 0, 27, 0)
        task_24_widget_clicked_grid.addWidget(self.task_24_show_descr_btn, 60, 0, 68, 0)
        self.task_24_widget.setLayout(task_24_widget_clicked_grid)

        def task_24_ans_button_clicked():
            self.task_24_show_ans_btn.setParent(None)
            task_24_widget_clicked_grid.addWidget(self.task_24_answer, 25, 0, 27, 0)
        def task_24_descr_button_clicked():
            self.task_24_show_descr_btn.setParent(None)
            task_24_widget_clicked_grid.addWidget(self.task_24_description_widget, 60, 0, 68, 0)

        self.task_24_show_ans_btn.clicked.connect(task_24_ans_button_clicked)
        self.task_24_show_descr_btn.clicked.connect(task_24_descr_button_clicked)

        def task_24_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_24_file_path, destination_path)
            except FileNotFoundError:
                pass
        self.task_24_get_file_btn.clicked.connect(task_24_get_file_button_clicked)


        # 2525252525252525252525252525
        self.task_25_widget = QWidget()
        task_25_data = Task_Chooser.choose_task_25()
        self.task_25_text = QLabel(task_25_data['text'])
        self.task_25_text.setWordWrap(True)
        self.task_25_text.setAlignment(Qt.AlignCenter)
        self.task_25_answer = QLabel('Ответ:\n' + task_25_data['answer'])
        self.task_25_answer.setWordWrap(True)
        self.task_25_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_25_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_25_description = task_25_data['description']
        if task_25_data['python'].strip() != 'нет':
            self.task_25_description = self.task_25_description + '\n\n' + task_25_data['python']
        self.task_25_description_widget = QLabel(self.task_25_description)
        self.task_25_description_widget.setWordWrap(True)
        task_25_widget_clicked_grid = QGridLayout()
        
        task_25_widget_clicked_grid.addWidget(self.task_25_text, 1, 0, 7, 0)
        task_25_widget_clicked_grid.addWidget(self.task_25_show_ans_btn, 10, 0, 12, 0)
        task_25_widget_clicked_grid.addWidget(self.task_25_show_descr_btn, 25, 0, 33, 0)
        self.task_25_widget.setLayout(task_25_widget_clicked_grid)

        def task_25_ans_button_clicked():
            self.task_25_show_ans_btn.setParent(None)
            task_25_widget_clicked_grid.addWidget(self.task_25_answer, 10, 0, 12, 0)
        def task_25_descr_button_clicked():
            self.task_25_show_descr_btn.setParent(None)
            task_25_widget_clicked_grid.addWidget(self.task_25_description_widget, 25, 0, 33, 0)

        self.task_25_show_ans_btn.clicked.connect(task_25_ans_button_clicked)
        self.task_25_show_descr_btn.clicked.connect(task_25_descr_button_clicked)


        # 2626262626262626262626262626
        self.task_26_widget = QWidget()
        task_26_data = Task_Chooser.choose_task_26()
        self.task_26_text = QLabel(task_26_data['text'])
        self.task_26_text.setWordWrap(True)
        self.task_26_text.setAlignment(Qt.AlignCenter)
        self.task_26_answer = QLabel('Ответ: ' + task_26_data['answer'])
        self.task_26_answer.setWordWrap(True)
        self.task_26_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_26_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_26_description = task_26_data['description']
        if task_26_data['python'].strip() != 'нет':
            self.task_26_description = self.task_26_description + '\n\n' + task_26_data['python']
        self.task_26_description_widget = QLabel(self.task_26_description)
        self.task_26_description_widget.setWordWrap(True)
        task_26_widget_clicked_grid = QGridLayout()

        self.task_26_get_file_btn = QPushButton(Localization.GET_FILE, self)
        self.task_26_file_path = 'data/tasks_data/26/' + task_26_data['id'] + '.txt'
        
        task_26_widget_clicked_grid.addWidget(self.task_26_text, 1, 0, 7, 0)
        task_26_widget_clicked_grid.addWidget(self.task_26_get_file_btn, 10, 0, 12, 0)
        task_26_widget_clicked_grid.addWidget(self.task_26_show_ans_btn, 25, 0, 27, 0)
        task_26_widget_clicked_grid.addWidget(self.task_26_show_descr_btn, 60, 0, 68, 0)
        self.task_26_widget.setLayout(task_26_widget_clicked_grid)

        def task_26_ans_button_clicked():
            self.task_26_show_ans_btn.setParent(None)
            task_26_widget_clicked_grid.addWidget(self.task_26_answer, 25, 0, 27, 0)
        def task_26_descr_button_clicked():
            self.task_26_show_descr_btn.setParent(None)
            task_26_widget_clicked_grid.addWidget(self.task_26_description_widget, 60, 0, 68, 0)

        self.task_26_show_ans_btn.clicked.connect(task_26_ans_button_clicked)
        self.task_26_show_descr_btn.clicked.connect(task_26_descr_button_clicked)

        def task_26_get_file_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_26_file_path, destination_path)
            except FileNotFoundError:
                pass
        self.task_26_get_file_btn.clicked.connect(task_26_get_file_button_clicked)


        # 2727272727272727272727272727
        self.task_27_widget = QWidget()
        task_27_data = Task_Chooser.choose_task_27()
        self.task_27_text = QLabel(task_27_data['text'])
        self.task_27_text.setWordWrap(True)
        self.task_27_text.setAlignment(Qt.AlignCenter)
        self.task_27_answer = QLabel('Ответ: ' + task_27_data['answer'])
        self.task_27_answer.setWordWrap(True)
        self.task_27_show_ans_btn = QPushButton(Localization.SHOW_ANSWER, self)
        self.task_27_show_descr_btn = QPushButton(Localization.SHOW_DESCRIPTION, self)
        self.task_27_description = task_27_data['description']
        if task_27_data['python'].strip() != 'нет':
            self.task_27_description = self.task_27_description + '\n\n' + task_27_data['python']
        self.task_27_description_widget = QLabel(self.task_27_description)
        self.task_27_description_widget.setWordWrap(True)
        task_27_widget_clicked_grid = QGridLayout()

        self.task_27_get_file_a_btn = QPushButton(Localization.GET_FILE_A, self)
        self.task_27_get_file_b_btn = QPushButton(Localization.GET_FILE_B, self)
        self.task_27_file_a_path = 'data/tasks_data/27/' + task_27_data['id'] + '_A.txt'
        self.task_27_file_b_path = 'data/tasks_data/27/' + task_27_data['id'] + '_B.txt'
        
        task_27_widget_clicked_grid.addWidget(self.task_27_text, 1, 0, 7, 0)
        task_27_widget_clicked_grid.addWidget(self.task_27_get_file_a_btn, 10, 0, 12, 1)
        task_27_widget_clicked_grid.addWidget(self.task_27_get_file_b_btn, 10, 1, 12, 1)
        task_27_widget_clicked_grid.addWidget(self.task_27_show_ans_btn, 25, 0, 27, 0)
        task_27_widget_clicked_grid.addWidget(self.task_27_show_descr_btn, 60, 0, 68, 0)
        self.task_27_widget.setLayout(task_27_widget_clicked_grid)

        def task_27_ans_button_clicked():
            self.task_27_show_ans_btn.setParent(None)
            task_27_widget_clicked_grid.addWidget(self.task_27_answer, 25, 0, 27, 0)
        def task_27_descr_button_clicked():
            self.task_27_show_descr_btn.setParent(None)
            task_27_widget_clicked_grid.addWidget(self.task_27_description_widget, 60, 0, 68, 0)

        self.task_27_show_ans_btn.clicked.connect(task_27_ans_button_clicked)
        self.task_27_show_descr_btn.clicked.connect(task_27_descr_button_clicked)

        def task_27_get_file_a_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_27_file_a_path, destination_path)
            except FileNotFoundError:
                pass
        self.task_27_get_file_a_btn.clicked.connect(task_27_get_file_a_button_clicked)

        def task_27_get_file_b_button_clicked():
            destination_path = QFileDialog.getExistingDirectory(self,Localization.FILE_DIALOG_SAVE,'.')
            try:
                shutil.copy(self.task_27_file_b_path, destination_path)
            except FileNotFoundError:
                pass
        self.task_27_get_file_b_btn.clicked.connect(task_27_get_file_b_button_clicked)


        # aft
        grid_clicked = QGridLayout()
        grid_clicked.addWidget(self.lbl2, 1, 0, alignment=Qt.AlignCenter)
        self.task_widgets = {
            '1': self.task_1_widget,
            '2': self.task_2_widget,
            '3': self.task_3_widget,
            '4': self.task_4_widget,
            '5': self.task_5_widget,
            '6': self.task_6_widget,
            '7': self.task_7_widget,
            '8': self.task_8_widget,
            '9': self.task_9_widget,
            '10': self.task_10_widget,
            '11': self.task_11_widget,
            '12': self.task_12_widget,
            '13': self.task_13_widget,
            '14': self.task_14_widget,
            '15': self.task_15_widget,
            '16': self.task_16_widget,
            '17': self.task_17_widget,
            '18': self.task_18_widget,
            '19': self.task_19_widget,
            '20': self.task_20_widget,
            '21': self.task_21_widget,
            '22': self.task_22_widget,
            '23': self.task_23_widget,
            '24': self.task_24_widget,
            '25': self.task_25_widget,
            '26': self.task_26_widget,
            '27': self.task_27_widget
        }
        try:
            grid_clicked.addWidget(self.task_widgets[task_num], 2, 0, 4, 0)
        except KeyError:
            pass
        grid_clicked.addWidget(self.back_btn, 6, 0, 8, 0)

        self.scrollArea = QScrollArea()
        self.setCentralWidget(self.scrollArea)
        self.scrollArea.setWidgetResizable(True)
        self.contents = QWidget()
        self.scrollArea.setWidget(self.contents)
        self.contents.setLayout(grid_clicked)

    def setupUi(self, BaseWindow):
        BaseWindow.resize(1000, 600)
        BaseWindow.move(100, 100)
        self.setupUi_continue()


class UI_MainWindow(object):
    "Главное окно программы."

    def setupUi(self, MainWindow):
        self.setWindowTitle(Localization.MAIN_WIN_TITLE) # заголовок окна
        self.setWindowIcon(QIcon('icons/icon.png'))
        self.setMinimumWidth(300)
        self.setMinimumHeight(300)
        MainWindow.resize(1000, 600)

        widget = QWidget()
        grid = QGridLayout()

        self.lbl = QLabel(Localization.MAIN_HEADER, self)
        self.lbl.setFont(QFont('Arial', 20))
        

        self.btn_1 = QPushButton(Localization.BASE_BUTTON, self)
        self.btn_2 = QPushButton(Localization.VAR_BUTTON, self)
        self.btn_3 = QPushButton(Localization.EXIT_BUTTON, self)
        self.btn_3.clicked.connect(QApplication.instance().quit)

        exitAction = QAction(QIcon('icons/exit.png'), '&' + Localization.EXIT, self)
        exitAction.setShortcut(Localization.EXIT_SHORTCUT)
        exitAction.setStatusTip(Localization.EXIT_STATUS_TIP)
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&' + Localization.FILE)
        fileMenu.addAction(exitAction)

        grid.setSpacing(10)
        grid.addWidget(self.lbl, 1, 0, alignment=Qt.AlignCenter)
        grid.addWidget(self.btn_1, 2, 0, 4, 0)
        grid.addWidget(self.btn_2, 3, 0, 5, 0)
        grid.addWidget(self.btn_3, 4, 0, 6, 0)

        widget.setLayout(grid)
        self.setCentralWidget(widget)

class BaseWindow(QMainWindow, UI_BaseWindow):
    def __init__(self, parent=None):
        super(BaseWindow, self).__init__(parent)
        
        self.setupUi(self)
        self.setWindowTitle(Localization.BASE_WIN_TITLE)

class VarWindow(QMainWindow, UI_VarWindow):
    def __init__(self, parent=None):
        super(VarWindow, self).__init__(parent)
        
        self.setupUi(self)
        self.setWindowTitle(Localization.VAR_WIN_TITLE)  

class Main(QMainWindow, UI_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        
        self.setupUi(self)

        self.btn_1.clicked.connect(self.show_window_2)
        self.btn_2.clicked.connect(self.show_window_3)

    def show_window_2(self):
        self.w2 = BaseWindow()
        self.w2.show()

    def show_window_3(self):
        self.w3 = VarWindow()
        self.w3.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())
