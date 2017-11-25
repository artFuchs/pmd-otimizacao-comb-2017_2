#!/usr/bin/env julia

using JuMP
using GLPKMathProgInterface

filename = "instancias/teste"

file = open(filename)
lines = readlines(file);

n=0
g=0
pv=0
vx=0
vy=0
M=0

for (number, content) in enumerate(lines)
    
    # Lê o número de vértices e o número de grupos.
    if number == 1
        (n, g) = split(content)
        n = parse(Int64, n)
        g = parse(Int64, g)

        pv = Array{Float64, 1}(n)
        vx = Array{Float64, 1}(n)
        vy = Array{Float64, 1}(n)
        M = Array{Float64, 1}(g)
    end
    
    # Lê os pesos e coordenadas dos vértices.
    if number > 1 && number < n + 2
        (p, x, y) = split(content)
        p = parse(Float64, p)
        x = parse(Float64, x)
        y = parse(Float64, y)
        
        pv[number - 1] = p
        vx[number - 1] = x
        vy[number - 1] = y
    
        
    end
    
    # Lê os pesos alvos dos grupos.
    if number >= n + 2 && number <= n + g + 1
        M[number - n - 1] = parse(Float64, content);
    end
end

println("leitura do arquivo concluida");

da = Array{Float64,2}(n,n);
H = 0;
for i = 1:n
    for j = (i+1):n
        dx = vx[i] - vx[j]
        dy = vy[i] - vy[j]
        da[i, j] = sqrt(dx*dx + dy*dy)
        da[j, i] = sqrt(dx*dx + dy*dy)
        if H < da[i, j]
            H = da[i,j]
        end
    end
end

println("calculos de distancias concluidos");

# Modelo e variaveis do problema
m = Model(solver = GLPKSolverMIP())

alpha = 0.05

@variable(m, minD[1:g] >= 0)
@variable(m, x[1:n, 1:g], Bin)

# Funcao objetivo
@objective(m, Max, sum(minD[1:g]))

# Restricoes
for v = 1:n
	for u = v+1:n
        	for i = 1:g
            	@constraint(m, minD[i] <= da[u,v] + (2-(x[v,i]+x[u,i]))*H)
	        end
	end

	@constraint(m, sum(x[v,k] for k in 1:g) == 1)
end

for k = 1:g
	@constraints(m, begin
		(1-alpha)*M[k] <= sum(x[v,k]*pv[v] for v in 1:n)
        	sum(x[v,k]*pv[v] for v in 1:n) <= (1+alpha)*M[k]
		end)
end

println("construcao do modelo concluida");
println(m)

# Resolver problema

solve(m)

# Mostrar resultados
for i = 1:g
    println("peso alvo do grupo $(i) = $(M[i])")
    println("peso total dos vertices do grupo $(i) = $(sum(getvalue(x[v,i])*pv[v] for v in 1:n))")
    println("distância minima dos vertices do grupo $(i) = $(getvalue(minD[i]))")
    println("vertices: $(getvalue(x[1:n, i]))")
end





