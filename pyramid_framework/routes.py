def includeme(config):
    config.add_route('index', '/')
    config.add_route('add_shop', '/add_shop')
    config.add_route('clear_shops_table', '/clear_shops_table')
    config.add_route('external_api_call', '/external_api_call')
    config.add_route('serialize_json', '/serialize_json')
    config.add_route('clear_student_table', '/clear_student_table')


