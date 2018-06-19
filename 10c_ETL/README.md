
# ETL

```
use python lib to copy a table from one db to another db
```

```python
import petl as etl, psycopg2 as pg, sys
from sqlalchemy import *

reload(sys)
sys.setdefaultencoding('utf8')


dbCnxns = {'operations':'dbname=operations user=etl host=127.0.0.1', 'python':"dbname=python user=etl host=127.0.0.1"}

# set my connection and cursors
sourceConn = pg.connect(dbCnxns['operations'])
targetConn = pg.connect(dbCnxns['python'])
sourceCursor = sourceConn.cursor()
targetCursor = targetConn.cursor()

sourceCursor.execute("""
select table_name from information_schema.columns
where table_schema = 'public'
and table_name in ('returns', 'salesperson')
group by 1
	""")

sourceTables = sourceCursor.fetchall()

for t in sourceTables:
	targetCursor.execute("drop table if exists %s" % (t[0]))
	sourceDs = etl.fromdb(sourceConn, "select * from %s" %(t[0]))
	etl.todb(sourceDs, targetConn, t[0], create=True, sample=1000)

```





