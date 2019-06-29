# To make attributes private, use __example
# Python, unlike Java or C++ doesn't have the concpt
# of privacy. Using __ is a convention for avoiding
# accidental modifications


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
print(cloud.__dict__)
# You canstill access the attribuates via this way!
print(cloud._TagCloud__tags)
