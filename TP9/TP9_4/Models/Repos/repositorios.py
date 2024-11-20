from Models.Repos.repo_poliza import RepoPoliza

repo_poliza = None

def getRepoPoliza():
    global repo_poliza
    if repo_poliza is None:
        repo_poliza = RepoPoliza()
    return repo_poliza    
    