my_dic={"student_name":"basu","student_id":301,"city":"bangalore"}
my_dic1={"student_name":"raghu,"student_id":201,"city":"pune"}
print(my_dic.values(),my_dic1.values())
print(my_dic.keys(),my_dic1.keys())
print(my_dic.get("student_name"))
my_dic.update(my_dic1)
print(my_dic)


#sort by key:
sorted_dict=dict(sorted(my_dic.items()))
print(sorted_dict)

#sort by value:
sorted_by_val=dict(sorted(my_dic.items(),key=lambda x: x[0]))
print(sorted_by_val)


#dictionary comprehension:
squared={x:x**2 for x in range(5)}
print(squared)


#word frequency in dict:
list1=["apple"]
count={}
for i in list1:
    count[i]=count.get(i,0)+1
print(count)
print("hello world")

