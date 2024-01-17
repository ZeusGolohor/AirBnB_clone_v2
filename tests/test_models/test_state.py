#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
# import os
# import MySQLdb


class test_state(test_basemodel):
    """ """
    # @classmethod
    # def setUpClass(cls):
    #     """
    #     This method is used to set up the class.
    #     """
    #     env_vs = {
    #         'host': os.environ.get('HBNB_MYSQL_HOST'),
    #         'port': 3306,
    #         'user': os.getenv('HBNB_MYSQL_USER', default=None),
    #         'passwd': os.getenv('HBNB_MYSQL_PWD', default=None),
    #         'db': os.getenv('HBNB_MYSQL_DB', default=None),
    #     }
    #     print(MySQLdb.version_info)
    #     print(os.environ)
    #     cls.env_vs = env_vs
    #     for key, value in env_vs.items():
    #         print(key, value)

    #     print(cls.env_vs['host'])
    #     conn = MySQLdb.connect(host=env_vs["host"], port=3306, user=env_vs["user"],
    #                            passwd=env_vs["passwd"], db=env_vs["db"], charset="utf8")

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
