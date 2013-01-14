from __future__ import with_statement
import contextlib
import sys
from pyke import knowledge_engine, krb_traceback, goal

engine = knowledge_engine.engine(__file__)

goals = [
	goal.compile('food.recipe_glycemic_load($recipe, $glycemic_load)'),
	goal.compile('food.recipe_saturated_fats($recipe, $saturated_fats)'),
	goal.compile('food.recipe_proteins($recipe, $proteins)'),
	goal.compile('food.recipe_fibers($recipe, $fibers)'),
	goal.compile('food.recipe_calories($recipe, $calories)'),
]

def recipe_calculation_test(recipe='spaghetti'):
	engine.reset()
	engine.activate('calculation_expressions')
	print("\n Goals for " + recipe + ":")
	for goal in goals: process_goal(goal, recipe)

def constraint_test():
        engine.activate('constraint_expressions')
        print("\n All asserted facts:")
        engine.get_kb('food').dump_specific_facts()

def process_goal(goal, recipe):
	with goal.prove(engine, recipe=recipe) as g:
		for vars, plan in g:
			print vars
	#engine.print_stats()
