function openPopup(title, image, ingredients, instructions) {
    document.getElementById('popupTitle').innerText = title;
    document.getElementById('popupImage').src = image;

    let ingredientsList = document.getElementById('popupIngredients');
    ingredientsList.innerHTML = '';
    ingredients.split('\\n').forEach(ingredient => {
        let li = document.createElement('li');
        li.innerText = ingredient.trim(); // trim för att ta bort extra mellanslag
        ingredientsList.appendChild(li);
    });

    document.getElementById('popupInstructions').innerText = instructions.trim().replace(/\\n/g, '\n'); // trim för att ta bort extra mellanslag
    document.getElementById('recipePopup').style.display = 'block';
}

function closePopup() {
    document.getElementById('recipePopup').style.display = 'none';
}
