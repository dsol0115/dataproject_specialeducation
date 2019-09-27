file = open('C:/Users/531U/Downloads/dataproject_specialeducation-master/dataproject_specialeducation-master/tweetwords.csv', 'r', encoding='utf-8')
lines = file.readlines()
sns1 = []
for line in lines:
    sns1.append(line)
file.close()

file2 = open('C:/Users/531U/Downloads/dataproject_specialeducation-master/dataproject_specialeducation-master/risswords.csv', 'r', encoding='utf-8')
lines2 = file2.readlines()
riss1 = []
for line2 in lines2:
    riss1.append(line2)
file2.close()

print(len(sns1))
print(len(riss1))

list = []

for i in range (0, len(riss1)):
    for j in range (0, len(sns1)):
        if riss1[i] == sns1[j]:
            list.append(riss1[i])