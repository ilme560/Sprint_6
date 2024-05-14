import faker


def get_sign_up_date():
    fake = faker.Faker('ru_RU')
    name = fake.first_name()
    last_name = fake.last_name()
    address = fake.street_address()

    return name, last_name, address
