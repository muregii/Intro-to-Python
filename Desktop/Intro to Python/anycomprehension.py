from data import people, basic_plants, plants_list

if all([person[1]] for person in people):
    print("send email")
else:
    print("User must edit the list of recipients")
    