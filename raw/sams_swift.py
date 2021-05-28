class Ingredient:
    # name = None
    # isCommon = None
    # tags = None

    def __init__(self, name, isCommon=True, tags):
        self.name = name
        self.isCommon = isCommon
        self.tags = tags


class RecipeClass:
    BROWNIE = "brownie"
    MUFFIN = 'muffin'
    BLONDIE = 'blondie'
    CUPCAKE = 'cupcake'


class Stage:
    createCookie = None
    createFullDough = None
    createSugarMixture = None


class Verb:
    bake = 'bake'
    combine = 'combine'
    mix = 'mix'


class Qualia:
    bitter = 'bitter'
    browned = 'browned'
    underbaked = 'underbaked'


class Time:
    var = None


# class Step(stage=Stage, id_, ingredients=IngredientAmount, equipment=[Equipment],
#            verb=Verb, duration=Time, notes, output=Ingredient): #review each one!!
class Step:
    index = 0

    def __init__(self, stage, ingredients, equipment, verb, duration, output, notes):
        self.stage = stage
        self.ingredients = ingredients
        self.equipment = equipment
        self.verb = verb
        self.duration = duration
        self.output = output
        self.notes = notes

        self.id = self.stage + '-' + str(self.index)
        self.index += 1


class Substitution:
    def __init__(self, name, stepsIn, stepsOut, qualiaChanges):
        self.name = name
        self.stepsIn = stepsIn
        self.stepsOut = stepsOut
        self.qualiaChanges = qualiaChanges


class Recipe:
    def __init__(self, name, recipeClass, ingredients, equipment, baseSteps, stages):
        self.name = name
        self.recipeClass = recipeClass
        self.ingredients = ingredients
        self.equipment = equipment
        self.baseSteps = baseSteps
        self.stages = stages


class WorkingRecipe:
    # (ingredients=IngredientAmount, equipment=[], steps={}, stages=Stage,
    #                 qualiaChanges=[], substitutionsPerformed=[]):
    qualiaChange = []
    substitutionsPerformed = []
    steps = {}

    def __init__(self, recipe):
        self.ingredients = recipe.ingredients
        self.equipment = recipe.equipment
        self.stages = recipe.stages


        for step in recipe.baseSteps:
            stageSteps = self.steps[step.stage]
            if stageSteps:
                stageSteps.append(step)
                self.steps[step.stage] = stageSteps
            else:
                self.steps[step.stage] = [step]

    def applySubstitution(self, **sub):
        self.substitutionsPerformed.append(sub)
        self.qualiaChanges += sub.qualiaChanges

        for stepOut in sub.stepsOut:
            stage = stepOut.stage
            stageSteps = self.steps[stage]
            index = stageSteps.firstIndex(stepOut)
            if stageSteps and index:
                stageSteps.drop(index)
                self.steps[stage] = stageSteps

        for stepIn in sub.stepsIn:
            self.steps[stepIn.stage].append(stepIn)