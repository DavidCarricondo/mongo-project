
import requests

#Get lat long for google API
def get_latlong(office):
 return str(office['location']['coordinates'][::-1]).replace(' ', '')[1:-1]

#Request from google API
def get_google(latlong, radius,typ, apiKey, keyw=None):
    keyword= '&keyword='+keyw if keyw else ''
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latlong}&radius={radius}&type={typ}{keyword}&key={apiKey}'
    res = requests.get(url)
    return res.json()['results']


def school_kinder_filter(lst, keys,new_field, radius, typ, keyw=None, apiKey=None):
    new_lst=[]
    for of in lst:
        school = get_google(get_latlong(of), radius=1000, typ =typ, keyw=keyw, apiKey=apiKey)
        count=0
        for e in school:
            if any(i in e['name'].lower() for i in keys):
                count+=1
        if count > 0:
            of[new_field] = count
            new_lst.append(of)

