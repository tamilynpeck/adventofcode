import pytest
from utils import read_txt
from day19 import Day19


test_data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


def test_part_one():
    data = read_txt(test_data)
    program = Day19(data)

    result = program.solve_part_one()

    assert result == 6


def test_part_two():
    data = read_txt(test_data)
    program = Day19(data)

    result = program.solve_part_two()

    assert result == 16


@pytest.mark.parametrize(
    "line,expected",
    [
        ("brwrr", True),
        ("bggr", True),
        ("gbbr", True),
        ("rrbgbr", True),
        ("ubwu", False),
        ("bwurrg", True),
        ("brgr", True),
        ("bbrgwb", False),
    ],
)
def test_program_function(line, expected):
    data = read_txt(test_data)
    program = Day19(data)

    result = program.is_possible(line)

    assert result == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        ("uggbggwuurbrgbwbwbgbwbwbbgrgbbwwuwbubguurbwbgrbbwwgrbuuw", True),
        ("bwbbrrgrrbrggubuggwgguguburbbgbgrruggugbggggb", False),
    ],
)
def test_program_function_real_data(line, expected):
    test_data = """rug, uugbb, bubbbr, bbubw, wwb, wbw, gwbbuw, ubg, ruwug, bbwuww, wubwrw, ug, ugu, ggrbg, ruw, rbur, uuubbuu, wb, wurrbgr, rwruwwuu, rwg, rwbb, bwugugg, bur, ggwub, brgbr, guuu, wgg, bbw, ugrbrb, ggrw, wbgu, rwgbg, ggwu, wurwuw, gruub, gugw, bgu, wrr, rbrg, bww, uggwrr, rgg, uugb, bbrwuru, rw, urbu, ggggg, ru, wrrgwrrb, uurrgur, bgrw, ubuwr, gwwgug, bggb, uwub, gwu, wrwbgw, rrbb, uuwrggb, uuugw, bbbubg, bg, ggr, rgw, ugburuw, ggbbww, rrgbru, wurg, wugu, rbuu, wgrg, ubugu, uuwuur, ur, wgbbg, wubu, gbrrwgu, bwbu, wbgguwg, rrwbwru, buggggg, bwu, uw, grubg, bggbw, ugwwgwu, rbubgwg, wgwuu, rrr, uubwwgrr, bbwguw, uuru, wgww, grbwu, gbgww, uuu, gruwwg, urgw, ubu, ggbgb, buwur, bbgb, bub, wbru, gbug, wgrruub, wrwwru, wuwgg, uwg, uuwgw, rrruwb, rbr, grrrugwb, rbgb, wwbr, ggbugg, ggg, buu, uwr, guug, wg, wbwu, wgb, rbbb, rub, wru, bubr, rgruwrgr, gwr, urru, wuw, uuwg, bbr, ruwg, urwgu, bwbugbb, wgbgrwgg, grwb, rwgg, uugg, uww, w, urwgrgb, gw, ubrb, grbrrbrw, wgwgrr, rggurb, buuww, bgrrb, wbrg, ggburu, rgwgb, wrw, bw, wubbb, bbwww, ubbg, bbg, ruururru, rbg, wgug, gur, rrugw, gwurbg, gr, bwwgrr, gub, wrgwrw, gbrrb, rr, rgbu, bbrur, ubgbu, wuwrw, guub, guu, uwbww, gguuww, ubuw, uuggu, wgwg, grwrr, bwg, uwgrb, grwu, gwbw, rwu, buubrb, ggbubw, wrgw, wwu, uuubwrgb, urwgbwu, rwggwrg, uuuw, gbrwb, bbuu, urgbgb, www, guw, uuw, wbubg, brw, gubruu, uwrg, bbbggg, bwr, wgbg, wguw, rbbgruru, uubgggr, ugw, grgugr, uugrrbb, rwgwg, ubgu, burgwgbw, gwrubbu, bwuug, bburur, burwu, wbb, ub, wr, ggubww, grw, ww, buw, urbru, gbgr, burwgur, ugr, gwwbgb, urr, wuwg, bbubrrgu, wuuwb, brrwg, g, gbgurrw, rgu, ubb, urggug, wub, gwubu, bgrr, wrbwwb, guuuuug, rrb, brugwu, wgrgwu, bru, wrbgugur, ubww, uur, uuub, wubwrb, uubggur, bbu, urb, rrggwuw, brgw, urbrrg, uwuur, bubw, bbwuu, gbu, rrg, rrgbw, gbr, wbu, ubrw, rww, ubw, wugr, rrur, bggu, uurrbwr, br, ggu, bgww, gwbbubgu, grwbw, uu, wguwg, urwubg, rruwg, wur, rgbwg, wbrgbg, ugrr, wbbggu, gww, bugb, wrbr, grurrg, gbrgwb, rur, gubbr, gbb, gggubwgu, gwbbbwru, rbbbu, rg, gwg, bgg, rgbg, uubbrwb, uwur, rwr, uwu, wbg, wwwbgurr, grb, gbg, rugg, wgub, bb, bgb, ubwbrww, gugbr, wwgwwwug, brb, rbb, uwgg, ubbbw, rwwr, urrw, ubuuub, wbub, ugbrr, ubrr, bgwr, gwb, wuuw, ggbuwb, wug, wgugr, urgrb, uwbbwr, gwgb, uug, gbur, wwr, gug, rgbubw, ruu, gbbw, grg, ggruwgb, urwggu, rrw, rgguuu, bgwg, uub, rbu, bu, grrr, r, ugb, bbrb, gwwbr, bwwur, wwg, grurrgb, wrguuu, rgggw, ugbwg, rwb, wubgw, grrww, uwb, bgw, bggrw, rgr, rbwg, buugbbb, bgr, gbgrgr, wbr, wgr, wbbr, gg, gru, urg, bguu, bbwbgur, bburgw, ubr, wrg, gu, rbw, rwbrur, bwgru, ubwrugb, uggubw, rgbr, bbgg, wrb, wwuug, bwbuw, rb, gwugbr, uuwrw, u, rburg, wguwgwu, bwrru, uguwgb, wuu, ugg, bgrg, wrrw, brg, rwwru, buuwg, ubuuwwr, ruwr, bbb, guwuwuug, rrbgg, ugwub, rrwwugb, bug, wgw, urw, brr, bwuwrw, bbug, rru, brbubb, bwb, ggbr, rgb, gwrwb, grbgw, rrwuruw, wruuwgrb, brruubu, bgwbu, grr, ubru, rbrr, wubwuub, grbr

    uggbggwuurbrgbwbwbgbwbwbbgrgbbwwuwbubguurbwbgrbbwwgrbuuw"""
    data = read_txt(test_data)
    program = Day19(data)

    result = program.is_possible(line)

    assert result == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        ("brwrr", 2),
        ("bggr", 1),
        ("gbbr", 4),
        ("rrbgbr", 6),
        ("ubwu", 0),
        ("bwurrg", 1),
        ("brgr", 2),
        ("bbrgwb", 0),
    ],
)
def test_program_function(line, expected):
    data = read_txt(test_data)
    program = Day19(data)

    result = program.how_many_possible(line)

    assert result == expected
