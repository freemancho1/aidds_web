from flask import Flask

from aidds_web.service import predict_route

app = Flask(__name__)

app.add_url_rule('/predict', view_func=predict_route.as_view('predict'))