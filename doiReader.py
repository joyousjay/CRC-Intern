from habanero import Crossref
cr = Crossref()
def test_works_with_one_id():
    "works - param: ids, one DOI"
    res = cr.works(ids='10.1007/s00256-021-03733-8')
    return res

'''
def test_works_with_many_ids():
    "works - param: ids, many DOIs"
    dois = [
        "10.1021/acs.jcim.0c00179",
        "10.1021/acsomega.9b04233",
        "10.1063/5.0019056",
        "10.1021/acschemneuro.9b00696",
        "10.1021/acs.jpcb.0c05385", 
        "10.1021/acs.jctc.0c00185",
        "10.1021/acs.jpcb.0c00739",
        "10.1021/acs.jpcb.0c05509",
        "10.1039/d0cp05016d",
        "10.1016/j.chemphyslip.2020.105030",
        "10.1021/acs.jctc.0c01267",
    ]
    res = cr.works(ids=dois)
'''

