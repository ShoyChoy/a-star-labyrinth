# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:09:27 2021

"""

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------

from simpleai.search import astar, SearchProblem


#------------------------------------------------------------------------------------------------------------------
#   Auxiliar functions
#------------------------------------------------------------------------------------------------------------------

def string_to_list(input_string):
    output_list = []
    row = []
    for i in input_string:
        if i != '\n':
            row.append(i)
        else:
            output_list.append(row)
            row = []
    output_list.append(row)
    return output_list

def list_to_string(input_list):
    output_string = ""
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            output_string += input_list[i][j]
        output_string += "\n"
    return output_string

def get_location(input_list, input_element):
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if input_list[i][j] == input_element:
                return (i, j)
    return (-1, -1)

def mueve_O(mapa, posicion):
    mapa[posicion[0]][posicion[1]] = 'O'
    mapa = list_to_string(mapa)
    return mapa

#------------------------------------------------------------------------------------------------------------------
#   Problem definition
#------------------------------------------------------------------------------------------------------------------

class Laberinto(SearchProblem):
    
    def __init__(self, initial_state):
        self.mapa = string_to_list(initial_state)
        self.goal = get_location(self.mapa, "X")
        self.initial_state = get_location(self.mapa, "O")
        SearchProblem.__init__(self, self.initial_state)
        
        
    def actions(self, state):
        i, j = state
        actions = []
        if self.mapa[i - 1][j] != '+':
            actions.append('Arriba')
        if self.mapa[i + 1][j] != '+':
            actions.append('Abajo')
        if self.mapa[i][j - 1] != '+':
            actions.append('Izquierda')
        if self.mapa[i][j + 1] != '+':
            actions.append('Derecha')
            
            
        return actions
    
    def result(self, state, action):
        i, j = state
        if action == 'Arriba':
            i -= 1
        if action == 'Abajo':
            i += 1
        if action == 'Izquierda':
            j -= 1
        if action == 'Derecha':
            j += 1
        
        new_state = (i,j)

        return new_state
    
    def is_goal(self, state):
        """ 
            This method evaluates whether the specified state is the goal state.

            state : The game state to test.
        """
        return state == self.goal
    
    def cost(self, state, action, state2):
        """ 
            This method receives two states and an action, and returns
            the cost of applying the action from the first state to the
            second state

            state : The initial game state.
            action : The action used to generate state2.
            state2 : The game state obtained after applying the specfied action.
        """
        return 1
    
    def heuristic(self, state):
        rows = string_to_list(state)
        fila_actual, columna_actual = get_location(rows, 'O')
        fila_objetivo, columna_objetivo = get_location(rows, 'X')
        distancia = abs(fila_objetivo - fila_actual) + abs(columna_objetivo - columna_actual)
        return distancia
    
#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------
  
initial_state = """++++++++++++++++++++++
+ O +   ++ ++        +
+     +     +++++++ ++
+ +    ++  ++++ +++ ++
+ +   + + ++         +
+          ++  ++  + +
+++++ + +      ++  + +
+++++ +++  + +  ++   +
+          + +  + +  +
+++++ +  + + +     X +
++++++++++++++++++++++"""

lista_initial = string_to_list(initial_state)
i, j = get_location(lista_initial, 'O')
lista_initial[i][j] = ' '


result = astar(Laberinto(initial_state), graph_search=True)


# Print results
for i, (action, state) in enumerate(result.path()):
    print()
    if action == None:
        print('Initial configuration')
    elif i == len(result.path()) - 1:
        print('Después de moverse ', action, '. Goal achieved!')
    else:
        print('Después de moverse ', action)
        

    print(state)
    mapa = mueve_O(lista_initial, state)
    print(mapa)
