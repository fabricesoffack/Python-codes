
# the with statement or context managercd
# defined function
# define a source file as "story.txt" and a destination file as "story_copy"

with open("story.txt", "w") as source:
        source.write("alice in wonderland part 1\n")
        source.write("alice in wonderland part 2\n")
        source.write("alice in wonderland part 3")

def copy(source, destination):

    with open("story.txt", "r") as source:
        content = source.read()
        
    with open("story_copy.txt", "w") as destination:
        destination.write(content)
        
copy("story.txt", "story_copy.txt")

