from mapper import Database
import sqlite3    
from pprint import pprint

def all_bills():
    keys=["bill_id","total_due","due_by", "due_to", "created_on", "caption"]
    with Database() as db:
        db.cursor.execute('''SELECT * FROM bills
                                ORDER BY created_on DESC;''')
        all_bills = db.cursor.fetchall()
        bills = [dict(zip(keys,i)) for i in all_bills]
        print (bills)
        return bills

def all_payments():
    keys=["payment_id", "amount_paid", "paid_by", "paid_to", "created_on", "note"]
    with Database() as db:
        db.cursor.execute('''SELECT * FROM payments 
                                ORDER BY created_on DESC;''')
        all_payments = db.cursor.fetchall()
        payments = [dict(zip(keys, i)) for i in all_payments]
        print (payments)
        return payments

all_bills()
all_payments()