from Models.Repos.repo_socio import RepoSocio

repo_socio = None

def getRepoSocio():
    global repo_socio
    if repo_socio == None:
        repo_socio = RepoSocio()
    return repo_socio