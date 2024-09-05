import tornado.ioloop
import tornado.web
import json
import pika


class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',
                    'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        self.send_to_queue(data)

    def send_to_queue(self, data):

        with pika.BlockingConnection(pika.ConnectionParameters(host='iprabbitmq', port=5672, credentials=pika.PlainCredentials('astra', 'astra') ))as conn:
            ch = conn.channel()
            ch.queue_declare(queue='requests')
            ch.basic_publish(exchange='', routing_key='requests',
                             body=json.dumps(data))



    def options(self):
        pass

def make_app():
    return tornado.web.Application([
        (r"/api/requests", MainHandler),
    ])


def main():
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
