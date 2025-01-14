# Titanic Dataset Analysis Project

## Overview
This project demonstrates advanced data cleaning and preprocessing techniques using the famous Titanic dataset. It showcases essential data science skills including handling missing values, feature engineering, and data visualization using Python, SQL, and Excel integration.

## Features
- **Comprehensive Data Cleaning**
  - Intelligent handling of missing values
  - Feature engineering and extraction
  - Categorical data encoding
- **Data Analysis & Visualization**
  - Survival rate analysis by various factors
  - Passenger demographics visualization
  - Interactive data exploration capabilities
- **Multiple Export Formats**
  - SQLite database integration
  - Excel workbook generation
  - Preprocessed CSV outputs

## Project Structure
```
titanic_analysis/
├── data/                   # Data files
│   ├── Titanic-Dataset.csv # Original dataset
│   ├── titanic.db         # SQLite database
│   └── titanic_processed.xlsx # Processed data
├── notebooks/             # Jupyter notebooks
├── src/                   # Source code
│   ├── data_processor.py  # Main processing class
│   └── run_analysis.py    # Analysis runner
├── sql/                   # SQL queries
│   └── analysis_queries.sql # Analysis queries
├── visualizations/        # Generated plots
└── requirements.txt       # Python dependencies
```

## Key Findings
- Missing Data Analysis:
  - Age: 19.87% missing values
  - Cabin: 77.10% missing values
  - Embarked: 0.22% missing values
- Feature Engineering:
  - Title extraction from names
  - Age group categorization
  - Family size calculation
- Survival Analysis:
  - Gender-based survival rates
  - Class-based survival patterns
  - Age group survival trends

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Instructions
1. Clone the repository:
```bash
git clone [repository-url]
cd titanic_analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Analysis
Execute the main analysis script:
```bash
python src/run_analysis.py
```

This will:
1. Load and clean the dataset
2. Generate visualizations
3. Create processed data files

### Accessing Results
- Visualizations: Check the `visualizations/` directory
- Processed data: 
  - Excel: `data/titanic_processed.xlsx`
  - SQLite: `data/titanic.db`
- SQL queries: Use the queries in `sql/analysis_queries.sql`

## Data Processing Features

### Missing Value Handling
- Age: Imputed using median values
- Cabin: Created binary feature for presence/absence
- Embarked: Filled with mode value

### Feature Engineering
- Title Extraction: Mr., Mrs., Miss., etc.
- Age Groups: Child, Teen, Adult, Senior
- Family Size: Combination of siblings and parents

### Data Export Options
- SQLite database for efficient querying
- Excel workbook for easy viewing
- Processed CSV for further analysis

## SQL Analysis
The project includes SQL queries for:
- Survival rates by passenger class
- Age group analysis
- Port of embarkation statistics
- Family size impact on survival

## Visualizations
Generated visualizations include:
- Survival rates by gender
- Passenger class distribution
- Age distribution analysis
- Family size impact plots

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Titanic dataset provided by Kaggle
- Inspired by the data science community
- Built with Python's data science stack
