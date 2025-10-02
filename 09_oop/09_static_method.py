class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = "   milk ,    water       , sugar    "

print(ChaiUtils.clean_ingredients(raw))

# what is the use of static method? : static method is used to group utility functions which are related to the class but do not need access to instance or class variables.

# i can access the class's method without using the static method but it is not a good practice.
