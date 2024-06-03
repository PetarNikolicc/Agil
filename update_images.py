import sqlite3

# Anslut till SQLite-databasen
conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

# Specifika värden att uppdatera
recipe_name = "Rostad kyckling"
new_instructions = """1. Förvärm ugnen till 200°C.
2. Skölj kycklingen både inuti och utanför och torka den torr med papper.
3. Placera kycklingen i en ugnsform.
4. Gnid in kycklingen med olivolja. Strö salt, peppar, paprikapulver, timjan och rosmarin över kycklingen. Placera citronhalvorna och krossade vitlöksklyftor inuti kycklingen.
5. Lägg morötter, lökar och potatis runt kycklingen i ugnsformen. Ringla lite olivolja över grönsakerna och krydda med salt och peppar.
6. Placera ugnsformen i ugnen och rosta kycklingen i cirka 60 minuter, eller tills kycklingen är genomstekt och saften är klar när du sticker en kniv i tjockaste delen av låret (innertemperaturen ska vara minst 75°C). Om kycklingen börjar bli för mörk innan den är genomstekt, täck den löst med aluminiumfolie.
7. Ta ut kycklingen från ugnen och låt den vila i cirka 10 minuter innan du skär upp den.
8. Servera kycklingen med de rostade grönsakerna."""

new_ingredients = """1 hel kyckling (ca 1,5 kg)
2 msk olivolja
1 citron, skuren i halvor
4 vitlöksklyftor, skalade och krossade
2 tsk salt
1 tsk svartpeppar
1 tsk paprikapulver
1 tsk torkad timjan
1 tsk torkad rosmarin
4 morötter, skurna i stora bitar
2 lökar, skurna i klyftor
4 potatisar, skurna i klyftor"""

# Kör en SQL-uppdatering
cursor.execute("""
    UPDATE recipes 
    SET instructions = ?, ingredients = ? 
    WHERE name = ?
""", (new_instructions, new_ingredients, recipe_name))

# Spara ändringarna och stäng anslutningen
conn.commit()
conn.close()

print(f"Instruktioner och ingredienser har uppdaterats för {recipe_name}.")
