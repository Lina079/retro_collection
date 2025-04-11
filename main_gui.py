import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel,
    QLineEdit, QTextEdit, QComboBox, QPushButton, QMessageBox
)
from ui_main_window import Ui_MainWindow
from item import Item
from config import TYPES
from collection import show_items_by_type, delete_item, edit_item, add_new_type
from storage import load_types, save_items, load_items

class AddItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Item")

        layout = QVBoxLayout()

        self.title_input = QLineEdit()
        layout.addWidget(QLabel("Title:"))
        layout.addWidget(self.title_input)

        self.type_box = QComboBox()
        for key in TYPES:
            self.type_box.addItem(TYPES[key], key)
        layout.addWidget(QLabel("Type:"))
        layout.addWidget(self.type_box)

        self.date_added_input = QLineEdit()
        layout.addWidget(QLabel("Date Added (DD/MM/YYYY):"))
        layout.addWidget(self.date_added_input)

        self.date_made_input = QLineEdit()
        layout.addWidget(QLabel("Date of Manufacture (DD/MM/YYYY):"))
        layout.addWidget(self.date_made_input)

        self.description_input = QTextEdit()
        layout.addWidget(QLabel("Description:"))
        layout.addWidget(self.description_input)

        self.save_button = QPushButton("Save Item")
        self.save_button.clicked.connect(self.save_item)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_item(self):
        title = self.title_input.text().strip()
        type_id = self.type_box.currentData()
        date_added = self.date_added_input.text().strip()
        date_made = self.date_made_input.text().strip()
        description = self.description_input.toPlainText().strip()

        if not title or not date_added or not date_made:
            QMessageBox.warning(self, "Missing Data", "Please fill in all required fields.")
            return

        Item(title, type_id, date_added, date_made, description)
        QMessageBox.information(self, "Success", "Item added successfully!")
        self.accept()

class ShowItemsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Show Items by Type")

        layout = QVBoxLayout()

        self.type_box = QComboBox()
        for key, value in TYPES.items():
            self.type_box.addItem(value, key)

        layout.addWidget(QLabel("Select Type:"))
        layout.addWidget(self.type_box)

        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

        show_button = QPushButton("Show Items")
        show_button.clicked.connect(self.show_items)
        layout.addWidget(show_button)

        self.setLayout(layout)

    def show_items(self):
        type_id = self.type_box.currentData()
        items = Item.get_all_by_type(type_id)

        if not items:
            self.output_area.setText("No items found for this type.")
            return

        output = f"Showing: {TYPES[type_id]}\n"
        output += "-" * 50 + "\n"
        for item in items:
            output += f"{item.title} | Added: {item.date_added} | Made: {item.date_made}\n"
        self.output_area.setText(output)

class DeleteItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Delete Item from Collection")

        layout = QVBoxLayout()

        self.item_box = QComboBox()
        self.items = Item.get_all_items()
        for i, item in enumerate(self.items):
            self.item_box.addItem(f"{item.title} (Added: {item.date_added})", i)

        layout.addWidget(QLabel("Select item to delete:"))
        layout.addWidget(self.item_box)

        delete_button = QPushButton("Delete Selected Item")
        delete_button.clicked.connect(self.delete_item)
        layout.addWidget(delete_button)

        self.setLayout(layout)

    def delete_item(self):
        index = self.item_box.currentData()
        if 0 <= index < len(self.items):
            item = Item.delete_by_index(index)
            if item:
                QMessageBox.information(self, "Deleted", f"{item.title} has been deleted.")
                self.accept()
            else:
                QMessageBox.warning(self, "Error", "Could not delete item.")
        else:
            QMessageBox.warning(self, "Error", "Invalid selection.")

class EditItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Existing Item")

        self.items = Item.get_all_items()

        layout = QVBoxLayout()

        self.item_box = QComboBox()
        for i, item in enumerate(self.items):
            self.item_box.addItem(f"{item.title} (Added: {item.date_added})", i)
        self.item_box.currentIndexChanged.connect(self.load_item_data)
        layout.addWidget(QLabel("Select item to edit:"))
        layout.addWidget(self.item_box)

        self.title_input = QLineEdit()
        layout.addWidget(QLabel("Title:"))
        layout.addWidget(self.title_input)

        self.type_box = QComboBox()
        for key, value in TYPES.items():
            self.type_box.addItem(value, key)
        layout.addWidget(QLabel("Type:"))
        layout.addWidget(self.type_box)

        self.date_added_input = QLineEdit()
        layout.addWidget(QLabel("Date Added (DD/MM/YYYY):"))
        layout.addWidget(self.date_added_input)

        self.date_made_input = QLineEdit()
        layout.addWidget(QLabel("Date of Manufacture (DD/MM/YYYY):"))
        layout.addWidget(self.date_made_input)

        self.description_input = QTextEdit()
        layout.addWidget(QLabel("Description:"))
        layout.addWidget(self.description_input)

        save_button = QPushButton("Save Changes")
        save_button.clicked.connect(self.save_changes)
        layout.addWidget(save_button)

        self.setLayout(layout)
        self.load_item_data(0)

    def load_item_data(self, index):
        if index < 0 or index >= len(self.items):
            return

        item = self.items[index]
        self.title_input.setText(item.title)
        self.date_added_input.setText(item.date_added)
        self.date_made_input.setText(item.date_made)
        self.description_input.setText(item.description)

        type_index = self.type_box.findData(item.type_id)
        if type_index >= 0:
            self.type_box.setCurrentIndex(type_index)

    def save_changes(self):
        index = self.item_box.currentData()
        if 0 <= index < len(self.items):
            item = self.items[index]
            item.title = self.title_input.text().strip()
            item.type_id = self.type_box.currentData()
            item.date_added = self.date_added_input.text().strip()
            item.date_made = self.date_made_input.text().strip()
            item.description = self.description_input.toPlainText().strip()
            QMessageBox.information(self, "Saved", "Changes saved successfully.")
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Invalid item selection.")

class AddTypeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Item Type")

        layout = QVBoxLayout()

        self.type_input = QLineEdit()
        layout.addWidget(QLabel("New Type Name:"))
        layout.addWidget(self.type_input)

        add_button = QPushButton("Add Type")
        add_button.clicked.connect(self.add_type)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_type(self):
        from config import TYPES  # Asegurarse de tener la versión más actual

        new_type = self.type_input.text().strip()
        if not new_type:
            QMessageBox.warning(self, "Empty Field", "Please enter a type name.")
            return

        if new_type in TYPES.values():
            QMessageBox.warning(self, "Duplicate", "This type already exists.")
            return

        new_id = max(TYPES.keys()) + 1
        TYPES[new_id] = new_type
        QMessageBox.information(self, "Success", f"Type '{new_type}' added successfully.")
        self.accept()

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnAddItem.clicked.connect(self.handle_add_item)
        self.ui.btnShowItems.clicked.connect(self.handle_show_items)
        self.ui.btnDeleteItem.clicked.connect(self.handle_delete_item)
        self.ui.btnEditItem.clicked.connect(self.handle_edit_item)
        self.ui.btnAddType.clicked.connect(self.handle_add_type)
        self.ui.btnExit.clicked.connect(self.close)

    def handle_add_item(self):
        dialog = AddItemDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            save_items()

    def handle_show_items(self):
        dialog = ShowItemsDialog(self)
        dialog.exec_()

    def handle_delete_item(self):
        dialog = DeleteItemDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            save_items()


    def handle_edit_item(self):
        dialog = EditItemDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            save_items()

    def handle_add_type(self):
        dialog = AddTypeDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            save_items()



if __name__ == "__main__":
    load_types()
    load_items()

    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

