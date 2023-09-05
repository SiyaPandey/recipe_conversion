def convert_chai_recipe(servings):
   
    WATER_ML_PER_SERVING = 150
    MILK_ML_PER_SERVING = 50
    TEA_ML_PER_SERVING = 5
    SUGAR_ML_PER_SERVING = 10
    SPICES_G_PER_SERVING = 5


    water_ml = servings * WATER_ML_PER_SERVING
    milk_ml = servings * MILK_ML_PER_SERVING
    tea_ml = servings * TEA_ML_PER_SERVING
    sugar_ml = servings * SUGAR_ML_PER_SERVING
    spices_g = servings * SPICES_G_PER_SERVING

    return {
        "Water (milliliters)": water_ml,
        "Milk (milliliters)": milk_ml,
        "Tea Leaves (milliliters)": tea_ml,
        "Sugar (milliliters)": sugar_ml,
        "Spices (grams)": spices_g,
    }

def convert_rice_recipe(servings):
    RICE_GRAMS_PER_SERVING = 60
    WATER_ML_PER_SERVING = 120
 
    rice_grams = servings * RICE_GRAMS_PER_SERVING
    water_ml = servings * WATER_ML_PER_SERVING

    return {
        "Rice (grams)": rice_grams,
        "Water (milliliters)": water_ml,
    }

def convert_roti_recipe(servings):
   
    FLOUR_GRAMS_PER_SERVING = 75
    WATER_ML_PER_SERVING = 30

    flour_grams = servings * FLOUR_GRAMS_PER_SERVING
    water_ml = servings * WATER_ML_PER_SERVING

    return {
        "Flour (grams)": flour_grams,
        "Water (milliliters)": water_ml,
    }

def convert_daal_recipe(servings):

    LENTILS_GRAMS_PER_SERVING = 50
    WATER_ML_PER_SERVING = 200

   
    lentils_grams = servings * LENTILS_GRAMS_PER_SERVING
    water_ml = servings * WATER_ML_PER_SERVING

    return {
        "Lentils (grams)": lentils_grams,
        "Water (milliliters)": water_ml,
    }

def convert_aloo_ki_sabji_recipe(servings):

    POTATOES_GRAMS_PER_SERVING = 100
    WATER_ML_PER_SERVING = 100


    potatoes_grams = servings * POTATOES_GRAMS_PER_SERVING
    water_ml = servings * WATER_ML_PER_SERVING

    return {
        "Potatoes (grams)": potatoes_grams,
        "Water (milliliters)": water_ml,
    }

def main():
    print("Indian Recipes Converter")
    print("========================")
    
    while True:
        recipe_choice = input("What do you want to make (Chai/Rice/Roti/Daal/Aloo ki Sabji)? ").lower()
        
        if recipe_choice == "chai":
            servings = float(input("Enter the number of servings for Chai Tea: "))
            converted_recipe = convert_chai_recipe(servings)
        elif recipe_choice == "rice":
            servings = float(input("Enter the number of servings for Rice: "))
            converted_recipe = convert_rice_recipe(servings)
        elif recipe_choice == "roti":
            servings = float(input("Enter the number of servings for Roti: "))
            converted_recipe = convert_roti_recipe(servings)
        elif recipe_choice == "daal":
            servings = float(input("Enter the number of servings for Daal: "))
            converted_recipe = convert_daal_recipe(servings)
        elif recipe_choice == "aloo ki sabji":
            servings = float(input("Enter the number of servings for Aloo ki Sabji: "))
            converted_recipe = convert_aloo_ki_sabji_recipe(servings)
        else:
            print("Invalid recipe choice.")
            continue

        print("\nRecipe for", servings, "serving(s) of", recipe_choice.capitalize(), ":")
        for ingredient, quantity in converted_recipe.items():
            print(f"{ingredient}: {quantity:.2f} (per serving)")

if __name__ == "__main__":
    main()
