from git import Repo
import os


"""
Get the lastest tag from a repository
"""
def get_latest_tag(path: str):
    repo = Repo(path)
    return sorted(repo.tags, key= lambda t: t.commit.committed_datetime)


def clone_repo(url: str):
    r = Repo(url)
    r.clone(os.environ['REPOS_DIR'])


def remove_project(id: int):
    #TODO: Implement after Persistence is implemented
    pass
