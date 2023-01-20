from faker import Faker
from faker.providers import internet, lorem

fake = Faker()
fake.add_provider(internet)
fake.add_provider(lorem)
