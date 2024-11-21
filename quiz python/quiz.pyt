import random

user = {}
quiz_data = {
    "C++": [
        {"q": "Which C++ keyword is used to create an object of a class?", "o": ["new", "create", "class", "object"], "a": "new"},
        {"q": "Which header file is required for input/output operations in C++?", "o": ["<iostream>", "<stdio.h>", "<conio.h>", "<input.h>"], "a": "<iostream>"},
        {"q": "What is the return type of the main() function in C++?", "o": ["int", "void", "float", "None"], "a": "int"},
        {"q": "Which of the following is used to terminate a statement in C++?", "o": [":", ".", ";", ","], "a": ";"},
        {"q": "What is the default access specifier for class members in C++?", "o": ["private", "protected", "public", "default"], "a": "private"},
        {"q": "Which function is used to dynamically allocate memory in C++?", "o": ["malloc", "new", "alloc", "allocate"], "a": "new"},
        {"q": "Which operator is used to overload a function in C++?", "o": ["()", "::", "->", "."], "a": "()"},
        {"q": "What is the purpose of the 'virtual' keyword in C++?", "o": ["For inheritance", "For polymorphism", "For abstraction", "For templates"], "a": "For polymorphism"},
        {"q": "Which of the following is not a valid loop structure in C++?", "o": ["for", "while", "do-while", "repeat-until"], "a": "repeat-until"},
        {"q": "What does STL stand for in C++?", "o": ["Standard Template Library", "System Template Library", "Simple Type Library", "Static Template Library"], "a": "Standard Template Library"}
    ],
    "Python": [
        {"q": "What does the len() function return in Python?", "o": ["The length of a string", "The number of elements in a list", "Both", "None"], "a": "Both"},
        {"q": "Which of these is an immutable data type in Python?", "o": ["List", "Set", "Tuple", "Dictionary"], "a": "Tuple"},
        {"q": "How do you start a for loop in Python?", "o": ["for x in range():", "for (x)", "loop x:", "iterate x:"], "a": "for x in range():"},
        {"q": "What is the output of 2 ** 3 in Python?", "o": ["5", "6", "8", "9"], "a": "8"},
        {"q": "What keyword is used to define a class in Python?", "o": ["class", "define", "object", "struct"], "a": "class"},
        {"q": "Which function is used to read input from the user?", "o": ["read()", "input()", "scan()", "get()"], "a": "input()"},
        {"q": "Which module in Python is used for mathematical functions?", "o": ["math", "numpy", "random", "cmath"], "a": "math"},
        {"q": "Which Python keyword is used to define a lambda function?", "o": ["lambda", "def", "function", "define"], "a": "lambda"},
        {"q": "What will 'print(type([]))' output?", "o": ["<class 'list'>", "<class 'set'>", "<class 'tuple'>", "<class 'dict'>"], "a": "<class 'list'>"},
        {"q": "How do you handle exceptions in Python?", "o": ["try-except", "if-else", "switch-case", "handle-error"], "a": "try-except"}
    ],
    "DSA": [
        {"q": "Which data structure is used to implement recursion?", "o": ["Queue", "Stack", "Heap", "Array"], "a": "Stack"},
        {"q": "What is the time complexity of bubble sort in the worst case?", "o": ["O(1)", "O(n)", "O(n^2)", "O(log n)"], "a": "O(n^2)"},
        {"q": "Which data structure is best for implementing a priority queue?", "o": ["Heap", "Queue", "Stack", "Linked List"], "a": "Heap"},
        {"q": "Which algorithm is used to find the shortest path in a graph?", "o": ["Dijkstra's", "DFS", "Merge Sort", "Flood Fill"], "a": "Dijkstra's"},
        {"q": "What is the main characteristic of a binary search tree?", "o": ["All left descendants are less than the node", "All right descendants are greater than the node", "Both", "None"], "a": "Both"},
        {"q": "Which traversal method uses a stack?", "o": ["Inorder", "DFS", "BFS", "Level-order"], "a": "DFS"},
        {"q": "What is the maximum number of nodes at level k in a binary tree?", "o": ["2^k", "k", "k^2", "k+1"], "a": "2^k"},
        {"q": "What is the height of an AVL tree with n nodes?", "o": ["O(log n)", "O(n)", "O(n^2)", "O(1)"], "a": "O(log n)"},
        {"q": "Which sorting algorithm is most efficient for small datasets?", "o": ["Bubble Sort", "Insertion Sort", "Merge Sort", "Heap Sort"], "a": "Insertion Sort"},
        {"q": "Which data structure is used to implement depth-first search?", "o": ["Stack", "Queue", "Graph", "Array"], "a": "Stack"}
    ]
}



def login():
    name = input("Enter your username: ")
    password = input("Enter your password: ")
    if user.get(name) == password:
        print("Login successful!")
        return name
    print("Invalid username or password!")
    return None

def register():
    name = input("Enter username: ")
    if name in user:
        print("User already exists!")
        return False
    password = input("Enter password: ")
    user[name] = password
    print("Registration successful!")
    return True

def quiz(subject, user, quiz_data):
    print(f"\nStarting {subject} quiz!")
    score = 0
    questions = random.sample(quiz_data[subject], len(quiz_data[subject]))[:5]

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['q']}")
        for idx, option in enumerate(q['o'], 1):
            print(f"{idx}. {option}")
        try:
            ans = int(input("Your answer (1/2/3/4): "))
            if q['o'][ans - 1] == q['a']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q['a']}")
        except (ValueError, IndexError):
            print("Invalid input! Skipping this question.")

    print(f"\n{user}, your score is {score}/5.")

def main():
    print("Welcome to the Quiz !")
    user = None

    while not user:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            if register():
                continue
        elif choice == "2":
            user = login()
        elif choice == "3":
            print("Thank you!")
            return
        else:
            print("Invalid choice!")

    while True:
        print("\nSubjects:\n1. C++\n2. Python\n3. DSA")
        choice = input("Choose a subject (1-3): ")
        if choice == "1":
            quiz("C++", user, quiz_data)
        elif choice == "2":
            quiz("Python", user, quiz_data)
        elif choice == "3":
            quiz("DSA", user, quiz_data)
        else:
            print("Invalid choice!")
            continue

        play_again = input("Do you want to take another quiz? (YES/NO): ").lower()
        if play_again != "yes":
            print("Thank you!")
            break

if __name__ == "__main__":
    main()