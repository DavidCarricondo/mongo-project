
#Extract the info from dictionary column

def extract_loc(x):
    of = x['offices']
    if of["longitude"]==None:
        return (of['country_code'],
           of['city'], 
                None)
    return (of['country_code'],
           of['city'],
           {"type":"Point",
                    "coordinates":[of["longitude"],of["latitude"]]})



#Function to format total_money_raised column

#As of 18th April 2020:
# Euros: 1.09 US dollars
# Pounds: 1.25 US dollars
def clean_raised(x):
    currency = {'$':1,'£':1.25,'€':1.09}
    a = 0
    if len(x)<3:
        return 0
    for c in currency:
        if c in x:
            a = float(x[1:-1])*currency[c]
    if 'k' in x:
        a = a/1000
    return round(a,3)


#Function for scoring results:
#It gives a value to each category that correspond to the 
#percentage of staff affected by that decision
score = lambda x:(-1 if x.pro_nearby==1 else x.pro_nearby)*0.17+\
                    (-1 if x.airp_nearby<3 else x.airp_nearby)*0.22+\
                    (-1 if x.kinder==1 or x.school==1 else x.kinder+x.school)*0.3+\
                    (-1 if x.starbucks==1 else 1)*0.11+\
                    (-1 if x.vegan==1 else 1)*0.011+\
                    (1 if x.disco>1 and x.disco<5 else 0)*1
        



