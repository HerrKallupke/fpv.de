import psycopg2 as db


connection = db.connect(host='127.0.0.1', port=5678, database='postgres', user='postgres', password='test')
cursor = connection.cursor()

def set_table(name, data):
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {name}(url VARCHAR(255), title VARCHAR(255), image VARCHAR(255), price FLOAT)')

    try:
        cursor.execute(f'TRUNCATE TABLE {name}')

        for row in data:
            cursor.execute(f"INSERT INTO {name} (url, title, image, price) VALUES ('{row[0]}', '{row[1]}', '{row[2]}', {row[3]})")

        connection.commit()
        print(f'Products in {name} updated!')
    except (Exception, db.DatabaseError) as error:
        print(f'Error: {error}')
        connection.rollback()