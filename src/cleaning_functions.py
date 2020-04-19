
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
        



