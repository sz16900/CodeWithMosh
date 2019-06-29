class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("python")
cloud["python"] = 10
print(len(cloud))
cloud.add("python")
cloud.add("python")
cloud.add("Python")
cloud.add("Pytsdashon")
cloud.add("Pytsdashonsdas")
print(cloud.tags)

for tag in cloud:
    print(tag)
