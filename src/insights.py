from src.jobs import read


def get_unique_job_types(path):
    jobs_data = read(path)
    job_types = set()
    for job in jobs_data:
        job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    filtred_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtred_jobs.append(job)

    return filtred_jobs


def get_unique_industries(path):
    jobs_data = read(path)
    industries_names = set()
    for industry in jobs_data:
        if industry["industry"] != "":
            industries_names.add(industry["industry"])

    return industries_names


def filter_by_industry(jobs, industry):
    filtred_industrys = []
    for job in jobs:
        if job["industry"] == industry:
            filtred_industrys.append(job)

    return filtred_industrys


def get_max_salary(path):
    jobs_data = read(path)
    max_salary_list = set()
    for max_salary in jobs_data:
        if max_salary["max_salary"].isdigit():
            max_salary_list.add(int(float(max_salary["max_salary"])))

    return max(list(max_salary_list))


def get_min_salary(path):
    jobs_data = read(path)
    min_salary_list = set()
    for min_salary in jobs_data:
        if min_salary["min_salary"].isdigit():
            min_salary_list.add(int(float(min_salary["min_salary"])))

    return min(list(min_salary_list))


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if (
        type(job["min_salary"]) != int
        and type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError  
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
