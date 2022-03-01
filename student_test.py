import pytest
import student 



def test_default(capsys):
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
    student.main()
    
    out, err = capsys.readouterr()
    assert '5' in out and '12' in out and '2' in out and '1' in out
    
def test_eight(capsys):
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
    student.main()
    out, err = capsys.readouterr()
    assert '9' in out and '24' in out and '4' in out and '1' in out

    
def test_eight(capsys):
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
    student.main()
    out, err = capsys.readouterr()
    assert '8' in out and '21' in out and '4' in out and '0' in out
