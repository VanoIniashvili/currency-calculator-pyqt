import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_MainWindow import Ui_MainWindow

user = {'username': 'admin', 'password': 'admin'}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.pushButton.clicked.connect(self.authenticate_user)

        self.ui.pushButton_2.clicked.connect(self.convert_currency)
        self.ui.pushButton_3.clicked.connect(self.reset_fields)
        self.ui.pushButton_4.clicked.connect(self.log_out)

        self.load_currencies()

    def authenticate_user(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if username == user['username'] and password == user['password']:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        else:
            self.ui.label_6.setText("სახელი ან პაროლი არასწორია!")


    def load_currencies(self):
        url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json'
        response = requests.get(url)
        currencies = []
        for currency in response.json().keys():
            currencies.append(currency)

        self.ui.comboBox.addItems(currencies)
        self.ui.comboBox_2.addItems(currencies)


    def convert_currency(self):
        from_currency = self.ui.comboBox.currentText()
        to_currency = self.ui.comboBox_2.currentText()
        initial_amount = self.ui.lineEdit_3.text()
        not_allowed_symbols = '~!@#$%^&*()_+-=,<>?/{}[]:";'

        if not initial_amount:
            self.ui.label_5.setText('ჩაწერე რაოდენობა!')
            return
        elif from_currency == to_currency:
            self.ui.label_5.setText('აირჩიე სხვადასხვა ვალუტა!')
            return
        elif any(char.isalpha() or char in not_allowed_symbols for char in initial_amount):
            self.ui.label_5.setText('არასწორი ფორმატი!')
            return

        currencies_data = requests.get(f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency}.json')

        data = currencies_data.json()

        conversion_rate = data[from_currency][to_currency]
        result = round(conversion_rate * float(initial_amount), 3)
        self.ui.label_5.setText(f'{result}')

    def reset_fields(self):
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox_2.setCurrentIndex(0)
        self.ui.lineEdit_3.clear()
        self.ui.label_5.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.label_6.clear()


    def log_out(self):
        self.reset_fields()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

