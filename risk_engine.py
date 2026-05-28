def calculate_score(
email_flags,
url_flags
):

    score=0

    score+=len(email_flags)*20

    score+=len(url_flags)*15

    return min(score,100)