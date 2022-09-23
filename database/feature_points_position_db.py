import MySQLdb
from database.db_protocol import DBProtocol

class FeaturePointsPositionDB(DBProtocol):
    def __init__(self):
        table_name = "feature_points_position"
        data_format = "(id INT, x FLOAT, y FLOAT, z FLOAT)"

        super().__init__(table_name, data_format)

    def create(self, fp_id, x, y, z):
        sql = "INSERT INTO {}(id, x, y, z) VALUES ({}, {}, {}, {})".format(self.table_name, fp_id, x, y, z)
        super().create(sql)

    def find(self, fp_id):
        sql = "SELECT * FROM {} WHERE id={}".format(self.table_name, fp_id)
        #TODO: add fetched data size check.
        return super().find(sql)[0]
