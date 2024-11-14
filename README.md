# Recipe_Recommendation_System
Recipe_Recommendation_System blah blah blah
This application is a recipe recommendation system built with Python and PyQt5. Users can input ingredients, and the app suggests recipes that match the given ingredients using a K-Nearest Neighbors (KNN) model for similarity-based recommendation. It features a GUI with light and dark themes.

## Key Features
Ingredient-Based Recommendations: Users enter ingredients, and the app suggests relevant recipes based on ingredient similarity.
K-Nearest Neighbors (KNN) Model: Utilizes cosine similarity to find recipes with matching ingredients.
Dynamic Recipe Details: Displays additional details about each recommended recipe.
Theme Toggle: Users can switch between light and dark themes.
## Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/recipe-recommendation-system.git
Install dependencies:
bash
Copy code
pip install PyQt5 pandas scikit-learn
Update the dataset path in the code if necessary (file_path variable).
## Dataset
The application uses a dataset in CSV format containing recipes and cleaned ingredients.
Update file_path in the code to point to the location of your dataset file.
## Usage
Run the application:
bash
Copy code
python guinterface.py
Enter a list of ingredients, and click "Recommend Recipe" to see suggestions.
Click on a recipe to view detailed information.
## Code Structure
Data Preprocessing: Vectorizes ingredients for cosine similarity.
KNN Model: Finds recipes similar to the user's input ingredients.
PyQt5 GUI: Provides an interactive interface with light and dark theme options.
## Technologies Used
Python: Core language
PyQt5: GUI framework
Pandas: Data manipulation
Scikit-Learn: KNN model for recipe recommendation
## License
This project is licensed under the MIT License - see the LICENSE file for details.
