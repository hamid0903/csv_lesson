
def get_column(data):
    column_name = []
    column_name=data[0:31]


    return column_name

data = open('data.csv').read()
print(get_column(data))
