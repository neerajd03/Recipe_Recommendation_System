import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QListWidget, QMessageBox, QCheckBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors

# Load the dataset
file_path = r'C:\Users\Neeraj\Desktop\RECIPE WIZARD\Datasets\Cleaned_IFD.csv'  # Update this to your dataset path
data = pd.read_csv(file_path)

# Preprocess the ingredients
vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','), binary=True, token_pattern=None)
X = vectorizer.fit_transform(data['Cleaned-Ingredients'])

# KNN Model
knn = NearestNeighbors(n_neighbors=100, metric='cosine')
knn.fit(X)

def preprocess_input(input_ingredients):
    return vectorizer.transform([input_ingredients])

def recommend_with_knn(input_ingredients, n_recommendations=100):
    input_vector = preprocess_input(input_ingredients)
    distances, indices = knn.kneighbors(input_vector, n_neighbors=n_recommendations)
    return data.iloc[indices[0]].to_dict('records')

class RecipeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recipe Recommendation System")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.title_label = QLabel("Recipe Recommendation System", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.theme_toggle = QCheckBox("Dark Theme", self)
        self.theme_toggle.stateChanged.connect(self.toggle_theme)
        self.layout.addWidget(self.theme_toggle)

        self.input_layout = QHBoxLayout()

        self.ingredients_label = QLabel("Enter Ingredients:", self)
        self.input_layout.addWidget(self.ingredients_label)

        self.ingredients_text = QTextEdit(self)
        self.input_layout.addWidget(self.ingredients_text)

        self.layout.addLayout(self.input_layout)

        self.buttons_layout = QHBoxLayout()

        self.recommend_button = QPushButton("Recommend Recipe", self)
        self.recommend_button.clicked.connect(self.recommend_recipe)
        self.buttons_layout.addWidget(self.recommend_button)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.clicked.connect(self.clear_input)
        self.buttons_layout.addWidget(self.clear_button)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.close)
        self.buttons_layout.addWidget(self.exit_button)

        self.layout.addLayout(self.buttons_layout)

        self.recommendations_label = QLabel("Recommended Recipes:", self)
        self.layout.addWidget(self.recommendations_label)

        self.recommendations_list = QListWidget(self)
        self.recommendations_list.itemClicked.connect(self.show_recipe_details)
        self.layout.addWidget(self.recommendations_list)

        self.recipe_details_label = QLabel("Recipe Details:", self)
        self.layout.addWidget(self.recipe_details_label)

        self.recipe_details_table = QTableWidget(self)
        self.recipe_details_table.setColumnCount(2)
        self.recipe_details_table.setHorizontalHeaderLabels(["Detail", "Value"])
        self.layout.addWidget(self.recipe_details_table)

        self.set_light_theme()

    def toggle_theme(self):
        if self.theme_toggle.isChecked():
            self.set_dark_theme()
        else:
            self.set_light_theme()

    def set_light_theme(self):
        self.central_widget.setStyleSheet("background-color: #FFFFFF;")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #000000; background-color: #EEEEEE;")
        self.ingredients_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #000000; background-color: #EEEEEE;")
        self.ingredients_text.setStyleSheet("font-size: 14px; color: #000000; background-color: #FFFFFF;")
        self.recommend_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                color: #000000;
                background-color: #FFA500;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #FF8C00;
            }
        """)
        self.clear_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                color: #000000;
                background-color: #808080;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #696969;
            }
        """)
        self.exit_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                color: #000000;
                background-color: #FF6347;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #FF4500;
            }
        """)
        self.recommendations_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #000000; background-color: #EEEEEE;")
        self.recommendations_list.setStyleSheet("font-size: 14px; color: #000000; background-color: #FFFFFF;")
        self.recipe_details_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #000000; background-color: #EEEEEE;")
        self.recipe_details_table.setStyleSheet("font-size: 14px; color: #000000; background-color: #FFFFFF;")

    def set_dark_theme(self):
        self.central_widget.setStyleSheet("background-color: #222222;")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #FFFFFF; background-color: #333333;")
        self.ingredients_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; background-color: #333333;")
        self.ingredients_text.setStyleSheet("font-size: 14px; color: #FFFFFF; background-color: #555555;")
        self.recommend_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                color: #ffffff;
                background-color: #FFA500;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #FF8C00;
            }
        """)
        self.clear_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                color: #ffffff;
                background-color: #808080;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #696969;
            }
        """)
        self.exit_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                color: #ffffff;
                background-color: #FF6347;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #FF4500;
            }
        """)
        self.recommendations_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; background-color: #333333;")
        self.recommendations_list.setStyleSheet("font-size: 14px; color: #FFFFFF; background-color: #555555;")
        self.recipe_details_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; background-color: #333333;")
        self.recipe_details_table.setStyleSheet("font-size: 14px; color: #FFFFFF; background-color: #555555;")

    def recommend_recipe(self):
        input_ingredients = self.ingredients_text.toPlainText()
        if not input_ingredients:
            QMessageBox.warning(self, "Input Error", "Please enter some ingredients")
            return

        recommendations = recommend_with_knn(input_ingredients)

        self.recommendations_list.clear()
        if recommendations:
            self.recommendation_details = recommendations
            for recipe in recommendations:
                self.recommendations_list.addItem(recipe['TranslatedRecipeName'])
        else:
            self.recommendations_list.addItem("No recommendations found.")

    def clear_input(self):
        self.ingredients_text.clear()
        self.recommendations_list.clear()
        self.recipe_details_table.clearContents()
        self.recipe_details_table.setRowCount(0)

    def show_recipe_details(self, item):
        selected_recipe_name = item.text()
        selected_recipe = next((recipe for recipe in self.recommendation_details if recipe['TranslatedRecipeName'] == selected_recipe_name), None)
        
        if selected_recipe:
            self.recipe_details_table.setRowCount(len(selected_recipe))
            for row, (key, value) in enumerate(selected_recipe.items()):
                self.recipe_details_table.setItem(row, 0, QTableWidgetItem(key))
                self.recipe_details_table.setItem(row, 1, QTableWidgetItem(str(value)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecipeApp()
    window.show()
    sys.exit(app.exec_())
