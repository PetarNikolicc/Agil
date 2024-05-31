import sqlite3

def remove_text_from_instructions():
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    # Hämta alla rader i tabellen recipes
    cursor.execute("SELECT id, instructions FROM recipes")
    rows = cursor.fetchall()

    # Uppdatera instruktionerna för varje rad
    for row in rows:
        id, instructions = row
        new_instructions = instructions.replace("Gör så här:", "").strip()
        cursor.execute("UPDATE recipes SET instructions = ? WHERE id = ?", (new_instructions, id))

    # Spara ändringarna och stäng anslutningen
    conn.commit()
    conn.close()

    print("Instruktionerna har uppdaterats i databasen.")

if __name__ == '__main__':
    remove_text_from_instructions()
