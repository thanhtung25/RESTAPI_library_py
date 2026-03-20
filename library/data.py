from datetime import date, datetime
from .extension import db
from .model import Users, Categories, Authors, Books, BookCopies


def seed_basic_library_data():
    # =========================
    # 1. USERS (10)
    # =========================
    users = [
        Users(
            full_name="Иван Петров",
            birth_day=date(2007, 3, 15),
            gender="мужской",
            email="ivan.petrov@example.ru",
            phone="+79990000001",
            username="ivan_petrov",
            password="123456",
            role="reader",
            status="active",
            library_card="LIB001",
            address="г. Москва, ул. Ленина, д. 12",
            avatar_url="http://127.0.0.1:5000/static/uploads/avatars/ivan_petrov.jpg"
        ),
        Users(
            full_name="Анна Смирнова",
            birth_day=date(2006, 7, 21),
            gender="женский",
            email="anna.smirnova@example.ru",
            phone="+79990000002",
            username="anna_smirnova",
            password="123456",
            role="reader",
            status="active",
            library_card="LIB002",
            address="г. Москва, пр-т Мира, д. 45",
            avatar_url="http://127.0.0.1:5000/static/uploads/avatars/anna_smirnova.jpg"
        ),
        Users(
            full_name="Дмитрий Кузнецов",
            birth_day=date(2005, 11, 9),
            gender="мужской",
            email="dmitry.kuznetsov@example.ru",
            phone="+79990000003",
            username="dmitry_kuznetsov",
            password="123456",
            role="reader",
            status="active",
            library_card="LIB003",
            address="г. Казань, ул. Баумана, д. 8",
            avatar_url="http://127.0.0.1:5000/static/uploads/avatars/dmitry_kuznetsov.jpg"
        ),
        Users(
            full_name="Екатерина Иванова",
            birth_day=date(2008, 1, 30),
            gender="женский",
            email="ekaterina.ivanova@example.ru",
            phone="+79990000004",
            username="ekaterina_ivanova",
            password="123456",
            role="reader",
            status="active",
            library_card="LIB004",
            address="г. Санкт-Петербург, Невский проспект, д. 20",
            avatar_url="http://127.0.0.1:5000/static/uploads/avatars/ekaterina_ivanova.jpg"
        ),
        Users(
            full_name="Сергей Волков",
            birth_day=date(2004, 5, 18),
            gender="мужской",
            email="sergey.volkov@example.ru",
            phone="+79990000005",
            username="sergey_volkov",
            password="123456",
            role="reader",
            status="active",
            library_card="LIB005",
            address="г. Нижний Новгород, ул. Горького, д. 17",
            avatar_url="http://127.0.0.1:5000/static/uploads/avatars/sergey_volkov.jpg"
        ),
        Users(
            full_name="Мария Соколова",
            birth_day=date(2007, 9, 2),
            gender="женский",
            email="maria.sokolova@example.ru",
            phone="+79990000006",
            username="maria_sokolova",
            password="123456",
            role="reader",
            status="active",
            library_card="LIB006",
            address="г. Екатеринбург, ул. Малышева, д. 31",
            avatar_url="http://127.0.0.1:5000/static/uploads/avatars/maria_sokolova.jpg"
        ),
        Users(
            full_name="Алексей Морозов",
            birth_day=date(2006, 12, 14),
            gender="мужской",
            email="alexey.morozov@example.ru",
            phone="+79990000007",
            username="alexey_morozov",
            password="123456",
            role="reader",
            status="active",
            library_card="LIB007",
            address="г. Самара, ул. Победы, д. 6",
            avatar_url="http://127.0.0.1:5000/static/uploads/avatars/alexey_morozov.jpg"
        ),
        Users(
            full_name="Ольга Васильева",
            birth_day=date(2005, 4, 25),
            gender="женский",
            email="olga.vasilyeva@example.ru",
            phone="+79990000008",
            username="olga_vasilyeva",
            password="123456",
            role="reader",
            status="active",
            library_card="LIB008",
            address="г. Новосибирск, Красный проспект, д. 50",
            avatar_url="http://127.0.0.1:5000/static/uploads/avatars/olga_vasilyeva.jpg"
        ),
        Users(
            full_name="Наталья Орлова",
            birth_day=date(1990, 8, 11),
            gender="женский",
            email="n.orlova@library.ru",
            phone="+79990000009",
            username="natalya_orlova",
            password="123456",
            role="librarian",
            status="active",
            library_card="LIB009",
            address="г. Москва, ул. Тверская, д. 5",
            avatar_url="http://127.0.0.1:5000/static/uploads/avatars/natalya_orlova.jpg"
        ),
        Users(
            full_name="Андрей Павлов",
            birth_day=date(1987, 2, 6),
            gender="мужской",
            email="a.pavlov@library.ru",
            phone="+79990000010",
            username="andrey_pavlov",
            password="123456",
            role="librarian",
            status="active",
            library_card="LIB010",
            address="г. Москва, ул. Арбат, д. 14",
            avatar_url="http://127.0.0.1:5000/static/uploads/avatars/andrey_pavlov.jpg"
        ),
    ]

    db.session.add_all(users)
    db.session.commit()

    # =========================
    # 2. CATEGORIES
    # =========================
    categories = [
        Categories(name="Русская классика", description="Произведения русской классической литературы"),
        Categories(name="Зарубежная классика", description="Произведения зарубежной классической литературы"),
        Categories(name="Фантастика", description="Научная фантастика и фэнтези"),
        Categories(name="Психология", description="Книги по психологии и саморазвитию"),
        Categories(name="Научно-популярная литература", description="Научно-популярные издания для молодежи"),
        Categories(name="Подростковая литература", description="Современная литература для подростков и юношества"),
    ]

    db.session.add_all(categories)
    db.session.commit()

    category_map = {c.name: c.id_category for c in Categories.query.all()}

    # =========================
    # 3. AUTHORS
    # =========================
    authors = [
        Authors(full_name="Александр Пушкин", biography="Русский поэт, драматург и прозаик."),
        Authors(full_name="Михаил Лермонтов", biography="Русский поэт, прозаик и драматург."),
        Authors(full_name="Лев Толстой", biography="Русский писатель, мыслитель и публицист."),
        Authors(full_name="Фёдор Достоевский", biography="Русский писатель, классик мировой литературы."),
        Authors(full_name="Антон Чехов", biography="Русский писатель, драматург, врач."),
        Authors(full_name="Жюль Верн", biography="Французский писатель, один из основоположников научной фантастики."),
        Authors(full_name="Рэй Брэдбери", biography="Американский писатель, автор фантастических произведений."),
        Authors(full_name="Дэниел Киз", biography="Американский писатель, автор психологической прозы."),
        Authors(full_name="Джоан Роулинг", biography="Британская писательница, автор серии о Гарри Поттере."),
        Authors(full_name="Антуан де Сент-Экзюпери", biography="Французский писатель и лётчик."),
        Authors(full_name="Борис Васильев", biography="Русский писатель, автор произведений о войне и нравственном выборе."),
        Authors(full_name="Аркадий и Борис Стругацкие", biography="Советские писатели-фантасты."),
    ]

    db.session.add_all(authors)
    db.session.commit()

    author_map = {a.full_name: a.id_author for a in Authors.query.all()}

    # =========================
    # 4. BOOKS (20)
    # =========================
    books = [

    Books(
        id_category=category_map["Подростковая литература"],
        id_author=author_map["Антуан де Сент-Экзюпери"],
        title="Маленький принц",
        isbn="978-5-00101-1001",
        language="Русский",
        publish_year=1943,
        description="Философская сказка, посвящённая вопросам дружбы, любви, ответственности и смысла жизни. Произведение широко используется в образовательной практике и рекомендовано для чтения подростками благодаря глубокому содержанию и доступному языку изложения.",
        image_url="http://127.0.0.1:5000/static/uploads/books/malenkiy_princ.jpg"
    ),

    Books(
        id_category=category_map["Подростковая литература"],
        id_author=author_map["Джоан Роулинг"],
        title="Гарри Поттер и философский камень",
        isbn="978-5-00101-1002",
        language="Русский",
        publish_year=1997,
        description="Первая книга популярной серии о юном волшебнике Гарри Поттере. Произведение рассказывает о взрослении, дружбе, выборе между добром и злом и является одной из самых востребованных книг среди подростков и молодежи.",
        image_url="http://127.0.0.1:5000/static/uploads/books/hp1.jpg"
    ),

    Books(
        id_category=category_map["Подростковая литература"],
        id_author=author_map["Джоан Роулинг"],
        title="Гарри Поттер и Тайная комната",
        isbn="978-5-00101-1003",
        language="Русский",
        publish_year=1998,
        description="Продолжение истории о приключениях учеников школы Хогвартс. Книга посвящена вопросам смелости, дружбы и ответственности за собственные поступки. Рекомендуется для чтения подросткам среднего школьного возраста.",
        image_url="http://127.0.0.1:5000/static/uploads/books/hp2.jpg"
    ),

    Books(
        id_category=category_map["Фантастика"],
        id_author=author_map["Рэй Брэдбери"],
        title="451 градус по Фаренгейту",
        isbn="978-5-00101-1004",
        language="Русский",
        publish_year=1953,
        description="Научно-фантастический роман-антиутопия, поднимающий вопросы роли книги и образования в жизни общества. Произведение рекомендовано для старшего школьного и юношеского возраста.",
        image_url="http://127.0.0.1:5000/static/uploads/books/451.jpg"
    ),

    Books(
        id_category=category_map["Фантастика"],
        id_author=author_map["Аркадий и Борис Стругацкие"],
        title="Пикник на обочине",
        isbn="978-5-00101-1005",
        language="Русский",
        publish_year=1972,
        description="Фантастическое произведение, рассказывающее о загадочной Зоне и людях, исследующих неизвестные явления. Книга способствует развитию интереса подростков к научной фантастике и философским вопросам.",
        image_url="http://127.0.0.1:5000/static/uploads/books/piknik.jpg"
    ),

    Books(
        id_category=category_map["Русская классика"],
        id_author=author_map["Александр Пушкин"],
        title="Капитанская дочка",
        isbn="978-5-00101-1006",
        language="Русский",
        publish_year=1836,
        description="Исторический роман, включённый в школьную программу. Произведение воспитывает чувство чести, долга и патриотизма и широко используется в работе юношеских библиотек.",
        image_url="http://127.0.0.1:5000/static/uploads/books/pushkin1.jpg"
    ),

    Books(
        id_category=category_map["Русская классика"],
        id_author=author_map["Александр Пушкин"],
        title="Евгений Онегин",
        isbn="978-5-00101-1007",
        language="Русский",
        publish_year=1833,
        description="Роман в стихах, изучаемый в старших классах школы. Книга помогает формированию литературного вкуса и пониманию классической русской культуры.",
        image_url="http://127.0.0.1:5000/static/uploads/books/onegin.jpg"
    ),

    Books(
        id_category=category_map["Русская классика"],
        id_author=author_map["Михаил Лермонтов"],
        title="Герой нашего времени",
        isbn="978-5-00101-1008",
        language="Русский",
        publish_year=1840,
        description="Психологический роман, раскрывающий особенности характера человека и общества. Рекомендуется для старшего школьного возраста.",
        image_url="http://127.0.0.1:5000/static/uploads/books/lermontov.jpg"
    ),

    Books(
        id_category=category_map["Русская классика"],
        id_author=author_map["Антон Чехов"],
        title="Каштанка",
        isbn="978-5-00101-1009",
        language="Русский",
        publish_year=1887,
        description="Классический рассказ, рекомендованный для подростков. Произведение развивает чувство сострадания и нравственные качества.",
        image_url="http://127.0.0.1:5000/static/uploads/books/kashtanka.jpg"
    ),

]

    db.session.add_all(books)
    db.session.commit()

    book_map = {b.title: b.id_book for b in Books.query.all()}

    # =========================
    # 5. BOOK COPIES (20)
    # mỗi sách 1 bản
    # =========================
    copies = [
    BookCopies(id_book=1,  barcode="06-001-010-RU-1943", qr_code="QR-06-001-010-RU-1943", location="1-1-01", received_date=date(2024, 1, 10), condition="отличное", status="available"),
    BookCopies(id_book=2,  barcode="06-002-009-RU-1997", qr_code="QR-06-002-009-RU-1997", location="1-1-02", received_date=date(2024, 1, 11), condition="отличное", status="available"),
    BookCopies(id_book=3,  barcode="06-003-009-RU-1998", qr_code="QR-06-003-009-RU-1998", location="1-1-03", received_date=date(2024, 1, 12), condition="хорошее", status="borrowed"),
    BookCopies(id_book=4,  barcode="03-004-007-RU-1953", qr_code="QR-03-004-007-RU-1953", location="1-2-01", received_date=date(2024, 1, 13), condition="хорошее", status="available"),
    BookCopies(id_book=5,  barcode="03-005-012-RU-1972", qr_code="QR-03-005-012-RU-1972", location="1-2-02", received_date=date(2024, 1, 14), condition="удовлетворительное", status="reserved"),

    BookCopies(id_book=6,  barcode="01-006-001-RU-1836", qr_code="QR-01-006-001-RU-1836", location="1-2-03", received_date=date(2024, 1, 15), condition="отличное", status="available"),
    BookCopies(id_book=7,  barcode="01-007-001-RU-1833", qr_code="QR-01-007-001-RU-1833", location="1-3-01", received_date=date(2024, 1, 16), condition="хорошее", status="available"),
    BookCopies(id_book=8,  barcode="01-008-002-RU-1840", qr_code="QR-01-008-002-RU-1840", location="1-3-02", received_date=date(2024, 1, 17), condition="хорошее", status="borrowed"),
    BookCopies(id_book=9,  barcode="01-009-005-RU-1887", qr_code="QR-01-009-005-RU-1887", location="1-3-03", received_date=date(2024, 1, 18), condition="отличное", status="available"),
]

    db.session.add_all(copies)
    db.session.commit()

    print("✅ Đã seed xong: 10 users, 20 books, 20 copies.")