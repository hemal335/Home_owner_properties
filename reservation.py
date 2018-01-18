from rewpapi.common.http import Request


class RemoteAgent(Request):
 
    def __init__(self, base_site, auth):
        super(RemoteAgent, self).__init__(auth)
        self._base_site = base_site
        self._auth = auth
        self._endpoint = base_site + "/api/property/"

    def get_all(self):
      
        remote_property = self.execute()
        property = []
        if remote_property:
            for a in remote_property:
                new_property = Property(self._base_site, self._auth)
                new_property.FIELDS = []
                for k, v in a.items():
                    setattr(new_property, k, v)
                    new_property.FIELDS.append(k)
                property.append(new_property)
            return property
        return None

    def get(self, uuid):
        b = Property()
        b.branch_name = "Foo"
        return b


class Property(RemoteAgent):

    def set_fields(self, property_object):
        self.FIELDS = property_object.FIELDS
        for field in property_object.FIELDS:
            setattr(self, field, getattr(property_object, field))

    def update(self):
        self._endpoint = self._base_site + "/api/property/%
