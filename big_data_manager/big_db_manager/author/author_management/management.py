class AuthorManager:
    @classmethod
    def write_into_a_table(cls, author_table, name_author: str):
        return f"INSERT INTO {author_table} (author_name) VALUES ('{name_author}')"
        # return f"SELECT EXISTS (SELECT author_name FROM {author_table} WHERE '{name_author}') THEN " \
        #             f"RETURN 'Такой автор уже есть в таблице';" \
        #        f"ELSE" \
        #             f"RETURN INSERT INTO {author_table} (author_name) VALUES ('{name_author}');"

    @classmethod
    def display_record(cls, author_table, name_author: str):
        if name_author == '*':
            # вывести всех
            ...
        # вывести введеного автора

    @classmethod
    def find_author_id(cls, name_author: str):
        return f"SELECT author_id FROM author WHERE author_name = '{name_author}'"


class ArticleManager:
    @classmethod
    def write_into_a_table(cls, article_table, name_article: str, article_text: str, author_id):
        return f"INSERT INTO {article_table} (article_name, article_text, fk_article_author) " \
               f"VALUES('{name_article}', '{article_text}', {author_id});"
        # по айди автора создать запись в таблицу статей

    @classmethod
    def display_record(cls, name_article: str, text_article):
        if name_article == '*':
            # вывести всех
            ...
        # вывести введенную статью

    @classmethod
    def find_article_id(cls, name_article: str, author_id):
        return f"SELECT article_id FROM article WHERE article_name = '{name_article}' " \
                                                f"AND fk_article_author = '{author_id}'"
        # ищет и возвращает айди статьи по имени


class CommentManager:
    @classmethod
    def write_into_a_table(cls, comment_table: str, comment_text: str, rating: int, article_id: int):
        # по айди статьи создать запись в таблицу комментариев
        if 0 <= rating <= 5:
            return f"INSERT INTO {comment_table} (comment_text, rating, fk_comment_article) " \
                   f"VALUES('{comment_text}', {rating}, {article_id});"
        else:
            print('рейтинг должен быть от 0 до 5')
            return
