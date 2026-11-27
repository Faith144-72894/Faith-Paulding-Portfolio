import pytest,sqlite3
from service import evaluate,record
@pytest.mark.parametrize('role,payload',[
    ("AI-Technical-Program-Manager",{'passed':95,'total':100,'critical':0}),
    ("Principal-AI-Solution-Architect",{'query':'leave'}),
    ("Director-AI-Digital-Transformation",{'hours':100,'rate':60,'adoption':.8,'cost':1000}),
    ("Principal-Technical-Program-Manager",{'tasks':{'A':{'days':3,'deps':[]}}}),
    ("Enterprise-AI-Architect",{'classification':'internal','approved':True}),
    ("Director-Business-Intelligence",{'rows':[['A',100,90]]}),
    ("Director-Enterprise-Applications",{'id':'X','amount':100}),
    ("Director-Technology-Programs",{'ev':80,'pv':100,'ac':90,'bac':200}),
])
def test_dispatch(role,payload,tmp_path):
    result=evaluate(role,payload)
    assert isinstance(result,dict)
    path=tmp_path/'test.sqlite'
    record(role,payload,result,path)
    with sqlite3.connect(path) as db: assert db.execute('select count(*) from runs').fetchone()[0]==1
def test_unknown_role():
    with pytest.raises(ValueError): evaluate('unknown',{})
