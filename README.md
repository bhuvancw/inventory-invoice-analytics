<<<<<<< HEAD
# Vendor Invoice Intelligence System
**Freight Cost Prediction & Invoice Risk Flagging**

## 📌 Table of Contents
- <a href="#project-overview">Project Overview</a>
- <a href="#business-objective">Business Objectives</a>
- <a href="#data-sources">Data Sources</a>
- <a href='#eda'>Exploratory Data Analysis</a>
- <a href="#models-used">Models Used</a>
- <a href="#metrics">Evaluation Metrics</a>
- <a href="#application">Application</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#author--contact">Author & Contact</a>
---

<h2><a class='anchor' id='project-overview'></a>📌 Project Overview</h2>

This project implements an **end-to-end machine learning system** designed to support finance teams by:

1. **Predicting expected freight cost** for vendor invoices.
2. **Flaggin high-risk invoices** that require manual review due to adnormal cost, freight, or operational
patterns.

---

<h2>🎯 Business Objectives</h2>

<h3>1. 🚚 Freight Cost Prediction (Regression)</h3>

<p><strong>Objective:</strong></p>
<p>
Predict the expected freight cost for a vendor invoice using quantity,
invoice value, and historical behavior.
</p>

<p><strong>Why it matters:</strong></p>

<ul>
<li>Freight is a non-trivial component of landed cost.</li>
<li>Poor freight estimation impacts margin analysis and budgeting.</li>
<li>Early prediction improves procurement planning and vendor negotiation.</li>
</ul>

<h3>2. 🚩 Invoice Risk Flagging (Classification)</h3>

<p><strong>Objective:</strong></p>
<p>
Predict whether a vendor invoice should be flagged for manual approval due to abnormal
cost, freight, or delivery patterns.
</p>

<p><strong>Why it matters:</strong></p>

<ul>
<li>Manual invoice review does not scale.</li>
<li>Financial leakage often occurs in large or complex invoices.</li>
<li>Early risk detection improves audit efficiency and operational control.</li>
</ul>

<h2>📂 Data Sources</h2>

<p>
Data is stored in a relational SQLite database (<code>inventory.db</code>) with the following tables:
</p>

<ul>
<li><code>vendor_invoice</code> — Invoice-level financial and timing data</li>
<li><code>purchases</code> — Item-level purchase details</li>
<li><code>purchase_prices</code> — Reference purchase prices</li>
<li><code>begin_inventory</code>, <code>end_inventory</code> — Inventory snapshots</li>
</ul>

<p>
SQL aggregation is used to generate invoice-level features.
</p>

<hr>

<h2>📊 Exploratory Data Analysis (EDA)</h2>

<p>
EDA focuses on <strong>business-driven questions</strong>, such as:
</p>

<ul>
<li>Do flagged invoices have higher financial exposure?</li>
<li>Does freight scale linearly with quantity?</li>
<li>Does freight cost depend on quantity?</li>
</ul>

<p>
Statistical tests (<code>t-tests</code>) are used to confirm that flagged invoices differ meaningfully from normal invoices.
</p>

<hr>

<h2>🤖 Models Used</h2>

<h3>Regression (Freight Prediction)</h3>

<ul>
<li>Linear Regression (baseline)</li>
<li>Decision Tree Regressor</li>
<li>Random Forest Regressor (final model)</li>
</ul>

<h3>Classification (Invoice Flagging)</h3>

<ul>
<li>Logistic Regression (baseline)</li>
<li>Decision Tree Classifier</li>
<li>Random Forest Classifier (final model with GridSearchCV)</li>
</ul>

<p>
Hyperparameter tuning is performed using <strong>GridSearchCV</strong> with 
<strong>F1-score</strong> to handle class imbalance.
</p>

<hr>

<h2>📈 Evaluation Metrics</h2>

<h3>Freight Prediction</h3>

<ul>
<li>MAE</li>
<li>RMSE</li>
<li>R<sup>2</sup> Score</li>
</ul>

<h3>Invoice Flagging</h3>

<ul>
<li>Accuracy</li>
<li>Precision, Recall, F1-score</li>
<li>Classification report</li>
<li>Feature importance analysis</li>
</ul>

<hr>

<h2>🖥️ End-to-End Application</h2>

<p>
A Streamlit application demonstrates the complete pipeline:
</p>

<ul>
<li>Input invoice details</li>
<li>Predict expected freight</li>
<li>Flag invoices in real time</li>
<li>Provide human-readable explanations</li>
</ul>

<h2>📁 Project Structure</h2>

<pre>
inventory-invoice-analytics/
│
├── data/
│   └── inventory.db
│
├── freight_cost_prediction/
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   └── train.py
│
├── invoice_flagging/
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   └── train.py
│
├── inference/
│   ├── predict_freight.py
│   └── predict_invoice_flag.py
│
├── models/
│   ├── predict_freight_model.pkl
│   ├── scaler.pkl
│   └── predict_flag_invoice.pkl
│
├── notebooks/
│   ├── Invoice Flagging.ipynb
│   └── Predict Freight Cost.ipynb
│
├── app.py
├── README.md
└── .gitignore
</pre>

<hr>

<h2>⚙️ How to Run This Project</h2>

<h3>1. Clone the repository:</h3>

<pre>
git clone https://github.com/yourusername/inventory-invoice-analytics.git
</pre>

<h3>2. Train and Save Best Fit Models:</h3>

<pre>
python freight_cost_prediction/train.py
python invoice_flagging/train.py
</pre>

<h3>3. Test Models:</h3>

<pre>
python inference/predict_freight.py
python inference/predict_invoice_flag.py
</pre>

<h3>4. Open Application:</h3>

<pre>
streamlit run app.py
</pre>
=======
# inventory-invoice-analytics
>>>>>>> 383a48e393d1fea76202772695005a43eae74a5c
