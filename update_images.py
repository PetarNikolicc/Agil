import sqlite3

# Anslut till SQLite-databasen
conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

# Hämta alla rader i tabellen
cursor.execute("SELECT id, instructions FROM recipes")
rows = cursor.fetchall()

# Uppdatera instruktionerna för varje rad
for row in rows:
    recipe_id = row[0]
    instructions = row[1]
    if not instructions.startswith("Gör så här:"):
        updated_instructions = "Gör så här: " + instructions
        cursor.execute("""
            UPDATE recipes 
            SET instructions = ? 
            WHERE id = ?
        """, (updated_instructions, recipe_id))

# Spara ändringarna och stäng anslutningen
conn.commit()
conn.close()

print("Instruktionerna har uppdaterats i databasen.")
