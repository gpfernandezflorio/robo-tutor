# -*- coding: utf-8 -*-

traza = {
  "tipo":"CODIGO",
  "id":"traza",
  "nombre":"5. Traza",
  "enunciado":"Implementar la función <code>traza(A)</code> que calcule la traza de una matriz cualquiera <i>A</i>.",
  "aridad":{"traza":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"traza(np.array([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]))==5"}
  ]
}
traspuesta = {
  "tipo":"CODIGO",
  "id":"traspuesta",
  "nombre":"6. Traspuesta",
  "enunciado":"Implementar la función <code>traspuesta(A)</code> que devuelva la matriz traspuesta de <i>A</i>.",
  "aridad":{"traspuesta":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.array_equal(traspuesta(np.array([[1,2],[3,4]])),np.array([[1,3],[2,4]]))"}
  ]
}
producto = {
  "tipo":"CODIGO",
  "id":"producto",
  "nombre":"8. Producto",
  "enunciado":"Implementar la función <code>calcularAx(A,x)</code> que recibe una matriz <i>A</i> de tamaño <i>n × m</i> y un vector <i>x</i> de largo <i>m</i> y devuelve un vector <i>b</i> de largo <i>n</i> resultado de la multiplicación vectorial de la matriz y el vector.",
  "aridad":{"calcularAx":2},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.array_equal(calcularAx(np.array([[1,2],[3,4]]),np.array([1,1])),np.array([3,7]))"}
  ]
}
esDiagonalDominante = {
  "tipo":"CODIGO",
  "id":"esDiagonalDominante",
  "nombre":"11. Diagonalmente dominante",
  "enunciado":"Implementar la función <code>esDiagonalmenteDominante(A)</code> que devuelva <code>True</code> si una matriz cuadrada <i>A</i> es estrictamente diagonalmente dominante. Esto ocurre si para cada fila, el valor absoluto del elemento en la diagonal es mayor que la suma de los valores absolutos de los demás elementos en esa fila.",
  "aridad":{"esDiagonalmenteDominante":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"esDiagonalmenteDominante(np.array([[10,1,1],[-2,8,1],[2,-1,-10]]))"}
  ]
}

fechas = {
  "1":"25/9/2025-8:30",
  "2":"29/9/2025-8:30",
  "3":"1/10/2025-8:30",
  "4":"3/10/2025-8:30"
}

def etiqueta(id, texto):
  return {
    "tipo":"SECCION",
    "id":id,
    "nombre":texto
  }

error = {
  "tipo":"CODIGO",
  "id":"error",
  "nombre":"error",
  "enunciado":"Implementar la función <code>error</code> que reciba dos numeros <code>x</code> e <code>y</code>, y calcule el error de aproximar <code>x</code> usando <code>y</code> en <code>float64</code>.",
  "base":"\
def error(x,y):\n\
  \"\"\"\n\
  Recibe dos numeros x e y, y calcula el error de aproximar x usando y en float64\n\
  \"\"\"\n",
  "aridad":{"error":2},
  "pre":"import numpy as np",
  "run_data":[
    # FALTAN TESTS!
  ],
  "disponible":{"desde":fechas["1"]}
}

error_relativo = {
  "tipo":"CODIGO",
  "id":"error_relativo",
  "nombre":"error_relativo",
  "enunciado":"Implementar la función <code>error_relativo</code> que reciba dos numeros <code>x</code> e <code>y</code>, y calcule el error relativo de aproximar <code>x</code> usando <code>y</code> en <code>float64</code>.",
  "base":"\
def error_relativo(x,y):\n\
  \"\"\"\n\
  Recibe dos numeros x e y, y calcula el error relativo de aproximar x usando y en float64\n\
  \"\"\"\n",
  "aridad":{"error_relativo":2},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.allclose(error_relativo(1,1.1),0.1)"},
    {"assert":"np.allclose(error_relativo(2,1),0.5)"},
    {"assert":"np.allclose(error_relativo(-1,-1),0)"},
    {"assert":"np.allclose(error_relativo(1,-1),2)"}
  ],
  "disponible":{"desde":fechas["1"]}
}

matricesIguales = {
  "tipo":"CODIGO",
  "id":"matricesIguales",
  "nombre":"matricesIguales",
  "enunciado":"Implementar la función <code>matricesIguales</code> que devuelva <code>True</code> si ambas matrices son iguales y <code>False</code> en otro caso. Considerar que las matrices pueden tener distintas dimensiones, ademas de distintos valores.",
  "base":"\
def matricesIguales(A,B):\n\
  \"\"\"\n\
  Devuelve True si ambas matrices son iguales y False en otro caso.\n\
  Considerar que las matrices pueden tener distintas dimensiones, ademas de distintos valores.\n\
  \"\"\"\n",
  "aridad":{"matricesIguales":2},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"matricesIguales(np.diag([1,1]),np.eye(2))"},
    {"assert":"matricesIguales(np.linalg.inv(np.array([[1,2],[3,4]]))@np.array([[1,2],[3,4]]),np.eye(2))"},
    {"assert":"not matricesIguales(np.array([[1,2],[3,4]]).T,np.array([[1,2],[3,4]]))"}
  ],
  "disponible":{"desde":fechas["1"]}
}

rota = {
  "tipo":"CODIGO",
  "id":"rota",
  "nombre":"rota",
  "enunciado":"Implementar la función <code>rota</code> que reciba un angulo <code>theta</code> y retorne una matriz de 2 x 2 que rota un vector dado en un angulo <code>theta</code>.",
  "base":"\
def rota(theta):\n\
  \"\"\"\n\
  Recibe un angulo theta y retorna una matriz de 2x2 que rota un vector dado en un angulo theta\n\
  \"\"\"\n",
  "aridad":{"rota":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.allclose(rota(0), np.eye(2))"},
    {"assert":"np.allclose(rota(np.pi/2), np.array([[0, -1],[1, 0]]))"},
    {"assert":"np.allclose(rota(np.pi), np.array([[-1, 0],[0, -1]]))"}
  ],
  "disponible":{"desde":fechas["2"]}
}

escala = {
  "tipo":"CODIGO",
  "id":"escala",
  "nombre":"escala",
  "enunciado":"Implementar la función <code>escala</code> que reciba una tira de números <code>s</code> y retorne una matriz cuadrada de <code>n</code> x <code>n</code>, donde <code>n</code> es el tamano de <code>s</code>. La matriz escala la componente <code>i</code> de un vector de R<sup>n</sup> en un factor <code>s[i]</code>.",
  "base":"\
def escala(s):\n\
  \"\"\"\n\
  % Recibe una tira de números s y retorna una matriz cuadrada de n x n, donde n es el tamano de s. La matriz escala la componente i de un vector de Rn en un factor s[i]\n\
  \"\"\"\n",
  "aridad":{"escala":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.allclose(escala([2,3]), np.array([[2,0],[0,3]]))"},
    {"assert":"np.allclose(escala([1,1,1]), np.eye(3))"},
    {"assert":"np.allclose(escala([0.5,0.25]), np.array([[0.5,0],[0,0.25]]))"}
  ],
  "disponible":{"desde":fechas["2"]}
}

rota_y_escala = {
  "tipo":"CODIGO",
  "id":"rota_y_escala",
  "nombre":"rota_y_escala",
  "enunciado":"Implementar la función <code>rota_y_escala</code> que reciba un ángulo <code>theta</code> y una tira de números <code>s</code>, y retorne una matriz de 2 x 2 que rota el vector en un ángulo <code>theta</code> y luego lo escala en un factor <code>s</code>.",
  "base":"\
def rota_y_escala(theta,s)\n\
  \"\"\"\n\
  % Recibe un ángulo theta y una tira de números s, y retorna una matriz de 2 x 2 que rota el vector en un ángulo theta y luego lo escala en un factor s\n\
  \"\"\"\n",
  "aridad":{"rota_y_escala":2},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.allclose(rota_y_escala(0,[2,3]), np.array([[2,0],[0,3]]))"},
    {"assert":"np.allclose(rota_y_escala(np.pi/2,[1,1]), np.array([[0,-1],[1,0]]))"},
    {"assert":"np.allclose(rota_y_escala(np.pi,[2,2]), np.array([[-2,0],[0,-2]]))"}
  ],
  "disponible":{"desde":fechas["2"]}
}

afin = {
  "tipo":"CODIGO",
  "id":"afin",
  "nombre":"afin",
  "enunciado":"Implementar la función <code>afin</code> que reciba un ángulo <code>theta</code>, una tira de números <code>s</code> (en R<sup>2</sup>), y un vector <code>b</code> en (R<sup>2</sup>) y retorne una matriz de 3 x 3 que rota el vector en un ángulo <code>theta</code>, luego lo escala en un factor <code>s</code> y por último lo muevo en un valor fijo <code>b</code>.",
  "base":"\
def afin(theta,s,b)\n\
  \"\"\"\n\
  % Recibe un ángulo theta, una tira de números s (en R2), y un vector b en (R2) y retorna una matriz de 3 x 3 que rota el vector en un ángulo theta, luego lo escala en un factor s y por último lo muevo en un valor fijo b\n\
  \"\"\"\n",
  "aridad":{"afin":3},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.allclose(\
      afin(0,[1,1],[1,2]),\
      np.array([[1,0,1],\
                [0,1,2],\
                [0,0,1]]))\
    "},
    {"assert":"np.allclose(\
      afin(np.pi/2,[1,1],[0,0]),\
      np.array([[0,-1,0],\
                [1, 0,0],\
                [0, 0,1]]))\
    "},
    {"assert":"np.allclose(\
      afin(0,[2,3],[1,1]),\
      np.array([[2,0,1],\
                [0,3,1],\
                [0,0,1]]))\
    "}
  ],
  "disponible":{"desde":fechas["2"]}
}

trans_afin = {
  "tipo":"CODIGO",
  "id":"trans_afin",
  "nombre":"trans_afin",
  "enunciado":"Implementar la función <code>trans_afin</code> que reciba un vector <code>v</code> (en R<sup>2</sup>), un ángulo <code>theta</code>, una tira de números <code>s</code> (en R<sup>2</sup>), y un vector <code>b</code> en (R<sup>2</sup>) y retorne el vector <code>w</code> resultante de aplicar la transformacion afin a <code>v</code>.",
  "base":"\
def trans_afin(v,theta,s,b)\n\
  \"\"\"\n\
  % Recibe un vector v (en R2), un ángulo theta, una tira de números s (en R2), y un vector b en (R2) y retorna el vector w resultante de aplicar la transformacion afin a v\n\
  \"\"\"\n",
  "aridad":{"trans_afin":4},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.allclose(\
      trans_afin(np.array([1,0]), np.pi/2,[1,1],[0,0]),\
      np.array([0,1]))\
    "},
    {"assert":"np.allclose(\
      trans_afin(np.array([1,1]), 0,[2,3],[0,0]),\
      np.array([2,3]))\
    "},
    {"assert":"np.allclose(\
      trans_afin(np.array([1,0]), np.pi/2,[3,2],[4,5]),\
      np.array([4,7]))\
    "}
  ],
  "disponible":{"desde":fechas["2"]}
}

norma = {
  "tipo":"CODIGO",
  "id":"norma",
  "nombre":"norma",
  "enunciado":"Implementar la función <code>norma</code> que la norma <code>p</code> del vector <code>x</code>.",
  "base":"\
def norma(x,p):\n\
  \"\"\"\n\
  Devuelve la norma p del vector x.\n\
  \"\"\"\n",
  "aridad":{"norma":2},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.allclose(norma(np.array([1,1]),2),np.sqrt(2))"},
    {"assert":"np.allclose(norma(np.array([1]*10),2),np.sqrt(10))"},
    {"assert":"norma(np.random.rand(10),2)<=np.sqrt(10)"},
    {"assert":"norma(np.random.rand(10),2)>=0"}
  ],
  "disponible":{"desde":fechas["3"]}
}

normaliza = { # OJO: Agregar la definición de norma al pre
  "tipo":"CODIGO",
  "id":"normaliza",
  "nombre":"normaliza",
  "enunciado":"Implementar la función <code>normaliza</code> que reciba <code>X</code>, una lista de vectores no vacios, y un escalar <code>p</code> y devuelva una lista donde cada elemento corresponde a normalizar los elementos de <code>X</code> con la norma <code>p</code>.",
  "base":"\
def normaliza(X, p):\n\
  \"\"\"\n\
  Recibe X, una lista de vectores no vacios, y un escalar p. Devuelve una lista donde cada elemento corresponde a normalizar los elementos de X con la norma p.\n\
  \"\"\"\n",
  "aridad":{"normaliza":2},
  "pre":"import numpy as np",
  "run_data":[
    # FALTAN TESTS (ver nota en el doc)!
  ],
  "disponible":{"desde":fechas["3"]}
}

normaMatMC = {
  "tipo":"CODIGO",
  "id":"normaMatMC",
  "nombre":"normaMatMC",
  "enunciado":"Implementar la función <code>normaMatMC</code> que devuelva la norma <code>||A||</code><sub>q,p</sup> y el vector <code>x</code> en el cual se alcanza el maximo.",
  "base":"\
def normaMatMC(A,q,p,Np):\n\
  \"\"\"\n\
  Devuelve la norma ||A||\\_{q,p} y el vector x en el cual se alcanza el maximo.\n\
  \"\"\"\n",
  "aridad":{"normaMatMC":4},
  "pre":"import numpy as np",
  "post":"\
nMC1 = normaMatMC(A=np.eye(2),q=2,p=1,Np=100000)\n\
nMC2 = normaMatMC(A=np.eye(2),q=2,p='inf',Np=100000)\n\
A = np.array([[1,2],[3,4]])\n\
nMC3 = normaMatMC(A=A,q='inf',p='inf',Np=1000000)\
  ",
  "run_data":[
    {"assert":"np.allclose(nMC1[0],1,atol=1e-3)"},
    {"assert":"np.allclose(np.abs(nMC1[1][0]),1,atol=1e-3) or np.allclose(np.abs(nMC1[1][1]),1,atol=1e-3)"},
    {"assert":"np.allclose(np.abs(nMC1[1][0]),0,atol=1e-3) or np.allclose(np.abs(nMC1[1][1]),0,atol=1e-3)"},
    {"assert":"np.allclose(nMC2[0],np.sqrt(2),atol=1e-3)"},
    {"assert":"np.allclose(np.abs(nMC2[1][0]),1,atol=1e-3) and np.allclose(np.abs(nMC2[1][1]),1,atol=1e-3)"},
    {"assert":"np.allclose(nMC3[0],normaExacta(A,'inf'),rtol=2e-1)"}
  ],
  "disponible":{"desde":fechas["3"]}
}

normaExacta = {
  "tipo":"CODIGO",
  "id":"normaExacta",
  "nombre":"normaExacta",
  "enunciado":"Implementar la función <code>normaExacta</code> que devuelva una lista con las normas 1 e infinito de una matriz <code>A</code> usando las expresiones del enunciado 2.(c).",
  "base":"\
def normaExacta(A,p=[1,'inf']):\n\
  \"\"\"\n\
  Devuelve una lista con las normas 1 e infinito de una matriz A usando las expresiones del enunciado 2.(c).\n\
  \"\"\"\n",
  "aridad":{"normaExacta":2},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.allclose(normaExacta(np.array([[1,-1],[-1,-1]]),1),2)"},
    {"assert":"np.allclose(normaExacta(np.array([[1,-2],[-3,-4]]),1),7)"},
    {"assert":"np.allclose(normaExacta(np.array([[1,-2],[-3,-4]]),'inf'),6)"},
    {"assert":"normaExacta(np.array([[1,-2],[-3,-4]]),2) is None"},
    {"assert":"normaExacta(np.random.random((10,10)),1)<=10"},
    {"assert":"normaExacta(np.random.random((4,4)),'inf')<=4)"}
  ],
  "disponible":{"desde":fechas["3"]}
}

condMC = { # OJO: Agregar la definición de normaMatMC al pre
  "tipo":"CODIGO",
  "id":"condMC",
  "nombre":"condMC",
  "enunciado":"Implementar la función <code>condMC</code> que devuelva el numero de condicion de <code>A</code> usando la norma inducida <code>p</code>.",
  "base":"\
def condMC(A, p):\n\
  \"\"\"\n\
  Devuelve el numero de condicion de A usando la norma inducida p.\n\
  \"\"\"\n",
  "aridad":{"condMC":2},
  "pre":"import numpy as np",
  "run_data":[
    {"pre":"\
A = np.array([[1,1],[0,1]])\n\
A_ = np.linalg.solve(A,np.eye(A.shape[0]))\n\
normaA = normaMatMC(A,2,2,10000)\n\
normaA_ = normaMatMC(A_,2,2,10000)\n\
condA = condMC(A,2,10000)\
","assert":"np.allclose(normaA[0]*normaA_[0],condA,atol=1e-3)"},
    {"pre":"\
A = np.array([[3,2],[4,1]])\n\
A_ = np.linalg.solve(A,np.eye(A.shape[0]))\n\
normaA = normaMatMC(A,2,2,10000)\n\
normaA_ = normaMatMC(A_,2,2,10000)\n\
condA = condMC(A,2,10000)\
","assert":"np.allclose(normaA[0]*normaA_[0],condA,atol=1e-3)"}
  ],
  "disponible":{"desde":fechas["3"]}
}

condExacto = { # OJO: Agregar la definición de normaExacta al pre
  "tipo":"CODIGO",
  "id":"condExacto",
  "nombre":"condExacto",
  "enunciado":"Implementar la función <code>condExacto</code> que devuelve el numero de condicion de <code>A</code> a partir de la formula de la ecuacion (1) usando la norma <code>p</code>.",
  "base":"\
def condExacto(A, p):\n\
  \"\"\"\n\
  Que devuelve el numero de condicion de A a partir de la formula de la ecuacion (1) usando la norma p.\n\
  \"\"\"\n",
  "aridad":{"condExacto":2},
  "pre":"import numpy as np",
  "run_data":[
    {"pre":"\
A = np.random.rand(10,10)\n\
A_ = np.linalg.solve(A,np.eye(A.shape[0]))\n\
normaA = normaExacta(A,1)\n\
normaA_ = normaExacta(A_,1)\n\
condA = condExacta(A,1)\
","assert":"np.allclose(normaA*normaA_,condA)"},
    {"pre":"\
A = np.random.rand(10,10)\n\
A_ = np.linalg.solve(A,np.eye(A.shape[0]))\n\
normaA = normaExacta(A,'inf')\n\
normaA_ = normaExacta(A_,'inf')\n\
condA = condExacta(A,'inf')\
","assert":"np.allclose(normaA*normaA_,condA)"}
  ],
  "disponible":{"desde":fechas["3"]}
}

calculaLU = {
  "tipo":"CODIGO",
  "id":"calculaLU",
  "nombre":"calculaLU",
  "enunciado":"Implementar la función <code>calculaLU</code> que calcule la factorizacion LU de la matriz <code>A</code> y retorne las matrices <code>L</code> y <code>U</code>, junto con el numero de operaciones realizadas. En caso de que la matriz no pueda factorizarse retorna <code>None</code>.",
  "base":"\
def calculaLU(A):\n\
  \"\"\"\n\
  Calcula la factorizacion LU de la matriz A y retorna las matrices L y U, junto con el numero de operaciones realizadas. En caso de que la matriz no pueda factorizarse retorna None.\n\
  \"\"\"\n",
  "aridad":{"calculaLU":1},
  "pre":"import numpy as np",
  "post":"\
L01 = np.array([[1,0,0],[0,1,0],[1,1,1]])\n\
U01 = np.array([[10,1,0],[0,2,1],[0,0,1]])\n\
A1 =  L01 @ U01\n\
L1,U1,nops1 = calculaLU(A1)\n\
L02 = np.array([[1,0,0],[1,1.001,0],[1,1,1]])\n\
U02 = np.array([[1,1,1],[0,1,1],[0,0,1]])\n\
A2 =  L02 @ U02\n\
L2,U2,nops2 = calculaLU(A2)\n\
L03 = np.array([[1,0,0],[1,1,0],[1,1,1]])\n\
U03 = np.array([[1,1,1],[0,0,1],[0,0,1]])\n\
A3 =  L03 @ U03\n\
L3,U3,nops3 = calculaLU(A3)\
  ",
  "run_data":[
    {"assert":"np.allclose(L1,L01)"},
    {"assert":"np.allclose(U1,U01)"},
    {"assert":"not np.allclose(L2,L02)"},
    {"assert":"not np.allclose(U2,U02)"},
    {"assert":"np.allclose(L2,L02,atol=1e-3)"},
    {"assert":"np.allclose(U2,U02,atol=1e-3)"},
    {"assert":"nops2 == 13"},
    {"assert":"L3 is None"},
    {"assert":"U3 is None"},
    {"assert":"nops3 == 0"}
  ],
  "disponible":{"desde":fechas["4"]}
}

res_tri = {
  "tipo":"CODIGO",
  "id":"res_tri",
  "nombre":"res_tri",
  "enunciado":"Implementar la función <code>res_tri</code> que resuelva el sistema <code>Lx = b</code>, donde <code>L</code> es triangular. Se puede indicar si es triangular inferior o superior usando el argumento inferior (por default asumir que es triangular inferior).",
  "base":"\
def res_tri(L,b,inferior=True):\n\
  \"\"\"\n\
  Resuelve el sistema Lx = b, donde L es triangular. Se puede indicar si es triangular inferior o superior usando el argumento inferior (por default asumir que es triangular inferior).\n\
  \"\"\"\n",
  "aridad":{"res_tri":3},
  "pre":"import numpy as np",
  "post":"\
A1 = np.array([[1,0,0],[1,1,0],[1,1,1]])\n\
A2 = np.array([[3,2,1],[0,2,1],[0,0,1]])\n\
A3 = np.array([[1,-1,1],[0,1,-1],[0,0,1]])\
  ",
  "run_data":[
    { "pre":"b = np.array([1,1,1])",
      "assert":"np.allclose(res_tri(A1,b),np.array([1,0,0]))"
    },
    { "pre":"b = np.array([0,1,0])",
      "assert":"np.allclose(res_tri(A1,b),np.array([0,1,-1]))"
    },
    { "pre":"b = np.array([-1,1,-1])",
      "assert":"np.allclose(res_tri(A1,b),np.array([-1,2,-2]))"
    },
    { "pre":"b = np.array([-1,1,-1])",
      "assert":"np.allclose(res_tri(A1,b,inferior=False),np.array([-1,1,-1]))"
    },
    { "pre":"b = np.array([3,2,1])",
      "assert":"np.allclose(res_tri(A2,b,inferior=False),np.array([1/3,1/2,1]))"
    },
    { "pre":"b = np.array([1,0,1])",
      "assert":"np.allclose(res_tri(A3,b,inferior=False),np.array([1,1,1]))"
    }
  ],
  "disponible":{"desde":fechas["4"]}
}

inversa = {
  "tipo":"CODIGO",
  "id":"inversa",
  "nombre":"inversa",
  "enunciado":"Implementar la función <code>inversa</code> que calcule la inversa de <code>A</code> empleando la factorizacion LU y las funciones que resuelven sistemas triangulares.",
  "base":"\
def inversa(A):\n\
  \"\"\"\n\
  Calcula la inversa de A empleando la factorizacion LU\n\
  y las funciones que resuelven sistemas triangulares.\n\
  \"\"\"\n",
  "aridad":{"inversa":1},
  "pre":"import numpy as np",
  "run_data":[
    {"pre":"\
asserts = []\n\
ntest = 10\n\
iter = 0\n\
while iter < ntest:\n\
    A = np.random.random((4,4))\n\
    A_ = inversa(A)\n\
    if not A_ is None:\n\
        asserts.append(np.allclose(np.linalg.inv(A),A_))\n\
        iter += 1\
    ","assert":"all(asserts)"},
    { "pre":"A = np.array([[1,2,3],[4,5,6],[7,8,9]])",
      "assert":"assert(inversa(A) is None)"
    }
  ],
  "disponible":{"desde":fechas["4"]}
}

calculaLDV = {
  "tipo":"CODIGO",
  "id":"calculaLDV",
  "nombre":"calculaLDV",
  "enunciado":"Implementar la función <code>calculaLDV</code> que calcule la factorizacion LDV de la matriz <code>A</code>, de forma tal que <code>A = LDV</code>, con <code>L</code> triangular inferior, <code>D</code> diagonal y <code>V</code> triangular superior. En caso de que la matriz no pueda factorizarse retorna <code>None</code>.",
  "base":"\
def calculaLDV(A):\n\
  \"\"\"\n\
  Calcula la factorizacion LDV de la matriz A, de forma tal que A = LDV, con L triangular inferior, D diagonal y V triangular superior. En caso de que la matriz no pueda factorizarse retorna None.\n\
  \"\"\"\n",
  "aridad":{"calculaLDV":1},
  "pre":"import numpy as np",
  "post":"\
L01 = np.array([[1,0,0],[1,1.,0],[1,1,1]])\n\
D01 = np.diag([1,2,3])\n\
V01 = np.array([[1,1,1],[0,1,1],[0,0,1]])\n\
A1 =  L01 @ D01  @ V01\n\
L1,D1,V1,nops1 = calculaLDV(A1)\n\
L02 = np.array([[1,0,0],[1,1.001,0],[1,1,1]])\n\
D02 = np.diag([3,2,1])\n\
V02 = np.array([[1,1,1],[0,1,1],[0,0,1.001]])\n\
A2 =  L02 @ D02  @ V02\n\
L2,D2,V2,nops2 = calculaLDV(A2)\
  ",
  "run_data":[
    {"assert":"np.allclose(L1,L01)"},
    {"assert":"np.allclose(D1,D01)"},
    {"assert":"np.allclose(V1,V01)"},
    {"assert":"np.allclose(L2,L02,1e-3)"},
    {"assert":"np.allclose(D2,D02,1e-3)"},
    {"assert":"np.allclose(V2,V02,1e-3)"}
  ],
  "disponible":{"desde":fechas["4"]}
}

esSDP = {
  "tipo":"CODIGO",
  "id":"esSDP",
  "nombre":"esSDP",
  "enunciado":"Implementar la función <code>esSDP</code> que checkea si la matriz <code>A</code> es simetrica definida positiva (SDP) usando la factorizacion LDV.",
  "base":"\
def esSDP(A,atol=1e-8):\n\
  \"\"\"\n\
  Checkea si la matriz A es simetrica definida positiva (SDP) usando la factorizacion LDV.\n\
  \"\"\"\n",
  "aridad":{"esSDP":2},
  "pre":"import numpy as np",
  "run_data":[
    {"pre":"\
L0 = np.array([[1,0,0],[1,1,0],[1,1,1]])\n\
D0 = np.diag([1,1,1])\n\
A = L0 @ D0 @ L0.T\
    ","assert":"esSDP(A)"},
    {"pre":"\
D0 = np.diag([1,-1,1])\n\
A = L0 @ D0 @ L0.T\
    ","assert":"not esSDP(A)"},
    {"pre":"\
D0 = np.diag([1,1,1e-16])\n\
A = L0 @ D0 @ L0.T\
    ","assert":"not esSDP(A)"},
    {"pre":"\
L0 = np.array([[1,0,0],[1,1,0],[1,1,1]])\n\
D0 = np.diag([1,1,1])\n\
V0 = np.array([[1,0,0],[1,1,0],[1,1+1e-10,1]]).T\n\
A = L0 @ D0 @ V0\
    ","assert":"not esSDP(A)"}
  ],
  "disponible":{"desde":fechas["4"]}
}

CURSOS = {
  "alc_prueba":{
    "nombre":"Álgebra Lineal Computacional - FCEN-UBA (PRUEBA)",
    "anio":"2025",
    "edicion":"Prueba",
    "descripcion":"Curso correspondiente a la materia Álgebra Lineal Computacional de la Facultad de Ciencias Exactas y Naturales (FCEyN), UBA",
    "responsable":{
      "nombre":"Equipo de ALC",
      "contacto":"? (AT) ?"
    },
    "institucion":"Facultad de Ciencias Exactas y Naturales (FCEyN) - UBA",
    "lenguaje":"Python",
    "lenguaje_display":"none",
    # "analisisCodigo":[
    #   {"key":"CMD_X_LINE"},
    #   {"key":"INDENT"},
    #   {"key":"NEST_CMD","max":1}
    # ],
    "actividades":[
      # traza,
      # traspuesta,
      # producto,
      # esDiagonalDominante,
      etiqueta("labo1","Labo 01 (" + fechas["1"] + ")"),
        error,
        error_relativo,
        matricesIguales,
      etiqueta("labo1","Labo 02 (" + fechas["2"] + ")"),
        rota,
        escala,
        rota_y_escala,
        afin,
        trans_afin,
      etiqueta("labo3","Labo 03 (" + fechas["3"] + ")"),
        norma,
        normaliza,
        normaMatMC,
        normaExacta,
        condMC,
        condExacto,
      etiqueta("labo4","Labo 04 (" + fechas["4"] + ")"),
        calculaLU,
        res_tri,
        inversa,
        calculaLDV,
        esSDP
    ],
    "planilla":{
      "url":"1FAIpQLSfijJIbAFHK5BNEJhi31q1kXa3Z_LuLdiZjz7_O9N4SGu58WA",
      "campos":{
        "usuario":"9867257",
        "actividad":"1165966175",
        "respuesta":"1778184894",
        "resultado":"1496208069",
        "duracion":"1460244707"
      }
    }
  }
}
