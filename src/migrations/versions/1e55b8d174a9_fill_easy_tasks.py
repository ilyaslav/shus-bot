"""fill easy tasks

Revision ID: 1e55b8d174a9
Revises: 876f6ff5d6fa
Create Date: 2024-12-01 22:06:29.681497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e55b8d174a9'
down_revision: Union[str, None] = '876f6ff5d6fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO tasks (key_word, reward, type, button_name, text) VALUES
        ('тест', 5, 'easy', 'Тест по молодежной политике Вологодской области', '<b>Тест по молодежной политике Вологодской области</b>
Вам предстоит пройти тест, состоящий из 10 вопросов. Некоторые вопросы имеют несколько вариантов ответов, из которых вам необходимо выбрать один правильный. Некоторые вопросы открытого типа. Тест поможет вам проверить свои знания о молодежной политике региона, а также узнать больше о возможностях, доступных для молодежи.

<b>Ссылка на тест:</b> https://forms.yandex.ru/u/674b1472068ff000715db6c9/

<b>Критерии:</b>
За каждый правильный ответ – 0,5.
<b>Максимальное количество баллов:</b> 5 баллов.
<b>Срок сдачи задания:</b> до 23:59 ч. 12 декабря 2024 года.'),
        ('мем', 4, 'easy', 'Создание мема по теме школьного ученического самоуправления', '<b>Создание мема по теме школьного ученического самоуправления</b>
Вам необходимо создать оригинальный мем связанный с темой школьного ученического самоуправления. Мем должен быть понятным, актуальным и корректным для школьной аудитории.

<b>Требования:</b>
1.Формат – JPEG или PNG.
2. Мем не должен содержать оскорбительных, унижающих человеческое достоинство, экстремистских материалов, а также любой другой информации, противоречащей законодательству Российской Федерации.

<b>Критерии:</b>
1. Оригинальность (мем должен быть уникальным и креативным. Использование популярных мемов допускается, но они должны быть адаптированы к теме) – 0–1.
2. Актуальность (мем должен четко отражать тему школьного ученического самоуправления) – 0–2.
3. Эстетика и дизайн (мем должен быть визуально привлекательным. Убедитесь в хорошем качестве картинки и читаемости текста) – 0–1.

<b>Максимальное количество баллов:</b> 4 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('буквы', 6, 'easy', 'Поиск букв «к», «о», «м», «а», «н», «д», «а» «Ш», «У», «С» в школе', '<b>Поиск букв «к», «о», «м», «а», «н», «д», «а» «Ш», «У», «С» в школе</b>
Ваша задача заключается в том, чтобы среди различных надписей в школе найти и сфотографировать по одной букве, из которых можно будет составить словосочетание «Команда ШУС».

<b>Требования:</b>
1. Буквы можно находить в учебниках, на плакатах, табличках и других источниках на территории школы. Специально печатать буквы нельзя.
2. На фотографиях должны быть:
- вся команда;
- предмет на котором находится буква;
- буква, на которую будет указывать кто-то из команды.
3. К фотографиям с буквами необходимо приложить список найденных букв и их местоположений.

<b>Критерии:</b>
1. Полнота (успешное нахождение всех букв, необходимых для составления словосочетания «Команда ШУС») – 0–1.
2. Оригинальность источников, на которых находится буква (балл дается за каждый неповторяющийся источник, на котором была найдена буква) – 0–0,5.

<b>Максимальное количество баллов:</b> 6 баллов.
<b>Срок сдачи задания:</b> до 23:59 ч. 12 декабря 2024 года.'),
        ('кроссворд', 8, 'easy', 'Создайте свой кроссворд на тему ШУС', '<b>Создайте свой кроссворд на тему ШУС</b>
Ваша задача – разработать оригинальный кроссворд на тему школьного ученического самоуправления. Кроссворд должен помочь закрепить основные понятия, термины и идеи, связанные с темой ШУС.

<b>Требования:</b>
1. Кроссворд должен включать 10 слов с определениями.
2. Все слова должны быть напрямую связаны с темой Школьного Ученического Самоуправления (ШУС), с четкой формулировкой, исключающей двусмысленность.
3. Файл кроссворда может быть представлен в одном из следующих форматов: JPEG, PNG, DOC или DOCX.
4. К пустому шаблону кроссворда необходимо приложить отдельный документ с вопросами и правильными ответами, пояснениями для тех слов, которые требуют дополнительных разъяснений.

<b>Критерии:</b>
1. Соответствие теме (все слова и определения должны быть непосредственно связаны с темой ШУС) – 0–1.
2. Количество слов (кроссворд должен содержать 10 слов, актуальных для темы) – 0–1.
3. Качество формулировок (определения должны быть понятными и однозначными) – 0–3.
4. Грамотность (в кроссворде не более двух орфографических, пунктуационных или грамматических ошибки) – 0–2.
5. Оформление (за качественное оформление кроссворда команде могут начислить дополнительные баллы) – 0–1.

<b>Максимальное количество баллов:</b> 8 баллов.
<b>Срок сдачи задания:</b> до 23:59 ч. 12 декабря 2024 года.')
""")

    op.execute(
        """
        INSERT INTO tasks (key_word, reward, type, button_name, date, attachments, attachment_type, text) VALUES
        ('замок', 2, 'easy', 'Решите ребус по теме молодежной политики Вологодской области и ШУС', '2024-12-02', 'AgACAgIAAxkBAAM0Z00clS4v2hlWgOTJaGnRfvQkh-oAAjf1MRsgZmhK4Wok7YKpLgcBAAMCAAN4AAM2BA', 'img', '<b>Решите ребус по теме молодежной политики Вологодской области и ШУС</b>
Ваша задача заключается в том, чтобы разгадать ребус, связанный с молодежной политикой Вологодской области или школьным ученическим самоуправлением (ШУС). Ребус включает визуальные подсказки, отражающие различные аспекты и мероприятия, проводимые в рамках молодежной политики региона и школьной активности. В результате разгадывания вы должны получить слово или словосочетание, которое нужно будет отправить в ответе на задание.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('пингвин', 2, 'easy', 'Решите ребус по теме молодежной политики Вологодской области и ШУС', '2024-12-03', 'AgACAgIAAxkBAAM3Z00cmNX7A1pFpoSTRPDMfCl750cAAgXsMRslY2BKkB5uzeA6_44BAAMCAANtAAM2BA', 'img', '<b>Решите ребус по теме молодежной политики Вологодской области и ШУС</b>
Ваша задача заключается в том, чтобы разгадать ребус, связанный с молодежной политикой Вологодской области или школьным ученическим самоуправлением (ШУС). Ребус включает визуальные подсказки, отражающие различные аспекты и мероприятия, проводимые в рамках молодежной политики региона и школьной активности. В результате разгадывания вы должны получить слово или словосочетание, которое нужно будет отправить в ответе на задание.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('чайник', 2, 'easy', 'Решите ребус по теме молодежной политики Вологодской области и ШУС', '2024-12-04', 'AgACAgIAAxkBAAM6Z00cmmkhVEBe3kJlfr0a4ywzdRgAAgbsMRslY2BKq656uVTZr2QBAAMCAAN4AAM2BA', 'img', '<b>Решите ребус по теме молодежной политики Вологодской области и ШУС</b>
Ваша задача заключается в том, чтобы разгадать ребус, связанный с молодежной политикой Вологодской области или школьным ученическим самоуправлением (ШУС). Ребус включает визуальные подсказки, отражающие различные аспекты и мероприятия, проводимые в рамках молодежной политики региона и школьной активности. В результате разгадывания вы должны получить слово или словосочетание, которое нужно будет отправить в ответе на задание.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('фонарь', 2, 'easy', 'Решите ребус по теме молодежной политики Вологодской области и ШУС', '2024-12-05', 'AgACAgIAAxkBAAM9Z00cn0d-pBcWvj8b8RpSXJmtTr0AAgfsMRslY2BK4j_DhAfBASABAAMCAAN4AAM2BA', 'img', '<b>Решите ребус по теме молодежной политики Вологодской области и ШУС</b>
Ваша задача заключается в том, чтобы разгадать ребус, связанный с молодежной политикой Вологодской области или школьным ученическим самоуправлением (ШУС). Ребус включает визуальные подсказки, отражающие различные аспекты и мероприятия, проводимые в рамках молодежной политики региона и школьной активности. В результате разгадывания вы должны получить слово или словосочетание, которое нужно будет отправить в ответе на задание.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('банка', 2, 'easy', 'Решите ребус по теме молодежной политики Вологодской области и ШУС', '2024-12-06', 'AgACAgIAAxkBAANAZ00cojjkn_KuudrZeiaV9rxNGJcAAgjsMRslY2BKr2-BJ_T7YmsBAAMCAAN4AAM2BA', 'img', '<b>Решите ребус по теме молодежной политики Вологодской области и ШУС</b>
Ваша задача заключается в том, чтобы разгадать ребус, связанный с молодежной политикой Вологодской области или школьным ученическим самоуправлением (ШУС). Ребус включает визуальные подсказки, отражающие различные аспекты и мероприятия, проводимые в рамках молодежной политики региона и школьной активности. В результате разгадывания вы должны получить слово или словосочетание, которое нужно будет отправить в ответе на задание.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('лошадь', 2, 'easy', 'Решите ребус по теме молодежной политики Вологодской области и ШУС', '2024-12-09', 'AgACAgIAAxkBAANDZ00cpQY4FT9tcl35hcUAARxr26dqAAIJ7DEbJWNgSss9T6t21BiKAQADAgADbQADNgQ', 'img', '<b>Решите ребус по теме молодежной политики Вологодской области и ШУС</b>
Ваша задача заключается в том, чтобы разгадать ребус, связанный с молодежной политикой Вологодской области или школьным ученическим самоуправлением (ШУС). Ребус включает визуальные подсказки, отражающие различные аспекты и мероприятия, проводимые в рамках молодежной политики региона и школьной активности. В результате разгадывания вы должны получить слово или словосочетание, которое нужно будет отправить в ответе на задание.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('камин', 2, 'easy', 'Решите ребус по теме молодежной политики Вологодской области и ШУС', '2024-12-10', 'AgACAgIAAxkBAANGZ00crMYl0otHEVfJ867kGhDCkJ0AAgrsMRslY2BKU8c6XUh7qcIBAAMCAAN4AAM2BA', 'img', '<b>Решите ребус по теме молодежной политики Вологодской области и ШУС</b>
Ваша задача заключается в том, чтобы разгадать ребус, связанный с молодежной политикой Вологодской области или школьным ученическим самоуправлением (ШУС). Ребус включает визуальные подсказки, отражающие различные аспекты и мероприятия, проводимые в рамках молодежной политики региона и школьной активности. В результате разгадывания вы должны получить слово или словосочетание, которое нужно будет отправить в ответе на задание.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('микробы', 2, 'easy', 'Решите ребус по теме молодежной политики Вологодской области и ШУС', '2024-12-11', 'AgACAgIAAxkBAANJZ00crnEFhA4YYzMQeafggz8AAfq5AAIL7DEbJWNgSiQZP7_f-_CAAQADAgADeAADNgQ', 'img', '<b>Решите ребус по теме молодежной политики Вологодской области и ШУС</b>
Ваша задача заключается в том, чтобы разгадать ребус, связанный с молодежной политикой Вологодской области или школьным ученическим самоуправлением (ШУС). Ребус включает визуальные подсказки, отражающие различные аспекты и мероприятия, проводимые в рамках молодежной политики региона и школьной активности. В результате разгадывания вы должны получить слово или словосочетание, которое нужно будет отправить в ответе на задание.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('лидер', 2, 'easy', 'Решите ребус по теме молодежной политики Вологодской области и ШУС', '2024-12-12', 'AgACAgIAAxkBAANMZ00csBIEg4ESRCxRrKMZpON1btkAAgzsMRslY2BKUM7SudTj3toBAAMCAAN4AAM2BA', 'img', '<b>Решите ребус по теме молодежной политики Вологодской области и ШУС</b>
Ваша задача заключается в том, чтобы разгадать ребус, связанный с молодежной политикой Вологодской области или школьным ученическим самоуправлением (ШУС). Ребус включает визуальные подсказки, отражающие различные аспекты и мероприятия, проводимые в рамках молодежной политики региона и школьной активности. В результате разгадывания вы должны получить слово или словосочетание, которое нужно будет отправить в ответе на задание.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('выборы', 2, 'easy', 'Где логика?', '2024-12-02', 'AgACAgIAAxkBAANPZ00eZBpU-qUippfy9udHcVj3wLYAAiLsMRslY2BKgj-5lX8-QzkBAAMCAAN5AAM2BA AgACAgIAAxkBAANSZ00eZ67Y3mSGA3_g1UcYcEMJdc8AAiPsMRslY2BKXY1R4O_gn-ABAAMCAAN5AAM2BA AgACAgIAAxkBAANVZ00eavcTM6OpSD5z9gsieqcSuJkAAiTsMRslY2BK8i1m4XBuUqcBAAMCAAN4AAM2BA', 'img', '<b>Где логика?</b>
Вам необходимо по трем представленным картинкам определить загаданное слово или словосочетание, связанное с молодежной политикой области или школьным ученическим самоуправлением.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('чашка', 2, 'easy', 'Где логика?', '2024-12-03', 'AgACAgIAAxkBAANYZ00ebXyCrM9glZMj7KLjhOBK11YAAiXsMRslY2BKtyqyuck0c8EBAAMCAAN5AAM2BA AgACAgIAAxkBAANbZ00eb9_Bu618gqHJTCz1DoaM6jIAAibsMRslY2BKPBhiLMm9LG0BAAMCAAN4AAM2BA AgACAgIAAxkBAANeZ00ecTvYR97yaxKrpYtqZ86Mh3EAAifsMRslY2BKYQ1od4EZ41oBAAMCAAN5AAM2BA', 'img', '<b>Где логика?</b>
Вам необходимо по трем представленным картинкам определить загаданное слово или словосочетание, связанное с молодежной политикой области или школьным ученическим самоуправлением.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('сковорода', 2, 'easy', 'Где логика?', '2024-12-04', 'AgACAgIAAxkBAANhZ00eczwo-2UsS12kDQwFMMqm7sUAAijsMRslY2BKBrRTacMQEWQBAAMCAAN4AAM2BA AgACAgIAAxkBAANkZ00edUio7eCaVSa68980aqMX1C4AAinsMRslY2BKalzkym1Zl2YBAAMCAAN4AAM2BA AgACAgIAAxkBAANnZ00eeL2EmMs-_c_RDzISiKLoXGoAAirsMRslY2BKqBhslRdcmrYBAAMCAAN5AAM2BA', 'img', '<b>Где логика?</b>
Вам необходимо по трем представленным картинкам определить загаданное слово или словосочетание, связанное с молодежной политикой области или школьным ученическим самоуправлением.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('конфета', 2, 'easy', 'Где логика?', '2024-12-05', 'AgACAgIAAxkBAANqZ00ee3_ENE0ne88sJ6jokO-5Jv0AAivsMRslY2BKOQMGMstMLjYBAAMCAAN4AAM2BA AgACAgIAAxkBAANtZ00efAjzn0rO2ohTR2tzbc8GJQwAAizsMRslY2BK7uRxLt57d94BAAMCAAN5AAM2BA AgACAgIAAxkBAANwZ00efkvR5UfWDpG2zhShLt87yVIAAi3sMRslY2BKDHVrFzG5bmUBAAMCAAN5AAM2BA', 'img', '<b>Где логика?</b>
Вам необходимо по трем представленным картинкам определить загаданное слово или словосочетание, связанное с молодежной политикой области или школьным ученическим самоуправлением.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('оса', 2, 'easy', 'Где логика?', '2024-12-06', 'AgACAgIAAxkBAANzZ00egJkrn4GRdbtTVwzLxTm6vgoAAi7sMRslY2BKOBUcBg6c-g8BAAMCAAN4AAM2BA AgACAgIAAxkBAAN2Z00egREYF4wAAaGg2nlrFYQ0yVE_AAIv7DEbJWNgSm4ZEBQuifOnAQADAgADbQADNgQ AgACAgIAAxkBAAN5Z00eg-aaThANMGwiIfgdfH_SP-AAAjDsMRslY2BKSk3moUYaJrIBAAMCAAN5AAM2BA', 'img', '<b>Где логика?</b>
Вам необходимо по трем представленным картинкам определить загаданное слово или словосочетание, связанное с молодежной политикой области или школьным ученическим самоуправлением.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('сбор', 2, 'easy', 'Где логика?', '2024-12-09', 'AgACAgIAAxkBAAN8Z00ehf-7vw1T2aCR_0AuOyh__3UAAjHsMRslY2BKWb4p3A-xDuEBAAMCAAN5AAM2BA AgACAgIAAxkBAAN_Z00eiSyxB_5ocX1OHqXbx3ZFFwsAAjLsMRslY2BKAoYiC6tJ89oBAAMCAAN4AAM2BA AgACAgIAAxkBAAOCZ00eizFujEvVylBPUlnkMufqo4cAAjPsMRslY2BK0srOAcLpr2wBAAMCAAN4AAM2BA', 'img', '<b>Где логика?</b>
Вам необходимо по трем представленным картинкам определить загаданное слово или словосочетание, связанное с молодежной политикой области или школьным ученическим самоуправлением.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('стена', 2, 'easy', 'Где логика?', '2024-12-10', 'AgACAgIAAxkBAAOFZ00ejdCkstjjottBGvg8n9Q8eXgAAjTsMRslY2BKTqdZmP0ud54BAAMCAAN5AAM2BA AgACAgIAAxkBAAOIZ00ejzYYIMCTn27kNdgV3NapG-IAAjXsMRslY2BKoadEhV8Lp7ABAAMCAAN4AAM2BA AgACAgIAAxkBAAOLZ00eks-EcbE7AAH7lU_beaqE_I8mAAI27DEbJWNgSgFwmUBF7N5TAQADAgADeAADNgQ', 'img', '<b>Где логика?</b>
Вам необходимо по трем представленным картинкам определить загаданное слово или словосочетание, связанное с молодежной политикой области или школьным ученическим самоуправлением.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('активист', 2, 'easy', 'Где логика?', '2024-12-11', 'AgACAgIAAxkBAAOOZ00elBhU5uY26HpabbsPevJMgQMAAjfsMRslY2BKoDHa8Ynh_PsBAAMCAAN5AAM2BA AgACAgIAAxkBAAORZ00ellQD9I1KZPo12WItZunDMLsAAjjsMRslY2BKQnI1omxk0S8BAAMCAAN5AAM2BA AgACAgIAAxkBAAOUZ00emJV6hvinG9-uKmm3gyJHyhsAAjnsMRslY2BKNagd_DtYGBkBAAMCAAN5AAM2BA', 'img', '<b>Где логика?</b>
Вам необходимо по трем представленным картинкам определить загаданное слово или словосочетание, связанное с молодежной политикой области или школьным ученическим самоуправлением.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('школа', 2, 'easy', 'Где логика?', '2024-12-12', 'AgACAgIAAxkBAAOXZ00emoAs8G7zbXe5kQg5gxT_FBEAAjrsMRslY2BKTOzv5NxHj6IBAAMCAAN4AAM2BA AgACAgIAAxkBAAOaZ00enPuE_s7suXEAAT1BJlast3WhAAI77DEbJWNgSho8nXbn494FAQADAgADeQADNgQ AgACAgIAAxkBAAOdZ00envfcml-iXWJLzhjD5toRDloAAjzsMRslY2BKzPHIlAeVeQYBAAMCAAN5AAM2BA', 'img', '<b>Где логика?</b>
Вам необходимо по трем представленным картинкам определить загаданное слово или словосочетание, связанное с молодежной политикой области или школьным ученическим самоуправлением.

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b> 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('яблоко', 2, 'easy', 'Угадай песню по облаку слов', '2024-12-02', 'AgACAgIAAxkBAAOgZ00f7l9_SEgah52LdCCYOz2ZkuIAAknsMRslY2BKZ5MGlWQCwMEBAAMCAAN4AAM2BA', 'img', '<b>Угадай песню по облаку слов</b>
Вы получили облако слов, в котором собраны ключевые слова из известной песни. Задача участников – по предложенным словам угадать, о какой песне идет речь!

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b>. 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('молодежь', 2, 'easy', 'Угадай песню по облаку слов', '2024-12-03', 'AgACAgIAAxkBAAOjZ00f8lHVOJ4hzYBv2sz0C14ljfQAAkrsMRslY2BKb58fPEyAoyYBAAMCAAN4AAM2BA', 'img', '<b>Угадай песню по облаку слов</b>
Вы получили облако слов, в котором собраны ключевые слова из известной песни. Задача участников – по предложенным словам угадать, о какой песне идет речь!

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b>. 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('регион', 2, 'easy', 'Угадай песню по облаку слов', '2024-12-04', 'AgACAgIAAxkBAAOmZ00f9KXISFjYJo5vAAFcwx3RSE_3AAJL7DEbJWNgSocp12Wkrjy3AQADAgADeAADNgQ', 'img', '<b>Угадай песню по облаку слов</b>
Вы получили облако слов, в котором собраны ключевые слова из известной песни. Задача участников – по предложенным словам угадать, о какой песне идет речь!

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b>. 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('вологда', 2, 'easy', 'Угадай песню по облаку слов', '2024-12-05', 'AgACAgIAAxkBAAOpZ00f9-kAAXFxsruHp7BlNoq6mHxxAAJM7DEbJWNgSnGdmxqXShdTAQADAgADeAADNgQ', 'img', '<b>Угадай песню по облаку слов</b>
Вы получили облако слов, в котором собраны ключевые слова из известной песни. Задача участников – по предложенным словам угадать, о какой песне идет речь!

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b>. 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('никто', 2, 'easy', 'Угадай песню по облаку слов', '2024-12-06', 'AgACAgIAAxkBAAOsZ00f-k-XPG-5oUZwbvvafiLIvHUAAk3sMRslY2BKW2v8ZSDE7vEBAAMCAAN4AAM2BA', 'img', '<b>Угадай песню по облаку слов</b>
Вы получили облако слов, в котором собраны ключевые слова из известной песни. Задача участников – по предложенным словам угадать, о какой песне идет речь!

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b>. 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('знак', 2, 'easy', 'Угадай песню по облаку слов', '2024-12-09', 'AgACAgIAAxkBAAOvZ00f_9VAlYHjmnCO16ZFzom5-Z4AAk7sMRslY2BKjFUCTMFVXOEBAAMCAAN4AAM2BA', 'img', '<b>Угадай песню по облаку слов</b>
Вы получили облако слов, в котором собраны ключевые слова из известной песни. Задача участников – по предложенным словам угадать, о какой песне идет речь!

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b>. 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('лук', 2, 'easy', 'Угадай песню по облаку слов', '2024-12-10', 'AgACAgIAAxkBAAOyZ00gAQABHMkaJk0C0iOPye0-vzOAAAJP7DEbJWNgShMvTbHdensLAQADAgADeAADNgQ', 'img', '<b>Угадай песню по облаку слов</b>
Вы получили облако слов, в котором собраны ключевые слова из известной песни. Задача участников – по предложенным словам угадать, о какой песне идет речь!

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b>. 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('листы', 2, 'easy', 'Угадай песню по облаку слов', '2024-12-11', 'AgACAgIAAxkBAAO1Z00gBjd816mwyZST23iO1b_ghMYAAlDsMRslY2BKcLTLj52EnxMBAAMCAAN4AAM2BA', 'img', '<b>Угадай песню по облаку слов</b>
Вы получили облако слов, в котором собраны ключевые слова из известной песни. Задача участников – по предложенным словам угадать, о какой песне идет речь!

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b>. 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.'),
        ('шок', 2, 'easy', 'Угадай песню по облаку слов', '2024-12-12', 'AgACAgIAAxkBAAO4Z00gCQQ-PaECzEulnUpYoYyHCDoAAlHsMRslY2BKm8_jbHglv48BAAMCAAN4AAM2BA', 'img', '<b>Угадай песню по облаку слов</b>
Вы получили облако слов, в котором собраны ключевые слова из известной песни. Задача участников – по предложенным словам угадать, о какой песне идет речь!

<b>Критерии:</b>
Правильный ответ – 2 балла.
<b>Максимальное количество баллов:</b>. 2 балла.
<b>Срок сдачи задания:</b> до 18:00 текущего дня.')
        """
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM tasks WHERE key_word IN ('тест',
'мем',
'буквы',
'кроссворд',
'замок',
'пингвин',
'чайник',
'фонарь',
'банка',
'лошадь',
'камин',
'микробы',
'лидер',
'выборы',
'чашка',
'сковорода',
'конфета',
'оса',
'сбор',
'стена',
'активист',
'школа',
'яблоко',
'молодежь',
'регион',
'вологда',
'никто',
'знак',
'лук',
'листы',
'шок')
        """
    )
