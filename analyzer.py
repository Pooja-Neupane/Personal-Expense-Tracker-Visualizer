import matplotlib.pyplot as plt

# Sample Expense Data
expenses = {
    'Rent': 12000,
    'Groceries': 4500,
    'Utilities': 2500,
    'Transport': 1500,
    'Entertainment': 2000,
    'Savings': 3000
}

# Extracting data
categories = list(expenses.keys())
amounts = list(expenses.values())

# ---- PIE CHART: Category-Wise Expense Distribution ----
plt.figure(figsize=(7, 7))
plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('📊 Monthly Expense Distribution')
plt.axis('equal')
plt.show()

# ---- BAR CHART: Expense Comparison ----
plt.figure(figsize=(9, 5))
plt.bar(categories, amounts, color='skyblue')
plt.title('💰 Monthly Expense Comparison')
plt.xlabel('Categories')
plt.ylabel('Amount (in Rs)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
