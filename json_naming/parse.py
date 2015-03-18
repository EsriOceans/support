import json
import dateutil.parser

with open('output.txt') as json_f:
    j = json.load(json_f)
    service_request = j['Response']['ListOfServiceRequest']['ServiceRequest'][0]
   
    # convert the string into a datetime object
    updated_date = dateutil.parser.parse(service_request['UpdatedDate'])
    created_date = dateutil.parser.parse(service_request['CreatedDate'])

    # an example time difference between two dates --
    delta = updated_date - created_date
    # now have a delta object that supports a bunch of things, like this:
    print("Minutes passed between creation and update: {}".format(delta.seconds / 60.0))

