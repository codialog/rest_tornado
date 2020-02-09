import datetime
import logging

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado_sqlalchemy import SessionMixin, SQLAlchemy

from models import TableItem


class TodoItems(SessionMixin, RequestHandler):

    async def post(self):

        message = {
            'result': 'ERROR'
        }

        def to_int_arr(str):
            str_array = str.strip('[').strip(']').split(',')
            int_array = [int(i) for i in str_array]
            return int_array

        try:
            data = self.get_body_argument("array")
            raw_array = to_int_arr(data)
            # if len(data) > 3:
            #     raise
            with self.make_session() as session:
                item = TableItem(raw_array=raw_array,
                                 sorted_array=sorted(raw_array),
                                 created_at=datetime.datetime.now())
                session.add(item)
                session.commit()
                message.update({'result': 'OK'})
                message.update({'id': item.id})
        except Exception as ex:
            logging.warning(ex)
        finally:
            self.write(message)


class TodoItem(SessionMixin, RequestHandler):

    async def get(self, id):
        message = {
            'result': 'ERROR'
        }
        try:
            with self.make_session() as session:
                item = session.query(TableItem).filter(TableItem.id == id).one()
                message.clear()
                message.update({'id': id})
                message.update({'result_array': item.sorted_array})
                message.update({'date_of_creation': str(item.created_at)})
                self.write(item.sorted_array)
        except Exception as err:
            logging.warning(err)
        finally:
            self.write(message)


def make_app():
    urls = [
        (r"/api/item/([^/]+)?", TodoItem),
        (r"/api/items", TodoItems)
    ]
    return Application(urls, db=SQLAlchemy('postgresql://root:root@localhost:5432/postgres'), debug=True)


if __name__ == '__main__':
    app = make_app()
    app.listen(8880)
    IOLoop.instance().start()
