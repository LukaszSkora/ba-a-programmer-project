"""

The email_list function receives a dictionary,
which contains domain names as keys, and a list of users as values.
Fill in the blanks to generate a list that contains
complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
	emails = []
	for ___:
	  for user in users:
	    emails.___
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon",
"jean.grey"], "hotmail.com": ["bruce.wayne"]}))

"""


def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            # Now add the group to the the list of
            user_groups[user].append(group)
    # groups for this user, creating the entry
    # in the dictionary if necessary

    return (user_groups)


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))
