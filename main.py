import speedtest
from datetime import datetime
from time import sleep, mktime

# 60 % logFrequency must equal 0
# 0 < logFrequency < 60
logFrequency = 5


# returns results dict + current unix time
def test():
    try:
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        s.results.share()

        results_dict = s.results.dict()
        results_dict['unixTime'] = mktime(datetime.now().timetuple())

        print(results_dict)
        return str(results_dict)
    except:
        print("owo error moment")
        return "owo error moment"


if __name__ == '__main__':
    # make sure logFrequency is valid
    if 60 % logFrequency == 0 and 0 < logFrequency < 60:
        with open('log.txt', 'w') as f:
            while True:
                if int(datetime.now().strftime("%M")) % logFrequency == 0:
                    f.write(test() + "\n")
                sleep(30)
    else:
        print("invalid logFrequency")
        print("logFrequency must return true to the following:")
        print("\t60 % logFrequency must equal 0")
        print("\t0 < logFrequency < 60")
        print("\tlogFrequency must be an integer value")
        input("press enter to continue")
