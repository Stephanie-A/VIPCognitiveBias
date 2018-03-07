import random
def anchoringbias(focus, dict1): # pass in the area of focus
    dict2 = [];
    for area in dict1:
        if area != focus:
            dict2.append(area);
    if len(dict2) == 0:
        return "You have focused on location, person, and time. Do you have other aspects you'd like to focus on?";
    newFocus = dict2[random.randrange(0, len(dict2))];

    return "You are focusing on " + focus + " too much." + " Do you have any hypothesis regarding " + newFocus;



