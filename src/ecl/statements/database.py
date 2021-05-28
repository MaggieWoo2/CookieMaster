"""This module is for defining the Database object"""

from ecl.statements import Equipment, Ingredient, Qualia, Recipe, RecipeFormat, Stage, Step, Substitution, Verb


class Database:
    """The database of each spreadsheet as a list of instances"""

    def __init__(self):
        self.ingredient = []
        self.qualia = []
        self.step = []
        self.recipe = []
        self.verb = []
        self.recipe_format = []
        self.equipment = []
        self.substitution = []
        self.stage = []

    def add_qualia(self, **kwargs):
        """Add each line of qualia and the associated attributes"""
        self.qualia.append(Qualia(self, **kwargs))  # appending an instance

    def add_ingredient(self, **kwargs):
        """Add each line of ingredient and the associated attributes"""
        self.ingredient.append(Ingredient(self, **kwargs))

    def add_step(self, **kwargs):
        """Add each line of step and the associated attributes"""
        self.step.append(Step(self, **kwargs))

    def add_verb(self, **kwargs):
        """Add each line of verb and the associated attributes"""
        self.verb.append(Verb(self, **kwargs))

    def add_recipe(self, **kwargs):
        """Add each line of recipe and the associated attributes"""
        self.recipe.append(Recipe(self, **kwargs))

    def add_recipe_format(self, **kwargs):
        """Add each line of recipe_format and the associated attributes"""
        self.recipe_format.append(RecipeFormat(self, **kwargs))

    def add_equipment(self, **kwargs):
        """Add each line of equipment and the associated attributes"""
        self.equipment.append(Equipment(self, **kwargs))

    def add_substitution(self, **kwargs):
        """Add each line of substitution and the associated attributes"""
        self.substitution.append(Substitution(self, **kwargs))

    def add_stage(self, **kwargs):
        """Add each line of stages"""
        self.stage.append(Stage(self, **kwargs))

    def get_qualia(self, q_name: str) -> object:
        """Get the qualia instance of q_name"""
        for i in self.qualia:
            if q_name == i.qualia:
                return i  # return the instance of the specific qualia q_name
        # warnings.warn(f"Qualia {q_name} not found")
        return Qualia(
            self,
            id_="DUMMY",
            qualia=f"MISMATCH: {q_name}",
            description="DUMMY",
            category="DUMMY",
            is_negative="DUMMY",
        )

    def get_verb(self, v_method: str) -> object:
        """Get the verb instance of v_method"""
        for i in self.verb:
            if v_method == i.method:
                return i
        return Verb(self, id_="DUMMY", method=f"MISMATCH: {v_method}", description="DUMMY")

    def get_ingredient(self, i_name: str) -> object:
        """Get the ingredient instance of i_name"""
        for i in self.ingredient:
            if i_name == i.item:
                return i

        return Ingredient(
            self,
            id_="DUMMY",
            item=f"MISMATCH: {i_name}",
            inherit="DUMMY",
            required_attribute="DUMMY",
            attribute_default="DUMMY",
            qualia="DUMMY",
            notes="DUMMY",
        )

    def get_ingredient_or_equip(self, i_name: str) -> object:
        """Get the equipment instance of i_name"""
        for i in self.ingredient:
            if i_name == i.item:
                return i
        for i in self.equipment:
            if i_name == i.item:
                return i

        return Ingredient(
            self,
            id_="DUMMY",
            item=f"MISMATCH: {i_name}",
            inherit="DUMMY",
            required_attribute="DUMMY",
            attribute_default="DUMMY",
            qualia="DUMMY",
            notes="DUMMY",
        )

    def get_step(self, step_id: str) -> object:
        """Get the step instance of step_id"""
        if step_id == "":
            return Step(
                self,
                id_="MISSING VALUE",
                stage="DUMMY",
                required_items="DUMMY",
                verb="DUMMY",
                action_notes="DUMMY",
                duration="DUMMY",
                output="DUMMY",
                complexity="DUMMY",
            )

        for i in self.step:
            if step_id in i.id_:
                return i

        return Step(
            self,
            id_=f"MISMATCH: {step_id}",
            stage="DUMMY",
            required_items="DUMMY",
            verb="DUMMY",
            action_notes="DUMMY",
            duration="DUMMY",
            output="DUMMY",
            complexity="DUMMY",
        )

    def get_stage(self, s_name: str) -> object:
        """Get the stage instance of stage_id"""
        if s_name == "":
            return Stage(self, id_="MISSING VALUE", stage="DUMMY")

        for i in self.stage:
            if s_name == i.stage:
                return i

        return Stage(self, id_="DUMMY", stage=f"MISMATCH: {s_name}")

    # def get_scope(self, scope):  # - add scope in Recipe
    #     """Get the scope instance of scope"""
    #     for i in self.recipe:
    #         if scope == i.name:
    #             return i
