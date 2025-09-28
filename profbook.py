import time
import os
from fuzzywuzzy import process
import pandas as pd

DISCLAIMER = """
──────────────────────────────────────────────
📘 ProfBook — Professor Lookup CLI
──────────────────────────────────────────────
⚠️ DISCLAIMER:
This tool uses manually collected public data 
from RateMyProfessors for personal, educational, 
and non-commercial use only.

It is NOT affiliated with RatemyProfessor OR St.
John's University. This tool is only for educational
and research purposes!!

I AM NOT RESPONSIBLE FOR ANY PROBLEMS YOU HAVE
IN YOUR CLASSES!!!

By continuing, you agree to use this responsibly.
──────────────────────────────────────────────
"""

print(DISCLAIMER)
proceed = input("Do you agree to the disclaimer? (Y/N): ").strip().lower()

if proceed != 'y':
    print("Exiting... You must agree to continue.")
    exit()

# Clear screen
os.system("clear" if os.name == "posix" else "cls")

# 📓 ASCII Art Banner
ascii_title = r"""
O---o
 O-o
  O
 o-O
o---O
O---o
 O-o
  O
 o-O
o---O
O---o
 O-o
  O
 o-O
o---O

"""
"""
    📓  RateMyProfessor Lookup Notebook  📓
   ─────────────────────────────────────────
   🔍 Search professors by name — even with typos!
   💾 All data collected manually from public RMP pages.
   🧠 Quickly view ratings, difficulty, and “Would take again”.
   ─────────────────────────────────────────
"""

print(ascii_title)
time.sleep(1)

# Load data
df = pd.read_csv("professors.csv")
names = df["Name"].tolist()

print("✏️  Type a professor's name to search.")
print("💡  Don’t worry about spelling — I’ll find the closest match!\n")

while True:
    query = input("📘 Enter professor name (or 'exit' to quit): ").strip()
    if query.lower() in ["exit", "quit"]:
        print("\n🗒️  Closing notebook... see you next time!\n")
        break

    match = process.extractOne(query, names)
    if match:
        best = match[0]
        row = df[df["Name"] == best].iloc[0]
        print("\n────────────────────────────────────────────")
        print(f"📍 Closest match: {best}")
        print(f"⭐ Overall Rating: {row['Overall_Rating']}")
        print(f"🔁 Would Take Again: {row['Would_Take_Again']}")
        print(f"📊 Difficulty: {row['Level_of_Difficulty']}")
        print(f"🧾 Number of Ratings: {row['Num_Ratings']}")
        print("────────────────────────────────────────────\n")
    else:
        print("❌ No match found.\n")
