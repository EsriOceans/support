import olefile

with open('test.ags', 'rb') as f:
    # see: https://bitbucket.org/decalage/olefileio_pl/wiki/API
    ole = olefile.OleFileIO(f)

    # list the detected properties
    print(ole.listdir())

    # what's the document structure?
    print(ole.dumpdirectory())

    ags_conn = ole.openstream('AGSConnProperties')
    data = ags_conn.read()

    # can print out the data -- its the raw binary stream as a string.
    
    # here's a filter to skip half the bytes and the header, print the rest.
    filtered  = ''.join([d for d in data[6:] if d != '\x00'])
    print(filtered)

    # next, you'd want to read the specific variables at the appropriate
    # offsets and write them out individually. Or as a hack:

    # the 'URL' result in this file:
    print(filtered[144:178])
    # 'http://rags2k:6080/arcgis/services'
