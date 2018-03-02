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
        second_train_day = (week_day + tpl[-1] - tpl[-2] + int(tpl[-4] > tpl[-3]))%7
        for offset in range(2):
            if week_day_2 != second_train_day:
                week_day_2 = (second_train_day +offset)%7
                list2 = trains_btw_with_times(intr, dst,week_day_2)
            if list2 is None or len(list2) <= 0:
                print('no train btw',intr, src)
                continue
            for tpl2 in list2:
                if tpl[-4] < tpl[-3]:
                    if tpl2[4] > tpl[5]:
                        result_list.append([[tpl,week_day],[tpl2,week_day_2]])
                else:
                    result_list.append([[tpl,week_day],[tpl2,week_day_2]])
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
    # for intr in stns_list:
    #     print(intr[0])
    train_pairs = get_trainspair(src,'VTM',dst,week_day)
    print(len(train_pairs))
    for row in train_pairs:
        print(row[0][0][0],row[0][1],row[1][0][0],row[1][1])
        # print(row[1])
        # print(row[0][0])
        # print(row[0][0][0],src,'BZA',jdate+dt.timedelta(days=(row[0][1]-week_day+7)%7)+row[0][0][4],jdate+dt.timedelta(days=(row[0][1]-week_day+7)%7)+row[0][0][5])
        # print(row[1][0][0],'BZA',dst,jdate+dt.timedelta(days=(row[0][1]-week_day+7)%7)+row[1][0][4],jdate+dt.timedelta(days=(row[0][1]-week_day+7)%7)+row[1][0][5])
        print(' ')

get_paths('KZJ', 'OGL',dt.datetime(2018,3,4))
# print(trains_btw('MAS','BZJ','SUN'))