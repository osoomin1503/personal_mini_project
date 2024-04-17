import sys

# 파일 불러오기
if len(sys.argv) != 2:
    filename = 'students.txt'
else:
    filename = sys.argv[1]

# score 함수 정의
def score(x):
    if x >= 90:
        return "A"
    if (x>=80)&(x<90):
        return "B"
    if (x>=70)&(x<80):
        return "C"
    if (x>=60)&(x<70):
        return "D"
    else:
        return "F"

#리스트 만들기
stu_list = list()

# 성적 출력
print('  Student           Name   Midterm   Final   Average  Grade')
print('- ' * 30)

# 데이터 읽기
with open(filename,'r') as fr: 
    while True:
        line = fr.readline()
        if line == "":
            break
        # 컬럼별로 데이터 자르기
        lis = line.split()
        stu = int(lis[0])
        name1 = lis[1]+' '+lis[2]
        mid=int(lis[3])
        fin = int(lis[4])
        total = (mid + fin)/2
        grade = score(total)
        name = [stu, name1, mid, fin, total, grade]
        stu_list.append(name)
        
stu_list.sort(key = lambda x:x[4], reverse=True)

# 학생들의 성적 목록 출력1
for i in stu_list:
    print('  {:<8} {:>13}{:8}{:8}{:10.1f}   {:^8}'.format(i[0],i[1],i[2],i[3],i[4], i[5]))

##### 함수 정의 #####
def show_function(stu_list):
    stu_list.sort(key = lambda x:x[4], reverse=True)
    print('  Student           Name   Midterm   Final   Average  Grade')
    print('- ' * 30)
    # 학생들의 성적 목록 출력2
    for i in stu_list:
        print('  {:<8} {:>13}{:8}{:8}{:10.1f}   {:^8}'.format(i[0],i[1],i[2],i[3],i[4], i[5]))

def search_function():
    sl = []
    for i in range(len(stu_list)):
        sl.append(stu_list[i][0])
    # 학번 입력 받기
    stu_id = int(input("Student ID: "))
    if stu_id in sl :
        print('  Student           Name   Midterm   Final   Average  Grade')
        print('- ' * 30)
        i = stu_list[sl.index(stu_id)]
        print('  {:<8} {:>13}{:8}{:8}{:10.1f}   {:^8}'.format(i[0],i[1],i[2],i[3],i[4], i[5]))
    else:
        print("NO SUCH PERSON")

def changescore_function():
    sl = []
    for i in range(len(stu_list)):
        sl.append(stu_list[i][0])
    # 학번 입력 받기
    stu_id = int(input("Student ID: "))
    if stu_id in sl :
        # 변경할 점수 고르기(중간/기말 중)
        what_score = input("Mid/Final? ")
        # 중간일 때
        if what_score == "mid" : 
            how_much = int(input('Input new score: '))
            if (how_much<0) | (how_much>100) :
                pass
            else:
                print('  Student           Name   Midterm   Final   Average  Grade')
                print('- ' * 30)
                i = stu_list[sl.index(stu_id)]
                print('  {:<8} {:>13}{:8}{:8}{:10.1f}   {:^8}'.format(i[0],i[1],i[2],i[3],i[4], i[5]))
                print("Score changed.")
                # 업데이트
                stu_list[sl.index(stu_id)][2] = how_much
                stu_list[sl.index(stu_id)][4] = (how_much + stu_list[sl.index(stu_id)][3])/2
                stu_list[sl.index(stu_id)][5] = score(stu_list[sl.index(stu_id)][4])
                i = stu_list[sl.index(stu_id)]
                print('  {:<8} {:>13}{:8}{:8}{:10.1f}   {:^8}'.format(i[0],i[1],i[2],i[3],i[4], i[5]))
        # 기말일 때
        elif what_score == "final":
            how_much = int(input('Input new score: '))
            if (how_much<0) | (how_much>100) :
                pass
            else:
                print('  Student           Name   Midterm   Final   Average  Grade')
                print('- ' * 30)
                i = stu_list[sl.index(stu_id)]
                print('  {:<8} {:>13}{:8}{:8}{:10.1f}   {:^8}'.format(i[0],i[1],i[2],i[3],i[4], i[5]))
                print("Score changed.")
                # 업데이트
                stu_list[sl.index(stu_id)][3] = how_much
                stu_list[sl.index(stu_id)][4] = (how_much + stu_list[sl.index(stu_id)][2])/2
                stu_list[sl.index(stu_id)][5] = score(stu_list[sl.index(stu_id)][4])
                i = stu_list[sl.index(stu_id)]
                print('  {:<8} {:>13}{:8}{:8}{:10.1f}   {:^8}'.format(i[0],i[1],i[2],i[3],i[4], i[5]))      
        else:
            pass
    else:
        print("NO SUCH PERSON")

def add_function():       
    sl = []
    for i in range(len(stu_list)):
        sl.append(stu_list[i][0])
    # 학번 입력 받기
    stu_id = int(input("Student ID: "))
    if stu_id in sl :
        print("ALREADY EXISTS.")
    else:
        who_name = input("Name: ")
        mid_score = int(input("Midterm Score: "))
        if (mid_score<0) | (mid_score>100) : 
            pass
        else : 
            fin_score = int(input("Final Score: "))
            if (fin_score<0) | (fin_score>100) :
                pass
            else:
                total = (mid_score+fin_score)/2
                grade = score(total)
                name = [stu_id, who_name, mid_score, fin_score, total, grade]
                stu_list.append(name)
                print("Student added")
    
def searchgrade_function():
    # 학점 입력받기
    stu_grade = input("Grade to search: ")
    # 가능한 학점
    list_grade = ['A','B','C','D','F']
    # 학생들의 학점
    gl = []
    for i in range(len(stu_list)):
        gl.append(stu_list[i][-1])
    if stu_grade not in list_grade :
        pass
    else:
        if stu_grade not in gl:
            print("NO RESULTS.")
        else:
            print('  Student           Name   Midterm   Final   Average  Grade')
            print('- ' * 30)
            for a in range(len(stu_list)):
                if stu_list[a][-1] == stu_grade:
                    i = stu_list[a]
                    print('  {:<8} {:>13}{:8}{:8}{:10.1f}   {:^8}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))

def remove_function():
    if len(stu_list) == 0:
        print("List is empty")
    else:
        sl = []
        for i in range(len(stu_list)):
            sl.append(stu_list[i][0])
        # 학번 입력 받기
        stu_id = int(input("Student ID: "))
        if stu_id in sl :
            del stu_list[sl.index(stu_id)]
            print('Student removed.')
        else:
            print("NO SUCH PERSON")

def quit_function():
    stu_list.sort(key = lambda x:x[4], reverse=True)
    finish = input("Save data?[yes/no] ")
    if finish == 'yes':
        file_name = input("File name: ")
        fw = open(file_name,'w')
        for i in stu_list:
            data = '{}\t{}\t{}\t{}\n'.format(i[0],i[1],i[2],i[3])
            fw.write(data)
        fw.close()
    elif finish =="no":
        pass
    
while True:
    command = input("# ").lower() 
    if command == "show":
        show_function(stu_list)
    elif command == "search":
        search_function()
    elif command == "changescore":
        changescore_function()
    elif command == "add":
        add_function()
    elif command == "searchgrade":
        searchgrade_function()
    elif command == "remove":
        remove_function()
    elif command == "quit":
        quit_function()
        break
    else:
        continue