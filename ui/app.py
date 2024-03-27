import logging
import sys
from typing import Sequence

from PySide6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem

from db.database import (
    Users,
    add_user,
    delete_user,
    get_all_users,
    select_users,
    update_user,
)
from ui.window_geter import MainWindow

logger = logging.getLogger(__name__)

app = QApplication(sys.argv)
window: MainWindow = MainWindow()


class UI:
    def __init__(self) -> None:
        self.selected_id: int = -1

    def add_signals(self):
        window.btnRefresh.clicked.connect(self.btn_reload_table_clicked)

        window.btnAdd.clicked.connect(self.btn_add_clicked)
        window.btnUpdate.clicked.connect(self.btn_update_clicked)
        window.btnRemove.clicked.connect(self.btn_remove_clicked)

        window.btnSearch.clicked.connect(self.btn_search_clicked)

        window.tblData.itemSelectionChanged.connect(self.tbl_data_selection_change)
        window.btnClear.clicked.connect(lambda: window.tblData.clearContents())

        window.acnExit.triggered.connect(self.exit)

    def exit(self):
        app.quit()

    def btn_search_clicked(self):
        name = window.txtSearchName.text()
        last = window.txtSearchLast.text()
        email = window.txtSearchEmail.text()
        id = window.txtSearchID.text()
        if not name and not last and not email and not id:
            QMessageBox.warning(
                window, "Fill all the info", "Please fill all the inputs"
            )
            return
        data = select_users(name=name, last=last, email=email, id=int(id) if id else -1)
        if data:
            self.btn_reload_table_clicked(data=[x[0] for x in data])
        else:
            QMessageBox.warning(
                window, "No match found", "No match found for your search"
            )

    def btn_remove_clicked(self):
        if self.selected_id is None:
            QMessageBox.warning(
                window, "Fill all the info", "Please fill all the inputs"
            )
            return
        ans=QMessageBox()
        ans.setText("Do you want to delete the user?")
        ans.setStandardButtons(QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        rel=ans.exec()
        if rel==QMessageBox.StandardButton.Yes:
            delete_user(self.selected_id)
            self.btn_reload_table_clicked()

    def btn_update_clicked(self):
        if (
            not (name := window.txtName.text())
            or not (last := window.txtLast.text())
            or not (email := window.txtEmail.text())
            or self.selected_id is None
        ):
            QMessageBox.warning(
                window, "Fill all the info", "Please fill all the inputs"
            )
            return
        update_user(Users(id=self.selected_id, name=name, last_name=last, email=email))
        self.btn_reload_table_clicked()

    def tbl_data_selection_change(self):
        items = window.tblData.selectedItems()
        selected_rows = set([x.row() for x in items])
        if len(selected_rows) == 1:
            index = selected_rows.pop()
            window.txtName.setText(window.tblData.item(index, 1).text())
            window.txtLast.setText(window.tblData.item(index, 2).text())
            window.txtEmail.setText(window.tblData.item(index, 3).text())
            self.selected_id = int(window.tblData.item(index, 0).text())

    def btn_add_clicked(self):
        if (
            not (name := window.txtName.text())
            or not (last := window.txtLast.text())
            or not (email := window.txtEmail.text())
        ):
            QMessageBox.warning(
                window, "Fill all the info", "Please fill all the inputs"
            )
            return
        add_user(Users(name=name, last_name=last, email=email))
        self.btn_reload_table_clicked()
        window.txtEmail.clear()
        window.txtLast.clear()
        window.txtName.clear()

    def setup_table(self):
        headers = ["ID", "Name", "Last Name", "Email"]
        window.tblData.setHorizontalHeaderLabels(headers)

    def btn_reload_table_clicked(self, data: Sequence[Users] | None = None):
        if not data:
            data= get_all_users()
        window.tblData.setRowCount(len(data))

        for row_index, user in enumerate(data):
            window.tblData.setItem(row_index, 0, QTableWidgetItem(str(user.id)))
            window.tblData.setItem(row_index, 1, QTableWidgetItem(user.name))
            window.tblData.setItem(row_index, 2, QTableWidgetItem(user.last_name))
            window.tblData.setItem(row_index, 3, QTableWidgetItem(user.email))

    def run(self):
        self.add_signals()
        self.setup_table()
        self.btn_reload_table_clicked()
        window.show()
        app.exec()
