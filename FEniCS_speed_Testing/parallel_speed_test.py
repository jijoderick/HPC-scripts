from dolfin import *
import time
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print("Running on {} processes".format(size))

t0 = time.time() if rank == 0 else None

mesh = UnitSquareMesh(1000, 1000)
V = FunctionSpace(mesh, "Lagrange", 1)

u_D = Constant(0.0)

def boundary(x, on_boundary):
    return on_boundary

bc = DirichletBC(V, u_D, boundary)
f = Constant(-6.0)

u = TrialFunction(V)
v = TestFunction(V)
a = dot(grad(u), grad(v)) * dx
L = f * v * dx

u = Function(V)
solve(a == L, u, bc)

comm.Barrier()

if rank == 0:
    t1 = time.time()
    print("Total time taken: {} seconds".format(t1 - t0))
