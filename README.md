NeuroScouting-Dev-Interview
===========================

Interview questions for dev summer intern position

The way I approached this problem was to first create a list representation
of the values of the tree. (valueCalc and finalListBuilder functions) Then convert the list representation to a tree
data structure. (createTree function) The main function uses all the other functions to create the final tree.

"""Sample Output for print main(5)."""
"""
                1
            1
                4
        1
                4
            3
                6
    1
                6
            3
                7
        2
                7
            4
                8
1
                8
            4
                7
        2
                7
            3
                6
    1
                6
            3
                4
        1
                4
            1
                1

"""
