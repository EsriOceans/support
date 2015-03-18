import arcpy

# an example for handling the column names more pythonicly


wanted_columns = ['something', 'something_else']

wanted_columns = {
    # JSON name  # my rad name
    'something': 'something_else',
    'JASON': 'nice_pythonic_name',
}
result_rows = []

for GIS in ...:
    # var_1 = GIS['something']
    # ...
    #result_vals = [GIS[r] for r in wanted_columns]
    #result_vals = [GIS[r] for r in wanted_columns]

    for (json_name, python_name) in wanted_columns.items():
        result_vals[python_name] = GIS[json_name]

    result = dict(keys=wanted_coumns, values=result_vals)
