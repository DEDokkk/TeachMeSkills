from postgres_manager.managers import PostgresManager
from postgres_manager.instances import UserRole, PostgresDB
from author.db_table_settings import pull_db, create_table_command, text_info, text_help
from author.author_management import *
from prettytable import from_db_cursor


class AuthorDBManager:
    def __init__(self, db_number: int):
        if db_number in pull_db:
            self.user = UserRole(pull_db[db_number]['user'], pull_db[db_number]['password'])
            self.db = PostgresDB(pull_db[db_number]['dbname'], self.user)
        else:
            raise ValueError('параметров такой таблицы не найдено')
        self.postman = None
        self.author = AuthorManager
        self.article = ArticleManager
        self.comment = CommentManager

    def create_db(self):
        self.postman = PostgresManager(self.db, True)
        print(f'DB: {self.db.name} create!')
        self.postman.cursor.execute(f"{create_table_command['author_db']['author']}")
        self.postman.cursor.execute(f"{create_table_command['author_db']['article']}")
        self.postman.cursor.execute(f"{create_table_command['author_db']['comment']}")
        self.postman = None

    def connection_to_base(self):
        self.postman = PostgresManager(self.db)

    def close_connection(self):
        self.postman.close_cursor()
        self.postman.close_connection()
        self.postman = None

    def write_into_a_table(self, author_name: str, article_name=None, text_article_or_comment=None, rating=None):
        if not self.postman:
            print('не выполнено подключение к базе')
            return
        if not article_name:
            # передано только имя автора, записываем его в таблицу
            try:
                self.postman.cursor.execute(self.author.write_into_a_table('author', author_name))
                return
            except:
                print('Такой автор уже записан в таблицу')
                return
        if not rating:
            # предано имя автора, название статьи и текст, без рейтинга, значит текст это текст статьи
            # записывает название статьи и текст
            self.postman.cursor.execute(self.author.find_author_id(author_name))
            author_id = self.postman.cursor.fetchone()[0]
            self.postman.cursor.execute(
                self.article.write_into_a_table(
                    'article', article_name, text_article_or_comment, author_id))
            return
        # передан автор, название статьи, текст и рейтинг, значит это комментарий, записывает комментарий
        self.postman.cursor.execute(self.author.find_author_id(author_name))
        author_id = self.postman.cursor.fetchone()[0]
        self.postman.cursor.execute(self.article.find_article_id(article_name, author_id))
        article_id = self.postman.cursor.fetchone()[0]
        self.postman.cursor.execute(self.comment.write_into_a_table(
            'comment', text_article_or_comment, rating, article_id))

    def display_record(self, author_name=None, article_name=None, comment=False):
        if not self.postman:
            print('не выполнено подключение к базе')
            return
        if not author_name:
            self.postman.cursor.execute("select author.author_name, "
                                        "article.article_name, "
                                        "round(avg(comment.rating),2) as average "
                                        "from author join article "
                                        "on author.author_id = article.fk_article_author "
                                        "join comment on article_id = comment.fk_comment_article "
                                        "group by author.author_id, author_name, "
                                        "article.article_id, article_name "
                                        "order by average desc")
            print(from_db_cursor(self.postman.cursor))
            # выводим всех авторов со всеми их статьями и рейтингом статей
            return
        if not article_name and author_name == 'all':
            self.postman.cursor.execute("select author_name from author;")
            print(from_db_cursor(self.postman.cursor))
            # выводим всех авторов
            return
        elif not article_name and author_name:
            self.postman.cursor.execute(self.author.find_author_id(author_name))
            author_id = self.postman.cursor.fetchone()[0]
            self.postman.cursor.execute(f"select author.author_name, "
                                        f"article.article_name, "
                                        f"round(avg(comment.rating),2) as average "
                                        f"from author join article on author.author_id = article.fk_article_author "
                                        f"join comment on article_id = comment.fk_comment_article "
                                        f"where author.author_id = '{author_id}' "
                                        f"group by author.author_id, author_name, article.article_id, article_name "
                                        f"order by average desc")
            print(from_db_cursor(self.postman.cursor))
            # выводим переданного автора и все его статьи со средним рейтингом
            return
        elif author_name and author_name and not comment and author_name != '-':
            self.postman.cursor.execute(self.author.find_author_id(author_name))
            author_id = self.postman.cursor.fetchone()[0]
            self.postman.cursor.execute(f"select author.author_name, "
                                        f"article.article_name, "
                                        f"article.article_text, "
                                        f"round(avg(comment.rating),2) as average "
                                        f"from author join article on author.author_id = article.fk_article_author "
                                        f"join comment on article_id = comment.fk_comment_article "
                                        f"where author.author_id = '{author_id}' "
                                        f"group by author.author_id, author_name, article.article_id, article_name "
                                        f"order by average desc")
            print(from_db_cursor(self.postman.cursor))
            # имя автора, название статьи, текст статьи, средний рейтинг
            return
        elif author_name == '-' and article_name:
            self.postman.cursor.execute(f"select author.author_name, article.article_name "
                                        f"from author join article on author.author_id = article.fk_article_author "
                                        f"where article.article_name = '{article_name}'")
            print(from_db_cursor(self.postman.cursor))
            # выводим все статьи с таким названием:
            return
        elif comment:
            self.postman.cursor.execute(self.author.find_author_id(author_name))
            author_id = self.postman.cursor.fetchone()[0]
            self.postman.cursor.execute(f"select author.author_name, "
                                        f"article.article_name, comment.comment_text, comment.rating "
                                        f"from author join article on author.author_id = article.fk_article_author "
                                        f"join comment on article.article_id = comment.fk_comment_article "
                                        f"where author.author_id = '{author_id}' "
                                        f"and article.article_name = '{article_name}'")
            print(from_db_cursor(self.postman.cursor))
            # выводим автора, название стать, все комментари с рейтингом
            return


class Info:
    def __init__(self, text):
        self.info = text

    def __repr__(self):
        return f"{self.info}"


info = Info(text_info)
help = Info(text_help)
psadb = AuthorDBManager(1)
jadb = AuthorDBManager(2)
ladb = AuthorDBManager(3)

# a.create_db()
# a.connection_to_base()
# a.write_into_a_table('King')
# a.write_into_a_table('Pehov')
# a.write_into_a_table('King', 'pervaia article', 'text article 1')
# a.write_into_a_table('King', 'vtoraia article', 'text article 2')
# a.write_into_a_table('Pehov', 'pervaia article', 'text article 1')
# a.write_into_a_table('Pehov', 'vtoraia article', 'text article 2')
#
# a.write_into_a_table('King', 'pervaia article', 'text comment 1', 3)
# a.write_into_a_table('King', 'pervaia article', 'text comment 2', 5)
# a.write_into_a_table('King', 'vtoraia article', 'text comment 3', 1)
# a.write_into_a_table('King', 'vtoraia article', 'text comment 4', 3)
# a.write_into_a_table('Pehov', 'pervaia article', 'text comment 1', 1)
# a.write_into_a_table('Pehov', 'pervaia article', 'text comment 2', 3)
# a.write_into_a_table('Pehov', 'vtoraia article', 'text comment 3', 5)
# a.write_into_a_table('Pehov', 'vtoraia article', 'text comment 4', 2)
