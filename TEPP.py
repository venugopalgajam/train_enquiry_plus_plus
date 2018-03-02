from db_tools import inter_stns, trains_btw, trains_btw_with_times, weekdays
import datetime as dt

def get_trainspair(src, intr, dst, week_day):
    print('get_trainpair',src,intr,dst,week_day)
    list1 = trains_btw_with_times(src, intr, week_day)
    list1 = sorted(list1, key= lambda x:x[-1])
    if len(list1) <= 0:
        print('no train btw',src, intr)
        return None 
    print(len(list1))
    print(list1[0])
    week_day_2 = -1
    list2 = None

    result_list =list()
    for tpl in list1:
        second_train_day = week_day + tpl[-1] - tpl[-2] + int(tpl[-4] > tpl[-3])
        if week_day_2 != second_train_day:
            list2 = trains_btw_with_times(intr, dst, second_train_day)
            week_day_2 = second_train_day
        if list2 is None or len(list2) <= 0:
            print('no train btw',intr, src)
            continue
        for tpl2 in list2:
            if tpl[-4] < tpl[-3]:
                if tpl2[4] > tpl[5]:
                    result_list.append([[tpl[0],week_day],[tpl2[0],week_day_2]])
            else:
                result_list.append([[tpl[0],week_day],[tpl2[0],week_day_2]])
    return result_list
    
def get_paths(src, dst, jdate):
    print('get_paths',src,dst,jdate)
    week_day = jdate.weekday()
    stns_list,_ = inter_stns(src, dst, week_day)
    stns_list = stns_list[:max([int(len(stns_list)/10), min([10,len(stns_list)])])] #top stations only
    # print(top_stns_list)
    if stns_list is None:
        print('no intermediate stations',src,dst)
        return None
    for intr in stns_list:
        print(intr[0])
        for row in get_trainspair(src,intr[0],dst,week_day):
            print(row)

get_paths('MAS', 'NDLS',dt.datetime(2018,3,4))