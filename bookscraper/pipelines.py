import psycopg2

class PostgreSQLPipeline:

    def open_spider(self, spider):
        hostname = 'localhost'
        port = 5433
        username = 'guillaumedemerges'
        password = ''
        database = 'bookscraper'

        # Debug print
        print(f"Connecting to PostgreSQL DB at {hostname}:{port} with user {username}")

        self.connection = psycopg2.connect(
            host=hostname,
            port=port,
            user=username,
            password=password,
            dbname=database
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "INSERT INTO books (title, price, stock, rating, category) VALUES (%s, %s, %s, %s, %s)",
                (item['title'], item['price'], item['stock'], item['rating'], item.get('category', ''))
            )
            self.connection.commit()
        except psycopg2.Error as e:
            self.connection.rollback()
            spider.logger.error(f"Error processing item: {e}")
        return item
