# README

## Test

Run tests:

    cd helloworld
    pip3 install -r requirements-testing.txt
    python setup.py nosetests --verbosity=2 

## Build Docker image
    
Build:    
    
    docker build . -t local/hello-flask:0.1

Try it:

    docker run --rm -it -p 5000:5000 -v $PWD/logs:/var/local/helloworld/logs local/hello-flask:0.1

