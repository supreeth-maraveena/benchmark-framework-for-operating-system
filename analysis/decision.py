EPS = 1e-6

def select_best(results):
    if not results:
        return []

    max_score = max(r.score for r in results)

    best_results = [
        r for r in results
        if abs(r.score - max_score) < EPS
    ]

    return best_results


def rank_results(results):
    # Descending (higher is better)
    return sorted(results, key=lambda r: r.score, reverse=True)