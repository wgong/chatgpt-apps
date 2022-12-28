

https://www.youtube.com/watch?v=iVCLg60ofKk


https://techvidvan.com/tutorials/create-web-browser-python-pyqt/

"""
conda create --name py38 python=3.8
activate py38
which python3.8
~/anaconda3/envs/py38/bin/python3.8
which pip3
~/anaconda3/envs/py38/bin/pip3
pip3 install PyQtWebEngine PyQt5
python3.8 main.py

"""

On Ubuntu, Window is created, but nothing displayed

Try on Windows, it worked

- Python 3.8.5 (Anaconda)
- pip3 install PyQt5==5.10.1  PyQtWebEngine  --user
downgrade PyQt5 (see https://stackoverflow.com/questions/55794101/valueerrorpycapsule-getpointer-called-with-incorrect-name-with-from-pyqt5-qtwe)


