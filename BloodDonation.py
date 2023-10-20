'''BloodDonation'''
def donation(age, weight, time):
    '''BloodDonation'''
    if 17 <= age <= 70:
        if age == 17 or 60 <= age <= 70:
            permission = input()
            if permission == "False":
                return "No"
        if weight < 45:
            return "No"
        if age > 55 and time < 1:
            return "No"
        else:
            return "Yes"
    else:
        return "No"

print(donation(int(input()), float(input()), int(input())))
