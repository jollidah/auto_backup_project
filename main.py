import sys
import GUI


def run():
    app = GUI.QApplication(sys.argv)
    window = GUI.Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
