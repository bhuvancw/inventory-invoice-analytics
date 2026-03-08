import joblib
import pandas as pd
model_path = r'C:\Users\bhuvancw\OneDrive\Desktop\Data Science Projects\Machine Learning\Vendor Invoice ML Project\invoice_flagging\models\predict_flag_invoice.pkl'

def load_model(model_path: str = model_path):
    """Load trained classifier model."""

    with open(model_path, 'rb') as f:
        model = joblib.load(f)

    return model

def predict_invoice_flag(input_data):
    """predict freight cost for new vendor invoices.
    
    parameters
    ----------
    input_data : dict
    
    Returns
    -------
    pd.DataFrame with predicted freight cost
    """
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Flag'] = model.predict(input_df).round()
    return input_df

if __name__ == '__main__':

    # Example inference run(local testing)
    sample_data = {
    "invoice_quantity": [100, 50, 30, 10],
    "invoice_dollars": [18500, 9000, 3000, 200],
    "freight": [400, 200, 120, 15],
    "total_item_quantity": [100, 50, 30, 10],
    "total_item_dollars": [18500, 9000, 3000, 200]
    }
    prediction = predict_invoice_flag(sample_data)
    print(prediction)

