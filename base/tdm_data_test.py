import redis
import json
import datetime


class AccelerationTrendRespDTO:
    def __init__(self, id, pt, vin, accelAvg, accelAvgModel, updateTime):
        self.id = id
        self.pt = pt
        self.vin = vin
        self.accelAvg = accelAvg
        self.accelAvgModel = accelAvgModel
        self.updateTime = updateTime

    def to_dict(self):
        return {
            'id': self.id,
            'pt': self.pt,
            'vin': self.vin,
            'accelAvg': self.accelAvg,
            'accelAvgModel': self.accelAvgModel,
            'updateTime': str(self.updateTime)
        }


class ChargingPerformanceRespDTO:
    def __init__(self, id, mm, vin, chargeMonth, slowChargeMonth, fastChargeMonth, slowCharge99PercentCnt, suggest,
                 updateTime):
        self.id = id
        self.mm = mm
        self.vin = vin
        self.chargeMonth = chargeMonth
        self.slowChargeMonth = slowChargeMonth
        self.fastChargeMonth = fastChargeMonth
        self.slowCharge99PercentCnt = slowCharge99PercentCnt
        self.suggest = suggest
        self.updateTime = updateTime

    def to_dict(self):
        return {
            'id': self.id,
            'mm': self.mm,
            'vin': self.vin,
            'chargeMonth': self.chargeMonth,
            'slowChargeMonth': self.slowChargeMonth,
            'fastChargeMonth': self.fastChargeMonth,
            'slowCharge99PercentCnt': self.slowCharge99PercentCnt,
            'suggest': self.suggest,
            'updateTime': str(self.updateTime)
        }


class ComprehensiveDataRespDTO:
    def __init__(self, id, mm, vin, ecLeadModelRate, ecPer100kmAvg, savedCost, costPerKmAvg, sumMileage,
                 costLeadModelRate, mileageLeadModelRate, ecRanking, mileageRanking, costRanking, updateTime):
        self.id = id
        self.mm = mm
        self.vin = vin
        self.ecLeadModelRate = ecLeadModelRate
        self.ecPer100kmAvg = ecPer100kmAvg
        self.savedCost = savedCost
        self.costPerKmAvg = costPerKmAvg
        self.sumMileage = sumMileage
        self.costLeadModelRate = costLeadModelRate
        self.mileageLeadModelRate = mileageLeadModelRate
        self.ecRanking = ecRanking
        self.mileageRanking = mileageRanking
        self.costRanking = costRanking
        self.updateTime = updateTime

    def to_dict(self):
        return {
            'id': self.id,
            'mm': self.mm,
            'vin': self.vin,
            'ecLeadModelRate': self.ecLeadModelRate,
            'ecPer100kmAvg': self.ecPer100kmAvg,
            'savedCost': self.savedCost,
            'costPerKmAvg': self.costPerKmAvg,
            'sumMileage': self.sumMileage,
            'costLeadModelRate': self.costLeadModelRate,
            'mileageLeadModelRate': self.mileageLeadModelRate,
            'ecRanking': self.ecRanking,
            'mileageRanking': self.mileageRanking,
            'costRanking': self.costRanking,
            'updateTime': str(self.updateTime)
        }


class DistributionOfChargingCapacityRespDTO:
    def __init__(self, id, pt, vin, chargeDay, chargeDuring, updateTime):
        self.id = id
        self.pt = pt
        self.vin = vin
        self.chargeDay = chargeDay
        self.chargeDuring = chargeDuring
        self.updateTime = updateTime

    def to_dict(self):
        return {
            'id': self.id,
            'pt': self.pt,
            'vin': self.vin,
            'chargeDay': self.chargeDay,
            'chargeDuring': self.chargeDuring,
            'updateTime': str(self.updateTime)
        }


class DrivingPerformanceRespDTO:
    def __init__(self, id, mm, vin, drivingStyle, speedAvg, rapAccelsCnt, rapDecelsCnt, sharpTurnsCnt, suggest,
                 updateTime):
        self.id = id
        self.mm = mm
        self.vin = vin
        self.drivingStyle = drivingStyle
        self.speedAvg = speedAvg
        self.rapAccelsCnt = rapAccelsCnt
        self.rapDecelsCnt = rapDecelsCnt
        self.sharpTurnsCnt = sharpTurnsCnt
        self.suggest = suggest
        self.updateTime = updateTime

    def to_dict(self):
        return {
            'id': self.id,
            'mm': self.mm,
            'vin': self.vin,
            'drivingStyle': self.drivingStyle,
            'speedAvg': self.speedAvg,
            'rapAccelsCnt': self.rapAccelsCnt,
            'rapDecelsCnt': self.rapDecelsCnt,
            'sharpTurnsCnt': self.sharpTurnsCnt,
            'suggest': self.suggest,
            'updateTime': str(self.updateTime)
        }


class EnergyConsumptionRespDTO:
    def __init__(self, id, mm, vin, sumElc, sumPwrtrnElc, acSumElc, lightSumElc, otherElc, sumElcDriving,
                 sumPwrtrnElcDriving, acSumElcDriving
                 , lightSumElcDriving, otherElcDriving, elcPark, sumPwrtrnElcPark, acSumElcPark, lightSumElcPark,
                 otherElcPark
                 , ecLeadModelRateStd, ecPer100kmAvgStd, costPerKmAvgStd, updateTime):
        self.id = id
        self.mm = mm
        self.vin = vin
        self.sumElc = sumElc
        self.sumPwrtrnElc = sumPwrtrnElc
        self.acSumElc = acSumElc
        self.lightSumElc = lightSumElc
        self.otherElc = otherElc
        self.sumElcDriving = sumElcDriving
        self.sumPwrtrnElcDriving = sumPwrtrnElcDriving
        self.acSumElcDriving = acSumElcDriving
        self.lightSumElcDriving = lightSumElcDriving
        self.otherElcDriving = otherElcDriving
        self.elcPark = elcPark
        self.sumPwrtrnElcPark = sumPwrtrnElcPark
        self.acSumElcPark = acSumElcPark
        self.lightSumElcPark = lightSumElcPark
        self.otherElcPark = otherElcPark
        self.ecLeadModelRateStd = ecLeadModelRateStd
        self.ecPer100kmAvgStd = ecPer100kmAvgStd
        self.costPerKmAvgStd = costPerKmAvgStd
        self.updateTime = updateTime

    def to_dict(self):
        return {
            'id': self.id,
            'mm': self.mm,
            'vin': self.vin,
            'sumElc': self.sumElc,
            'sumPwrtrnElc': self.sumPwrtrnElc,
            'acSumElc': self.acSumElc,
            'lightSumElc': self.lightSumElc,
            'otherElc': self.otherElc,
            'sumElcDriving': self.sumElcDriving,
            'sumPwrtrnElcDriving': self.sumPwrtrnElcDriving,
            'acSumElcDriving': self.acSumElcDriving,
            'lightSumElcDriving': self.lightSumElcDriving,
            'otherElcDriving': self.otherElcDriving,
            'elcPark': self.elcPark,
            'sumPwrtrnElcPark': self.sumPwrtrnElcPark,
            'acSumElcPark': self.acSumElcPark,
            'lightSumElcPark': self.lightSumElcPark,
            'otherElcPark': self.otherElcPark,
            'ecLeadModelRateStd': self.ecLeadModelRateStd,
            'ecPer100kmAvgStd': self.ecPer100kmAvgStd,
            'costPerKmAvgStd': self.costPerKmAvgStd,
            'updateTime': str(self.updateTime)
        }


class EnergyConsumptionTrendRespDTO:
    def __init__(self, id, pt, vin, ecPer100kmAvg, ecPer100kmAvgModel, updateTime):
        self.id = id
        self.pt = pt
        self.vin = vin
        self.ecPer100kmAvg = ecPer100kmAvg
        self.ecPer100kmAvgModel = ecPer100kmAvgModel
        self.updateTime = updateTime

    def to_dict(self):
        return {
            'id': self.id,
            'pt': self.pt,
            'vin': self.vin,
            'ecPer100kmAvg': self.ecPer100kmAvg,
            'ecPer100kmAvgModel': self.ecPer100kmAvgModel,
            'updateTime': str(self.updateTime)
        }


class RankingListRespDTO:
    def __init__(self, id, mm, vin, leadModelRate, userNickname, userProfilePictureUrl, vinData, ranking, updateTime):
        self.id = id
        self.mm = mm
        self.vin = vin
        self.leadModelRate = leadModelRate
        self.userNickname = userNickname
        self.userProfilePictureUrl = userProfilePictureUrl
        self.vinData = vinData
        self.ranking = ranking
        self.updateTime = updateTime

    def to_dict(self):
        return {
            'id': self.id,
            'mm': self.mm,
            'vin': self.vin,
            'leadModelRate': self.leadModelRate,
            'userNickname': self.userNickname,
            'userProfilePictureUrl': self.userProfilePictureUrl,
            'vinData': self.vinData,
            'ranking': self.ranking,
            'updateTime': str(self.updateTime)
        }


# def insert_data_to_redis():
#     # 连接到Redis服务器
#     client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
#
#     # 循环插入10万条数据
#     for i in range(100000):
#         key = f'tmd_key_{i}'
#         value = f'value_{i}'
#         client.set(key, value)
#
#         # 打印进度
#         if i % 10000 == 0:
#             print(f'Inserted {i} keys')
#
#     print('Finished inserting 100000 keys')


def insert_object_to_redis(obj, key, client):
    # 循环插入10万条数据
    for i in range(200000):
        # 将对象转换为JSON字符串
        obj.id = i
        # 将对象存储到Redis中，使用对象的id作为键
        obj_json = json.dumps(obj.to_dict())
        k = f'{key}_{i}'
        client.set(k, obj_json)

    print(f'Object with id {obj.id} inserted to Redis')


if __name__ == '__main__':
    # 连接到Redis服务器
    client = redis.StrictRedis(host='localhost', port=6379, db=0)

    acceleration_trend_resp_dto = AccelerationTrendRespDTO(0, '20240610', '12345678', 1, 2, datetime.datetime.now())
    charging_performance_resp_dto = ChargingPerformanceRespDTO(0, '202406', '12345678', 1, 2, 3, 4, 'suggest',
                                                               datetime.datetime.now())
    comprehensive_data_resp_dto = ComprehensiveDataRespDTO(0, '202406', '12345678', 1,2,3,4,5,6,7,8,9,10, datetime.datetime.now())
    distribution_of_charging_capacity_resp_dto = DistributionOfChargingCapacityRespDTO(0, '20240610', '12345678', 1,2, datetime.datetime.now())
    driving_performance_resp_dto = DrivingPerformanceRespDTO(0, '202406', '12345678',1,2,3,4,5,'suggest', datetime.datetime.now())
    energy_consumption_resp_dto = EnergyConsumptionRespDTO(0, '202406', '12345678',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18, datetime.datetime.now())
    energy_consumption_trend_resp_dto = EnergyConsumptionTrendRespDTO(0, '20240610', '12345678', 1,2, datetime.datetime.now())
    ranking_list_resp_dto = RankingListRespDTO(0, '202406', '12345678', 1,'test', 'https://www.baidu.com', 123213, 1, datetime.datetime.now())


    insert_object_to_redis(acceleration_trend_resp_dto, "tmd_acceleration_trend_", client)
    insert_object_to_redis(charging_performance_resp_dto, "tmd_charging_performance_", client)
    insert_object_to_redis(distribution_of_charging_capacity_resp_dto, "tmd_distribution_of_charging_capacity_", client)
    insert_object_to_redis(driving_performance_resp_dto, "tmd_driving_performance_", client)
    insert_object_to_redis(energy_consumption_resp_dto, "tmd_energy_consumption_", client)
    insert_object_to_redis(energy_consumption_trend_resp_dto, "tmd_energy_consumption_trend_", client)
    insert_object_to_redis(ranking_list_resp_dto, "tmd_ranking_list_trend_", client)
