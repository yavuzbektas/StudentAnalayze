from apps.classes.models import Classes
from apps.student.models import StudentList
def all_class_levels():
    classes = Classes.objects.all()
    all_class_levels = []
    all_class_levels_levels = []
    for i in classes:
        if i.level not in all_class_levels:
            all_class_levels.append(i.level)

    for i in all_class_levels:
        names = []
        for x in classes:
            if x.level == i:
                names.append(x.className)
        for z in names:
            names[names.index(z)] = str(names[names.index(z)])
        names.sort()
        all_class_levels[all_class_levels.index(i)] = (str(all_class_levels[all_class_levels.index(i)]),names)

    for i in all_class_levels:
        all_class_levels_levels.append(int(i[0]))
    all_class_levels_levels.sort()
    for i in all_class_levels_levels:
        all_class_levels_levels[all_class_levels_levels.index(i)] = str(all_class_levels_levels[all_class_levels_levels.index(i)])

    for i in all_class_levels_levels:
        for x in all_class_levels:
            if i == x[0]:
                all_class_levels_levels[all_class_levels_levels.index(i)] = (all_class_levels_levels[all_class_levels_levels.index(i)],x[1])
    for i in all_class_levels_levels:
        for name in i[1]:
            name_count=i[1].count(name)
            if name_count > 1:
                for count in range(name_count-1):
                    i[1].remove(name)
    classes_all = []
    for i in StudentList.objects.all():
        if str(i.className) not in classes_all:
            classes_all.append(str(i.className))
    for i in all_class_levels_levels:
        for name in i[1]:
            if i[0]+name not in classes_all:
                all_class_levels_levels[all_class_levels_levels.index(i)][1].remove(name)
        if i[1] == []:
            all_class_levels_levels.remove(i)
    return(all_class_levels_levels)