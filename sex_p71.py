import pymysql
#conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',user='root', password='password',db='scraping')
conn = pymysql.connect(host='127.0.0.1', port=3307,user='root', password='password',db='scraping')
#conn = pymysql.connect('localhost','root','password','scraping')

cur = conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages WHERE id = 3")
print(cur.fetchone())
cur.close()
conn.close()