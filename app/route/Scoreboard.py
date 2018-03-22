# coding=utf-8
from flask_restful import Resource, reqparse
from flask import request
from api.config import HEADER
import api.scoreboard.get_scoreboard as score
import api.auth.auth as auth
import api.base_name as names
from api.service import GameService as gs


class Scoreboard(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('data')
        self.__args = self.__parser.parse_args()
        self.data = None

    def parse_data(self):
        self.data = self.__args.get('data', None)
        self.data = gs.converter(self.data)
        print("data: ", self.data)
        return

    def switch(self):
        answer = gs.converter(score.get_scoreboard(self.data["id_event"]))
        return answer

    def get(self):
        try:
            print("Scoreboard")
            self.parse_data()
            answer = self.switch()
            print("answer: ", answer)
            return answer, 200, {'Access-Control-Allow-Origin': '*'}
        except:
            return "Error", 200, {'Access-Control-Allow-Origin': '*'}