from bin import make_app, models, db
from bin.api import User

app, api = make_app()

if __name__ == '__main__':
    app.run(debug=True)