# -*- coding =utf-8 -*-

'''主界面文件，实现界面和逻辑结合
opencv处理的界面
'''
# from graphicUI import *
from UIImpliment import *


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    formObj=QtWidgets.QMainWindow()  #注意，这里和我们一开始创建窗体时使用的界面类型相同
    # ui = Ui_MainWindow()
    ui = uiWindows(formObj)
    #ui.setupUi(formObj)
    formObj.show()
    sys.exit(app.exec_())