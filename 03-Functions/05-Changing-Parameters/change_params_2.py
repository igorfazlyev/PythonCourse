def main():
    singer = dict(
        first_name = 'Angela',
        last_name = 'Merkel'
    )
    print(singer.get('first_name'), singer.get('last_name'))
    change_param(singer)
    print(singer.get('first_name'), singer.get('last_name'))

def change_param(param):
    param['first_name'] = 'Peter'
    param['last_name'] = 'Gabriel'

main()