import json,phone
class CountryDecoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, o):
        decoded_country =  phone.Phone(
            o.get('imei'), 
            o.get('brand'), 
            o.get('model'),
        )
        return decoded_country

with open('sample.json','r') as f:
    country_object = json.load(f, cls=CountryDecoder)

print(type(country_object))