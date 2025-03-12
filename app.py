from flask import Flask, render_template, request

app = Flask(__name__)

def get_zodiac_sign(day, month):
    zodiac_signs = [
        ("Capricorn", (12, 22), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21))
    ]
    
    for sign, start, end in zodiac_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return None

def zodiac_traits(sign):
    traits = {
        "Aries": "Courageous, determined, confident, enthusiastic, optimistic, honest.",
        "Taurus": "Reliable, patient, practical, devoted, responsible, stable.",
        "Gemini": "Gentle, affectionate, curious, adaptable, quick learner.",
        "Cancer": "Tenacious, highly imaginative, loyal, emotional, sympathetic.",
        "Leo": "Creative, passionate, generous, warm-hearted, cheerful.",
        "Virgo": "Loyal, analytical, kind, hardworking, practical.",
        "Libra": "Cooperative, diplomatic, gracious, fair-minded, social.",
        "Scorpio": "Resourceful, brave, passionate, stubborn, determined.",
        "Sagittarius": "Generous, idealistic, great sense of humor.",
        "Capricorn": "Responsible, disciplined, self-control, good managers.",
        "Aquarius": "Progressive, original, independent, humanitarian.",
        "Pisces": "Compassionate, artistic, intuitive, gentle, wise, musical."
    }
    return traits.get(sign, "Unknown")

def zodiac_compatibility(sign):
    compatibility = {
        "Aries": "Best with Leo, Sagittarius, Gemini, Aquarius.",
        "Taurus": "Best with Virgo, Capricorn, Cancer, Pisces.",
        "Gemini": "Best with Libra, Aquarius, Aries, Leo.",
        "Cancer": "Best with Scorpio, Pisces, Taurus, Virgo.",
        "Leo": "Best with Aries, Sagittarius, Gemini, Libra.",
        "Virgo": "Best with Taurus, Capricorn, Cancer, Scorpio.",
        "Libra": "Best with Gemini, Aquarius, Leo, Sagittarius.",
        "Scorpio": "Best with Cancer, Pisces, Virgo, Capricorn.",
        "Sagittarius": "Best with Aries, Leo, Libra, Aquarius.",
        "Capricorn": "Best with Taurus, Virgo, Scorpio, Pisces.",
        "Aquarius": "Best with Gemini, Libra, Aries, Sagittarius.",
        "Pisces": "Best with Cancer, Scorpio, Taurus, Capricorn."
    }
    return compatibility.get(sign, "Unknown")

def zodiac_lucky_info(sign):
    lucky_info = {
        "Aries": ("Red", "Tuesday"),
        "Taurus": ("Green", "Friday"),
        "Gemini": ("Yellow", "Wednesday"),
        "Cancer": ("White", "Monday"),
        "Leo": ("Gold", "Sunday"),
        "Virgo": ("Blue", "Wednesday"),
        "Libra": ("Pink", "Friday"),
        "Scorpio": ("Black", "Tuesday"),
        "Sagittarius": ("Purple", "Thursday"),
        "Capricorn": ("Brown", "Saturday"),
        "Aquarius": ("Blue", "Saturday"),
        "Pisces": ("Sea Green", "Thursday")
    }
    return lucky_info.get(sign, ("Unknown", "Unknown"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        name = request.form["name"]
        dob = request.form["dob"]
        try:
            day, month, year = map(int, dob.split('-'))
            zodiac_sign = get_zodiac_sign(day, month)
            if zodiac_sign:
                color, lucky_day = zodiac_lucky_info(zodiac_sign)
                result = {
                    "name": name,
                    "sign": zodiac_sign,
                    "traits": zodiac_traits(zodiac_sign),
                    "compatibility": zodiac_compatibility(zodiac_sign),
                    "lucky_color": color,
                    "lucky_day": lucky_day
                }
        except ValueError:
            result = {"error": "Invalid date format! Use DD-MM-YYYY."}
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
