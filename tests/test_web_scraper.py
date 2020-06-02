from web_scraper.scraper import *

def test_count():
    test = get_citations_needed_count('https://en.wikipedia.org/wiki/Battle_of_the_Bulge')

    assert test == 9


def test_report():
    test = get_citations_needed_report('https://en.wikipedia.org/wiki/Battle_of_the_Bulge')
    
    report1 = "There are 9 cases need" in test
    report2 = 'Five copies of a report by "C"' in test
    assert report1
    assert report2