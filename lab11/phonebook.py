import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    dbname='Phonebook',
    user='postgres',
    password='postgres',
)

def get_records_by_pattern(pattern):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", ('%'+pattern+'%', '%'+pattern+'%'))
    rows = cur.fetchall()
    cur.close()
    return rows

def add_user(name, phone):
    cur = conn.cursor()
    cur.callproc('add_user', (name, phone))
    conn.commit()
    cur.close()

def add_many_users(users):
    cur = conn.cursor()
    cur.callproc('add_many_users', (users,))
    conn.commit()
    cur.close()

def get_records_with_pagination(limit, offset):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook ORDER BY name LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    cur.close()
    return rows

def delete_user(pattern):
    cur = conn.cursor()
    cur.callproc('delete_user', (pattern,))
    conn.commit()
    cur.close()

while True:
    print("Phonebook Program")
    print("1. Add Entry")
    print("2. Search Entry")
    print("3. Display Entries")
    print("4. Update Entry")
    print("5. Upload CSV File")
    print("6. Quit")
    print("7. Delete Entry")
    print("8. Search Records by Pattern")
    print("9. Add User")
    print("10. Add Many Users")
    print("11. Get Records with Pagination")
    print("12. Delete User")

    choice = input("Enter your choice (1-12): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_entry(name, phone)
    elif choice == '2':
        name = input("Enter name to search: ")
        rows = search_entry(name)
        for row in rows:
            print(row)
    elif choice == '3':
        display_entries()
    elif choice == '4':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        update_user(name, phone)
    elif choice == '5':
        filename = input("Enter CSV filename: ")
        upload_csv(filename)
    elif choice == '6':
        break
    elif choice == '7':
        pattern = input("Enter pattern of Entry, that you want to delete: ")
        delete_entry(pattern)
    elif choice == '8':
        pattern = input("Enter pattern: ")
        rows = get_records_by_pattern(pattern)
        for row in rows:
            print(row)
    elif choice == '9':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        add_user(name, phone)
    elif choice == '10':
        users = []
        while True:
            name = input("Enter name (or 'done' to exit): ")
            if name == 'done':
                break
            phone = input("Enter phone: ")
            users.append((name, phone))
        add_many_users(users)
    elif choice == '11':
        limit = input("Enter limit: ")
        offset = input("Enter offset: ")
        rows = get_records_with_pagination(limit, offset)
        for row in rows:
            print(row)
    elif choice == '12':
        pattern = input("Enter pattern: ")
        delete_user(pattern)