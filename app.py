
# Problem Statement: Compute the average number of books each student has read this year

student_books_list = [5, 3, 0, 7, 2, 4, 6, 8, 1, 3, 9, 5, 2, 6, 7, 4]

num_of_students = len(student_books_list)
print(f"There are {num_of_students} students in the class.")

# sum / num of students

item_at_index_3 = student_books_list[3]

#iindex Error : list index out of range

# print(student_books_list[20])

# access items from back

item_3_from_back = student_books_list[-3]
print(f"The 3 item from back is {item_3_from_back} ")

total_books = 0

for individual_books in student_books_list:
  total_books += individual_books
print(total_books)

avarage_books = total_books / num_of_students

print(f"Avarage Numbers of books per student is {avarage_books:.2f}")