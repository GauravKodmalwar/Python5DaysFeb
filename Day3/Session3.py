# Exception is an event where execution of a program is halted\disturbed
# Handling exceptions - warning\log message and continue run for other data\loop
# Specific exceptions or global exception handling
# Raise an exception ==> place or code where exception arrises
# Catch them
# Continue processing of other file or other customer
import requests

def myFunction():
    try:
        news = requests.get('https://timesofindia.indiatimes.com/india/how-modi-made-it-ministry-burn-the-midnight-oil-to-ban-chinese-apps/articleshow/80889692.cms')
        print(news.text)
        var1 = 10
        var2 = 0
        assert 1==0, 'Not a valid scenario' # assert boolen statement, message (optional)
        if True != False:
            raise FileNotFoundError("File is wrong")
        assert 2==9, 'File is not correct'
        open('dsfadsfasf')
        print(var1/var2)
        var1 = 10 * 5
        print('Program completed', var1)
    except FileNotFoundError as ex:
        print('Inside a FileNotFound except block', ex)
    except InterruptedError as ex:
        pass
    except NotADirectoryError as ex:
        pass
    except Exception as ex:
        print('Global Except block: {}'.format(ex))
    finally:
        print('Completed and closing connections, cleaning memory')
try:
    myFunction()
    print('My job is done')
except Exception as e:
    print(e)

# Move yesterday's word count function from news inside try-except-finally block
# run it, try it