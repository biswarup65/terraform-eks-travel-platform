from flask import Flask, render_template, request

app = Flask(__name__)

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


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)