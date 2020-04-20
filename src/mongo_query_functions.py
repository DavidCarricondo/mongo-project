def near_success_offices(db_collection,location, dist=5000):
    offices = db_collection.find({'$and':[{'deadpooled_year':None},
                                                        {'category_code':{'$in':['biotech', 'cleantech', 
                                                                                 'games_video', 'mobile', 
                                                                                 'nanotech', 'network_hosting',
                                                                                 'software', 'web']}},
                                                        {'$and':[{'raised':{'$gte':1}},
                                                                        {'location':{'$near':{'$geometry':location,
                                                                                              '$maxDistance':dist}}}]
                                               }]})
    return list(offices)



def near_filter(db_collection, lst, fn, new_field):
    filtered_lst=[]
    for of in lst:
        nr = len(fn(db_collection, of['location']))
        if nr > 0:
            of[new_field] = nr 
            filtered_lst.append(of)
    return filtered_lst


#CReate GeoJson from a dataframe with Longitude and Latitude
def create_geojson(df):
    return {'type':'Point',
            'coordinates':[df['Longitude'], df['Latitude']]}
            

#Find starbucks close to a location
def near_starbuck(db_collection, location, dist):
    nmbr_starb = db_collection.find({'location':{'$near':{'$geometry':location,
                                                                     '$maxDistance':dist}}}
                                               ).count()
    return nmbr_starb