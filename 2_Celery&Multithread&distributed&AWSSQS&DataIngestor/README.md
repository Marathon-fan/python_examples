# python

table of content    

setting up the environment    

Multithreading in Python

Core Celery Distributed Tasks

Distributed tasks with AWS SQS

Distributed data ingestor Project 


## setting up the environment    

after install python3 under mac, use python3 to launch python3, use pip3 to launch pip3    

(we can see pip3, python3 using "ls /usr/local/bin")

> sudo pip3 install celery
Successfully installed amqp-2.3.2 billiard-3.5.0.3 celery-4.1.1 kombu-4.2.1 pytz-2018.4 vine-1.1.4

> sudo pip3 install redis    

> sudo pip3 install scrapy   
Scrapy | A Fast and Powerful Scraping and Web Crawling Framework

> pip3 freeze > requirements.txt    

download redis and install redis
```
tar xvzf redis-stable.tar.gz
cd redis-stable
make
sudo make install  (this can:  sudo cp src/redis-server /usr/local/bin/     sudo cp src/redis-cli /usr/local/bin/)
```

starting Redis
```
$ redis-server
```






