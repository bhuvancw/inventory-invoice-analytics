import sqlite3

conn = sqlite3.connect(r'C:\Users\bhuvancw\OneDrive\Desktop\Data Science Projects\Machine Learning\Vendor Invoice ML Project\data\inventory.db')
cursor = conn.cursor()

# Check columns in purchases table
cursor.execute("PRAGMA table_info(purchases)")
columns = cursor.fetchall()
print('Columns in purchases table:')
for col in columns:
    print(f'  - {col[1]}')

conn.close()
