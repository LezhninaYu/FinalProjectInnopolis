import random
import aiohttp


async def create_users():
    user1 = {
        "email": "admin@example.com",
        "password": "admin"
    }
    user2 = {
        "email": "user@example.com",
        "password": "user"
    }
    user3 = {
        "email": "user1@example.com",
        "password": "user1"
    }

    async with aiohttp.ClientSession() as session:
        await session.post("http://localhost:8080/api/v1/users/create", json=user1)
        await session.post("http://localhost:8080/api/v1/users/create", json=user2)
        await session.post("http://localhost:8080/api/v1/users/create", json=user3)


async def create_posts():
    content = [
        'Пингвиновые, или пингвины, — семейство нелетающих морских птиц, единственное современное в отряде пингвинообразных. В него включают 18 современных видов. Все представители этого семейства хорошо плавают и ныряют.',
        'Паук шпион: Паук шпион, который ползает по потолку и смотрит всё, что происходит в доме.',
        'Длинный длинный длинный длинный длинный длинный длинный контент',
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel congue arcu, non tempus dui. Nullam mollis consectetur imperdiet. Nunc imperdiet rhoncus lobortis. Nullam id ornare dui, non aliquam purus. Proin condimentum massa ante, in vestibulum arcu blandit in. Nunc massa nulla, volutpat a scelerisque sed, vehicula at nibh. Nunc iaculis quis elit sit amet varius. Aenean ac ligula ipsum. Nulla molestie hendrerit commodo. Vivamus quis dolor ex. Nullam ac vulputate magna, a congue elit.'
    ]
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            post = {
                "name": f"Название {i}",
                "text": random.choice(content),
                "user_id": 0
            }
            await session.post("http://localhost:8080/api/v1/post", json=post)


async def migrate():
    await create_users()
    await create_posts()
