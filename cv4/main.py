import sys
from cv4.utils import a
from cv4.cc import dd
from cv4.app import eyeDetectionApp
import helper


def x():
    a.a1()
    helper.hello()
    app = eyeDetectionApp.QApplication(sys.argv)
    dd.ee()
    # 创建应用窗口
    window = eyeDetectionApp.EyeDetectionApp()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    x()