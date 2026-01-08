import math
from datetime import date

# Enable arrow-key history
try:
    import readline
except ImportError:
    readline = None

# ---------------- SAFE MATH ENV ----------------
SAFE_ENV = {
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "log": math.log10,
    "ln": math.log,
    "sqrt": math.sqrt,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
    "round": round
}

# ---------------- AGE CALCULATOR ----------------
def calculate_age():
    try:
        print("📅 Age Calculator")
        y = int(input("Birth year: "))
        m = int(input("Birth month: "))
        d = int(input("Birth day: "))
        birth = date(y, m, d)
        today = date.today()

        years = today.year - birth.year
        months = today.month - birth.month
        days = today.day - birth.day

        if days < 0:
            months -= 1
            days += 30
        if months < 0:
            years -= 1
            months += 12

        print(f"🎂 Age: {years} years, {months} months, {days} days\n")
    except:
        print("❌ Invalid date\n")

# ---------------- BMI CALCULATOR ----------------
def calculate_bmi():
    try:
        w = float(input("Weight (kg): "))
        h = float(input("Height (m): "))
        bmi = w / (h ** 2)
        category = (
            "Underweight" if bmi < 18.5 else
            "Normal" if bmi < 25 else
            "Overweight" if bmi < 30 else
            "Obese"
        )
        print(f"📊 BMI: {round(bmi,2)} ({category})\n")
    except:
        print("❌ Invalid input\n")

# ---------------- NUMBER SYSTEM ----------------
def number_system_converter():
    try:
        n = input("Enter number: ")
        base = int(input("Base (2/8/10/16): "))
        dec = int(n, base)
        print(f"Binary: {bin(dec)}")
        print(f"Octal: {oct(dec)}")
        print(f"Decimal: {dec}")
        print(f"Hex: {hex(dec)}\n")
    except:
        print("❌ Invalid number/base\n")

# ---------------- CURRENCY CONVERTER ----------------
def currency_converter():
    rates = {
        "USD": 1,
        "INR": 83,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 150
    }
    try:
        amt = float(input("Amount: "))
        frm = input("From (USD/INR/EUR/GBP/JPY): ").upper()
        to = input("To (USD/INR/EUR/GBP/JPY): ").upper()
        result = (amt / rates[frm]) * rates[to]
        print(f"💱 Converted Amount: {round(result,2)} {to}\n")
    except:
        print("❌ Invalid currency\n")

# ---------------- COMPOUND INTEREST ----------------
def compound_interest():
    try:
        p = float(input("Principal: "))
        r = float(input("Rate (%): "))
        t = float(input("Time (years): "))
        n = int(input("Compounds per year: "))
        amount = p * (1 + r / (100 * n)) ** (n * t)
        print(f"💰 Final Amount: {round(amount,2)}")
        print(f"📈 Interest: {round(amount-p,2)}\n")
    except:
        print("❌ Invalid input\n")

# ---------------- UNIT CONVERTER ----------------
def unit_converter():
    print("""
Units:
1. Length (m ↔ km ↔ cm)
2. Weight (kg ↔ g ↔ lb)
3. Temperature (C ↔ F)
""")
    try:
        ch = int(input("Choose: "))
        if ch == 1:
            m = float(input("Meters: "))
            print(f"km: {m/1000}, cm: {m*100}\n")
        elif ch == 2:
            kg = float(input("Kilograms: "))
            print(f"grams: {kg*1000}, pounds: {kg*2.205}\n")
        elif ch == 3:
            c = float(input("Celsius: "))
            print(f"Fahrenheit: {(c*9/5)+32}\n")
        else:
            print("❌ Invalid choice\n")
    except:
        print("❌ Invalid input\n")

# ---------------- MAIN CALCULATOR ----------------
def homura_expression_calculator():
    history = []

    print("🔥 HOMURA ALL-IN-ONE CALCULATOR 🔥")
    print("""
Commands:
 history   clear   exit
 age       bmi
 number    currency
 interest  unit

Tips:
 ↑ / ↓ → recall expressions
 ^ → power operator
""")

    while True:
        try:
            expr = input(">>> ").strip()
        except:
            break

        if not expr:
            continue

        cmd = expr.lower()

        if cmd == "exit":
            print("👋 Goodbye")
            break
        if cmd == "history":
            print("\n".join(history) if history else "📭 No history\n")
            continue
        if cmd == "clear":
            history.clear()
            if readline:
                readline.clear_history()
            print("🧹 Cleared\n")
            continue
        if cmd == "age":
            calculate_age(); continue
        if cmd == "bmi":
            calculate_bmi(); continue
        if cmd == "number":
            number_system_converter(); continue
        if cmd == "currency":
            currency_converter(); continue
        if cmd == "interest":
            compound_interest(); continue
        if cmd == "unit":
            unit_converter(); continue

        try:
            expr_eval = expr.replace("^", "**")
            res = eval(expr_eval, {"__builtins__": None}, SAFE_ENV)
            history.append(f"{expr} = {res}")
            if readline:
                readline.add_history(expr)
            print(f"✅ Result: {res}\n")
        except:
            print("❌ Invalid expression\n")


if __name__ == "__main__":
    homura_expression_calculator()
