from functions import *


if __name__ == '__main__':
    data = get_request(api_key='a4mhZVRyfw2zDiGRDZXAHEf')
    table = create_table(data)
    plot_chart(table).show()
