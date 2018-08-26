

how to use it
```

step1: start redis server
$> redis-server

step2:
in window1
$> celery -A tasks worker --loglevel=info

step3:
in window2
$> python3 invoker.py


```
