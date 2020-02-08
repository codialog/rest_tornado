import json
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

items = []


class TodoItems(RequestHandler):
    def get(self):
        write_message = []
        for item in items:
            write_message.append(json.loads(item))
        self.write({'items': write_message})


class TodoItem(RequestHandler):
    def post(self):
        items.append(self.request.body)
        self.write({'message': 'new item added'})


def make_app():
    urls = [
        ("/", TodoItems),
        ("/api/item/", TodoItem)
    ]
    return Application(urls, debug=True)


if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()