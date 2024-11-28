import sys
from Utils.Helpers import Helpers
from PyQt6.QtWidgets import QApplication
from View.Login import LoginWindow


if __name__ == "__main__":
    ui_login = Helpers.get_base_path() + "/Ui/login.ui"

    app = QApplication(sys.argv)
    window_login = LoginWindow(ui_login)
    
    sys.exit(app.exec())