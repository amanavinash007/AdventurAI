import cgi
import sys
import openai
sys.path.append("Users/amanavi/Downloads/AdventurAI")
import AdventurAI

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
answers = [form.getvalue('question1'), form.getvalue('question2'), form.getvalue('question3'), form.getvalue('question4'), form.getvalue('question5'), form.getvalue('question6'), form.getvalue('question7'), form.getvalue('question8')]

# Call the simulateQuestions function with the answers
pe = answers
print (pe)
# Generate the prompt and call the accessGPT function
prompt = f"Plan a {pe[1]} day long trip and include a full and complete itinerary to {pe[0]}. The specific type of trip that this should be is a {pe[2]}. The estimated budget for this trip is ${pe[3]}. Transportation preferences include traveling by {pe[4]}. Sorts of things that the travelers enjoy doing include {pe[5]}. Dietary restrictions that travelers have are {pe[6]}. Please give your output such that a {pe[7]} year old person would understand. Clearly detail what to do each day. First put the day number as a heading. Then create a list of restaurants, activities and give a short description of each right next to it. Format your response as a JSON object with each day as a key and the value being another dictionary containing the keys 'activities' and 'restaurants'. The values to both of these dictionaries should be a list of other dictionaries with the activity or restaurant name appropriately as the key and the description as the value."
AdventurAI.accessGPT(prompt)