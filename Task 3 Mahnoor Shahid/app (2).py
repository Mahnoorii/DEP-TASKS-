import mysql.connector  # Import for MySQL connection

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost", 
        user="Mahnoor", 
        password="123",  
        database="task_03"  
    )
    return conn

@app.route('/products')
def products():
    conn = get_db_connection()
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('SELECT * FROM products')  
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('products.html', products=products)