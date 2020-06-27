import pytest
from data.read_sum import read_data

class Test_Sumnumber:
    @pytest.mark.parametrize("a,b,c,d", read_data())
    def test_sum(self,a,b,c,d):
        print("{}+{}+{}={}".format(a,b,c,d))
        assert a + b + c == d
