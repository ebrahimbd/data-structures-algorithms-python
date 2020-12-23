#function for depth first search
def dfs(data, start,employee,visited=set()):
    
    #if not visited print it
    if start not in visited:
        print(start,end=" ")
        
        if start==employee:
            print(":",end=" ")
        
    
    visited.add(start)


    for i in data[start] - visited:
        
        #if not visited go in depth of it
        dfs(data, i, visited)
        
    return 



#sample data in dictionary form
data = {"karan": {"darshan","nikhil"},
        "darshan": {"khantil", "tanuj"},
        'tanuj': {"nikhil"},
        "krinish": {"hetul"},
        "khantil" : set(),
        "nikhil" : set()
        }


if __name__ == '__main__':

    dfs(data, "karan","karan")
