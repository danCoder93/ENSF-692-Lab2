# ENSF 692 Spring 2025
# May 8 Lab 2
# Exercise 2


# Trace through the execution of the following program. 
# Answer the questions in the comments with your group members.
# After discussing, use print statements to confirm your answers.

foo = 100
bar = foo
foo + bar

# POINT 1
# What is the value of foo at this point?
# [Danish Shahid]
#    Python variables are passed by object reference i.e.
#    variables are initialize with the pointer to the memory address
#    that is created for the data
#  foo value is 100

# What is the type of foo at this point?
# [DS] foo type is int

# What is the value of bar at this point?
# [DS] bar value is 100

# What is the type of bar at this point?
# [DS] bar type is int


spam = foo + bar
foo += 50
eggs = foo + bar
ham = [1, 2, 3]
baz = ham
ham.append(bar)

# POINT 2
# What is the value of foo at this point?
# [DS] foo value is 150

# What is the value of bar at this point?
# [DS] bar value is 100

# What is the value of spam at this point?
# [DS] spam value is 200

# What is the value of eggs at this point?
# [DS] egg value is 250

# What is the value of ham at this point?
# [DS] ham value is [1, 2, 3, 100]

# What is the value of baz at this point?
# [DS] baz is [1, 2, 3, 100]

eggs = "Python is very flexible!"
spam = ham
ham = bar
bar += bar
foo = eggs
eggs = bar + ham
baz.append(bar)

# POINT 3
# What is the value of foo at this point?
# [DS] foo value is 'Python is very flexible!'

# What is the value of bar at this point?
# [DS] bar value is 200

# What is the value of spam at this point?
# [DS] spam value is [1, 2, 3, 100, 200]

# What is the value of eggs at this point?
# [DS] eggs value is 300

# What is the value of ham at this point?
# [DS] ham value is 100

# What is the value of baz at this point?
# [DS] baz value is [1, 2, 3, 100, 200]

# Print out the types and final values of each variable.
print(f'foo - Value : {foo}; Type : {type(foo).__name__}')
print(f'bar - Value : {bar}; Type : {type(bar).__name__}')
print(f'spam - Value : {spam}; Type : {type(spam).__name__}')
print(f'eggs - Value : {eggs}; Type : {type(eggs).__name__}')
print(f'ham - Value : {ham}; Type : {type(ham).__name__}')
print(f'baz - Value : {baz}; Type : {type(baz).__name__}')