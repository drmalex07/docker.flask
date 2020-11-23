import logging

from helloworld.app import app

def setup_module():
    #print(" * Setting up tests for %s"  % (__name__)) 
    app.config['TESTING'] = True
    pass

def teardown_module():
    #print(" * Tearing down tests for %s"  % (__name__)) 
    pass

# Tests

def test_1():
    print("everything is fine: app=%s" % (app));

def test_get_1():
    with app.test_client() as client:
        res = client.get('/get', query_string=dict(a=199,b='boo'), headers=dict())
        assert res.status_code == 200
        r = res.get_json();

def test_post_1():
    with app.test_client() as client:
        res = client.post('/post', data=dict(a=199,b='boo'), headers=dict(foo='Bar'))
        assert res.status_code == 200
        r = res.get_json();

   

