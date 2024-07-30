# app.py

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    # Fetch products from the database
    return render_template('products.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Fetch product details from the database
    return render_template('product_detail.html', product=product)

@app.route('/cart')
def cart():
    # Fetch cart items from the session or database
    return render_template('cart.html', cart=cart_items)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Process checkout
        return jsonify({'message': 'Order placed successfully'})
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
