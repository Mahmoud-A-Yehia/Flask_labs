from app import create_app

app = create_app(config_type='dev')


if __name__ == '__main__':
    print(app.url_map)
    print(f'admin name is "Ahmed Ayman" and password is "password"')
    app.run(port=5000)