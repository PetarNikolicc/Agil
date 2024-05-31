Vi har skapat en hemsida för recept där man enkelt kan sortera på tid.

.github innehåller .yml för att köra tester av programmet innan det hamnar på github. (testet som körs är det som heter test_app.py)

/static innehåller våra statiska filer som .css, bilder samt .js filer.

/template innehåller våra .html filer för vad som ska visas på hemsidan.

app.py innehåller våra routes
recipes.db är våran databas som vi läser in ifrån
requirements.txt är en fil för att enkelt kunna installera alla "dependencies" med pip.

*********
Programmet går att köra lokalt efter att du installerat alla dependencies, med "pip install -r requirements.txt"
Därefter kan man köra "flask run --debug" i terminalen.

Hemsidan finns även live på: http://petarnikolic.pythonanywhere.com/