import sqlite3

# Anslut till SQLite-databasen
conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

# Lista med recept-ID och deras nya bildvägar
recipes_to_update = [
    {"id": 9, "image_path": "/static/images/Pulled_Pork.png"},
    {"id": 10, "image_path": "/static/images/Chili_con_Carne.png"}
]

# Uppdatera bildvägarna i databasen
for recipe in recipes_to_update:
    cursor.execute("""
        UPDATE recipes 
        SET image_path = ? 
        WHERE id = ?
    """, (recipe["image_path"], recipe["id"]))

# Spara ändringarna och stäng anslutningen
conn.commit()
conn.close()

print("Bildvägar har uppdaterats i databasen.")



