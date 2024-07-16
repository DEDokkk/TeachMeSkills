popular_science_article = dict(dbname="psadb", user="victor", password="12345", host="127.0.0.1", port="5432")
journalistic_article = dict(dbname="jadb", user="andry", password="12345", host="127.0.0.1", port="5432")
literary_article = dict(dbname="ladb", user="vasia", password="12345", host="127.0.0.1", port="5432")

pull_db = {1: popular_science_article,
           2: journalistic_article,
           3: literary_article}

create_table_command = {'author_db': {'author': "CREATE TABLE author ("
                                                "author_id SERIAL PRIMARY KEY, "
                                                "author_name VARCHAR(100) NOT NULL UNIQUE"
                                                ");",

                                      'article': "CREATE TABLE article ("
                                                 "article_id SERIAL PRIMARY KEY, "
                                                 "article_name VARCHAR(250) NOT NULL, "
                                                 "article_text TEXT NOT NULL, "
                                                 "fk_article_author INT REFERENCES author(author_id)"
                                                 ");",

                                      'comment': "CREATE TABLE comment ("
                                                 "comment_id SERIAL PRIMARY KEY, "
                                                 "comment_text VARCHAR(400) NOT NULL, "
                                                 "rating INT NOT NULL, "
                                                 "fk_comment_article INT REFERENCES article(article_id)"
                                                 ");"}
                        }


text_info = "Добро пожаловать! Данная программа предназначена для управления базами данных «Библиотеки». \n" \
            "Здесь вы можете управлять одновременно несколькими базами данных, \n" \
            "каждая база хранит в себе отдельные стили статей, с их авторами, \n" \
            "а также комментариями к статьям и рейтингом этих статей.\n" \
            "Доступные Вам базы:\n" \
            "1. popular science article (краткое название: psadb;\n" \
            "2. journalistic article (кратное название: jadb;\n" \
            "3. literary article (кратное название: ladb;\n" \
            "Статья должна иметь автора\n" \
            "Для получения инструкции к использованию введите команду help."
text_help = "тут должен быть текст с описанием команд, пока в разработке!"
