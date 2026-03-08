import joblib
from pathlib import Path

from data_preprocessing import load_vendor_invoice_data, prepare_features, split_data

from model_evaluation import (
    train_linear_regression,
    train_decision_tree,
    train_random_forest,
    evaluate_model
)

def main():
    db_path = Path(r"C:\Users\bhuvancw\OneDrive\Desktop\Data Science Projects\Machine Learning\Vendor Invoice ML Project\data\inventory.db")            # relative path under project
    db_path.parent.mkdir(parents=True, exist_ok=True)  # make sure "data" folder exists

    model_dir = Path("models")
    model_dir.mkdir(exist_ok=True)

    #Load data (sqlite will create an empty file if it doesn't exist)
    df = load_vendor_invoice_data(str(db_path))

    #Prepare data
    X, y = prepare_features(df)
    # train_test_split returns X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = split_data(X, y)

    #Train models
    lr_model = train_linear_regression(X_train, y_train)
    df_model = train_decision_tree(X_train, y_train)
    rf_model = train_random_forest(X_train, y_train)

    #Evaluate models
    results = []
    results.append(evaluate_model(lr_model, X_test, y_test, 'Linear Regression'))
    results.append(evaluate_model(df_model, X_test, y_test, 'Decision Tree Regression'))
    results.append(evaluate_model(rf_model, X_test, y_test, 'Random Forest Regression'))

    #Select best model
    best_model_info = min(results, key = lambda x: x['mae'])
    best_model_name = best_model_info['model_name']

    best_model = {
        "Linear Regression":lr_model,
        "Decision Tree Regression":df_model,
        "Random Forest Regression":rf_model
        }[best_model_name]

    # Save best model
    model_path = model_dir/"predict_freight_model.pkl"
    joblib.dump(best_model, model_path)

    print(f"\nBest model saved : {best_model_name}")
    print(f"Model path : {model_path}")

if __name__ == "__main__":
    main()




