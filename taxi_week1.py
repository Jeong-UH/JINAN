# 택시 시스템

from datetime import datetime

def taxiMeterDevice(distance) :

    total = 0 # 최종 금액
    now_hour = datetime.now().hour # 출발 시간의 시(시스템 시간을 받아 옴)
    now_minute = datetime.now().minute # 출발 시간의 분(시스템 시간을 받아 옴)
    print("\n현재 시간은 %02d시 %02d분 입니다. 택시 출발합니다.\n"%(now_hour,now_minute))
    # TODO : 서울 택시 요금 미터기를 구현하는 코드를 작성 ( TODO 사이에 코드를 입력 할 것! )
    # 조건 : 기본요금 - 주간 3800원  심야 4600 (심야기준 00~04시)
    #        거리요금 - 132m당 100원 심야할증 20%
    # 택시는 시속 1분에 100를 달린다고 가정

    # 필수로 구해야 할 변수
    total = 1000 # 최종 금액
    arrived_hour = 0   # 도착 예상 시간
    arrived_minute = 0

    # TODO끝

    return total,arrived_hour, arrived_minute


# main(건들지 마시오)
print("택시에 탑승했습니다.")
distance = int(input("목적지와의 거리를 입력하세요 : "))
total, arrived_hour, arrived_minute = taxiMeterDevice(distance)
print("목적지까지 예상 금액은 %s원 "%format(total,","))
print("예상 도착시간은 %02d시 %02d분 입니다."%(arrived_hour, arrived_minute) )
