course = "    Python Programming"

print(course.upper())
print(course.lower())
print(course.title())

print(course.strip())

print(course.find("pro"))  # doesn't exist. Case sensitive
print(course.replace("P", "-"))

print("Programming" in course)
print("Programming" not in course)
