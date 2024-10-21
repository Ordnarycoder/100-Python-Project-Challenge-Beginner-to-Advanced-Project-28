with open("C:\\Users\\msı\\Desktop\\example.txt", "w+") as f:
    f.write("don't forget my dear friend.\n")
    f.write("everybody lies!\n")
    
    f.seek(0)
    
    content = f.read()

content = content.upper()

with open("C:\\Users\\msı\\Desktop\\example2.txt", "w+") as e:
    e.write("Example 2\n")
    e.write(content)

    e.seek(0) 
    print(e.read())
