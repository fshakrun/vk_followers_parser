# Парсер целевой аудитории VK

Программа решает задачу получения активной целевой аудитории — подписчиков нужного вам паблика VK. Парсер работает с помощью взаимодействия по API. 

### Особенности работы:

1. Парсинг происходит путем отправки запросов по api и для работы необходим соответствующий токен, подробности: [Ключ доступа API VK](https://dev.vk.com/api/access-token/getting-started). 
2. Реализована функция получения id сообщества по его короткому названию (например, https://vk.com/petersburg.live — вводим petersburg.live и получаем id).
3. Реализована логика обхода ограничения в 1000 результатов, характерная для VK Api — парсер получает id всех подписчиков сообщества, в зависимости от введенной пользователем даты последнего визита.
4. Полученные id пользователей сохраняются в txt файл, который можно загрузить, например, в рекламный кабинет VK и настроить рекламу на этих конкретных пользователей.
