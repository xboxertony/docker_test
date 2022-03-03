from flask import Flask
import MySQLdb

app = Flask(__name__)

connargs = {"host":"db","user":"user","password":"pass","db":"mydb"}


@app.route("/create")
def create():
    conn = MySQLdb.connect(**connargs)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE user (name VARCHAR(255), address VARCHAR(255))")
    cursor.execute("insert into user (name, address) values ('Tony','okok') ")
    conn.commit()
    cursor.close()
    return "ok"

@app.route("/")
def home():
    conn = MySQLdb.connect(**connargs)
    cursor = conn.cursor()
    cursor.execute("select name from user")
    print("ok")
    rows = cursor.fetchall()
    arr = [
    ]
    s = ""
    for r in rows:
        arr.append("".join(list(r)))
        s+="".join(arr)
    cursor.close()
    return s

if __name__=="__main__":
    app.run(host="0.0.0.0",port=3000,debug=True)