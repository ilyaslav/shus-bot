"""fill hard tasks

Revision ID: 883bbb51afd3
Revises: 1e55b8d174a9
Create Date: 2024-12-02 00:24:31.577872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '883bbb51afd3'
down_revision: Union[str, None] = '1e55b8d174a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO tasks (key_word, reward, type, button_name, text) VALUES
        ('подкаст', 26, 'hard', 'Видеоподскаст с руководителем органа ШУС', '<b>Видеоподскаст с руководителем органа ШУС</b>
Вам необходимо записать видеоподкаст с руководителем органа ШУС (президентом/председателем из числа обучающихся) в образовательной организации на тему «Школьное ученическое самоуправление».

<b>Требование:</b>
Написать пост ВКонтакте, в сообществе своего органа ШУС или на странице образовательной организации и прислать на него ссылку @shinshila_shus. Пост должен включать небольшой содержательный текст, отражающий суть задания, а также видеоролик продолжительностью не более 3 минут с обсуждением тем, относящихся к деятельности органа ШУС, самоуправлению, работе в команде. Пост публикуется с хештегом #Команда_ШУС2024.

<b>Критерии оценки:</b>
1. Оригинальность и креативность – 0–1.
2. Содержательность видеоподскаста – 0–15.
3. Качество видео и звука – 0–5.
4. Текст поста – 0–5.

<b>Максимальное количество баллов:</b> 26 баллов.
<b>Срок сдачи задания:</b> до 23:59 12 декабря 2024 года.'),
        ('аудио', 26, 'hard', 'Аудиоподскаст с руководителем органа ШУС', '<b>Аудиоподскаст с руководителем органа ШУС</b>
Вам необходимо записать аудиооподкаст с руководителем органа ШУС (президентом/председателем из числа обучающихся) в образовательной организации на тему «Ученическое самоуправление: подготовка к успешной взрослой жизни».

<b>Требования:</b>
Написать пост ВКонтакте, в сообществе своего органа ШУС или на странице образовательной организации и прислать на него ссылку @shinshila_shus. Пост должен включать небольшой содержательный текст отражающий суть задания, а также аудиофайл продолжительностью не более 3 минут с обсуждением тем, относящихся к самоуправлению, как социальному лифту, лидерских качеств активистов, самоуправления, как ступени к успешной взрослой жизни и т. д. Пост публикуется с хештегом #Команда_ШУС2024.

<b>Критерии оценки:</b>
1. Оригинальность и креативность – 0–1.
2. Содержательность – 0–15.
3. Качество звука – 0–1.
4. Текст поста – 0–5.

<b>Максимальное количество баллов:</b> 26 баллов.
<b>Срок сдачи задания:</b> до 23:59 12 декабря 2024 года.'),
        ('встреча', 25, 'hard', 'Профориентационная встреча', '<b>Профориентационная встреча</b>
Вам необходимо провести профориентационную встречу с человеком интересной профессии о его профессиональном пути.
Цель – знакомство обучающихся с интересной профессией, профориентация. Возможные форматы: дискуссия, игровой вечер, классная встреча и др. – на выбор участников конкурса.

<b>Требования:</b>
1. Целевая аудитория: обучающиеся школы 8–11 классов.
2. Участие всех членов команды в организации всех этапов встречи.
3. Приглашенный гость НЕ должен быть сотрудником школы.
4. Продолжительность встречи: 45 минут.
5. Написать пост ВКонтакте, в сообществе своего органа ШУС или на странице образовательной организации, и прислать на него ссылку @shinshila_shus. Пост должен включать небольшой содержательный текст, отражающий содержание и суть встречи, а также фото или видео со встречи. В посте должна быть отражена профессия гостя и количество обучающихся, посетивших встречу. Пост публикуется с хештегом #Команда_ШУС2024.


<b>Критерии оценки:</b>
1. Содержательность встречи– 0–15.
2. Написание поста – 0–10.
<b>Максимальное количество баллов:</b> 25 баллов.
<b>Срок сдачи задания:</b> до 23:59 12 декабря 2024 года.'),
        ('презентация', 25, 'hard', 'Презентация ШУС для учеников своей школы, не состоящих в органах ШУС', '<b>Презентация ШУС для учеников своей школы не состоящих в органах ШУС</b>
Ваша задача – провести очную презентацию ШУС для учеников своей школы (охватить как можно больше обучающихся).
Цель презентации – рассказать школьникам, НЕ состоящим в органе ШУС, о деятельности органа ШУС в их школе так, чтобы они захотели вступить.

<b>Требования:</b>
1.Целевая аудитория: школьники 11–17 лет.
2.Продолжительность презентации: до 20 минут.
3.Визуальное сопровождение презентации может быть любым (видеоролик, презентация, фоторяд и т. д.).
4.Пост ВКонтакте в сообществе своего органа ШУС или на странице образовательной организации. Пост должен отражать краткую концепцию презентации, характеристику организаторов и участников, цель проведения и должен содержать хештег #Команда_ШУС2024.
5.В момент проведения презентации необходимо отправить от 2 до 4 видеосообщений. Перед первым видеособщением необходимо написать название команды и название задания.
6.Ссылку на пост, видеосообщения, файлы визуального ряда необходимо направить в личные сообщения Шиншилле Сушке (@shinshila_shus).

<b>Критерии оценки:</b>
1. Содержательность презентации – 0–10.
2. Качество визуального ряда – 0–5.
3. Написание поста – 0–5.
4. Отражение этапов презентации в видеосообщениях – 0–5.

<b>Максимальное количество баллов:</b> 25 баллов.
<b>Срок сдачи задания:</b> до 23:59 12 декабря 2024 года.')
        """
    )

    op.execute(
        """
            INSERT INTO tasks (key_word, reward, type, button_name, attachments, attachment_type, text) VALUES
            ('предприниматель', 32, 'hard', 'Предпринимательская игра', 'BQACAgIAAxkBAAPZZ00huxvyzzuiInGec4vp2x51ng0AAstUAALDHmhKJhnQqJ4IuCU2BA BQACAgIAAxkBAAPcZ00hv7YZRzAQiNtOzj2e5vdGbuIAAsxUAALDHmhKvnBS4vUoQt42BA BQACAgIAAxkBAAPfZ00hwrH2JSteEqU7s3amQXGogVUAAs1UAALDHmhKrzRdBIq-4TI2BA', 'doc', '<b>Предпринимательская игра</b>
Вам необходимо спланировать, провести и проанализировать мероприятие в школе, направленное на развитие ШУС, в формате предпринимательской игры.

<b>Требования:</b>
1. Продолжительность: 45 минут.
2. Тематика и/или наполнение мероприятия должны быть связаны с ученическим самоуправлением.
3. Для проведения мероприятия необходимо заполнить файл «Концепция» по форме.
4.Участие всех членов команды в организации всех этапов игры.
5.В момент проведения необходимо отправить от 5 до 10 видеосообщений с описанием событий внутри игры во время проведения. Перед первым видеосообщением написать название задания.
6.После проведения мероприятия необходимо собрать обратную связь с участников, провести рефлексию внутри команды и заполнить файл «Анализ мероприятия» по форме.
7.По окончании мероприятия команда должна подготовить пост на странице группы в ВКонтакте образовательной организации или органа ШУС, о проведенном мероприятии, его целях, результатах и интересных моментах с прикреплением фото-видеоматериалов и хештегом #Команда_ШУС2024.
8.Ссылку на пост, файлы «Концепция» и «Анализ мероприятия» необходимо направить в личные сообщения Шиншилле Сушке (@shinshila_shus).

<b>Критерии:</b>
1. Оригинальность и креативность – 0–5.
2. Отражение этапов игры в видеосообщениях – 0–5.
3. Участие всей команды в проведении игры – 0–1.
4. Написание поста – 0–1.
5. Документирование и отчетность (качественно и правильно заполненная концепция, и анализ) – 0–20.

<b>Максимальное количество баллов:</b> 32 балла.
<b>Срок сдачи задания:</b> до 23:59 ч. 12 декабря 2024 года.'),
            ('квиз', 32, 'hard', 'Квиз', 'BQACAgIAAxkBAAPQZ00hf0weOpQJv-twuRtygHdF8dsAAshUAALDHmhKuzkok3UYfEM2BA BQACAgIAAxkBAAPTZ00hg7Ti4_i8wpQOSlu5qEI7UjIAAslUAALDHmhK_yLNKCsXdMk2BA BQACAgIAAxkBAAPWZ00hhqoH4sPdORU4NEl7neJeOuAAAspUAALDHmhKUbB9aSt9aHY2BA', 'doc', '<b>Квиз</b>
Вам необходимо спланировать, провести и проанализировать мероприятие в школе направленное на развитие ШУС, в формате квиза.

<b>Требования:</b>
1.Продолжительность: 45 минут.
2.Тематика и/или наполнение мероприятия должны быть связаны с ученическим самоуправлением.
3.Для проведения мероприятия необходимо заполнить файл «Концепция» по форме.
4.Участие всех членов команды в организации всех этапов игры.
5.В момент проведения необходимо отправить от 5 до 10 видеосообщений с описанием событий внутри игры во время проведения. Перед первым видеосообщением написать название задания.
6.После проведения мероприятия необходимо собрать обратную связь с участников, провести рефлексию внутри команды и заполнить файл «Анализ мероприятия» по форме.
7.По окончании мероприятия команда должна подготовить пост на странице группы в ВКонтакте образовательной организации или органа ШУС, о проведенном мероприятии, его целях, результатах и интересных моментах с прикреплением фото-видеоматериалов и хештегом #Команда_ШУС2024.
8.Ссылку на пост, файлы «Концепция» и «Анализ мероприятия» необходимо направить в личные сообщения Шиншилле Сушке (@shinshila_shus).

<b>Критерии:</b>
1. Оригинальность и креативность – 0–5.
2. Отражение этапов игры в видеосообщениях – 0–5.
3. Участие всей команды в проведении игры – 0–1.
4. Написание поста – 0–1.
5. Документирование и отчетность (качественно и правильно заполненная концепция, и анализ) – 0–20.

<b>Максимальное количество баллов:</b> 32 балла.
<b>Срок сдачи задания:</b> до 23:59 ч. 12 декабря 2024 года.'),
            ('детектив', 32, 'hard', 'Детективный квест (не по станциям)', 'BQACAgIAAxkBAAPHZ00hLmJhNkao-Aw5vFDmbqjupRQAAsVUAALDHmhKeCLaUUsT__42BA BQACAgIAAxkBAAPKZ00hMd2fzvqw3OZ1qku40XusFxoAAsZUAALDHmhKI2oWyDP4BMY2BA BQACAgIAAxkBAAPNZ00hNAsnJjtq7ij6du4vzDWpKBgAAsdUAALDHmhKKhnKY-ofvg82BA', 'doc', '<b>Детективный квест (не по станциям)</b>
Вам необходимо спланировать, провести и проанализировать мероприятие в школе направленное на развитие ШУС, в формате квеста.

<b>Требования:</b>
1.Продолжительность: 45 минут.
2.Тематика и/или наполнение мероприятия должны быть связаны с ученическим самоуправлением.
3.Для проведения мероприятия необходимо заполнить файл «Концепция» по форме.
4.Участие всех членов команды в организации всех этапов игры.
5.В момент проведения необходимо отправить от 5 до 10 видеосообщений с описанием событий внутри игры во время проведения. Перед первым видеосообщением написать название задания.
6.После проведения мероприятия необходимо собрать обратную связь с участников, провести рефлексию внутри команды и заполнить файл «Анализ мероприятия» по форме.
7.По окончании мероприятия команда должна подготовить пост на странице группы в ВКонтакте образовательной организации или органа ШУС, о проведенном мероприятии, его целях, результатах и интересных моментах с прикреплением фото-видеоматериалов и хештегом #Команда_ШУС2024.
8.Ссылку на пост, файлы «Концепция» и «Анализ мероприятия» необходимо направить в личные сообщения Шиншилле Сушке (@shinshila_shus).

<b>Критерии:</b>
1. Оригинальность и креативность – 0–5.
2. Отражение этапов игры в видеосообщениях – 0–5.
3. Участие всей команды в проведении игры – 0–1.
4. Написание поста – 0–1.
5. Документирование и отчетность (качественно и правильно заполненная концепция, и анализ) – 0–20.

<b>Максимальное количество баллов:</b> 32 балла.
<b>Срок сдачи задания:</b> до 23:59 ч. 12 декабря 2024 года.'),
            ('знакомство', 32, 'hard', 'Шоу-игра на знакомство между классами в параллели', 'BQACAgIAAxkBAAO-Z00gwmp2J6h-ieQAAcQyvwcIvgPoAALCVAACwx5oSpjrm5WwpwT7NgQ BQACAgIAAxkBAAPBZ00gxbe4MWpbHJBSRxmWpLQCXs8AAsNUAALDHmhK6cfQXmg5lR02BA BQACAgIAAxkBAAPEZ00gyIqxhaiz1d5C9FCKyf9BFKUAAsRUAALDHmhKGuqiFsMWJ202BA', 'doc', '<b>Шоу-игра на знакомство между классами в параллели.</b>
Вам необходимо спланировать, провести и проанализировать мероприятие в школе направленное на развитие ШУС, в формате шоу-игры.

<b>Требования:</b>
1.Продолжительность: 45 минут.
2.Тематика и/или наполнение мероприятия должны быть связаны с ученическим самоуправлением.
3.Для проведения мероприятия необходимо заполнить файл «Концепция» по форме.
4.Участие всех членов команды в организации всех этапов игры.
5.В момент проведения необходимо отправить от 5 до 10 видеосообщений с описанием событий внутри игры во время проведения. Перед первым видеосообщением написать название задания.
6.После проведения мероприятия необходимо собрать обратную связь с участников, провести рефлексию внутри команды и заполнить файл «Анализ мероприятия» по форме.
7.По окончании мероприятия команда должна подготовить пост на странице группы в ВКонтакте образовательной организации или органа ШУС, о проведенном мероприятии, его целях, результатах и интересных моментах с прикреплением фото-видеоматериалов и хештегом #Команда_ШУС2024.
8.Ссылку на пост, файлы «Концепция» и «Анализ мероприятия» необходимо направить в личные сообщения Шиншилле Сушке (@shinshila_shus).

<b>Критерии:</b>
1. Оригинальность и креативность – 0–5.
2. Отражение этапов игры в видеосообщениях – 0–5.
3. Участие всей команды в проведении игры – 0–1.
4. Написание поста – 0–1.
5. Документирование и отчетность (качественно и правильно заполненная концепция, и анализ) – 0–20.

<b>Максимальное количество баллов:</b> 32 балла.
<b>Срок сдачи задания:</b> до 23:59 ч. 12 декабря 2024 года.'),
            ('занятие', 25, 'hard', 'Занятие для членов органа ШУС', 'BQACAgIAAxkBAAO7Z00gvYg6n2xuKcAugnk-BLTsfo0AAsFUAALDHmhKiCa68WepR_c2BA', 'doc', '<b>Занятие для членов органа ШУС</b>
Вам необходимо провести занятие для членов органа ШУС на актуальную тему для развития вашей команды органа ШУС.
Цель – повысить уровень знаний и понимания деятельности органа ШУС.

<b>Требования:</b>
1.Длительность занятия: от 20 до 40 минут.
2.В момент проведения занятия необходимо отправить от 2 до 4 видеосообщений в Telegram @shinshila_shus, отображающих разные этапы проведения занятия. Перед первым видеособщением необходимо написать название команды и название задания.
3.Направить форму с описанием концепции занятия.

<b>Критерии оценки:</b>
1. Документирование и отчетность (качественно и правильно заполненная форма описания занятия) – 0–20.
2. Написание поста – 0-5.
3. Отражение этапов в видеосообщениях – 0-5.

<b>Максимальное количество баллов:</b> 25 баллов.
<b>Срок сдачи задания:</b> до 23:59 12 декабря 2024 года.')
        """
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM tasks WHERE key_word IN ('подкаст',
'аудио',
'встреча',
'презентация',
'предприниматель',
'квиз',
'детектив',
'знакомство',
'занятие'
)
        """
    )
