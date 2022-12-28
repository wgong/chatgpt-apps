# https://www.youtube.com/watch?v=iVCLg60ofKk
# ChatGPT demo

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)

view = QWebEngineView()
view.load(QUrl("https://www.vanguard.com"))
view.show()

sys.exit(app.exec_())

# Not working
"""
    Traceback (most recent call last):
  File "browser.py", line 4, in <module>
    from PyQt5.QtWebEngineWidgets import QWebEngineView
ImportError: /home/wengong/anaconda3/lib/python3.8/site-packages/PyQt5/../../../libQt5Network.so.5: undefined symbol: _ZN15QIPAddressUtils8toStringER7QStringPh, version Qt_5

"""

