import json
import io
import os
import sys
import unittest
import importlib
import signal
from unittest import mock
import random

mf = "noughtsandcrosses.py"  # Your file must be called noughtsandcrosses.py
md = mf[0:-3]
print('Automated Python unit test : Testing the file "'+mf+'"')
try:
    m = importlib.import_module(md,mf)
except Exception as ex:
    print('\nError! Problem loading the file "'+mf+'"\n')
    print("Exception : ",ex)
    print('\nCannot run any tests')
    print('\nFinal Grade =  0 ')

def handler(signum, frame):
    print('CTRL-C pressed')
    raise Exception("Function timed out")


def restore_leaderboard():
    filename = 'leaderboard.txt'
    leaders = {'Sarah': 5, 'Jeffrey': 1, 'Ian': -10, 'Ali': 2, 'Ahmed': 10} 
    f = open(filename, 'w')
    try:
        f.write(json.dumps(leaders))
    except Exception as error:
        print(error)
    f.close()
    return

def get_leaderboard():
    filename = 'leaderboard.txt'
    if not os.path.isfile(filename):
        return dict()
    f = open(filename)
    try:
        leaders = json.loads(f.read())
    except:
        leaders = dict()
    f.close()
    return leaders

def random_element_generator(lst):
    while True:
        yield lst[random.randint(0, len(lst)-1)]

class TestCoursework(unittest.TestCase):
    
    Grade = 0    

    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_01_draw_board(self,mocked_input):
        print('\n\nTesting the "function draw_board()" (2%)')
        print('This function should draw the Noughts and Crosses board.\n')
        mocked_input.side_effect = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        capturedOutput = io.StringIO()              # Create StringIO object
        x = sys.stdout
        sys.stdout = capturedOutput                 #  and redirect stdout.
        err = ''
        board = [ ['1','4','7'],\
                  ['2','5','8'],\
                  ['3','6','9']]
        try:
            m.draw_board(board)                                 # Call function.
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        print(capturedOutput.getvalue())
        # answer = capturedOutput.getvalue().lower().find('caesar')
        answer = capturedOutput.getvalue()
        strboard = ''
        for c in answer:
            if c in ['1','2','3','4','5','6','7','8','9']:
                strboard = strboard + c
        if strboard == '147258369':
            TestCoursework.Grade = TestCoursework.Grade + 2
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        elif strboard == '123456789':
            TestCoursework.Grade = TestCoursework.Grade + 1
            print('Partial Success. Current Grade = '+str(TestCoursework.Grade))    
        else:
            if err != '': print( err )
            print('Unexpected output.')
            print('Failure. Current Grade = 0')


    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_01a_welcome(self,mocked_input):
        print('\n\nTesting the "function welcome()"')
        print('This function should print the welcome message and display the board by calling "draw_board(board)".\n')
        mocked_input.side_effect = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        capturedOutput = io.StringIO()              # Create StringIO object
        x = sys.stdout
        sys.stdout = capturedOutput                 #  and redirect stdout.
        err = ''
        board = [ ['1','4','7'],\
                  ['2','5','8'],\
                  ['3','6','9']]
        try:
            m.welcome(board)                                 # Call function.
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        answer = capturedOutput.getvalue()
        strboard = ''
        print(answer)
        for c in answer:
            if c in ['1','2','3','4','5','6','7','8','9']:
                strboard = strboard + c
        if strboard == '147258369':
            TestCoursework.Grade = TestCoursework.Grade + 2
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        elif strboard == '123456789':
            TestCoursework.Grade = TestCoursework.Grade + 1
            print('Partial Success. Current Grade = '+str(TestCoursework.Grade))    
        elif 'welcome' in answer.lower():
            TestCoursework.Grade = TestCoursework.Grade + 1
            print('Partial Success. Current Grade = '+str(TestCoursework.Grade))    
        else:
            if err != '': print( err )
            print('Unexpected output.')
            print('Failure. Current Grade = 0')



    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_02_initialise_board(self,mocked_input):
        print('\n\nTesting the "function initialise_board()" (2%)')
        print('This function should initialise the board by setting all elemetns to one space.\n')
        mocked_input.side_effect = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        capturedOutput = io.StringIO()              # Create StringIO object
        x = sys.stdout
        sys.stdout = capturedOutput                 #  and redirect stdout.
        err = ''
        result = None
        board = [ ['1','4','7'],\
                  ['2','5','8'],\
                  ['3','6','9']]
        answer = [ [' ',' ',' '],\
                  [' ',' ',' '],\
                  [' ',' ',' ']]
        try:
            result = m.initialise_board(board)                                 # Call function.
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        # print(capturedOutput.getvalue())
        # answer = capturedOutput.getvalue().lower().find('caesar')
        # answer = capturedOutput.getvalue()
        # print(result)
        print('Expecting the function to return ',answer,'. Received the values',result)
        if result == answer:
            TestCoursework.Grade = TestCoursework.Grade + 2
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Unexpected output.')
            print('Failure. Current Grade = 0')


    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_03_get_player_move(self,mocked_input):
        print('\n\nTesting the function "get_player_move()"')
        print('This function should get the player move and return it.The player has to input a valid cell.\n')
        capturedOutput = io.StringIO()              # Create StringIO object
        x = sys.stdout
        sys.stdout = capturedOutput                 #  and redirect stdout.
        result1 = None
        result2 = None
        result3 = None
        result4 = None
        result5 = None
        board1 = [ [' ',' ',' '],\
                   [' ',' ',' '],\
                   [' ',' ',' ']]
        board2 = [ [' ',' ','X'],\
                   [' ',' ',' '],\
                   [' ',' ',' ']]
        board3 = [ [' ',' ',' '],\
                   [' ','O',' '],\
                   [' ',' ',' ']]
        board4 = [ [' ',' ',' '],\
                   [' ',' ',' '],\
                   [' ',' ',' ']]
        board5 = [ [' ',' ',' '],\
                   [' ',' ','X'],\
                   [' ',' ',' ']]
        try:
            err = ''
            mocked_input.side_effect = ['3', '3', '4', '5', '6', 'a', '0', '34', '1', '6', '7', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2']
            result1 = m.get_player_move(board1)
            mocked_input.side_effect = ['3', '4', '5', '6', 'a', '0', '34', '1', '6', '7', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ',  
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0 0', '0 1', '0 2', '1 0', '1 1', '1 2', '2 0', '2 1', '2 2', '0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2']
            result2 = m.get_player_move(board2)
            mocked_input.side_effect = ['5', '6', 'a', '0', '34', '1', '6', '7', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', 
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0 0', '0 1', '0 2', '1 0', '1 1', '1 2', '2 0', '2 1', '2 2', '0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2']
            result3 = m.get_player_move(board3)
            mocked_input.side_effect = ['a', '0', '34', '1', '6', '7', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', 
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0 0', '0 1', '0 2', '1 0', '1 1', '1 2', '2 0', '2 1', '2 2', '0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2']
            result4 = m.get_player_move(board4)
            mocked_input.side_effect = ['6', '7', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', 
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2', '0', '0', '0', '1', '0', '2', '1', '0', '1', '1', '1', '2', '2', '0', '2', '1', '2', '2',
                                        '0 0', '0 1', '0 2', '1 0', '1 1', '1 2', '2 0', '2 1', '2 2', '0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2']
            result5 = m.get_player_move(board5)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        print(capturedOutput.getvalue())
        answer1 = (0, 2)
        print('\nCalling the function "get_player_move()" with input of "3" with the board :')
        print(board1[0])
        print(board1[1])
        print(board1[2])
        print('Expecting the function to return ',answer1,'. Received the values ',result1)
        if result1 ==  answer1:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer2 = (1, 0)
        print('\nCalling the function "get_player_move()" with input of "3" and "4" with the board :')
        print(board2[0])
        print(board2[1])
        print(board2[2])
        print('Expecting the function to return ',answer2,'. Received the values ',result2)
        if result2 ==  answer2:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer3 = (1, 2)
        print('\nCalling the function "get_player_move()" with input of "5" and "6" with the board :')
        print(board3[0])
        print(board3[1])
        print(board3[2])
        print('Expecting the function to return ',answer3,'. Received the values ',result3)
        if result3 ==  answer3:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer4 = (0, 0)
        print('\nCalling the function "get_player_move()" with input of "a", "0", "34" and "1" with the board :')
        print(board4[0])
        print(board4[1])
        print(board4[2])
        print('Expecting the function to return ',answer4,'. Received the values ',result4)
        if result4 ==  answer4:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer5 = (2, 0)
        print('\nCalling the function "get_player_move()" with input of "6" and "7" with the board :')
        print(board5[0])
        print(board5[1])
        print(board5[2])
        print('Expecting the function to return ',answer5,'. Received the values ',result5)
        if result5 ==  answer5:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))

    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_04_choose_computer_move(self,mocked_input):
        print('\n\nTesting the function "choose_computer_move()" (25%)')
        print('This function should let the computer chose a cell to put a nought in and return the row and column.')
        mocked_input.side_effect = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        capturedOutput = io.StringIO()              # Create StringIO object
        x = sys.stdout
        sys.stdout = capturedOutput                 #  and redirect stdout.
        result1 = None
        result2 = None
        result3 = None
        result4 = None
        result5 = None
        board1 = [ ['O','X','O'],\
                   ['X','O',' '],\
                   ['O','X','O']]
        board2 = [ ['X','O',' '],\
                   [' ','X','X'],\
                   ['O',' ','O']]
        board3 = [ [' ','X',' '],\
                   ['X','O','X'],\
                   ['O',' ','X']]
        board4 = [ [' ','X',' '],\
                   ['X',' ','X'],\
                   ['O',' ',' ']]
        board5 = [ ['O','X','O'],\
                   [' ','O','X'],\
                   [' ','X','X']]
        try:
            err = ''
            result1 = m.choose_computer_move(board1)
            result2 = m.choose_computer_move(board2)
            result3 = m.choose_computer_move(board3)
            result4 = m.choose_computer_move(board4)
            result5 = m.choose_computer_move(board5)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        answer1 = (1, 2)
        print('\nCalling the function "choose_computer_move()" with the board :')
        print(board1[0])
        print(board1[1])
        print(board1[2])
        print('Expecting the function to return ',answer1,'. Received the values ',result1)
        if result1 ==  answer1:
            TestCoursework.Grade = TestCoursework.Grade +5
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer2 = (2, 1)
        print('\nCalling the function "choose_computer_move()" with the board :')
        print(board2[0])
        print(board2[1])
        print(board2[2])
        print('Expecting the function to return ',answer2,'. Received the values ',result2)
        if result2 ==  answer2:
            TestCoursework.Grade = TestCoursework.Grade +5
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer3 = (0, 2)
        print('\nCalling the function "choose_computer_move()" with the board :')
        print(board3[0])
        print(board3[1])
        print(board3[2])
        print('Expecting the function to return ',answer3,'. Received the values ',result3)
        if result3 ==  answer3:
            TestCoursework.Grade = TestCoursework.Grade +5
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer4 = (1, 1)
        print('\nCalling the function "choose_computer_move()" with the board :')
        print(board4[0])
        print(board4[1])
        print(board4[2])
        print('Expecting the function to return ',answer4,'. Received the values ',result4)
        if result4 ==  answer4:
            TestCoursework.Grade = TestCoursework.Grade +5
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer5 = (2, 0)
        print('\nCalling the function "choose_computer_move()" with the board :')
        print(board5[0])
        print(board5[1])
        print(board5[2])
        print('Expecting the function to return ',answer5,'. Received the values ',result5)
        if result5 ==  answer5:
            TestCoursework.Grade = TestCoursework.Grade +5
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))

    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_05_check_for_win(self,mocked_input):
        print('\n\nTesting the function "check_for_win()" (5%)')
        print('This function should check if either the player or the computer has won and return True if someone won, False otherwise.')
        mocked_input.side_effect = ['3', '3', '4', '5', '6', 'a', '0', '34', '1', '6', '7']
        capturedOutput = io.StringIO()              # Create StringIO object
        x = sys.stdout
        sys.stdout = capturedOutput                 #  and redirect stdout.
        result1 = None
        result2 = None
        result3 = None
        result4 = None
        result5 = None
        board1 = [ ['O','X','O'],\
                   ['X','X',' '],\
                   ['O','X','O']]
        board2 = [ ['X','O',' '],\
                   ['X','X','X'],\
                   ['O',' ','O']]
        board3 = [ ['O','X','X'],\
                   ['X','O','O'],\
                   ['O','O','X']]
        board4 = [ [' ','X',' '],\
                   ['X',' ','X'],\
                   ['O','O','O']]
        board5 = [ ['O','X','O'],\
                   ['X','O','X'],\
                   ['O','X','X']]
        try:
            err = ''
            result1 = m.check_for_win(board1,'X')
            result2 = m.check_for_win(board2,'O')
            result3 = m.check_for_win(board3,'X')
            result4 = m.check_for_win(board4,'O')
            result5 = m.check_for_win(board5,'X')
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        answer1 = True
        print('\nCalling the function "check_for_win()" with "X" and the board :')
        print(board1[0])
        print(board1[1])
        print(board1[2])
        print('Expecting the function to return ',answer1,'. Received the value ',result1)
        if result1 ==  answer1:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer2 = False
        print('\nCalling the function "check_for_win()" with "O" and the board :')
        print(board2[0])
        print(board2[1])
        print(board2[2])
        print('Expecting the function to return ',answer2,'. Received the value ',result2)
        if result2 ==  answer2:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer3 = False
        print('\nCalling the function "check_for_win()" with "X" and the board :')
        print(board3[0])
        print(board3[1])
        print(board3[2])
        print('Expecting the function to return ',answer3,'. Received the value ',result3)
        if result3 ==  answer3:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer4 = True
        print('\nCalling the function "check_for_win()" with "O" and the board :')
        print(board4[0])
        print(board4[1])
        print(board4[2])
        print('Expecting the function to return ',answer4,'. Received the value ',result4)
        if result4 ==  answer4:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer5 = False
        print('\nCalling the function "check_for_win()" with "X" and the board :')
        print(board5[0])
        print(board5[1])
        print(board5[2])
        print('Expecting the function to return ',answer5,'. Received the value ',result5)
        if result5 ==  answer5:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))


    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_06_check_for_draw(self,mocked_input):
        print('\n\nTesting the function "check_for_draw()"')
        mocked_input.side_effect = ['3', '3', '4', '5', '6', 'a', '0', '34', '1', '6', '7']
        capturedOutput = io.StringIO()              # Create StringIO object
        x = sys.stdout
        sys.stdout = capturedOutput                 #  and redirect stdout.
        result1 = None
        result2 = None
        board1 = [ ['O','X','O'],\
                   ['X','O','X'],\
                   ['X','O','X']]
        board2 = [ ['X','O',' '],\
                   ['X','X','X'],\
                   ['O',' ','O']]
        try:
            err = ''
            result1 = m.check_for_draw(board1)
            result2 = m.check_for_draw(board2)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        answer1 = True
        print('\nCalling the function "check_for_draw()" with the board :')
        print(board1[0])
        print(board1[1])
        print(board1[2])
        print('Expecting the function to return ',answer1,'. Received the value ',result1)
        if result1 ==  answer1:
            TestCoursework.Grade = TestCoursework.Grade +2
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer2 = False
        print('\nCalling the function "check_for_draw()" with the board :')
        print(board2[0])
        print(board2[1])
        print(board2[2])
        print('Expecting the function to return ',answer2,'. Received the value ',result2)
        if result2 ==  answer2:
            TestCoursework.Grade = TestCoursework.Grade +2
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))


    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_07_play_game(self,mocked_input):
        print('\n\nTesting the function "play_game()" (25%)')
        print('This function should:')
        print('''1.	Start with a call to the initialise_board(board) function to set the board cells to all single spaces
2.	Then draw the board
3.	Then in a loop, get the player move
4.	Update and draw the board
5.	Check if the player has won by calling check_for_win(board, mark), if so, return 1 for the score. 
6.	If not check for a draw by calling check_for_draw(board). 
7.	If drawn, return 0 for the score
8.	If not, then call choose_computer_move(board) to choose a move for the computer
9.	Update and draw the board
10.	Check if the computer has won by calling check_for_win(board, mark),
11.	If so, return -1 for the score
12.	If not check for a draw by calling check_for_draw(board)
13.	If drawn, return 0 for the score
14.	Repeat the loop from (3)
''')
        mocked_input.side_effect = random_element_generator(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                                                             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                                                             ' ', 'q', 'a', 'b', 'c', '.', 'm', 'yes', 'no', 'y', 'n', 
                                                             '0 0', '0 1', '0 2', '1 0', '1 1', '1 2', '2 0', '2 1', '2 2',
                                                             '0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2'])
        
        # capturedOutput = io.StringIO()              # Create StringIO object
        # x = sys.stdout
        # sys.stdout = capturedOutput                 #  and redirect stdout.
        result1 = None
        result2 = None
        result3 = None
        result4 = None
        result5 = None
        board  = [ [' ',' ',' '],\
                   [' ',' ',' '],\
                   [' ',' ',' ']]
        try:
            err = ''
            result1 = m.play_game(board)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        print('Game 1. Result = ',result1)
        if result1 ==  -1:
            TestCoursework.Grade = TestCoursework.Grade +5
            print('Computer won. Current Grade = '+str(TestCoursework.Grade))
        elif result1 ==  0:
            TestCoursework.Grade = TestCoursework.Grade +4
            print('Game drawn. Current Grade = '+str(TestCoursework.Grade))
        elif result1 ==  1:
            TestCoursework.Grade = TestCoursework.Grade +3
            print('Player won. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        try:
            err = ''
            result2 = m.play_game(board)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        print('Game 2. Result = ',result2)
        if result2 ==  -1:
            TestCoursework.Grade = TestCoursework.Grade +5
            print('Computer won. Current Grade = '+str(TestCoursework.Grade))
        elif result2 ==  0:
            TestCoursework.Grade = TestCoursework.Grade +4
            print('Game drawn. Current Grade = '+str(TestCoursework.Grade))
        elif result2 ==  1:
            TestCoursework.Grade = TestCoursework.Grade +3
            print('Player won. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        try:
            err = ''
            result3 = m.play_game(board)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        print('Game 3. Result = ',result3)
        if result3 ==  -1:
            TestCoursework.Grade = TestCoursework.Grade +5
            print('Computer won. Current Grade = '+str(TestCoursework.Grade))
        elif result3 ==  0:
            TestCoursework.Grade = TestCoursework.Grade +4
            print('Game drawn. Current Grade = '+str(TestCoursework.Grade))
        elif result3 ==  1:
            TestCoursework.Grade = TestCoursework.Grade +3
            print('Player won. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        try:
            err = ''
            result4 = m.play_game(board)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        print('Game 4. Result = ',result4)
        if result4 ==  -1:
            TestCoursework.Grade = TestCoursework.Grade +5
            print('Computer won. Current Grade = '+str(TestCoursework.Grade))
        elif result4 ==  0:
            TestCoursework.Grade = TestCoursework.Grade +4
            print('Game drawn. Current Grade = '+str(TestCoursework.Grade))
        elif result4 ==  1:
            TestCoursework.Grade = TestCoursework.Grade +3
            print('Player won. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        try:
            err = ''
            result5 = m.play_game(board)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        print('Game 5. Result = ',result5)
        if result5 ==  -1:
            TestCoursework.Grade = TestCoursework.Grade +5
            print('Computer won. Current Grade = '+str(TestCoursework.Grade))
        elif result5 ==  0:
            TestCoursework.Grade = TestCoursework.Grade +4
            print('Game drawn. Current Grade = '+str(TestCoursework.Grade))
        elif result5 ==  1:
            TestCoursework.Grade = TestCoursework.Grade +3
            print('Player won. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))


    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_08_menu(self,mocked_input):
        print('\n\nTesting the function "menu()" (5%)')
        print('This function should get user input of either "1", "2", "3" or "q" and return the value entered.')
        capturedOutput = io.StringIO()              # Create StringIO object
        x = sys.stdout
        sys.stdout = capturedOutput                 #  and redirect stdout.
        result1 = None
        result2 = None
        result3 = None
        result4 = None
        try:
            err = ''
            mocked_input.side_effect = ['1', '2', '3', '5', '9', 'a', '0', '34', '11', '6', 'q']
            result1 = m.menu()
            mocked_input.side_effect = ['2', '3', '5', '9', 'a', '0', '34', '11', '6', 'q']
            result2 = m.menu()
            mocked_input.side_effect = ['3', '5', '9', 'a', '0', '34', '11', '6', 'q']
            result3 = m.menu()
            mocked_input.side_effect = ['5', '9', 'a', '0', '34', '11', '6', 'q']
            result4 = m.menu()
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        answer1 = '1'
        print('\nCalling the function "menu()"')
        print('Expecting the function to return ',answer1,'. Received the value ',result1)
        if result1 ==  answer1:
            TestCoursework.Grade = TestCoursework.Grade +2
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        elif str(result1) ==  answer1:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Partial Success. Expecting a String. Received an Integer. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer2 = '2'
        print('\nCalling the function "menu()"')
        print('Expecting the function to return ',answer2,'. Received the value ',result2)
        if result2 ==  answer2:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        elif str(result2) ==  answer2:
            TestCoursework.Grade = TestCoursework.Grade + 0.5
            print('Partial Success. Expecting a String. Received an Integer. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer3 = '3'
        print('\nCalling the function "menu()"')
        print('Expecting the function to return ',answer3,'. Received the value ',result3)
        if result3 ==  answer3:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        elif str(result3) ==  answer3:
            TestCoursework.Grade = TestCoursework.Grade + 0.5
            print('Partial Success. Expecting a String. Received an Integer. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        answer4 = 'q'
        print('\nCalling the function "menu()"')
        print('Expecting the function to return ',answer4,'. Received the value ',result4)
        if result4 ==  answer4:
            TestCoursework.Grade = TestCoursework.Grade +1
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        elif str(result4) ==  answer4:
            TestCoursework.Grade = TestCoursework.Grade + 0.5
            print('Partial Success. Expecting a String. Received an Integer. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))


    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_09_load_scores(self,mocked_input):
        print('\n\nTesting the function "load_scores()" (10%)')
        print('This function should load the leaderboard scores from the file "leaderboard.txt". '
              'The function has to  return the scores in a Python dictionary, with the player names as key and the scores as values.')
        mocked_input.side_effect = ['1', '2', '3', '5', '2', 'a', '0', '34', '1', '6', 'q']
        restore_leaderboard()
        result = None
        answer = {'Sarah': 5, 'Jeffrey': 1, 'Ian': -10, 'Ali': 2, 'Ahmed': 10}
        try:
            err = ''
            result = m.load_scores()
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        print('\nCalling the function "load_scores()"')
        print('Expecting the function to return ',answer,'. Received the value ',result)
        if result ==  answer:
            TestCoursework.Grade = TestCoursework.Grade +10
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))


    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_10_save_score(self,mocked_input):
        print('\n\nTesting the function "save_score()" (10%)')
        print('This function should ask the player for their name and then save the current score to the file "leaderboard.txt"')
        mocked_input.side_effect = ['Qwerty', '2', '3', '5', '2', 'a', '0', '34', '1', '6', 'q']
        restore_leaderboard()
        result = None
        answer = {'Sarah': 5, 'Jeffrey': 1, 'Ian': -10, 'Ali': 2, 'Ahmed': 10, 'Qwerty':999}
        try:
            err = ''
            m.save_score(999)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        result = get_leaderboard()
        print('\nCalling the function "save_score()"with "Qwerty" and 999')
        print('Expecting the file to contain',answer,'. It contains ',result)
        if result ==  answer:
            TestCoursework.Grade = TestCoursework.Grade +10
            print('Success. Current Grade = '+str(TestCoursework.Grade))
        else:
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))
        restore_leaderboard()


    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_11_display_leaderboard(self,mocked_input):
        print('\n\nTesting the "function display_leaderboard()" (5%)')
        print('This function should display the leaderboard scores passed in the Python dictionary parameter "leader"')
        mocked_input.side_effect = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        leaders = {'Sarah': 5, 'Jeffrey': 1, 'Ian': -10, 'Ali': 2, 'Ahmed': 10}
        capturedOutput = io.StringIO()              # Create StringIO object
        x = sys.stdout
        sys.stdout = capturedOutput                 #  and redirect stdout.
        err = ''
        try:
            m.display_leaderboard(leaders)                                 # Call function.
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        print(capturedOutput.getvalue())
        answer = capturedOutput.getvalue()
        print('Calling the function "display_leaderboard()" with',leaders)
        for leader, score in leaders.items():
            if str(score) in answer and leader in answer:
                TestCoursework.Grade = TestCoursework.Grade + 1
                print('Found '+leader+' : '+ str(score) +'. Current Grade = '+str(TestCoursework.Grade))
        if answer.strip() == '':
            if err != '': print( err )
            print('Failure. Current Grade = '+str(TestCoursework.Grade))

    @classmethod
    def tearDownClass(cls):
        print('\n\nFinal Grade = ', TestCoursework.Grade)
        print('\n\n')
        try:
            os.remove("results.txt")
        except:
            pass

    @classmethod
    def setUpClass(cls):
        try:
            os.remove("results.txt")
        except:
            pass

if __name__ == '__main__':
    unittest.main()
