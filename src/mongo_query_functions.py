def near_success_offices(location, dist=5000):
    nmbr_offices = db.offices_loc_england.find({'$and':[{'deadpooled_year':None},
                                                        {'category_code':{'$in':['biotech', 'cleantech', 
                                                                                 'games_video', 'mobile', 
                                                                                 'nanotech', 'network_hosting',
                                                                                 'software', 'web']}},
                                                        {'$and':[{'raised':{'$gte':1}},
                                                                        {'location':{'$near':{'$geometry':location,
                                                                                              '$maxDistance':dist}}}]
                                               }]}).count()
    return nmbr_offices



def near_filter(lst, fn):
    filtered_lst=[]
    for of in lst:
        nr = fn(of['location'])
        if nr > 0:
            of['pro_nearby'] = nr 
            filtered_lst.append(of)
    return filtered_lst


#CReate GeoJson from a dataframe with Longitude and Latitude
def create_geojson(df):
    return {'type':'Point',
            'coordinates':[df['Longitude'], df['Latitude']]}
            

#Find starbucks close to a location
def near_starbuck(location, dist=200):
    nmbr_starb = db.starbucks.find({'location':{'$near':{'$geometry':location,
                                                                     '$maxDistance':dist}}}
                                               ).count()
    return nmbr_starb