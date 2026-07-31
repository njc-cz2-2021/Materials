

# == Exact
# < Less
# > More
# <= Less than or equal to
# >= More than or equal to 
# != Not

def furry_checker(person):
    if "likes animals" in person:
        return "Yep that's a furry"
    else: 
        return "That's not a furry"

hauyu = "likes animals"
jovan = "likes animals but not in that way"
print(furry_checker(jovan))