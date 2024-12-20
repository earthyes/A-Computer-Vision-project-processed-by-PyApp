from PyQt5.QtWidgets import QMessageBox
from cv4.error.title import titlename

def show_error_message(message):
    # 创建一个消息框来显示错误信息
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)  # 设置消息框为错误类型
    msg_box.setWindowTitle(titlename.x)  # 设置窗口标题
    msg_box.setText(message)  # 设置消息文本
    msg_box.setStandardButtons(QMessageBox.Ok)  # 添加 "确定" 按钮
    msg_box.exec_()  # 显示消息框