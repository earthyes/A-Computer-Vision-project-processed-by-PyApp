from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import cv2
from cv4.error import errorMessage

class EyeDetectionApp(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("人眼检测")

        # 设置窗口大小
        self.setGeometry(100, 100, 800, 600)

        # 创建一个布局和控件
        self.layout = QVBoxLayout()

        # 添加按钮来导入图片
        self.button = QPushButton("导入图片", self)
        self.button.clicked.connect(self.load_image)

        # 添加标签来显示图片
        self.image_label = QLabel(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.image_label)

        self.setLayout(self.layout)

        # 加载Haar Cascade 人脸检测和人眼检测分类器
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    def load_image(self):
        # 打开文件对话框选择图片
        file_path, _ = QFileDialog.getOpenFileName(self, "打开图片", "",
                                                   "Images (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")

        if file_path:
            # 读取图片
            image = cv2.imread(file_path)
            if image is None:
                # print("无法读取图片")
                errorMessage.show_error_message("无法读取图片")
                return

            # 转换为灰度图像
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # 使用 Haar Cascade 检测人脸
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # 在图片上绘制矩形框标记检测到的人脸
            for (x, y, w, h) in faces:
                # 在每个检测到的人脸区域中继续检测眼睛
                roi_gray = gray[y:y + h, x:x + w]
                eyes = self.eye_cascade.detectMultiScale(roi_gray)

                # 在人脸区域内绘制检测到的眼睛
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(image, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)

            # 将图片转换为 Qt 兼容的格式以显示
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 转换为 RGB 格式
            h, w, _ = image_rgb.shape
            qimg = QImage(image_rgb.data, w, h, 3 * w, QImage.Format_RGB888)
            pixmap = QPixmap(qimg)

            # 设置标签显示图像
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)

