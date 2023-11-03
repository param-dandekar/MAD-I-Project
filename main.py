from bin import make_app

app, api = make_app()

from bin.controllers import *

if __name__ == '__main__':
    app.run(debug=True)
    