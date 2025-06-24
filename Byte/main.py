from collections import Counter
import os
from typing import Tuple
from urllib.request import urlretrieve
from pprint import pp

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), "commits")

urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out", commits)

# you can use this constant as key to the yyyymm:count dict

YEAR_MONTH = "{y}-{m:02d}"


def get_min_max_amount_of_commits(
    commit_log: str = commits, year: int | None = None
) -> Tuple[str, str]:
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.
    Returns a tuple of (least_active_month, most_active_month)
    """
    cnt = Counter()

    with open(commits) as f:
        for line in f.readlines():
            date, counter = line.split("|")
            _, date = date.split(":", 1)
            date = parse(date.strip())
            if (
                year is not None and year != date.year
            ):  # is the [optional] year provided?
                continue
            counter_parts = [s.strip() for s in counter.split(",")]

            ym = YEAR_MONTH.format(y=date.year, m=date.month)

            insert_and_deletes = counter_parts[1:]
            num = sum(int(el.split()[0]) for el in insert_and_deletes)

            cnt[ym] += num

    all_counts = cnt.most_common()
    highest = all_counts[0]
    lowest = all_counts[-1]
    print(highest, lowest)
    return (lowest[0], highest[0])


if __name__ == "__main__":
    get_min_max_amount_of_commits()
