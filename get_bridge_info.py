import os
import ydb
import ydb.iam
import json
import uuid
from datetime import datetime

def get_bridges_info():
    driver = ydb.Driver(
        endpoint="grpcs://ydb.serverless.yandexcloud.net:2135",
        database="/ru-central1/b1g2vfpb61j21c575ok3/etn03lo383ndqufkrivb",
        credentials=ydb.iam.ServiceAccountCredentials.from_file(
            './sa.json',
        )
    )

    def query(session):
        return session.transaction().execute(
            "SELECT bridge_name, bridge_open_time, bridge_close_time FROM bridges_time INNER JOIN bridges_table ON bridges_time.bridge_id = bridges_table.bridge_id",
            commit_tx=True,
            settings=ydb.BaseRequestSettings().with_timeout(3).with_operation_timeout(2)
        )

    with driver:
        driver.wait(fail_fast=True, timeout=5)

        with ydb.SessionPool(driver) as pool:
            query = pool.retry_operation_sync(query)[0].rows
            current_time = datetime.now()
            seconds = int(current_time.hour) * 3600 + int(current_time.minute) * 60
            
            open_bridges_name = []
            close_bridges_name = []
            for i in range(len(query)):
                bridge_close_time_seconds = int(query[i]['bridge_close_time'].split(":")[0]) * 3600 + int(query[i]['bridge_close_time'].split(":")[1]) * 60
                bridge_open_time_seconds = int(query[i]['bridge_open_time'].split(":")[0]) * 3600 + int(query[i]['bridge_open_time'].split(":")[1]) * 60
                if seconds < bridge_close_time_seconds or seconds >= bridge_open_time_seconds:
                    if query[i]['bridge_name'] not in open_bridges_name:
                        open_bridges_name.append(query[i]['bridge_name'])
                else:
                    close_bridges_name.append(query[i]['bridge_name'])

            return open_bridges_name, close_bridges_name


print(get_bridges_info())
