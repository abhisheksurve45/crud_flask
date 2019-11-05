from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'A6HZkAtXV1'
app.config['MYSQL_DATABASE_PASSWORD'] = 'axrHwbkA5n'
app.config['MYSQL_DATABASE_DB'] = 'A6HZkAtXV1'
app.config['MYSQL_DATABASE_HOST'] = '37.59.55.185'
mysql.init_app(app)