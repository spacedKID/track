import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QRadioButton, QButtonGroup, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout
from data_flow_logic import get_categories

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Track Application')
        self.setGeometry(100, 100, 800, 600)
        self.initUI()
    
    def initUI(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.mainLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.mainLayout)
        
        # Initialize category selection
        self.categroyGroup = QButtonGroup(self.centralWidget) # Group for radio buttons
        self.categoriesLayout = QVBoxLayout()

        categories = get_categories()
        for category_id, category_name in categories:
            radioButton = QRadioButton(category_name)
            self.categroyGroup.addButton(radioButton, category_id) # Assign ID for identification
            self.categoriesLayout.addWidget(radioButton)

        # Add the categories layout to the main layout
        self.mainLayout.addLayout(self.categoriesLayout)

        self.categoryPlaceholder = QLabel('Category Selector Placeholder')
        self.subCategoryPlaceholder = QLabel('Sub-Category Selector Placeholder')
        self.trackableObjectPlaceholder = QLabel('Trackable Object Selector Placeholder')
        self.inputField = QLineEdit()
        self.inputField.setPlaceholderText('Input for Trackable Object')
        self.confirmButton = QPushButton('Confirm')
        self.cancelButton = QPushButton('Cancel')
        self.settingsButton = QPushButton('Settings')
        
        self.mainLayout.addWidget(self.categoryPlaceholder)
        self.mainLayout.addWidget(self.subCategoryPlaceholder)
        self.mainLayout.addWidget(self.trackableObjectPlaceholder)
        self.mainLayout.addWidget(self.inputField)
        self.mainLayout.addWidget(self.confirmButton)
        self.mainLayout.addWidget(self.cancelButton)
        self.mainLayout.addWidget(self.settingsButton)
        
        # Connect buttons to functions
        self.settingsButton.clicked.connect(self.openSettings)
        self.cancelButton.clicked.connect(self.close)
        # Placeholder: Connect confirmButton and settingsButton to their respective functions
        
    def openSettings(self):
        for i in reversed(range(self.mainLayout.count())): 
            widget = self.mainLayout.takeAt(i).widget()
            if widget is not None: 
                widget.deleteLater()
        
        self.addCategoryButton = QPushButton('Add Category')
        self.addSubCategoryButton = QPushButton('Add Sub-Category')
        self.addTrackableObjectButton = QPushButton('Add Trackable Object')
        self.editButton = QPushButton('Edit')
        self.returnMainPageButton = QPushButton('Return to Main Page')
        
        self.mainLayout.addWidget(self.addCategoryButton)
        self.mainLayout.addWidget(self.addSubCategoryButton)
        self.mainLayout.addWidget(self.addTrackableObjectButton)
        self.mainLayout.addWidget(self.editButton)
        self.mainLayout.addWidget(self.returnMainPageButton)
        
        self.returnMainPageButton.clicked.connect(self.initUI)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
