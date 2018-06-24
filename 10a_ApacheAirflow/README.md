
# Airflow

Airflow is a platform to programmatically author, schedule and monitor workflows.


## core concepts    

### DAG   
In Airflow, a DAG – or a Directed Acyclic Graph – is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies.

## architecture    
```
airflow comes with 5 main types of built in execution modes:
1 sequential                    runs on a single machine
2 local                         runs on a single machine
3 celery(out of the box)        runs on distributed system
4 Mesos(community driven)       runs on distributed system
5 Kubernetes(community driven)  runs on distributed system
```

