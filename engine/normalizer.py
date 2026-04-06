def normalize_results(results):
    # Extract all values
    wt_list = [r.avg_waiting_time for r in results]
    pf_list = [r.page_faults for r in results]
    st_list = [r.seek_time for r in results]

    # Find max values (for normalization)
    max_wt = max(wt_list) if wt_list else 1
    max_pf = max(pf_list) if pf_list else 1
    max_st = max(st_list) if st_list else 1

    # Avoid division by zero
    if max_wt == 0: max_wt = 1
    if max_pf == 0: max_pf = 1
    if max_st == 0: max_st = 1

    # Step 1: Compute base score (lower is better)
    for r in results:
        wt_norm = r.avg_waiting_time / max_wt
        pf_norm = r.page_faults / max_pf
        st_norm = r.seek_time / max_st

        score = wt_norm + pf_norm + st_norm
        r.set_score(score)

    # Step 2: Relative normalization (x / y)
    min_score = min(r.score for r in results)

    # Safety check
    if min_score == 0:
        min_score = 1e-6

    for r in results:
        r.set_score(min_score / r.score)

    return results