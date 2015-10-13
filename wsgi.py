import os

from helloworld.app import app

if __name__ == '__main__':
    listen_address = os.environ.get('LISTEN_ADDRESS', '127.0.0.1')
    app.run(host=listen_address)

