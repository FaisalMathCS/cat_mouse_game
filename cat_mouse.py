import sys

graph = {
    "A": ("B", "Center", "E"), 
    "B": ("A", "C"), 
    "C": ("B", "Center", "D"), 
    "D": ("C", "Center", "E"), 
    "E": ("D", "A"), 
    "Center": ("A", "C", "D")
}

max_depth = 500
memo = {}

def can_cat_force_win(mouse, cat, turn, depth):
    state = (mouse, cat, turn, depth)
    if state in memo:
        return memo[state]
    
    if mouse == cat:
        return True
    
    if depth >= max_depth:
        return False

    if turn == "mouse":
        safe_move_found = False
        for next_mouse in graph[mouse]:
            if next_mouse == cat:
                continue
            if not can_cat_force_win(next_mouse, cat, "cat", depth + 1):
                safe_move_found = True
                break
        memo[state] = not safe_move_found
        return memo[state]
    else:  
        for next_cat in graph[cat]:
            if next_cat == mouse:
                memo[state] = True
                return True
            if can_cat_force_win(mouse, next_cat, "mouse", depth + 1):
                memo[state] = True
                return True
        memo[state] = False
        return False

def main(): 
    print("Starting")
    if len(sys.argv) < 3:
        print("No arguments!\nStart Position: \nMouse: A\nCat: E")
        mouse_start = "A"
        cat_start = "E" 
    elif len(sys.argv) == 3:
        mouse_start = sys.argv[1] 
        cat_start = sys.argv[2] 

    if mouse_start not in graph or cat_start not in graph:
        print("Not in Graph!", list(graph.keys()))
        sys.exit(1)

    if can_cat_force_win(mouse_start, cat_start, "mouse", 0):
        print("Cat always wins")
    else:
        print("Mouse can RUN!") 

if __name__ == "__main__":
    main()
