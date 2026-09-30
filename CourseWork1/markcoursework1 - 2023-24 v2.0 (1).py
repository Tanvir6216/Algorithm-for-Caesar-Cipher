import io
import os
import sys
import unittest
import importlib
import signal
from unittest import mock
mf = "caesar.py" # Your file must be called "caesar.py"
md = mf[0:-3]
print('Automated Python unit test : Testing the file "'+mf+'"')
try:
    m = importlib.import_module(md,mf)
except Exception as ex:
    print('\nError! Problem loading the file "'+mf+'"\n')
    print("Exception : ",ex)
    print('\nCannot run any tests')
    print('\nFinal Grade =  0 ')

def tuple_upper_compare(tuple1,tuple2):
    return all(str(x).upper() == str(y).upper() for x, y in zip(tuple1, tuple2))

def strip_all_white_spaces(string):
    return ''.join(string.split())  

class TestCoursework(unittest.TestCase):
    
    Score = 0    

    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_01_welcome(self,mocked_input):
        print('\n\nTesting the function "welcome()" (10%)')
        print('This function should output the following text:\nWelcome to the Caesar Cipher\nThis program encrypts and '
              'decrypts text with the Caesar Cipher.')
        mocked_input.side_effect = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        answer=''
        capturedOutput = io.StringIO()              
        x = sys.stdout
        sys.stdout = capturedOutput                 
        err = ''
        try:
            m.welcome()                                 # Call function.
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        print(capturedOutput.getvalue())
        # answer = capturedOutput.getvalue().lower().find('caesar')
        answer = capturedOutput.getvalue().strip()
        print(answer)
        if strip_all_white_spaces(answer) == strip_all_white_spaces('Welcome to the Caesar Cipher\nThis program encrypts and decrypts text with the Caesar Cipher.') :
            TestCoursework.Score = TestCoursework.Score + 10
            print('Success. The function "welcome()" output matches. Current Score = '+str(TestCoursework.Score))
        else:
            answer = answer.lower().find('caesar')
            if  answer >=0 :
                #print(capturedOutput.getvalue())
                TestCoursework.Score = TestCoursework.Score + 9
                print('Success. The function "welcome()" output mostly matches. Current Score = '+str(TestCoursework.Score))
            else:
                answer = capturedOutput.getvalue().strip()
                answer = answer.lower().find('cipher')
                if  answer >=0 :
                    #print(capturedOutput.getvalue())
                    TestCoursework.Score = TestCoursework.Score + 8
                    print('Success. The function "welcome()" output mostly matches. Current Score = '+str(TestCoursework.Score))
                else:
                    if err != '': print( err )
                    print('Unexpected output.')
                    print('Failure. The function "welcome()" output does not match expected output. Current Score = 0')

        print("=====================================================");
    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_02_enter_message(self,mocked_input):
        print('\n\nTesting the function "enter_message()" (15%)')
        print('This function should return two strings and a number - the mode of conversion, the message, and the shift. '
              'The message should be converted to upper case.\n')
        mocked_input.side_effect = ['e', 'Hello', '3', 'd', 'World', '4', 'g', 'n','n','n','e', 'Good Bye', '6']
        capturedOutput = io.StringIO()              
        x = sys.stdout
        sys.stdout = capturedOutput                 
        result1 = None
        result2 = None
        result3 = None
        try:
            err = ''
            result1 = m.enter_message()
            result2 = m.enter_message()
            result3 = m.enter_message()
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        print('Calling the function "enter_message()" with input of "e", "Hello", "3"')
        answer1 = ('e', 'HELLO', 3)
        print('Expecting the function to return ',answer1,'. Received the values',result1)
        if result1 ==  answer1:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        elif result1 is not None and tuple_upper_compare(result1, answer1):
            TestCoursework.Score = TestCoursework.Score +4
            print('Partial Success. Current Score = '+str(TestCoursework.Score))
        else:
            if err != '': print( err )
            print('Failure. Current Score = '+str(TestCoursework.Score))
        print('Calling the function "enter_message()" with input of "d", "World", "4"')
        answer2 = ('d', 'WORLD', 4)
        print('Expecting the function to return ',answer2,'. Received the values',result2)
        if result2 ==  answer2:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        elif result2 is not None and tuple_upper_compare(result2, answer2):
            TestCoursework.Score = TestCoursework.Score +4
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if err != '': print( err )
            print('Failure. Current Score = '+str(TestCoursework.Score))
        print('Calling the function "enter_message()" with input of "g", "n", "n", "n", "e", "Good Bye", "6"')
        answer3 = ('e', 'GOOD BYE', 6)
        print('Expecting the function to return ',answer3,'. Received the values',result3)
        if result3 ==  answer3:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        elif result3 is not None and tuple_upper_compare(result3, answer3):
            TestCoursework.Score = TestCoursework.Score +4
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if err != '': print( err )
            print('Failure. Current Score = '+str(TestCoursework.Score))

        print("=====================================================");

    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_03_encrypt(self,mocked_input):
        print('\n\nTesting the function "encrypt()" (25%)')
        print('This function should take 2 parameters, the message to be encrypted, and the shift number, and return a single value, '
              'a string - the encrypted message.')
        mocked_input.side_effect = ['.', '.', '.', '.', '.', '.', '.', '.','.','.','.', '.', '.']
        capturedOutput = io.StringIO()              
        x = sys.stdout
        sys.stdout = capturedOutput                 
        result1 = None
        result2 = None
        result3 = None
        result4 = None
        result5 = None
        try:
            err = ''
            result1 = m.encrypt("ABC", 3)
            result2 = m.encrypt("XYZ", 3)
            result3 = m.encrypt("Hello", 3)
            result4 = m.encrypt("a b c", 4)
            result5 = m.encrypt("ab456c", 5)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        if err != '': print( err )
        answer1 = "DEF"
        print('Calling the function "encrypt()" with input of "ABC", 3')
        print('Expecting the function to return ',answer1,'. Received the value ',result1)
        if result1 ==  answer1:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if result1 is not None and answer1 in str(result1).upper():
                TestCoursework.Score = TestCoursework.Score +4
                print('Partial success. Current Score = '+str(TestCoursework.Score))
            else:
                if err != '': print( err )
                print('Failure. Current Score = '+str(TestCoursework.Score))
        answer2 = "ABC"
        print('Calling the function "encrypt()" with input of "XYZ", 3')
        print('Expecting the function to return ',answer2,'. Received the value ',result2)
        if result2 ==  answer2:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if result2 is not None and answer2 in str(result2).upper():
                TestCoursework.Score = TestCoursework.Score +4
                print('Partial success. Current Score = '+str(TestCoursework.Score))
            else:
                if err != '': print( err )
                print('Failure. Current Score = '+str(TestCoursework.Score))
        answer3 = "KHOOR"
        print('Calling the function "encrypt()" with input of "Hello", 3')
        print('Expecting the function to return ',answer3,'. Received the value ',result3)
        if result3 ==  answer3:
            print('Success. Current Score = '+str(TestCoursework.Score))
            TestCoursework.Score = TestCoursework.Score +5
        else:
            if result3 is not None and answer3 in str(result3).upper():
                TestCoursework.Score = TestCoursework.Score +4
                print('Partial success. Current Score = '+str(TestCoursework.Score))
            else:
                if err != '': print( err )
                print('Failure. Current Score = '+str(TestCoursework.Score))
        answer4 = "E F G"
        print('Calling the function "encrypt()" with input of "a b c", 4')
        print('Expecting the function to return ',answer4,'. Received the value ',result4)
        if result4 ==  answer4:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if result4 is not None and answer4 in str(result4).upper():
                TestCoursework.Score = TestCoursework.Score +4
                print('Partial success. Current Score = '+str(TestCoursework.Score))
            else:
                if err != '': print( err )
                print('Failure. Current Score = '+str(TestCoursework.Score))
        answer5 = "FG456H"
        print('Calling the function "encrypt()" with input of "ab456c", 5')
        print('Expecting the function to return ',answer5,'. Received the value ',result5)
        if result5 ==  answer5:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if result5 is not None and answer5 in str(result5).upper():
                TestCoursework.Score = TestCoursework.Score +4
                print('Partial success. Current Score = '+str(TestCoursework.Score))
            else:
                if err != '': print( err )
                print('Failure. Current Score = '+str(TestCoursework.Score))
        print("=====================================================");

    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_04_decrypt(self,mocked_input):
        print('\n\nTesting the function "decrypt()" (25%)')
        print('This function should take 2 parameters, the message to be decrypted, and the shift number, and return a single value, '
              'a string - the decrypted message.')
        mocked_input.side_effect = ['.', '.', '.', '.', '.', '.', '.', '.','.','.','.', '.', '.']
        capturedOutput = io.StringIO()              
        x = sys.stdout
        sys.stdout = capturedOutput                 
        result1 = None
        result2 = None
        result3 = None
        result4 = None
        result5 = None
        try:
            err = ''
            result1 = m.decrypt("ABC", 3)
            result2 = m.decrypt("XYZ", 3)
            result3 = m.decrypt("Hello", 3)
            result4 = m.decrypt("a b c", 4)
            result5 = m.decrypt("ab456c", 5)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        if err != '': print( err )
        answer1 = "XYZ"
        print('Calling the function "decrypt()" with input of "ABC", 3')
        print('Expecting the function to return ',answer1,'. Received the value ',result1)
        if result1 ==  answer1:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if result1 is not None and answer1 in str(result1).upper():
                TestCoursework.Score = TestCoursework.Score +4
                print('Partial success. Current Score = '+str(TestCoursework.Score))
            else:
                if err != '': print( err )
                print('Failure. Current Score = '+str(TestCoursework.Score))
        answer2 = "UVW"
        print('Calling the function "decrypt()" with input of "XYZ", 3')
        print('Expecting the function to return ',answer2,'. Received the value ',result2)
        if result2 ==  answer2:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if result2 is not None and answer2 in str(result2).upper():
                TestCoursework.Score = TestCoursework.Score +4
                print('Partial success. Current Score = '+str(TestCoursework.Score))
            else:
                if err != '': print( err )
                print('Failure. Current Score = '+str(TestCoursework.Score))
        answer3 = "EBIIL"
        print('Calling the function "decrypt()" with input of "Hello", 3')
        print('Expecting the function to return ',answer3,'. Received the value ',result3)
        if result3 ==  answer3:
            print('Success. Current Score = '+str(TestCoursework.Score))
            TestCoursework.Score = TestCoursework.Score +5
        else:
            if result3 is not None and answer3 in str(result3).upper():
                TestCoursework.Score = TestCoursework.Score +4
                print('Partial success. Current Score = '+str(TestCoursework.Score))
            else:
                if err != '': print( err )
                print('Failure. Current Score = '+str(TestCoursework.Score))
        answer4 = "W X Y"
        print('Calling the function "decrypt()" with input of "a b c", 4')
        print('Expecting the function to return ',answer4,'. Received the value ',result4)
        if result4 ==  answer4:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if result4 is not None and answer4 in str(result4).upper():
                TestCoursework.Score = TestCoursework.Score +4
                print('Partial success. Current Score = '+str(TestCoursework.Score))
            else:
                if err != '': print( err )
                print('Failure. Current Score = '+str(TestCoursework.Score))
        answer5 = "VW456X"
        print('Calling the function "decrypt()" with input of "ab456c", 5')
        print('Expecting the function to return ',answer5,'. Received the value ',result5)
        if result5 ==  answer5:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if result5 is not None and answer5 in str(result5).upper():
                TestCoursework.Score = TestCoursework.Score +4
                print('Partial success. Current Score = '+str(TestCoursework.Score))
            else:
                if err != '': print( err )
                print('Failure. Current Score = '+str(TestCoursework.Score))
        print("=====================================================");
        
    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_05_is_file(self,mocked_input):
        print('\n\nTesting the function "is_file()" (5%)')
        print('This function should take 1 parameter, the name of the file to be checked, and return a single value, '
              'a boolean - True if the file exists, False if it does not.')
        mocked_input.side_effect = ['.', '.', '.', '.', '.', '.', '.', '.','.','.','.', '.', '.']
        capturedOutput = io.StringIO()              
        x = sys.stdout
        sys.stdout = capturedOutput                 
        err = ''
        result1 = None
        result2 = None
        try:
            result1 = m.is_file("messages.txt")
            result2 = m.is_file("12345")
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        if err != '': print( err )
        answer1 = True
        print('Calling the function "is_file()" with input of "messages.txt"')
        print('Expecting the function to return ',answer1,', received',result1)
        if result1 ==  answer1:
            TestCoursework.Score = TestCoursework.Score +3
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            print('Failure. Current Score = '+str(TestCoursework.Score))
        answer2 = False
        print('Calling the function "is_file()" with input of "12345"')
        print('Expecting the function to return ',answer2,', received',result2)
        if result2 ==  answer2:
            TestCoursework.Score = TestCoursework.Score +2
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            print('Failure. Current Score = '+str(TestCoursework.Score))
        print("=====================================================");
        
    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_06_write_messages(self,mocked_input):
        print('\n\nTesting the function "write_messages()" (5%)')
        print('This function should take a single parameter, a list of strings. It should write these strings to a file called "results.txt", '
              'with each item taking up a single line.')
        mocked_input.side_effect = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        capturedOutput = io.StringIO()              
        x = sys.stdout
        sys.stdout = capturedOutput                 
        err = ''
        answer = ['abc','def','123']
        result = []
        try:
            m.write_messages(answer)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        if err != '': print( err )
        try:
            file = open('results.txt','r')
            for line in file:
                print(line)
                result.append(line.strip())
            file.close()
        except Exception as ex:
            err = 'Error! : '+str(ex)
            print(err)
        print('Calling the function "write_messages()" with input of ',answer)
        print('Expecting the "results.txt" to contain',answer,'. The file contains ',result)
        if result ==  answer:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            print('Failure. Current Score = '+str(TestCoursework.Score))
        print("=====================================================");

    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_07_process_file(self,mocked_input):
        print('\n\nTesting the function "process_file()" (10%)')
        print('This function should take 3 parameters, the name of the file to be processed, the mode (e or d), and the shift value. '
              'It should return a list of strings, each string being the result of processing the corresponding line in the file.')
        mocked_input.side_effect = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        capturedOutput = io.StringIO()              
        x = sys.stdout
        sys.stdout = capturedOutput                 
        answer1 = ['LIPPS', 'LIPPS ASVPH', 'ALEX!?', 'W S W', '0 1 2 3 4 5 6 7 8 9', 'XLI UYMGO FVSAR JSB NYQTW SZIV XLI PEDC HSK.', 'KSSHFCI.']
        answer2 = ['CZGGJ', 'CZGGJ RJMGY', 'RCVO!?', 'N J N', '0 1 2 3 4 5 6 7 8 9', 'OCZ LPDXF WMJRI AJS EPHKN JQZM OCZ GVUT YJB.', 'BJJYWTZ.']
        result1 = None
        result2 = None
        try:
            err = ''
            result1 =  m.process_file('messages.txt','e',4)
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        try:
            result2 =  m.process_file('messages.txt','d',5)
        except Exception as ex:
            err = err + 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x

        # Alix - 19/09/2023
        result1 = list(map(str.strip,result1))
        answer1 = list(map(str.strip,answer1))
        result2 = list(map(str.strip,result2))
        answer2 = list(map(str.strip,answer2))

        print('Calling the function "process_file()" with input of "messages.txt", "e" and 4')
        print('Expecting the function to return ',answer1,'. Received',result1)
        if result1 ==  answer1:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            print('Failure. Current Score = '+str(TestCoursework.Score))
        print('Calling the function "process_file()" with input of "messages.txt", "d" and 5')
        print('Expecting the function to return ',answer2,'. Received',result2)
        if result2 ==  answer2:
            TestCoursework.Score = TestCoursework.Score +5
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            print('Failure. Current Score = '+str(TestCoursework.Score))
        print("=====================================================");


    @classmethod
    @mock.patch(md+'.input', create=True)
    def test_08_message_or_file(self,mocked_input):
        print('\n\nTesting the function "message_or_file()" (5%)')
        print('This function should return three values, the mode ("e" or "d" based on whether the user would '
              'like to encrypt or decrypt), a message if the user would like to process messages using the console (or None) '
              'and a filename if the user would like to process data in a file (or None). '
              'It should continue to validate the mode that the user enters as well as the input mechanism (file/console). '
              'In addition, it should call the is_file() function to verify filenames. '
              'Users should be repeatedly prompted to enter the filename if the file doesn’t exist.')
        mocked_input.side_effect = ['e','c','Hello','3', 'd','c','LIPPS','4', 'e','f','messages.txt','4','n','w','x','zz','d','f','messages.txt','4']
        capturedOutput = io.StringIO()              
        x = sys.stdout
        sys.stdout = capturedOutput                 
        result1 = None
        result2 = None
        result3 = None
        result4 = None
        try:
            err = ''
            result1 = m.message_or_file()
            result2 = m.message_or_file()
            result3 = m.message_or_file()
            result4 = m.message_or_file()
        except Exception as ex:
            err = 'Error! : '+str(ex).replace('attribute', 'function called')
        sys.stdout = x
        answer1 = ('e', 'Hello', None,3)
        print('Calling the function "message_or_file()" with input of "e","c","Hello","3"')
        print('Expecting the function to return ',answer1,'. Received ',result1)
        if result1 ==  answer1:
            TestCoursework.Score = TestCoursework.Score +1
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if err != '': print( err )
            print('Failure. Current Score = '+str(TestCoursework.Score))
        answer2 = ('d', 'LIPPS', None, 4)
        print('Calling the function "message_or_file()" with input of "d","c","LIPPS","4"')
        print('Expecting the function to return ',answer2,'. Received ',result2)
        if result2 ==  answer2:
            TestCoursework.Score = TestCoursework.Score +1
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if err != '': print( err )
            print('Failure. Current Score = '+str(TestCoursework.Score))
        answer3 = ('e', None, 'messages.txt', 4)
        print('Calling the function "message_or_file()" with input of "e","f","messages.txt","4"')
        print('Expecting the function to return ',answer3,'. Received ',result3)
        if result3 ==  answer3:
            TestCoursework.Score = TestCoursework.Score +1
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if err != '': print( err )
            print('Failure. Current Score = '+str(TestCoursework.Score))
        answer4 = ('d', None, 'messages.txt', 4)
        print('Calling the function "message_or_file()" with input of "n","w","x","zz","d","f","messages.txt","4"')
        print('Expecting the function to return ',answer4,'. Received ',result4)
        if result4 ==  answer4:
            TestCoursework.Score = TestCoursework.Score +2
            print('Success. Current Score = '+str(TestCoursework.Score))
        else:
            if err != '': print( err )
            print('Failure. Current Score = '+str(TestCoursework.Score))
        print("=====================================================");

    @classmethod
    def tearDownClass(cls):
        print('\n\nFinal Score = ', TestCoursework.Score)
        print('\n')
        try:
            # os.remove("results.txt")
            pass
        except:
            pass


    @classmethod
    def setUpClass(cls):
        try:
            os.remove("results.txt")
            pass
        except:
            pass


if __name__ == '__main__':
    unittest.main()
