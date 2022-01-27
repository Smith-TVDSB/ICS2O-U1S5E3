import pytest
import student 



def test_default():
    input_values=['4','green']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert '5' in output[2] and '12' in output[2]
    
def test_eight():
    input_values=['8','blue']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert '9' in output[2] and '24' in output[2] and '4' in output[2] and '0' in output[2]

    
def test_eight():
    input_values=['7','blue']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert '8' in output[2] and '21' in output[2] and '3' in output[2] and '1' in output[2]
