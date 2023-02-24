def relate_to_luke(name):
    if name == "Darth Vader":
        return "Luke, I am your father."
    elif name == "Leia":
        return "Luke, I am your sister."
    elif name == "Han":
        return "Luke, I am your brother in law."
    elif name == "R2D2":
        return "Luke I am your brother in law."

relation = relate_to_luke("Darth Vader")
print(relation)

relation = relate_to_luke("Leia")
print(relation)

relation = relate_to_luke("Han")
print(relation)