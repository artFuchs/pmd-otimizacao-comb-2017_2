#!/usr/bin/env julia

using JuMP
using GLPKMathProgInterface

#instância de exemplo
n = 5
g = 3

pv = [1, 2, 3, 4, 5]
vx = [50, 0, 23, 55, 103]
vy = [-25, 0, 27, 28, 2]

da = Array{Float64,2}(n,n);
for i = 1:n
	for j = (i+1):n
		dx = vx[i] - vx[j]
		dy = vy[i] - vy[j]
		da[i, j] = sqrt(dx*dx + dy*dy)
		da[j, i] = sqrt(dx*dx + dy*dy)
	end
end

H = 100

#modelo e variaveis do problema
m = Model(solver = GLPKSolverMIP())

alpha = 0.05

@variable(m, minD[1:g] >= 0)
@variable(m, M[1:g] >= 0)
@variable(m, x[1:n, 1:g], Bin)

#funcao objetivo
@objective(m, Max, sum(minD[1:g]))

#restricoes
for v = 1:n
	for u = v+1:n
        	for i = 1:g
            		@constraint(m, minD[i] <= da[u,v] + (2-(x[v,i]+x[u,i])*H))
	        end
	end

	@constraint(m, sum(x[v,k] for k in 1:g) <= 1)
end

for k = 1:g
	@constraints(m, begin
		sum(x[v,k]*pv[v] for v in 1:n) >= (1-alpha)*M[k]
		sum(x[v,k]*pv[v] for v in 1:n) <= (1+alpha)*M[k]
		end)
end

#print(m)

#resolução do problema
solve(m)





