from abc import ABC, abstractmethod

class JobPosting(ABC):
    @abstractmethod
    def __init__(self, title: str, description: str, salary: float):
        self.title = title
        self.description = description
        self.salary = salary

    @abstractmethod
    def apply(self, job_seeker):
        pass

class FullTimeJobPosting(JobPosting):
    def __init__(self, title: str, description: str, salary: float):
        super().__init__(title, description, salary)
        self.job_type = "Full Time"

    def apply(self, job_seeker):
        # logic for applying to full-time job posting
        pass

class PartTimeJobPosting(JobPosting):
    def __init__(self, title: str, description: str, salary: float):
        super().__init__(title, description, salary)
        self.job_type = "Part Time"

    def apply(self, job_seeker):
        # logic for applying to part-time job posting
        pass

class JobSearch(ABC):
    @abstractmethod
    def search_jobs(self, query):
        pass

    @abstractmethod
    def apply_to_job(self, job_posting, job_seeker):
        pass
