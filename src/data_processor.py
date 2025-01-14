import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import sqlite3
from pathlib import Path
import os

# Set the backend to Agg for better compatibility
import matplotlib
matplotlib.use('Agg')

class TitanicDataProcessor:
    def __init__(self, data_path):
        """Initialize the data processor with the path to the Titanic dataset."""
        self.data_path = data_path
        self.df = None
        self.original_df = None

    def load_data(self):
        """Load the Titanic dataset."""
        self.df = pd.read_csv(self.data_path)
        self.original_df = self.df.copy()
        return self.df.head()

    def analyze_missing_values(self):
        """Analyze missing values in the dataset."""
        missing_values = self.df.isnull().sum()
        missing_percentages = (missing_values / len(self.df)) * 100
        return pd.DataFrame({
            'Missing Values': missing_values,
            'Percentage': missing_percentages
        })

    def handle_missing_values(self):
        """Handle missing values in the dataset."""
        # Age: Fill with median
        self.df['Age'].fillna(self.df['Age'].median(), inplace=True)
        
        # Embarked: Fill with mode
        self.df['Embarked'].fillna(self.df['Embarked'].mode()[0], inplace=True)
        
        # Cabin: Create a binary feature indicating if cabin is missing
        self.df['HasCabin'] = self.df['Cabin'].notna().astype(int)

    def engineer_features(self):
        """Create new features from existing data."""
        # Extract titles from names
        self.df['Title'] = self.df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
        
        # Create age groups
        self.df['AgeGroup'] = pd.cut(self.df['Age'], 
                                   bins=[0, 12, 18, 35, 50, np.inf],
                                   labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])
        
        # Create family size feature
        self.df['FamilySize'] = self.df['SibSp'] + self.df['Parch'] + 1

    def encode_categorical_features(self):
        """Encode categorical features."""
        le = LabelEncoder()
        categorical_features = ['Sex', 'Embarked', 'Title']
        
        for feature in categorical_features:
            if feature in self.df.columns:
                self.df[feature + '_Encoded'] = le.fit_transform(self.df[feature].astype(str))

    def export_to_sqlite(self, db_path):
        """Export the processed dataset to SQLite database."""
        conn = sqlite3.connect(db_path)
        self.df.to_sql('titanic', conn, if_exists='replace', index=False)
        conn.close()

    def export_to_excel(self, output_path):
        """Export the processed dataset to Excel."""
        self.df.to_excel(output_path, index=False)

    def plot_survival_statistics(self, output_dir):
        """Create visualizations for survival statistics."""
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        try:
            # 1. Correlation Heatmap
            plt.figure(figsize=(10, 8))
            numeric_cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
            correlation_matrix = self.df[numeric_cols].corr()
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
            plt.title('Correlation Heatmap of Survival Factors')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
            plt.close()

            # 2. Class Survival Rate
            plt.figure(figsize=(8, 6))
            sns.barplot(x='Pclass', y='Survived', data=self.df, 
                       order=[1, 2, 3], 
                       palette='viridis')
            plt.title('Survival Rate by Class')
            plt.xlabel('Class')
            plt.ylabel('Survival Rate')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'class_survival_rate.png'))
            plt.close()

            # 3. Age Distribution
            plt.figure(figsize=(10, 6))
            sns.histplot(data=self.df, x='Age', hue='Survived', multiple="stack", bins=30)
            plt.title('Age Distribution by Survival')
            plt.xlabel('Age')
            plt.ylabel('Count')
            plt.legend(title='Survived', labels=['No', 'Yes'])
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'age_distribution.png'))
            plt.close()

            # 4. Family Size Impact
            plt.figure(figsize=(8, 6))
            survival_by_family = self.df.groupby('FamilySize')['Survived'].mean().reset_index()
            sns.barplot(x='FamilySize', y='Survived', data=survival_by_family)
            plt.title('Survival Rate by Family Size')
            plt.xlabel('Family Size')
            plt.ylabel('Survival Rate')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'family_size_impact.png'))
            plt.close()

            # 5. Gender Survival Rate
            plt.figure(figsize=(8, 6))
            sns.barplot(x='Sex', y='Survived', data=self.df, 
                       palette=['lightcoral', 'lightblue'])
            plt.title('Survival Rate by Gender')
            plt.xlabel('Gender')
            plt.ylabel('Survival Rate')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'gender_survival_rate.png'))
            plt.close()

            print("All visualizations generated successfully!")
            
        except Exception as e:
            print(f"Error generating visualizations: {str(e)}")
            import traceback
            print(traceback.format_exc())

if __name__ == "__main__":
    # Example usage
    processor = TitanicDataProcessor('data/titanic.csv')
    processor.load_data()
    processor.handle_missing_values()
    processor.engineer_features()
    processor.encode_categorical_features()
    processor.plot_survival_statistics('visualizations')
    processor.export_to_sqlite('data/titanic.db')
    processor.export_to_excel('data/titanic_processed.xlsx')
