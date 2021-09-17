import os
import ydb
import ydb.iam
import json
import uuid

def read_json():
    file = open("bridge.json", "r", encoding="utf-8")
    j = json.load(file)

    def d(k):
        k.pop("river")
        k.pop("link")
        k.pop("stop_water_trans")
        k.pop("start_water_trans")
        return k

    j = list(map(d, j))

    return j

def execute_query(session):
    massive = read_json()
    for i in massive:
        l = len(i["start_land_trans"])
        query = "INSERT INTO bridges_table(bridge_id, bridge_alt, bridge_long, bridge_name) VALUES ('" + i["id"]+ "', " + str(i["location"][1]) + ", " + str(i["location"][0]) + ", '" + i['name'] + "'); "
        print(query)
        session.transaction().execute(
            query,
            commit_tx=True,
            settings=ydb.BaseRequestSettings().with_timeout(3).with_operation_timeout(2)
        )
        for j in range(0, l):
            query1 = "INSERT INTO bridges_time(bridge_time_id, bridge_id, bridge_close_time, bridge_open_time) VALUES ('" + str(uuid.uuid4()) + "', '" + i["id"] + "', '" + i["stop_land_trans"][j] + "', '" + i["start_land_trans"][j] + "');"
            print(query1)
            session.transaction().execute(
                query1,
                commit_tx=True,
                settings=ydb.BaseRequestSettings().with_timeout(3).with_operation_timeout(2)
            )


def main():
    driver = ydb.Driver(
        endpoint="grpcs://ydb.serverless.yandexcloud.net:2135",
        database="/ru-central1/b1g2vfpb61j21c575ok3/etn03lo383ndqufkrivb",
        credentials=ydb.iam.ServiceAccountCredentials.from_file(
            '~/.ydb/sa.json',
        )
    )

    with driver:
        driver.wait(fail_fast=True, timeout=5)

        with ydb.SessionPool(driver) as pool:
            result = pool.retry_operation_sync(execute_query)
            #print(result[0].columns)
            #print(result[0].rows[0].bridges_table)

main()
