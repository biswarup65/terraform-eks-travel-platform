from flask import Flask, render_template, request, Response

from prometheus_client import Counter
from prometheus_client import generate_latest
from prometheus_client import CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total HTTP Request Count'
)

destinations = [

    {
        "name": "Goa",
        "price": "₹12,000",
        "description": "Experience beaches, nightlife, and luxury resorts.",
        "image": "goa.jpg"
    },

    {
        "name": "Manali",
        "price": "₹18,000",
        "description": "Snow mountains, adventure sports, and scenic beauty.",
        "image": "manali.jpg"
    },

    {
        "name": "Kerala",
        "price": "₹22,000",
        "description": "Backwaters, greenery, and peaceful vacations.",
        "image": "kerala.jpg"
    },

    {
        "name": "Rajasthan",
        "price": "₹25,000",
        "description": "Royal palaces, desert safaris, and cultural heritage.",
        "image": "rajasthan.jpg"
    },

    {
        "name": "Kashmir",
        "price": "₹30,000",
        "description": "Snowy valleys, lakes, and breathtaking mountain views.",
        "image": "kashmir.jpg"
    },

    {
        "name": "Andaman",
        "price": "₹35,000",
        "description": "Crystal clear beaches and exotic island experiences.",
        "image": "andaman.jpg"
    },

    {
        "name": "Darjeeling",
        "price": "₹16,000",
        "description": "Tea gardens, toy train rides, and Himalayan beauty.",
        "image": "darjeeling.jpg"
    },

    {
        "name": "Sikkim",
        "price": "₹24,000",
        "description": "Peaceful monasteries and scenic mountain landscapes.",
        "image": "sikkim.jpg"
    }

]

# Count every request
@app.before_request
def before_request():
    REQUEST_COUNT.inc()


@app.route("/")
def home():
    return render_template("index.html", destinations=destinations)


@app.route("/destinations")
def destination_page():
    return render_template("destinations.html", destinations=destinations)


@app.route("/booking", methods=["GET", "POST"])
def booking():

    success_message = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        destination = request.form.get("destination")

        success_message = (
            f"Booking confirmed for {name} to {destination}"
        )

    return render_template(
        "booking.html",
        success_message=success_message,
        destinations=destinations
    )


# Prometheus metrics endpoint
@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)