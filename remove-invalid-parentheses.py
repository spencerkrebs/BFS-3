class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Helper function to check if a string has balanced parentheses
        def isValid(string: str) -> bool:
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                # If balance drops below 0, there are unmatched closing brackets
                if balance < 0:
                    return False
            return balance == 0

        # Initialize BFS queue using a set to automatically avoid processing duplicates
        queue = {s}
        # q = {"()())()"}
        while queue:
            # Check if any strings at the current level are valid
            valid_outputs = []
            for string in queue:
                if isValid(string):
                    valid_outputs.append(string)
            
            # Since BFS operates level-by-level, the first level containing
            # valid strings represents the minimum number of removals.
            # because if you keep going, you'll remove more parenthesis from those already-valid levels.
            # If you got a valid string at level 1, you won't get a valid from that string at the next level
            if valid_outputs:
                return valid_outputs
            
            # Generate the next level by removing one parenthesis at a time
            next_level = set() # )())() | (())() | ()))() | ()()() | ()()() | ()())) | ()())(
            for string in queue:
                for i in range(len(string)):#0->7
                    # Only attempt removal if the character is a parenthesis
                    if string[i] in ('(', ')'):
                        # removes 1 character by skipping i
                        new_string = string[:i] + string[i+1:]
                        next_level.add(new_string)
                        
                     
            
            queue = next_level
            #  {'()())(', '(())()', '()))()', '()()))', '()()()', ')())()'}
            #                valid                        valid
            
        return [""]
