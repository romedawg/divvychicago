from blog import app, db

if __name__ == "__main__":
    db.create_all(app=app)
    app.run('0.0.0.0')
