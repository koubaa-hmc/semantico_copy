import os
import logging
import json

from neo4j import GraphDatabase


class Boundary:
    def __init__(self, points: dict):
        self.lt = points['lt']
        try:
            self.lb = points['lb']
        except 'KeyError':
            logging.warning('lb is not given')
        try:
            self.mu = points['mt']
        except 'KeyError':
            logging.warning('lb is not given')
        try:
            self.mb = points['mb']
        except 'KeyError':
            logging.warning('lb is not given')
        try:
            self.ru = points['rt']
        except 'KeyError':
            logging.warning('lb is not given')
        try:
            self.rb = points['rb']
        except 'KeyError':
            logging.warning('lb is not given')


class Component:
    def __init__(self, boundary: dict):
        # get current path
        current_path = os.getcwd()
        # set configurations and headers path
        conf_path = os.path.join(current_path, "configuration/spoker.json")
        with open(conf_path) as conf:
            self.conf = json.load(conf)
        self.threshold = self.conf['threshold']
        self.pdf_ui = ''
        self.page = 0
        self.boundary = Boundary(boundary)
        self.text = ''

    def is_next(self, other: 'Component') -> float:
        """
        calculate the probability of neighbourhood
        :rtype: a float btw. 0 and 1 giving the probability of other being the next component to self
        """
        dist = (other.boundary.rb - self.boundary.lt + other.boundary.ru - self.boundary.lb) / 2
        return 0 < dist < self.threshold


class Worph(Component):
    def __init__(self, pdf_ui: str, page: int, boundary: dict, text: str):
        super().__init__(boundary)
        self.pdf_ui = pdf_ui
        self.page = page
        self.text = text
        self.create_worph()

    def create_worph(self):
        with GraphDatabase.driver(self.conf['uri'], auth=(self.conf['user'], self.conf['password'])) as driver:
            driver.execute_query(
                "MERGE (a:Word {text: $text, lt: point({x: $X1, y: $Y1}), rb: point({x: $X2, y: $Y2})})",
                text=self.text,
                X1=self.boundary.lt[0],
                Y1=self.boundary.lt[1],
                X2=self.boundary.rb[0],
                Y2=self.boundary.rb[1],
                database_="neo4j"
            )


class Plumph(Component):
    def __init__(self, pdf_ui: str, page: int, boundary: dict):
        super().__init__(boundary)
        self.pdf_ui = pdf_ui
        self.page = page
        self.create_plumph()

    def create_plumph(self):
        with GraphDatabase.driver(self.conf['uri'], auth=(self.conf['user'], self.conf['password'])) as driver:
            driver.execute_query(
                "MERGE (a:Plumph {lt: point({x: $X1, y: $Y1}), rb: point({x: $X2, y: $Y2})})",
                X1=self.boundary.lt[0],
                Y1=self.boundary.lt[1],
                X2=self.boundary.rb[0],
                Y2=self.boundary.rb[1],
                database_="neo4j"
            )
