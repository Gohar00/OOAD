from abc import  ABC, abstractmethod

class User:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.favorite_recipes = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_contact(self, contact):
        self.contact = contact

    def get_contact(self):
        return self.contact

    def save_recipe(self, recipe):
        if recipe not in self.favorite_recipes:
            self.favorite_recipes.append(recipe)

    def share_recipe(self, recipe, user):
        user.save_recipe(recipe)



class Recipe(ABC):
    def __init__(self, title, ingredients, instruction):
        self.title = title
        self.ingredients = ingredients
        self.instruction = instruction
        self.rating = []

    @abstractmethod
    def get_recipe_type(self):
        pass

    def add_rating(self, rating):
        self.rating.append(rating)

    def get_average_rating(self):
        if len(self.rating) == 0:
            return 0
        else:
            total_score = sum(r.rating_score for r in self.rating)
            return total_score / len(self.rating)


class Vegetarian(Recipe):
    def __init__(self, title, ingredients, instructions):
        super().__init__(title, ingredients, instructions)

    def get_recipe_type(self):
        return "Vegetarian"


class Dessert(Recipe):
    def __init__(self, title, ingredients, instructions):
        super().__init__(title, ingredients, instructions)

    def get_recipe_type(self):
        return "Dessert"


class Rating:
    def __init__(self, recipe, user, score):