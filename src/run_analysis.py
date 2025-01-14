from data_processor import TitanicDataProcessor
import os

def main():
    # Initialize the processor with the data file
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'Titanic-Dataset.csv')
    processor = TitanicDataProcessor(data_path)
    
    # Load and display initial data info
    print("\n=== Loading Data ===")
    df = processor.load_data()
    print("\nFirst few rows of the dataset:")
    print(df)
    
    # Analyze missing values
    print("\n=== Missing Values Analysis ===")
    missing_analysis = processor.analyze_missing_values()
    print(missing_analysis)
    
    # Handle missing values and engineer features
    print("\n=== Processing Data ===")
    processor.handle_missing_values()
    processor.engineer_features()
    processor.encode_categorical_features()
    
    # Create visualizations
    print("\n=== Creating Visualizations ===")
    visualizations_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'visualizations')
    processor.plot_survival_statistics(visualizations_dir)
    print(f"Visualizations have been saved to: {visualizations_dir}")
    
    # Export processed data
    print("\n=== Exporting Processed Data ===")
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'titanic.db')
    excel_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'titanic_processed.xlsx')
    
    processor.export_to_sqlite(db_path)
    processor.export_to_excel(excel_path)
    print(f"Processed data exported to:\n- SQLite: {db_path}\n- Excel: {excel_path}")

if __name__ == "__main__":
    main()
