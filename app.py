from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple food items (you can edit this list)
FOOD_ITEMS = [
    {"id": 1, "name": "Masala Dosa", "price": 80},
    {"id": 2, "name": "Veg Biryani", "price": 150},
    {"id": 3, "name": "Chicken Biryani", "price": 200},
    {"id": 4, "name": "Paneer Butter Masala", "price": 180},
]

# Cart will be stored in memory for demo
cart = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/menu")
def menu():
    return render_template("menu.html", items=FOOD_ITEMS)


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    item_id = int(request.form.get("item_id"))
    # Find item by id
    for item in FOOD_ITEMS:
        if item["id"] == item_id:
            cart.append(item)
            break
    return redirect(url_for("cart_page"))


@app.route("/cart")
def cart_page():
    total = sum(item["price"] for item in cart)
    return render_template("cart.html", cart=cart, total=total)


if __name__ == "__main__":
    app.run(debug=True)
