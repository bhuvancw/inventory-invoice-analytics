import sqlite3
import pandas as pd

conn = sqlite3.connect(r'C:\Users\bhuvancw\OneDrive\Desktop\Data Science Projects\Machine Learning\Vendor Invoice ML Project\data\inventory.db')
cursor = conn.cursor()

# Check tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print('Tables in database:')
for table in tables:
    print(f'  - {table[0]}')

# Check columns in vendor_invoice table
cursor.execute("PRAGMA table_info(vendor_invoice)")
columns = cursor.fetchall()
print('\nColumns in vendor_invoice table:')
for col in columns:
    print(f'  - {col[1]}')

conn.close()
