from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data contoh buah-buahan (diimplementasikan sebagai list of dictionaries)
fruits = [
    {"id": 1, "name": "Apple", "quantity": 10},
    {"id": 2, "name": "Banana", "quantity": 15},
    {"id": 3, "name": "Orange", "quantity": 20}
]

# Route untuk halaman utama (Read)
@app.route('/')
def index():
    return render_template('index.html', fruits=fruits)

# Route untuk halaman tambah buah (Create)
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        fruit = {"id": len(fruits) + 1, "name": name, "quantity": quantity}
        fruits.append(fruit)
        return redirect(url_for('index'))
    return render_template('add.html')

# Route untuk halaman edit buah (Update)
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    fruit = [f for f in fruits if f['id'] == id][0]
    if request.method == 'POST':
        fruit['name'] = request.form['name']
        fruit['quantity'] = int(request.form['quantity'])
        return redirect(url_for('index'))
    return render_template('edit.html', fruit=fruit)

# Route untuk menghapus buah (Delete)
@app.route('/delete/<int:id>')
def delete(id):
    fruit = [f for f in fruits if f['id'] == id][0]
    fruits.remove(fruit)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
