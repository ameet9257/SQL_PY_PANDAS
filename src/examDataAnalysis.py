import pandas as pd

#Reading CSV data and loading into the data frame. Skiping the first line from the file
exam1_df = pd.read_csv(r"C:\EDC\Other\pythonSkills\ExamData\exam1_data.csv",header = 1)
exam2_df = pd.read_csv(r"C:\EDC\Other\pythonSkills\ExamData\exam2_data.csv",header = 1)

#Replcaing the space from the column name
exam1_df.columns =[column.replace(" ", "_") for column in exam1_df.columns]
exam2_df.columns =[column.replace(" ", "_") for column in exam2_df.columns]

#df = pd.DataFrame(data,columns=['first_set','second_set'])
#print(pd.merge(exam2_df,exam1_df,how='left',left_on=['Student_name','Exam_name']))

# Left outer join -> Joining data frame 
exam2_left_join_exam1 = pd.merge(exam2_df,exam1_df,on=['Student_name','Exam_name'],how='left')
exam2_right_join_exam1 = pd.merge(exam2_df,exam1_df,on=['Student_name','Exam_name'],how='right')

# Getting the records from the data frame which having the null value
nan_values_exam2_left_join_exam1 = exam2_left_join_exam1[exam2_left_join_exam1['Exam_points_y'].isna()]
nan_values_exam2_right_join_exam1 = exam2_right_join_exam1[exam2_right_join_exam1['Exam_points_x'].isna()]

#print(nan_values_exam2_join_exam1)
#print(nan_values_exam1_join_exam2)

#combining the two data frame into one; ignore_index=True => If you want the row labels to adjust automatically according to the join
#df_combine_exam1_2 = pd.concat([nan_values_exam2_left_join_exam1,nan_values_exam2_right_join_exam1],ignore_index=True)

df_combine_exam1_2 = pd.concat([exam2_left_join_exam1,exam2_right_join_exam1],ignore_index=True)
#print(df_combine_exam1_2)

df_result_columns = ["Student_name","Exam_name","Exam1_points","Exam2_points","Flag"]
df_result = pd.DataFrame(columns = df_result_columns)

#print(df_result)

for index, row in df_combine_exam1_2.iterrows():
    if pd.isna(row['Exam_points_y']):
        flag = "Insert"
    elif pd.isna(row['Exam_points_x']):
        flag = "Delete"
    elif row['Exam_points_x'] == row['Exam_points_y']:
        flag = "No Change"
    else:
        flag = "Updates"
        
    new_row = {'Student_name':row['Student_name'], 'Exam_name':row['Exam_name'], 'Exam1_points':row['Exam_points_y'], 'Exam2_points':row['Exam_points_x'], 'Flag' : flag}
    df_result = df_result.append(new_row, ignore_index=True)

#getting details of students
#print(df_result)


#print(exam2_but_not_1.query('Exam_points_y == 81.0'))
#print(pd.isnull(exam2_but_not_1))

#print(exam1_df)
#print(exam2_df)


############################################################################################################################


#get list of unique records from the column
distinct_exam_name = exam2_df.Exam_name.unique()
#print(distinct_exam_name)

#get the size of ndarray
#print(distinct_exam_name.size)

#Grouping of records based on the student name and taking the count. 
student_grp_by_name = exam2_df.groupby("Student_name").count()

#Get the records of student who's appeared for all the exam.  
# @distinct_exam_name.size -> to pass the userdefined value into the query 
lsit_of_std = student_grp_by_name.query('Exam_name >= @distinct_exam_name.size')

#print(lsit_of_std.loc[:,'Student_name'])

print(lsit_of_std)

############################################################################################################################

