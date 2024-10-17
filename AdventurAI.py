import openai
from dotenv import load_dotenv
import os
load_dotenv()

def oneQuestionInputHelper(question, number):
   return input(str(number) + ") " + question + " >>> ")

def oneQuestion(question, number, multiple):
   command =  ""
   returning = ""
   if (multiple):
       command = oneQuestionInputHelper(question + "\nThe following question takes multiple answers, type \'done\' to quit\n", number)
       returning += command
       while command != "done":
           command = input(" >>> ")
           if (command == 'done'): break
           returning += ", " + command
       return returning
   else:
    return oneQuestionInputHelper(question, number)

def simulateQuestions():
   questionList = []
   questionList.append(['Where do you want to go? ','single'])
   questionList.append(['How many days is your trip? ','single'])
   questionList.append(['What type of trip do you want to go on? Options include:\n\t-> Business Trip\n\t-> Solo trip\n\t-> Family trip\n\t-> Staycation\n\t-> Girls trip \n\t-> Guys trip \n\t-> Road trip\n   ','single'])
   questionList.append(['What is your estimated total trip budget? ','single'])
   questionList.append(['Do you have transportation preferences (car, plane, bus, train, bike, walk, metro, horse, ship, etc)? ','single'])
   questionList.append(['What sorts of things do you like? Options include:\n\t-> Animals\n\t-> Architecture\n\t-> Art\n\t-> Beaches\n\t-> Cruises\n\t-> Family time\n\t-> Fine arts\n\t-> Mountains\n\t-> Museums\n\t-> National Parks\n\t-> Parks\n\t-> Resorts\n\t-> Shopping\n\t-> Shows\n\t-> Sports\n\t-> Visual Arts\n\t-> Water Sports','multiple'])
   questionList.append(['Enter your dietary preferences ','multiple'])
   questionList.append(['What is your age?','single'])

   counter = 1
   answers = []
   try:
       for question in questionList:
           answers.append(oneQuestion(question[0], counter, question[1]=='multiple'))
           counter += 1
       return answers
   except Exception as e:
       print(f"An error occurred while collecting user input: {e}")
       return None

def accessGPT(prompt):
   openai.api_key = os.getenv('anything_in_the_world')
   messages = [ {"role": "system", "content":
             """You are an intelligent assistant that is used for choices on places to visit for the purpose
                 of planning a trip itinerary. Possible prompts that you may get and be required to answer is places
                 that people may visit, things that people can do in those places, and generating summaries for the given
                 places. Furthermore, you will also have to take in consideration the specific requirements presented to you."""}]

   message =  prompt
   if message:
       messages.append(
           {"role": "user", "content": message},
       )
       chat = openai.chat.completions.create(
           model="gpt-3.5-turbo", messages=messages
       )
   reply = chat.choices[0].message.content
   return reply  # Return the reply instead of printing it

def generate_prompt(pe):
   return f"Plan a {pe[1]} day long trip and include a full and complete itinerary to {pe[0]}. The specific type of trip that this should be is a {pe[2]}. The estimated budget for this trip is ${pe[3]}. Transportation preferences include traveling by {pe[4]}. Sorts of things that the travelers enjoy doing include {pe[5]}. Dietary restrictions that travelers have are {pe[6]}. Please give your output such that a {pe[7]} year old person would understand. Clearly detail what to do each day. First put the day number as a heading. Then create a list of restaurants, activities and give a short description of each right next to it. Format your response as a JSON object with each day as a key and the value being another dictionary containing the keys 'activities' and 'restaurants'. The values to both of these dictionaries should be a list of other dictionaries with the activity or restaurant name appropriately as the key and the description as the value."

def get_itinerary(answers):
   pe = answers
   prompt = generate_prompt(pe)
   return accessGPT(prompt)