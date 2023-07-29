import math
import haversine as hv
import DATA as d


def average_over_time (speedlist, timelength):
   if len(speedlist) < timelength*4:
       return sum(speedlist)/len(speedlist)
   return sum(speedlist[:timelength*4])/(timelength*4)

def mph_from_twopoints(pointa, pointb):
    hyp = [pointa[0] - pointb[0], pointa[1] - pointb[1]]
    distance_travelled = math.sqrt(hyp[0]**2 + hyp[0]**2)
    return abs(distance_travelled)

def add_to_list(speed):
    global ltest
    if len(ltest) > 536870910:
        ltest = ltest[1:]
    ltest[:0] = [speed]



def getspeed():
    distance = hv.haversine(d.LAST_TWO_GPS[0],d.LAST_TWO_GPS[1], unit = hv.Unit.MILES)
    hours = d.SMALL_TIME_INTERVAL/3600
    return distance/hours

'''def test():
    global ltest 
    ltest = ltest[1:]'''



print(d.TIME_UNITS)
print(d.CURRENT_SPEED)

d.LAST_TWO_GPS[0] = [4,1]; d.LAST_TWO_GPS[1] = [5,1]
d.CURRENT_SPEED = getspeed()

print(getspeed())
print(d.CURRENT_SPEED)