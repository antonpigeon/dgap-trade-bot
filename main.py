from functions import *
from graphics import *
#functions: get_request, create_table, plot_chart

if __name__ == '__main__':
    data = get_request(api_key='a4mhZVRyfw2zDiGRDZXAHEf')
    table = create_table(data)
    fig = plot_chart(table)
    page_setup(fig)
    run_server()
