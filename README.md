##Heart Disease Prediction Project

##Overview

##This project aims to predict the presence of heart disease in patients based on various medical attributes. It utilizes machine learning algorithms, including hyperparameter tuning techniques, to improve prediction accuracy.

##Technologies Used

- Python: Main programming language
- Libraries: scikit-learn, pandas, numpy, matplotlib, seaborn
- Machine Learning Models: Logistic Regression, Random Forest, XGBoost
- Hyperparameter Tuning: GridSearchCV, RandomizedSearchCV

## Project Structure

- `/data`: Contains the dataset used (`heart_disease_data.csv`).
- `/notebooks`: Jupyter notebooks for data exploration, model development, and hyperparameter tuning.
- `/models`: Python scripts for final trained models.
- `/results`: Evaluation metrics and visualization outputs.

## Setup Instructions

1. Clone the repository:
   ```bash
   https://github.com/ashpaqueshaikh4236/Heart_Disease_Classification.git
   cd heart-disease-prediction
   ```

2. Setup Python environment:
   ```bash
   pip install -r requirements.txt
   ```

3. Run Jupyter notebooks:
   - Explore data: `jupyter notebook notebooks/Heart  Disease Classification.ipynb`
   - Model development: `jupyter notebook notebooks/Heart  Disease Classification.ipynb`
   - Hyperparameter tuning: `jupyter notebook notebooks/Heart  Disease Classification.ipynb`

## Machine Learning Process

### Data Preprocessing

- Data Cleaning: Handling missing values and outliers.
- Feature Engineering: Creating new features or transforming existing ones.

### Model Development

- Logistic Regression: Baseline model for heart disease prediction.
- Random Forest: Ensemble model for improved accuracy.
- XGBoost: Gradient boosting model for further performance enhancement.

### Hyperparameter Tuning

- GridSearchCV: Exhaustive search over specified parameter values for optimal performance.
- RandomizedSearchCV: Randomized search over hyperparameter distributions to save computation time.

## Model Evaluation

- Metrics: Accuracy, Precision, Recall, F1-score.
- Visualizations: Confusion matrix.

## Results and Conclusion

- Best Model: Identified through hyperparameter tuning.
- Performance: Evaluation metrics and comparison between models.
