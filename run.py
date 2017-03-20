import logging
from logging.handlers import RotatingFileHandler
from app import app

formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler("app.out.log", maxBytes=10000000, backupCount=5)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

app.logger.addHandler(handler)
app.run(debug=True)
