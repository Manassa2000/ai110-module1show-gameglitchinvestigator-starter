from logic_utils import check_guess, get_range_for_difficulty, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_easy_range():
    # Easy should have the smallest range
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    # Normal should have a medium range
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_hard_range():
    # Hard should have the largest range
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_difficulty_ranges_increase():
    # Each level should be harder than the previous (larger range)
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high


def test_parse_guess_valid_in_range():
    # A guess within range should be accepted
    ok, value, err = parse_guess("10", 1, 20)
    assert ok is True
    assert value == 10
    assert err is None

def test_parse_guess_below_range():
    # A guess below the range should be rejected
    ok, value, err = parse_guess("0", 1, 20)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_above_range():
    # A guess above the range should be rejected
    ok, value, err = parse_guess("21", 1, 20)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_negative_number():
    # A negative number is outside the range and should be rejected
    ok, value, err = parse_guess("-5", 1, 20)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_decimal_truncates_and_validates():
    # A decimal within range should be accepted (truncated to int)
    ok, value, err = parse_guess("10.7", 1, 20)
    assert ok is True
    assert value == 10
    assert err is None

def test_parse_guess_decimal_out_of_range():
    # A decimal outside the range should be rejected
    ok, value, err = parse_guess("25.5", 1, 20)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_extremely_large_value():
    # An extremely large number should be rejected
    ok, value, err = parse_guess("999999999", 1, 20)
    assert ok is False
    assert value is None
    assert err is not None
