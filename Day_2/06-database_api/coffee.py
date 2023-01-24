import json
from sqlalchemy import create_engine
from model import Coffee, Base
from sqlalchemy.orm import sessionmaker
from flask import jsonify