import json
import sys
import os
from datetime import datetime

FILENAME = "transactions.json"
FILENAME2 = "categories.json"
VALID_TYPE = ["thu", "chi"]

def load_tasks(file):
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return json.load(f)

def save_tasks(tasks, file):
    with open(file, "w") as f:
        return json.dump(tasks, f, indent=2)
    
def add_transaction(date, _type, amount, category, description, transactions):
    transaction = {
        "id" : len(transactions) + 1,
        "date" : date,
        "type" : _type,
        "amount" : amount,
        "category" : category,
        "description" : description
    }
    transactions.append(transaction)
    save_tasks(transactions, FILENAME)
    print(f'Added transaction #{transaction["id"]}')

def add_category(description, _type, categories):
    category = {
        "desc" : description,
        "type" : _type
    }
    categories.append(category)
    save_tasks(categories, FILENAME2)
    print(f'Added categories #{category["desc"]}')

def show_history(transactions, month=None, year=None):
    if len(transactions) == 0:
        print("There is no transaction")
        return
    else:
        cnt = 0
        if month is None and year is None:
            for transaction in transactions:
                print(f'#{transaction["id"]}: {transaction["description"]}, {transaction["amount"]}, {transaction["category"]}, {transaction["type"]}, {transaction["date"]}')
                cnt += 1
                if cnt >= 10:
                    return
        else:
            for transaction in transactions:
                date_obj = datetime.strptime(transaction["date"], "%d/%m/%Y")
                transaction_month = date_obj.month
                transaction_year = date_obj.year
                if transaction_month == month and transaction_year == year:
                    print(f'#{transaction["id"]}: {transaction["description"]}, {transaction["amount"]}, {transaction["category"]}, {transaction["type"]}, {transaction["date"]}')
                    cnt += 1
                    if cnt >= 10:
                        return
                    
def month_stats(transactions, month, year):
    # Lấy thánh trước
    prev_month = month
    prev_year = year
    if month == 1:
        prev_month = 12
        prev_year -= 1
    else:
        prev_month -= 1
    # Lọc ra tháng hiện tại
    transactions_this_month = [transaction for transaction in transactions 
                                if datetime.strptime(transaction["date"], "%d/%m/%Y").month == month
                                and datetime.strptime(transaction["date"], "%d/%m/%Y").year == year]
    if not transactions_this_month:
        print("Không có dữ liệu tháng này")

    # Lọc ra tháng trước đó
    transactions_prev_month = [transaction for transaction in transactions 
                                if datetime.strptime(transaction["date"], "%d/%m/%Y").month == prev_month
                                and datetime.strptime(transaction["date"], "%d/%m/%Y").year == prev_year]
    if not transactions_prev_month:
        print("Không có dữ liệu tháng trước")

    # Số dư của tháng này
    total_income_this_month = sum([transaction["amount"] for transaction in transactions_this_month
                               if transaction["type"] == "thu"])
    total_expense_this_month = sum([transaction["amount"] for transaction in transactions_this_month
                               if transaction["type"] == "chi"])
    balance_this_month = total_income_this_month - total_expense_this_month
    
    # Số dư của tháng trước
    total_income_prev_month = sum([transaction["amount"] for transaction in transactions_prev_month
                               if transaction["type"] == "thu"])
    total_expense_prev_month = sum([transaction["amount"] for transaction in transactions_prev_month
                               if transaction["type"] == "chi"])
    balance_prev_month = total_income_prev_month - total_expense_prev_month
    
    return {
        "this_month": {
            "total_income": total_income_this_month,
            "total_expense": total_expense_this_month,
            "balance": balance_this_month,
            "transaction_count": len(transactions_this_month)
        },
        "prev_month": {
            "total_income": total_income_prev_month,
            "total_expense": total_expense_prev_month,
            "balance": balance_prev_month,
            "transaction_count": len(transactions_prev_month)
        }
    }

def category_stats(transactions, month, year):
    expenses = [
    transaction for transaction in transactions
    if datetime.strptime(transaction["date"], "%d/%m/%Y").month == month
    and datetime.strptime(transaction["date"], "%d/%m/%Y").year == year
    and transaction["type"] == "chi"]
    
    total_expenses = sum(transaction["amount"] for transaction in expenses)
    
    category_summary = {}
    for transaction in expenses:
        cat = transaction["category"]
        category_summary[cat] = category_summary.get(cat, 0) + transaction["amount"]
    
    if total_expenses == 0:
        print("Không có chi tiêu cho tháng này")
        return
    
    for cat, amount in category_summary.items():
        percent = (amount / total_expenses) * 100
        print(f'- {cat}: {amount} ({percent:.2f}%)')
    
def calculate_balance(transactions):
    income = [transaction for transaction in transactions if transaction['type'] == 'thu']
    expense = [transaction for transaction in transactions if transaction['type'] == 'chi']
    
    total_income = sum([transaction['amount'] for transaction in income])   
    total_expense = sum([transaction['amount'] for transaction in expense])   
    balance = total_income - total_expense
    
    return {
        "total_balance" : {
            "total_income" : total_income,
            "total_expense" : total_expense,
            "balance" : balance
        }
    }
    
# Kiểm tra ngày hợp lệ
def validate_date(date_str):
    try:
        if len(date_str.strip()) != 10: # 01/01/0001
            return False
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except:
        return False

# Kiểm tra số tiền
def validate_amount(amount):
    try:
        return amount > 0
    except:
        return False

    
def Menu():    
    
    transactions = load_tasks(FILENAME)
    print(" ========== QUẢN LÝ CHI TIÊU ========== ")    
    while True:
        print("1. Nhập dữ liệu giao dịch")
        print("2. Hiển thị lịch sử giao dịch")
        print("3. Thống kê theo tháng")
        print("4. Thống kê theo danh mục")
        print("5. Kiểm tra số dư còn lại")
        print("6. Báo cáo nâng cao")
        print("7. Thoát")
        print(" ========== QUẢN LÝ CHI TIÊU ========== ")    

        option = int(input("Chọn: "))

        if option == 1:
            date = input("Nhập ngày tháng năm(dd/mm/yyyy): ")
            _type = input("Nhập loại(thu/chi): ")
            amount = int(input("Nhập số tiền: "))
            category = input("Nhập danh mục: ")
            description = input("Nhập mô tả: ")
            check = 1
            if(validate_date(date) == False):
                print("[Error]: Format ngày tháng sai hoặc không hợp lệ")
                check = 0
            if(validate_amount(amount) == False):
                print("[Error]: Số tiền phải lớn hơn 0")
                check = 0
            
            if(check): 
                add_transaction(date, _type, amount, category, description, transactions)
        elif option == 2:
            month = input("Nhập tháng (có thể để trống): ")
            year = input("Nhập năm (có thể để trống): ")
            show_history(transactions, month, year)
        elif option == 3:
            month = input("Nhập tháng: ")
            year = input("Nhập năm: ")
            month_stats(transactions, month, year)
        elif option == 4:
            month = input("Nhập tháng: ")
            year = input("Nhập năm: ")
            list =category_stats(transactions, month, year)
            print(list)
        elif option == 5:
            list = calculate_balance(transactions)
            print(list)
        # elif option == 6:
            
        elif option == 7:
            break
        else:
            print("Lựa chọn không hợp lệ.")


def main():
    Menu()
    
if __name__ == "__main__":
    main()