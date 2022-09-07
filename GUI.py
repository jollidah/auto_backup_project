import sys
from PyQt5.QtWidgets import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.parent_url = "/."
        self.child_url = "/."
        self.interval = 30 * 60 * 1000
        self.sys_log = "Starting System..."
        self.is_run = False
        self. initUI()


    def set_parent_url(self):
        file_url = QFileDialog.getExistingDirectory(self, "Open Folder", self.parent_url)
        if file_url[0]:
            self.parent_url = file_url
            self.text_parent_url.setText(self.parent_url)
            print(self.parent_url)
        else:
            pass

    def set_child_url(self):
        file_url = QFileDialog.getExistingDirectory(self, "Open Folder", self.child_url)
        if file_url[0]:
            self.child_url = file_url
            self.text_child_url.setText(self.child_url)
            print(self.child_url)
        else:
            pass


    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.create_option_label(), 0, 0)
        grid.addWidget(self.create_sys_label(), 1, 0)
        grid.addWidget(self.create_option_box(), 0, 1)
        grid.addWidget(self.create_sys_box(), 1, 1)

        self.setWindowTitle("PNCTECH Backup Program")
        self.setGeometry(600, 300, 800, 500)
        self. show()

    def create_option_label(self):
        self.option_label = QLabel("옵션", self)
        self.option_label.move(160, 30)
        return self.option_label

    def create_sys_label(self):
        self.sys_label = QLabel("System Log", self)
        self.sys_label.move(510, 30)
        return self.sys_label

    def create_option_box(self):
        self.option_box = QGroupBox(self)
        self.option_box.move(50, 50)
        self.option_box.resize(250, 400)

        # Button
        button_parent_url_change = QPushButton("...찾아보기", self)
        button_parent_url_change.clicked.connect(self.set_parent_url)

        button_child_url_change = QPushButton("...찾아보기", self)
        button_child_url_change.clicked.connect(self.set_child_url)

        self.button_run = QPushButton(self.option_box)
        self.button_run.setText("프로그램 시작")

        # Label
        label_parent = QLabel("부모 폴더")
        label_child = QLabel("자식 폴더")

        label_interval_option = QLabel()
        label_interval_option.setText("백업 간격")

        # Radio Button
        self.radio_interval_10 = QRadioButton("10분", self)
        self.radio_interval_30 = QRadioButton("30분", self)
        self.radio_interval_60 = QRadioButton("60분", self)


        # URL text
        self.text_parent_url = QLineEdit()      # URL of parent
        self.text_parent_url.setText(self.parent_url)
        self.text_parent_url.setReadOnly(True)

        self.text_child_url = QLineEdit()       # URL of child
        self.text_child_url.setText(self.child_url)
        self.text_child_url.setReadOnly(True)

        # GroupBox for url setting
        url_option_box = QGroupBox(self.option_box)
        url_option_box.move(10, 10)
        url_option_box.resize(230, 200)

        # Put GridLayout in GroupBox
        url_option_grid_box = QGridLayout(url_option_box)

        # Set position of parent URL
        url_option_grid_box.addWidget(label_parent, 0, 0, 1, 1)
        url_option_grid_box.addWidget(button_parent_url_change, 0, 1, 1, 1)
        url_option_grid_box.addWidget(self.text_parent_url, 1, 0, 1, 2)

        # Set position of child URL
        url_option_grid_box.addWidget(label_child, 5, 0, 1, 1)
        url_option_grid_box.addWidget(button_child_url_change, 5, 1, 1, 1)
        url_option_grid_box.addWidget(self.text_child_url, 6, 0, 1, 2)

        # Set interval of doing back up
        interval_option_box = QGroupBox(self.option_box)
        interval_option_box.move(10, 220)
        interval_option_box.resize(230, 120)

        # GridLayout for option of interval
        interval_option_gird_box = QGridLayout(interval_option_box)

        interval_option_gird_box.addWidget(label_interval_option, 0, 0, 1, 1)
        interval_option_gird_box.addWidget(self.radio_interval_10, 0, 1, 1, 1)
        interval_option_gird_box.addWidget(self.radio_interval_30, 1, 1, 1, 1)
        interval_option_gird_box.addWidget(self.radio_interval_60, 2, 1, 1, 1)

        self.button_run.move(70, 355)

        return self.option_box

    def create_sys_box(self):
        self.sys_box = QPlainTextEdit(self)
        self.sys_box.move(350, 50)
        self.sys_box.resize(400, 400)
        self.sys_box.setPlainText(self.sys_log)
        self.sys_box.setReadOnly(True)

        return self.sys_box


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
