# stacks - LIFO (last in first out)
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
# if no more items in the list, disable back button :)
if not browsing_session:
    print("disable")
# always use -1 to get to the last item in the list
print("redirect", browsing_session[-1])
