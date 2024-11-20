from Models.Repos.repo_socio import RepoSocio
from Models.Repos.repo_libro import RepoLibro
from Models.Repos.repo_prestamo import RepoPrestamo

repo_socio = None
repo_libro = None
repo_prestamo = None

def getRepoSocio():
    global repo_socio
    if repo_socio == None:
        repo_socio = RepoSocio()
    return repo_socio

def getRepoLibro():
    global repo_libro
    if repo_libro == None:
        repo_libro = RepoLibro()
    return repo_libro

def getRepoPrestamo():
    global repo_prestamo
    if repo_prestamo == None:
        repo_prestamo = RepoPrestamo()
    return repo_prestamo
