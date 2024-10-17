import sys
sys.path.append("Users/amanavi/Downloads/AdventurAI")
import AdventurAI

def handle_form(answers):
    # Generate the prompt
    prompt = f"Plan a {answers[1]} day long trip and include a full and complete itinerary to {answers[0]}. The specific type of trip that this should be is a {answers[2]}. The estimated budget for this trip is ${answers[3]}. Transportation preferences include traveling by {answers[4]}. Sorts of things that the travelers enjoy doing include {answers[5]}. Dietary restrictions that travelers have are {answers[6]}. Please give your output such that a {answers[7]} year old person would understand. Clearly detail what to do each day. First put the day number as a heading. Then create a list of restaurants, activities and give a short description of each right next to it. Format your response as a JSON object with each day as a key and the value being another dictionary containing the keys 'activities' and 'restaurants'. The values to both of these dictionaries should be a list of other dictionaries with the activity or restaurant name appropriately as the key and the description as the value."

    # Call the accessGPT function and return the result
    return AdventurAI.accessGPT(prompt)