# README


## Test

Run tests:

    cd helloworld
    pip3 install -r requirements-testing.txt
    python setup.py nosetests -v


## Build Docker image
    
Build:    
    
    docker build . -t local/hello-flask:0.1

Try it:

    docker run --rm -it -p 5000:5000 --volume $PWD/logs:/var/local/helloworld/logs local/hello-flask:0.1

