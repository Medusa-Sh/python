"id1"={"name": "Sara","class": "V","subject_integration":"Science, English, Math"}
"id2"={"name": "david","class": "V","subject_integration":"Science, English, Math"}
"id3"={"name": "Sara","class": "V","subject_integration":"Science, English, Math"}
"id4"={"name": "Ema","class": "V","subject_integration":"Science, English, Math"}
result={}
seen_keys=set()
for student_id, details in student_data.items():
    unique_keys=(details["name"], details["class"], details["subject_integration"])
    if unique_keys not in seen_keys:
        seen_keys.add(unique_keys)
        result[student_id]=details

for k,v in result.items():
    print(k,":",v)  