from Models.Repos.repo_libro import RepoLibro

repo_libro = None

def getRepoLibro():
    global repo_libro
    if repo_libro == None:
        repo_libro = RepoLibro()
    return repo_libro