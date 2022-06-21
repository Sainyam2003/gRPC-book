from .book import api as book_ns
from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint, title="gRPC API", version="1.0", description="A gRPC API written in Python "
)


api.add_namespace(book_ns, path="/book")