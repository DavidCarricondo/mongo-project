
#Get lat long for google API
def get_latlong(office):
 return str(office['location']['coordinates'][::-1]).replace(' ', '')[1:-1]

#Request from google API
def get_google(latlong, radius,typ, apiKey, keyw=None):
    keyword= '&keyword='+keyw if keyw else ''
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latlong}&radius={radius}&type={typ}{keyword}&key={apiKey}'
    res = requests.get(url)
    return res.json()['results']
