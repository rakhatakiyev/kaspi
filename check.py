from flask import Flask, render_template

app = Flask(__name__)

# Примерные данные о заказах
orders = [
    {
        "order_id": "376617118",
        "customer_name": "Зенебе",
        "items": [
            {
                "item_name": "Мягкая игрушка Гусь обнимусь",
                "price": 1500,
                "quantity": 1,
                "cost": 1000,  # Себестоимость товара
                "discount": 0
            }
        ],
        "shipping_cost": 200,
        "commission": 150
    },
    {
        "order_id": "376617119",
        "customer_name": "Айжан",
        "items": [
            {
                "item_name": "Рюкзак спортивный",
                "price": 1200,
                "quantity": 2,
                "cost": 800,  # Себестоимость товара
                "discount": 100
            }
        ],
        "shipping_cost": 150,
        "commission": 120
    }
]

# Функция для расчёта чистого дохода и маржинального дохода
def calculate_net_profit_and_margin(orders):
    total_revenue = 0
    total_cost = 0
    total_shipping_cost = 0
    total_commission = 0

    for order in orders:
        for item in order.get("items", []):
            price = item.get("price", 0)
            quantity = item.get("quantity", 0)
            cost = item.get("cost", 0)
            discount = item.get("discount", 0)
            shipping_cost = order.get("shipping_cost", 0)
            commission = order.get("commission", 0)

            revenue = (price * quantity) - discount
            total_revenue += revenue
            total_cost += (cost * quantity)
            total_shipping_cost += shipping_cost
            total_commission += commission

    # Маржинальный доход = Выручка - Себестоимость
    gross_profit = total_revenue - total_cost
    net_profit = total_revenue - (total_shipping_cost + total_commission)
    return net_profit, gross_profit, total_revenue, total_shipping_cost, total_commission

@app.route('/')
def index():
    # Пересчитываем чистый доход и маржинальный доход
    net_profit, gross_profit, total_revenue, total_shipping_cost, total_commission = calculate_net_profit_and_margin(orders)

    return render_template('index.html', net_profit=net_profit, gross_profit=gross_profit, total_revenue=total_revenue,
                           total_shipping_cost=total_shipping_cost, total_commission=total_commission,
                           orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
