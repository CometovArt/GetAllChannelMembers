import asyncio
from pyrogram import Client

api_id = 9545469
api_hash = '004d9e767672f364cbae700905837819'
phone_number = '+7' #укажите тут свой номер телефона аккаунта, который админ в канале

TARGET = 1234 #укажите тут id своего канала

# При запуске скрипта клиент запросит аутентификацию
userbot = Client(
    name='userbot', 
    api_id=api_id, 
    api_hash=api_hash, 
    phone_number=phone_number, 
)


async def main():
    async with userbot:
        unique_ids = []
        users = []
        members = []

        # Поиск юзеров основывается на последовательном получении результатов get_chat_members с фильтром по каждой букве алфавита
        # Для большого числа подписчиков, или при низкой точности, рекомендую добавить словари не кириллических/латинских символов
        # и/или добавить словари составных букв типа 'aa', 'ab' и тд.
        russian_lowercase = [chr(code) for code in range(ord('а'), ord('я')+1)]
        english_lowercase = [chr(code) for code in range(ord('a'), ord('z')+1)]
        all_lowercase_letters = russian_lowercase + english_lowercase

        for letter in all_lowercase_letters:
            await asyncio.sleep(3)
            print(letter)
            async for member in userbot.get_chat_members(TARGET, query=letter):
                if member.user.id not in unique_ids:
                    members.append(member)
                    users.append({'id': member.user.id, 'username': member.user.username, 'full_name': member.user.full_name})
                    unique_ids.append(member.user.id)

        async for member in userbot.get_chat_members(TARGET):
            if member.user.id not in unique_ids:
                members.append(member)
                users.append({'id': member.user.id, 'username': member.user.username, 'full_name': member.user.full_name})
                unique_ids.append(member.user.id)

        count = await userbot.get_chat_members_count(TARGET)
        
        print(f'Всего юзеров канала: {count}')
        print(f'Спаршено юзеров: {len(users)}')

        if len(users) < count:
            print(f'Не было получено {count - len(users)} юзеров')
        elif len(users) == count:
            print('Все юзеры успешно получены')

        print('Список юзеров:')
        for user in users:
            print(user)


userbot.run(main())
