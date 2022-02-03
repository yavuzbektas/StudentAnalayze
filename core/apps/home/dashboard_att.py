from datetime import datetime,timedelta
from apps.attendance.models import DailyAttendance, LessonPeriods
from apps.home.models import Session,Period
from apps.student.models import StudentList
def class_name(student):
    for class_name in StudentList.objects.all():
        for student_object in class_name.students.all():
            if student_object == student:
                className_first = str(class_name.className)
                level_list = []
                name_list = []
                for i in className_first:
                    try:
                        i = int(i)
                        i = str(i)
                        level_list.append(i)
                    except:
                        name_list.append(i)
                level = ''.join(level_list)
                class_name = ''.join(name_list)
                class_name_list = []
                class_name_list.append(level)
                class_name_list.append("-")
                class_name_list.append(class_name)
                className = "".join(class_name_list)
                return (className,className_first)
def first_lesson_absent_list_students():
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    today = datetime.today().date()
    first_lesson_absent_list_att = list(DailyAttendance.objects.filter(day=today,session=session,periods=period))
    first_lesson_absent_list_att_remove = []
    for student in first_lesson_absent_list_att:
        if (str(student.lesPeriod.lessName) != "1.Ders"):
            first_lesson_absent_list_att_remove.append(student)
    for student in first_lesson_absent_list_att_remove:
        first_lesson_absent_list_att.remove(student)
    first_lesson_absent_list_students = []
    for student in first_lesson_absent_list_att:
        first_lesson_absent_list_students.append(student.student)
    for student in first_lesson_absent_list_students:
        className = class_name(student)
        first_lesson_absent_list_students[first_lesson_absent_list_students.index(student)] = (student,className[0],className[1])
    return first_lesson_absent_list_students
def today_absent_list_students():
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    today = datetime.today().date()
    now = datetime.now().time()
    today_absent_list_att = list(DailyAttendance.objects.filter(day=today,session=session,periods=period))
    day_length = 0
    lesson_periods = LessonPeriods.objects.filter(session=session,periods=period)
    for lesson_period in lesson_periods:
        time_object = datetime.strptime(lesson_period.lesPeriod.split("-")[1], '%H:%M').time()
        if now > time_object:
            day_length += 1
    today_absent_list_students = []
    for student_att in today_absent_list_att:
        student_object = student_att.student
        student_object_counter = 0
        for student in today_absent_list_att:
            if student.student == student_object:
                student_object_counter += 1
        if((student_object_counter >= day_length) and (student_object not in today_absent_list_students)):
            today_absent_list_students.append(student_object)
    for student in today_absent_list_students:
        className = class_name(student)
        today_absent_list_students[today_absent_list_students.index(student)] = (student,className[0],className[1])
    return today_absent_list_students
def week_absent_list_students():
    session=Session.objects.get(active=True)
    period=Period.objects.get(active=True)
    today = datetime.today().date()
    week_dates = [today + timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
    week_absent_list_students = []
    for i in week_dates:
        if week_dates.index(i) == 0:
            day_name_str = "Pazartesi"
        elif week_dates.index(i) == 1:
            day_name_str = "Salı"
        elif week_dates.index(i) == 2:
            day_name_str = "Çarşamba"
        elif week_dates.index(i) == 3:
            day_name_str = "Perşembe"
        elif week_dates.index(i) == 4:
            day_name_str = "Cuma"
        elif week_dates.index(i) == 5:
            day_name_str = "Cumartesi"
        else:
            day_name_str = "Pazar"
        week_dates[week_dates.index(i)] = (week_dates[week_dates.index(i)],day_name_str)
    lesson_periods = LessonPeriods.objects.filter(session=session,periods=period)
    day_length = len(lesson_periods)
    for day,day_name_str in week_dates:
        day_absent_list_att = list(DailyAttendance.objects.filter(day=day,session=session,periods=period))
        day_absent_list_students = []
        for student_att in day_absent_list_att:
            student_object = student_att.student
            student_object_counter = 0
            for student in day_absent_list_att:
                if student.student == student_object:
                    student_object_counter += 1
            if((student_object_counter == day_length) and (student_object not in day_absent_list_students)):
                day_absent_list_students.append(student_object)
        if day_absent_list_students:
            for student in day_absent_list_students:
                week_absent_list_students.append((student,day_name_str))
    for student in week_absent_list_students:
        className = class_name(student[0])
        week_absent_list_students[week_absent_list_students.index(student)] = (student[0],student[1],className[0],className[1])
    return week_absent_list_students