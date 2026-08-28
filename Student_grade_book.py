names_scores={"Saket":78,"Anshuman":85,"Mithran":79,"Alson":90,"Aarush":45}
print(names_scores)
sum=0
for names,scores in names_scores.items():
     sum+=scores
avg=sum/5
print("The class average is : ",avg)
for names,scores in names_scores.items():
     if scores==max(list(names_scores.values())):
          print(names,":",max(list(names_scores.values())))
for names,scores in names_scores.items():
     if scores==min(list(names_scores.values())):
          print(names,":",min(list(names_scores.values())))
name=input("Enter name of student :").lower().strip().capitalize()
print(names_scores.get(name,"Student not found, try different name"))