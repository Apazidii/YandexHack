import os
import ydb
import ydb.iam
import json
import uuid

def get_data(bridge_name):
    driver = ydb.Driver(
        endpoint="grpcs://ydb.serverless.yandexcloud.net:2135",
        database="/ru-central1/b1g2vfpb61j21c575ok3/etn03lo383ndqufkrivb",
        credentials=ydb.iam.ServiceAccountCredentials.from_file(
            './sa.json',
        )
    )

    def get_bridge_id(session):
        return session.transaction().execute(
            "SELECT bridge_id FROM bridges_table WHERE bridge_name='" + bridge_name + "'",
            commit_tx=True,
            settings=ydb.BaseRequestSettings().with_timeout(3).with_operation_timeout(2)
        )

    def get_bridges_table_query(session):
        return session.transaction().execute(
            "SELECT bridge_name, fullname, fullname2, bridge_alt, bridge_long FROM bridges_table WHERE bridge_name='" + bridge_name + "'",
            commit_tx=True,
            settings=ydb.BaseRequestSettings().with_timeout(3).with_operation_timeout(2)
        )

    def get_bridges_time(session):
        return session.transaction().execute(
            "SELECT bridge_close_time, bridge_open_time FROM bridges_time WHERE bridge_id='" + b_id + "'",
            commit_tx=True,
            settings=ydb.BaseRequestSettings().with_timeout(3).with_operation_timeout(2)
        )
    
    with driver:
        driver.wait(fail_fast=True, timeout=5)

        with ydb.SessionPool(driver) as pool:
            b_id = pool.retry_operation_sync(get_bridge_id)[0].rows[0]["bridge_id"]
            b_table = pool.retry_operation_sync(get_bridges_table_query)[0].rows[0]
            b_time = pool.retry_operation_sync(get_bridges_time)[0].rows

            result = {}
            result["name"] = b_table['bridge_name']
            result["fullname"] = b_table["fullname"]
            result["fullname2"] = b_table["fullname2"]
            result["coord"] = [b_table["bridge_alt"], b_table["bridge_long"]]
            result["time"] = []
            for el in b_time:
                result["time"].append(list(el.values()))
            return result

print(get_data("Дворцовый"))
