#Programmer Carlos Adrian Naal Avila
#Date 20/Oct/2019 

import n_queen_cn

#TESTS
#def test_1queen():
#    assert n_queen_cn.compute(1) == 1

#def test_2queen():
#    assert n_queen_cn.compute(2) is None or n_queen_cn.compute(2) == 0

#def test_3queen():
#    assert n_queen_cn.compute(3) is None or n_queen_cn.compute(3) == 0

#def test_4queen():
#    assert n_queen_cn.compute(4) == 2

#def test_5queen():
 #   assert n_queen_cn.compute(5) == 10

#def test_6queen():
#    assert n_queen_cn.compute(6) == 4

#def test_7queen():
 #   assert n_queen_cn.compute(7) == 40

#def test_8queen():
 #   assert n_queen_cn.compute(8) == 92
    
#def test_9queen():
 #   assert n_queen_cn.compute(9) == 352
    
#def test_10queen():
 #   assert n_queen_cn.compute(10) == 724

#def test_11queen():
 #   assert n_queen_cn.compute(11)== 2680

#def test_12queen():
 #   assert n_queen_cn.compute(12) == 14200

def test_13queen():
    assert n_queen_cn.compute(13) == 73712

#def test_14queen():
#    assert n_queen_cn.compute(14) == 365596

#def test_15queen():
#    assert n_queen_cn.compute(15) == 2279184

#def test_16queen():
#    assert n_queen_cn.compute(16) == 14772512

#def test_17queen():
#    assert n_queen_cn.compute(17) == 95815104