#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)

print len(enron_data["SKILLING JEFFREY K"])

count = 0
for n in enron_data:
	if enron_data[n]["poi"] == 1:
		count += 1
print count


poi = open("../final_project/poi_names.txt")
c = 0
for a in poi:
	c += 1
print c-2

for v in enron_data["PRENTICE JAMES"]:
	print v
print enron_data["PRENTICE JAMES"]["total_stock_value"]

print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
	
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]

print enron_data["FASTOW ANDREW S"]

sal = 0
email_add = 0
for i in enron_data:
	if enron_data[i]["salary"] != 'NaN':
		sal += 1
	if enron_data[i]["email_address"] != 'NaN':
		email_add += 1

print sal, email_add

tp1 = 0
for i in enron_data:
	if enron_data[i]["total_payments"] == 'NaN':
		tp1 += 1

total = 0
for j in enron_data:
	total += 1

print (tp1*100.0)/total

tp = 0
for i in enron_data:
	if enron_data[i]["total_payments"] == 'NaN' and enron_data[i]["poi"] == True:
		tp += 1

total = 0
for j in enron_data:
	total += 1

print (tp*100.0)/total

print total,tp1,tp,count