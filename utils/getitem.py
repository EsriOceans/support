import arcpy


class ItemArray(arcpy.Array):
    def __init__(self, array=None):
        if array is None:
            arcpy.Array
        super(arcpy.Array, self).__init__(array)

    def __getitem__(self, item):
        # we can be sent a slice, or an index
        if isinstance(item, slice):
            indices = item.indices(len(self))
            return ItemArray([self.getObject(i) for i in range(*indices)])
        else:
            self.array.getObject(index)
    
    
