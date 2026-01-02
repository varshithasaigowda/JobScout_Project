from backend.jobs import filter_matching_jobs

def test_job_match_limit():
    jobs = [{"id": i, "match_score": 90} for i in range(30)]

    selected = filter_matching_jobs(jobs)

    assert len(selected) == 15
