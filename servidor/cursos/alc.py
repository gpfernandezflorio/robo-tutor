# -*- coding: utf-8 -*-

## EJERCICIOS (definidos como funciones que toman como único parámetro la fecha a partir de la cual se pueden resolver).

def traza(fecha):
  return {
  "tipo":"CODIGO",
  "id":"traza",
  "nombre":"5. Traza",
  "enunciado":"Implementar la función <code>traza(A)</code> que calcule la traza de una matriz cualquiera <i>A</i>.",
  "aridad":{"traza":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"traza(np.array([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]))==5"},
    {"assert":"traza(np.array([[1,2,3],[4,5,6],[7,8,9]]))==15"},
    {"assert":"traza(np.array([[1,2],[3,4]]))==5"},
    {"assert":"traza(np.eye(4))==4.0"},
    {"assert":"traza(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))==18"},
    {"assert":"traza(np.array([[1,2],[3,4],[5,6],[7,8]]))==5"},
    {"assert":"traza(np.array([[7]]))==7"},
    {"post":"A = np.array([[1,2],[3,4]])\nA_original = A.copy()\ntraza(A)","assert":"np.allclose(A,A_original)"}
  ],
  "disponible":{"desde":fecha}
}

def traspuesta(fecha):
  return {
  "tipo":"CODIGO",
  "id":"traspuesta",
  "nombre":"6. Traspuesta",
  "enunciado":"Implementar la función <code>traspuesta(A)</code> que devuelva la matriz traspuesta de <i>A</i>.",
  "aridad":{"traspuesta":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.array_equal(traspuesta(np.array([[1,2],[3,4]])),np.array([[1,3],[2,4]]))"},
    {"assert":"np.allclose(traspuesta(np.array([[1,2,3],[4,5,6],[7,8,9]])),np.array([[1,4,7],[2,5,8],[3,6,9]]))"},
    {"assert":"np.allclose(traspuesta(np.array([[1,2,3],[4,5,6]])),np.array([[1,4],[2,5],[3,6]]))"},
    {"assert":"np.allclose(traspuesta(np.array([[1,2],[3,4],[5,6]])),np.array([[1,3,5],[2,4,6]]))"},
    {"post":"A = np.array([[1,2,3],[4,5,6]])\nA_original = A.copy()\ntraspuesta(A)","assert":"np.allclose(A,A_original)"},
    {"assert":"np.allclose(traspuesta(np.array([[5]])),np.array([[5]]))"},
    {"assert":"np.allclose(traspuesta(traspuesta(np.array([[1,2,3],[4,5,6]]))),np.array([[1,2,3],[4,5,6]]))"}
  ],
  "disponible":{"desde":fecha}
}

def triangSup(fecha):
  return {
  "tipo":"CODIGO",
  "id":"triangSup",
  "nombre":"2. Triangular superior",
  "enunciado":"Implementar la función <code>triangSup(A)</code> que devuelva la matriz <i>U</i> correspondiente a la matriz triangular superior de <i>A</i> sin su diagonal.",
  "aridad":{"triangSup":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.array_equal(triangSup(np.array([[1,2,3],[4,5,6],[7,8,9]])),np.array([[0,2,3],[0,0,6],[0,0,0]]))"},
    {"assert":"np.array_equal(triangSup(np.array([[1,2],[3,4]])),np.array([[0,2],[0,0]]))"},
    {"post":"A = np.array([[1,2,3],[4,5,6],[7,8,9]])\nA_original = A.copy()\ntriangSup(A)","assert":"np.allclose(A,A_original)"},
    {"assert":"np.array_equal(triangSup(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])),np.array([[0,2,3,4],[0,0,7,8],[0,0,0,12]]))"},
    {"assert":"np.array_equal(triangSup(np.array([[5]])),np.array([[0]]))"}
  ],
  "disponible":{"desde":fecha}
}

def triangInf(fecha):
  return {
  "tipo":"CODIGO",
  "id":"triangInf",
  "nombre":"3. Triangular inferior",
  "enunciado":"Implementar la función <code>triangInf(A)</code> que devuelva la matriz <i>L</i> correspondiente a la matriz triangular inferior de <i>A</i> sin su diagonal.",
  "aridad":{"triangInf":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.array_equal(triangInf(np.array([[1,2,3],[4,5,6],[7,8,9]])),np.array([[0,0,0],[4,0,0],[7,8,0]]))"},
    {"assert":"np.array_equal(triangInf(np.array([[1,2],[3,4]])),np.array([[0,0],[3,0]]))"},
    {"post":"A = np.array([[1,2,3],[4,5,6],[7,8,9]])\nA_original = A.copy()\ntriangInf(A)","assert":"np.allclose(A,A_original)"},
    {"assert":"np.array_equal(triangInf(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])),np.array([[0,0,0,0],[5,0,0,0],[9,10,0,0]]))"},
    {"assert":"np.array_equal(triangInf(np.array([[5]])),np.array([[0]]))"}
  ],
  "disponible":{"desde":fecha}
}

def esCuadrada(fecha):
  return {
  "tipo":"CODIGO",
  "id":"esCuadrada",
  "nombre":"1. Es cuadrada",
  "enunciado":"Implementar la función <code>esCuadrada(A)</code> que devuelva verdadero si la matriz <i>A</i> es cuadrada y Falso en caso contrario.",
  "aridad":{"esCuadrada":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"esCuadrada(np.eye(3))"},
    {"assert":"esCuadrada(np.array([[1,2],[3,4]]))"},
    {"assert":"not esCuadrada(np.array([[1,2,3],[4,5,6]]))"},
    {"assert":"not esCuadrada(np.array([[1],[2],[3]]))"},
    {"assert":"esCuadrada(np.array([[1,2,3],[4,5,6],[7,8,9]]))"},
    {"assert":"not esCuadrada(np.array([[1,2],[3,4],[5,6]]))"},
    {"assert":"esCuadrada(np.array([[5]]))"}
  ],
  "disponible":{"desde":fecha}
}

def diagonal(fecha):
  return {
  "tipo":"CODIGO",
  "id":"diagonal",
  "nombre":"4. Diagonal",
  "enunciado":"Implementar la función <code>diagonal(A)</code> que devuelva la matriz <i>D</i> correspondiente a la matriz diagonal de <i>A</i>.",
  "aridad":{"diagonal":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.array_equal(diagonal(np.array([[1,2],[3,4]])),np.array([[1,0],[0,4]]))"},
    {"assert":"np.array_equal(diagonal(np.eye(3)),np.eye(3))"},
    {"assert":"np.array_equal(diagonal(np.array([[5,1,2],[3,6,4],[7,8,9]])),np.diag([5,6,9]))"},
    {"assert":"np.allclose(diagonal(np.array([[1,2,3],[4,5,6],[7,8,9]])),np.array([[1,0,0],[0,5,0],[0,0,9]]))"},
    {"post":"A = np.array([[1,2,3],[4,5,6],[7,8,9]])\nA_original = A.copy()\ndiagonal(A)","assert":"np.allclose(A,A_original)"},
    {"assert":"np.allclose(diagonal(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])),np.array([[1,0,0,0],[0,6,0,0],[0,0,11,0]]))"},
    {"assert":"np.allclose(diagonal(np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])),np.array([[1,0,0],[0,5,0],[0,0,9],[0,0,0]]))"},
    {"assert":"np.allclose(diagonal(np.array([[5]])),np.array([[5]]))"}
  ],
  "disponible":{"desde":fecha}
}

def esSimetrica(fecha):
  return {
  "tipo":"CODIGO",
  "id":"esSimetrica",
  "nombre":"7. Es simétrica",
  "enunciado":"Implementar la función <code>esSimetrica(A)</code> que devuelva <code>True</code> si la matriz <i>A</i> es simétrica y <code>False</code> en caso contrario.",
  "aridad":{"esSimetrica":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"esSimetrica(np.eye(3))"},
    {"assert":"esSimetrica(np.array([[1,2],[2,1]]))"},
    {"assert":"not esSimetrica(np.array([[1,2],[3,4]]))"},
    {"post":"A = np.random.rand(4,4)","assert":"esSimetrica(A.T@A)"},
    {"assert":"esSimetrica(np.array([[1,2,3],[2,4,5],[3,5,6]]))"},
    {"assert":"not esSimetrica(np.array([[1,2,3],[4,5,6],[7,8,9]]))"},
    {"assert":"not esSimetrica(np.array([[1,2,3],[4,5,6]]))"},
    {"assert":"esSimetrica(np.eye(4))"},
    {"assert":"esSimetrica(np.array([[5]]))"},
    {"post":"A = np.array([[1,2],[2,4]])\nA_original = A.copy()\nesSimetrica(A)","assert":"np.allclose(A,A_original)"}
  ],
  "disponible":{"desde":fecha}
}

def producto(fecha):
  return {
  "tipo":"CODIGO",
  "id":"producto",
  "nombre":"8. Producto",
  "enunciado":"Implementar la función <code>calcularAx(A,x)</code> que recibe una matriz <i>A</i> de tamaño <i>n × m</i> y un vector <i>x</i> de largo <i>m</i> y devuelve un vector <i>b</i> de largo <i>n</i> resultado de la multiplicación vectorial de la matriz y el vector.",
  "aridad":{"calcularAx":2},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.array_equal(calcularAx(np.array([[1,2],[3,4]]),np.array([1,1])),np.array([3,7]))"},
    {"assert":"np.allclose(calcularAx(np.array([[1,2,3],[4,5,6],[7,8,9]]),np.array([1,0,1])),np.array([4,10,16]))"},
    {"assert":"np.allclose(calcularAx(np.array([[1,2],[3,4]]),np.array([2,3])),np.array([8,18]))"},
    {"assert":"np.allclose(calcularAx(np.array([[1,2,3],[4,5,6]]),np.array([1,2,3])),np.array([14,32]))"},
    {"assert":"np.allclose(calcularAx(np.array([[1,2],[3,4]]),np.array([0,0])),np.array([0,0]))"},
    {"assert":"np.allclose(calcularAx(np.eye(3),np.array([1,2,3])),np.array([1,2,3]))"},
    {"post":"A = np.array([[1,2],[3,4]])\nx = np.array([1,2])\nA_original = A.copy()\nx_original = x.copy()\ncalcularAx(A,x)","assert":"np.allclose(A,A_original) and np.allclose(x,x_original)"}
  ],
  "disponible":{"desde":fecha}
}

def intercambiarFilas(fecha):
  return {
  "tipo":"CODIGO",
  "id":"intercambiarFilas",
  "nombre":"9. Intercambiar filas",
  "enunciado":"Implementar la función <code>intercambiarFilas(A,i,j)</code> que intercambie las filas <i>i</i> y <i>j</i> de la matriz <i>A</i>. El intercambio tiene que ser in-place.",
  "aridad":{"intercambiarFilas":3},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.allclose(intercambiarFilas(np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float),0,2),np.array([[7,8,9],[4,5,6],[1,2,3]],dtype=float))"},
    {"post":"A = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float)\nA_id = id(A)\nresultado = intercambiarFilas(A,0,1)","assert":"np.allclose(A,np.array([[4,5,6],[1,2,3],[7,8,9]],dtype=float)) and id(resultado) == A_id"},
    {"post":"A = np.array([[1,2],[3,4]],dtype=float)\nA_original = A.copy()\nintercambiarFilas(A,0,0)","assert":"np.allclose(A,A_original)"},
    {"post":"A = np.array([[1,2],[3,4],[5,6],[7,8]],dtype=float)\nintercambiarFilas(A,1,3)","assert":"np.allclose(A,np.array([[1,2],[7,8],[5,6],[3,4]],dtype=float))"},
    {"post":"A = np.array([[1,2,3,4],[5,6,7,8]],dtype=float)\nintercambiarFilas(A,0,1)","assert":"np.allclose(A,np.array([[5,6,7,8],[1,2,3,4]],dtype=float))"}
  ],
  "disponible":{"desde":fecha}
}

def sumar_fila_multiplo(fecha):
  return {
  "tipo":"CODIGO",
  "id":"sumar_fila_multiplo",
  "nombre":"10. Sumar fila múltiplo",
  "enunciado":"Implementar la función <code>sumar_fila_multiplo(A,i,j,s)</code> que a la fila <i>i</i> le sume la fila <i>j</i> multiplicada por un escalar <i>s</i>. Esta es una operación elemental clave en la eliminación gaussiana. La operación debe ser in-place.",
  "aridad":{"sumar_fila_multiplo":4},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.allclose(sumar_fila_multiplo(np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float),0,1,2),np.array([[9,12,15],[4,5,6],[7,8,9]],dtype=float))"},
    {"post":"A = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float)\nA_id = id(A)\nresultado = sumar_fila_multiplo(A,1,0,3)","assert":"np.allclose(A,np.array([[1,2,3],[7,11,15],[7,8,9]],dtype=float)) and id(resultado) == A_id"},
    {"post":"A = np.array([[2,4,6],[1,2,3]],dtype=float)\nsumar_fila_multiplo(A,0,1,-2)","assert":"np.allclose(A,np.array([[0,0,0],[1,2,3]],dtype=float))"},
    {"post":"A = np.array([[1,2],[3,4]],dtype=float)\nA_original = A.copy()\nsumar_fila_multiplo(A,0,1,0)","assert":"np.allclose(A,A_original)"},
    {"post":"A = np.array([[2,4],[3,5]],dtype=float)\nsumar_fila_multiplo(A,0,0,3)","assert":"np.allclose(A,np.array([[8,16],[3,5]],dtype=float))"},
    {"post":"A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],dtype=float)\nsumar_fila_multiplo(A,2,0,-9)","assert":"np.allclose(A,np.array([[1,2,3,4],[5,6,7,8],[0,-8,-16,-24]],dtype=float))"}
  ],
  "disponible":{"desde":fecha}
}

def esDiagonalDominante(fecha):
  return {
  "tipo":"CODIGO",
  "id":"esDiagonalDominante",
  "nombre":"11. Diagonalmente dominante",
  "enunciado":"Implementar la función <code>esDiagonalmenteDominante(A)</code> que devuelva <code>True</code> si una matriz cuadrada <i>A</i> es estrictamente diagonalmente dominante. Esto ocurre si para cada fila, el valor absoluto del elemento en la diagonal es mayor que la suma de los valores absolutos de los demás elementos en esa fila.",
  "aridad":{"esDiagonalmenteDominante":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"esDiagonalmenteDominante(np.array([[10,1,1],[-2,8,1],[2,-1,-10]]))"},
    {"assert":"esDiagonalmenteDominante(np.array([[5,1,1],[1,6,2],[1,1,4]]))"},
    {"assert":"not esDiagonalmenteDominante(np.array([[1,2,3],[4,5,6],[7,8,9]]))"},
    {"assert":"not esDiagonalmenteDominante(np.array([[2,1,1],[1,3,2],[1,1,2]]))"},
    {"assert":"esDiagonalmenteDominante(np.array([[-5,-1,-1],[1,6,2],[1,1,4]]))"},
    {"assert":"not esDiagonalmenteDominante(np.array([[5,9,-4],[1,6,2],[1,-1,4]]))"},
    {"assert":"esDiagonalmenteDominante(np.eye(4))"},
    {"assert":"esDiagonalmenteDominante(np.array([[5,0,0],[0,3,0],[0,0,7]]))"},
    {"assert":"not esDiagonalmenteDominante(np.array([[0,1,2],[1,5,1],[2,1,4]]))"},
    {"post":"A = np.array([[5,1],[1,3]])\nA_original = A.copy()\nesDiagonalmenteDominante(A)","assert":"np.allclose(A,A_original)"}
  ],
  "disponible":{"desde":fecha}
}

def matrizCirculante(fecha):
  return {
  "tipo":"CODIGO",
  "id":"matrizCirculante",
  "nombre":"12. Matriz circulante",
  "enunciado":"Implementar la función <code>matrizCirculante(v)</code> que genere una matriz circulante a partir de un vector. En una matriz circulante la primer fila es igual al vector <i>v</i>, y en cada fila se encuentra una permutación cíclica de la fila anterior, moviendo los elementos un lugar hacia la derecha.",
  "aridad":{"matrizCirculante":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.array_equal(matrizCirculante(np.array([1,2,3])),np.array([[1,2,3],[2,3,1],[3,1,2]]))"},
    {"assert":"np.array_equal(matrizCirculante(np.array([1,2,3,4])),np.array([[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]]))"},
    {"assert":"np.array_equal(matrizCirculante(np.array([5,7])),np.array([[5,7],[7,5]]))"},
    {"assert":"np.array_equal(matrizCirculante(np.array([9])),np.array([[9]]))"},
    {"post":"v = np.array([1,2,3,4])\nv_original = v.copy()\nmatrizCirculante(v)","assert":"np.allclose(v,v_original)"},
    {"post":"v = np.array([1,2,3,4,5])\nresultado = matrizCirculante(v)","assert":"resultado.shape[0] == resultado.shape[1] == len(v)"}
  ],
  "disponible":{"desde":fecha}
}

def matrizVandermonde(fecha):
  return {
  "tipo":"CODIGO",
  "id":"matrizVandermonde",
  "nombre":"13. Matriz de Vandermonde",
  "enunciado":"Implementar la función <code>matrizVandermonde(v)</code>, donde <i>v</i> ∈ R<sup>n</sup>, que devuelva la matriz de Vandermonde <i>V</i> ∈ R<sup>n×n</sup> cuya fila <i>i</i>-ésima corresponde con las potencias (<i>i</i>-1)-ésima de los elementos de <i>v</i>.",
  "aridad":{"matrizVandermonde":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.array_equal(matrizVandermonde(np.array([1,2,3])),np.array([[1,1,1],[1,2,3],[1,4,9]]))"},
    {"assert":"np.array_equal(matrizVandermonde(np.array([1,2,3,4])),np.array([[1,1,1,1],[1,2,3,4],[1,4,9,16],[1,8,27,64]]))"},
    {"assert":"np.array_equal(matrizVandermonde(np.array([0,1,2])),np.array([[1,1,1],[0,1,2],[0,1,4]]))"},
    {"assert":"np.array_equal(matrizVandermonde(np.array([5])),np.array([[1]]))"},
    {"assert":"np.array_equal(matrizVandermonde(np.array([2,3])),np.array([[1,1],[2,3]]))"},
    {"post":"v = np.array([1,2,3])\nv_original = v.copy()\nmatrizVandermonde(v)","assert":"np.allclose(v,v_original)"}
  ],
  "disponible":{"desde":fecha}
}

def numeroAureo(fecha):
  return {
  "tipo":"CODIGO",
  "id":"numeroAureo",
  "nombre":"14. Número áureo",
  "enunciado":"Implementar la función <code>numeroAureo(n)</code> que estime el número áureo φ como F<sub>k+1</sub>/F<sub>k</sub>, siendo F<sub>k</sub> el k-ésimo número de la sucesión de Fibonacci, formulando la sucesión de forma matricial con la semilla F<sub>0</sub>=0, F<sub>1</sub>=1.",
  "aridad":{"numeroAureo":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.isclose(numeroAureo(1),1.0)"},
    {"assert":"np.isclose(numeroAureo(2),2.0)"},
    {"assert":"np.isclose(numeroAureo(3),1.5)"},
    {"assert":"np.isclose(numeroAureo(4),1.6666666666666667)"},
    {"assert":"np.isclose(numeroAureo(5),1.6)"},
    {"assert":"np.isclose(numeroAureo(6),1.625)"},
    {"assert":"np.isclose(numeroAureo(7),1.6153846153846154)"},
    {"assert":"np.isclose(numeroAureo(8),1.619047619047619)"},
    {"assert":"np.isclose(numeroAureo(9),1.6176470588235294)"},
    {"assert":"np.isclose(numeroAureo(100),(1 + np.sqrt(5))/2,rtol=1e-5)"}
  ],
  "disponible":{"desde":fecha}
}

def matrizFiboncacci(fecha):
  return {
  "tipo":"CODIGO",
  "id":"matrizFiboncacci",
  "nombre":"15. Matriz de Fibonacci",
  "enunciado":"Implementar la función <code>matrizFiboncacci(n)</code> que genere una matriz <i>A</i> de <i>n</i> × <i>n</i>, donde cada a<sub>ij</sub> = F<sub>i+j</sub>, siendo F<sub>k</sub> el k-ésimo número de la sucesión de Fibonacci (considerando F<sub>0</sub>=0, F<sub>1</sub>=1).",
  "aridad":{"matrizFiboncacci":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.array_equal(matrizFiboncacci(1),np.array([[0]]))"},
    {"assert":"np.array_equal(matrizFiboncacci(2),np.array([[0,1],[1,1]]))"},
    {"assert":"np.array_equal(matrizFiboncacci(3),np.array([[0,1,1],[1,1,2],[1,2,3]]))"},
    {"assert":"np.array_equal(matrizFiboncacci(4),np.array([[0,1,1,2],[1,1,2,3],[1,2,3,5],[2,3,5,8]]))"},
    {"post":"n = 5\nresultado = matrizFiboncacci(n)","assert":"np.allclose(resultado,resultado.T)"},
    {"post":"n = 6\nresultado = matrizFiboncacci(n)","assert":"resultado.shape == (n,n)"}
  ],
  "disponible":{"desde":fecha}
}

def matrizHilbert(fecha):
  return {
  "tipo":"CODIGO",
  "id":"matrizHilbert",
  "nombre":"16. Matriz de Hilbert",
  "enunciado":"Implementar la función <code>matrizHilbert(n)</code> que genere una matriz de Hilbert <i>H</i> de <i>n</i> × <i>n</i>, donde cada h<sub>ij</sub> = 1 / (i+j+1).",
  "aridad":{"matrizHilbert":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.allclose(matrizHilbert(1),np.array([[1.0]]))"},
    {"assert":"np.allclose(matrizHilbert(2),np.array([[1.0,1/2],[1/2,1/3]]))"},
    {"assert":"np.allclose(matrizHilbert(3),np.array([[1.0,1/2,1/3],[1/2,1/3,1/4],[1/3,1/4,1/5]]))"},
    {"assert":"np.allclose(matrizHilbert(4),np.array([[1.0,1/2,1/3,1/4],[1/2,1/3,1/4,1/5],[1/3,1/4,1/5,1/6],[1/4,1/5,1/6,1/7]]))"},
    {"post":"n = 5\nresultado = matrizHilbert(n)","assert":"np.allclose(resultado,resultado.T)"},
    {"assert":"np.all(matrizHilbert(5) > 0)"},
    {"post":"n = 25\nresultado = matrizHilbert(n)\nvals = [np.isclose(resultado[i,j],1/(i+j+1)) for i in range(n) for j in range(n)]","assert":"all(vals)"}
  ],
  "disponible":{"desde":fecha}
}

def error(fecha):
  return {
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
  "post":"\
def sonIguales(x,y,atol=1e-08):\n\
  return np.allclose(error(x,y),0,atol=atol)\n\n",
  "run_data":[
    {"assert":"not sonIguales(1,1.1)"},
    {"assert":"sonIguales(1,1 + np.finfo('float64').eps)"},
    {"assert":"not sonIguales(1,1 + np.finfo('float32').eps)"},
    {"assert":"not sonIguales(np.float16(1),np.float16(1) + np.finfo('float32').eps)"},
    {"assert":"sonIguales(np.float16(1),np.float16(1) + np.finfo('float16').eps,atol=1e-3)"},
    {"assert":"error(5.0,5.0)==0.0"},
    {"assert":"np.isclose(error(3.14159,3.14),abs(3.14159-3.14))"},
    {"assert":"error(5.0,3.0)==error(3.0,5.0)"},
    {"assert":"error(5.0,3.0)>0"},
    {"assert":"np.isclose(error(-5.0,-3.0),2.0)"},
    {"assert":"np.isclose(error(-5.0,5.0),10.0)"}
  ],
  "disponible":{"desde":fecha}
}

def error_relativo(fecha):
  return {
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
    {"assert":"np.allclose(error_relativo(1,-1),2)"},
    {"assert":"np.isclose(error_relativo(5.0,5.0),0.0)"},
    {"assert":"np.isclose(error_relativo(100.0,90.0),0.1)"},
    {"assert":"np.isclose(error_relativo(-100.0,-90.0),0.1)"},
    {"post":"err1 = error_relativo(100.0,90.0)\nerr2 = error_relativo(1000.0,900.0)","assert":"np.isclose(err1,err2)"}
  ],
  "disponible":{"desde":fecha}
}

def matricesIguales(fecha):
  return {
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
    {"assert":"not matricesIguales(np.array([[1,2],[3,4]]).T,np.array([[1,2],[3,4]]))"},
    {"assert":"matricesIguales(np.array([[1,2,3],[4,5,6]]),np.array([[1,2,3],[4,5,6]]))"},
    {"assert":"not matricesIguales(np.array([[1,2],[3,4]]),np.array([[1,2,3],[4,5,6]]))"},
    {"assert":"matricesIguales(np.array([[1.0,2.0],[3.0,4.0]]),np.array([[1.0 + 1e-8,2.0 - 1e-9],[3.0 + 5e-8,4.0]]))"},
    {"assert":"not matricesIguales(np.array([[1.0,2.0],[3.0,4.0]]),np.array([[1.0 + 1e-4,2.0],[3.0,4.0]]))"}
  ],
  "disponible":{"desde":fecha}
}

def rota(fecha):
  return {
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
    {"assert":"np.allclose(rota(np.pi), np.array([[-1, 0],[0, -1]]))"},
    {"post":"theta = np.pi/6\nR = rota(theta)","assert":"np.allclose(R.T@R, np.eye(2))"},
    {"assert":"np.isclose(np.linalg.det(rota(np.pi/3)), 1.0)"},
    {"assert":"np.allclose(rota(np.pi/2)@np.array([1,0]), np.array([0,1]), atol=1e-5)"},
    {"assert":"np.allclose(rota(np.pi/2)@np.array([0,1]), np.array([-1,0]), atol=1e-5)"},
    {"assert":"np.allclose(rota(np.pi/4), np.array([[np.sqrt(2)/2,-np.sqrt(2)/2],[np.sqrt(2)/2,np.sqrt(2)/2]]), atol=1e-5)"}
  ],
  "disponible":{"desde":fecha}
}

def escala(fecha):
  return {
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
    {"assert":"np.allclose(escala([0.5,0.25]), np.array([[0.5,0],[0,0.25]]))"},
    {"post":"S = escala([2,3])","assert":"S[0,1]==0.0 and S[1,0]==0.0 and np.isclose(S[0,0],2.0) and np.isclose(S[1,1],3.0)"},
    {"assert":"np.allclose(escala([3,-5])@np.array([1,1]), np.array([3,-5]))"}
  ],
  "disponible":{"desde":fecha}
}

def rota_y_escala(fecha):
  return {
  "tipo":"CODIGO",
  "id":"rota_y_escala",
  "nombre":"rota_y_escala",
  "enunciado":"Implementar la función <code>rota_y_escala</code> que reciba un ángulo <code>theta</code> y una tira de números <code>s</code>, y retorne una matriz de 2 x 2 que rota el vector en un ángulo <code>theta</code> y luego lo escala en un factor <code>s</code>.",
  "base":"\
def rota_y_escala(theta,s):\n\
  \"\"\"\n\
  % Recibe un ángulo theta y una tira de números s, y retorna una matriz de 2 x 2 que rota el vector en un ángulo theta y luego lo escala en un factor s\n\
  \"\"\"\n",
  "aridad":{"rota_y_escala":2},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.allclose(rota_y_escala(0,[2,3]), np.array([[2,0],[0,3]]))"},
    {"assert":"np.allclose(rota_y_escala(np.pi/2,[1,1]), np.array([[0,-1],[1,0]]))"},
    {"assert":"np.allclose(rota_y_escala(np.pi,[2,2]), np.array([[-2,0],[0,-2]]))"},
    {"post":"theta = np.pi/4\nM = rota_y_escala(theta,[2,2])\nR = rota(theta)","assert":"np.allclose(M, 2*R)"},
    {"post":"theta = np.pi/4\nM = rota_y_escala(theta,[2,1])\nR = rota(theta)\nS = escala([2,1])\nesperado_correcto = S@R\nesperado_incorrecto = R@S","assert":"not np.allclose(M,esperado_incorrecto) and np.allclose(M,esperado_correcto)"}
  ],
  "disponible":{"desde":fecha}
}

def afin(fecha):
  return {
  "tipo":"CODIGO",
  "id":"afin",
  "nombre":"afin",
  "enunciado":"Implementar la función <code>afin</code> que reciba un ángulo <code>theta</code>, una tira de números <code>s</code> (en R<sup>2</sup>), y un vector <code>b</code> en (R<sup>2</sup>) y retorne una matriz de 3 x 3 que rota el vector en un ángulo <code>theta</code>, luego lo escala en un factor <code>s</code> y por último lo muevo en un valor fijo <code>b</code>.",
  "base":"\
def afin(theta,s,b):\n\
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
    "},
    {"post":"T = afin(0,[1,1],[5,3])","assert":"T.shape == (3,3) and np.allclose(T[2,:],[0,0,1])"},
    {"assert":"np.allclose(afin(0,[1,1],[5,3]), np.array([[1,0,5],[0,1,3],[0,0,1]]))"}
  ],
  "disponible":{"desde":fecha}
}

def trans_afin(fecha):
  return {
  "tipo":"CODIGO",
  "id":"trans_afin",
  "nombre":"trans_afin",
  "enunciado":"Implementar la función <code>trans_afin</code> que reciba un vector <code>v</code> (en R<sup>2</sup>), un ángulo <code>theta</code>, una tira de números <code>s</code> (en R<sup>2</sup>), y un vector <code>b</code> en (R<sup>2</sup>) y retorne el vector <code>w</code> resultante de aplicar la transformacion afin a <code>v</code>.",
  "base":"\
def trans_afin(v,theta,s,b):\n\
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
    "},
    {"assert":"np.allclose(trans_afin(np.array([1,2]),0,[1,1],[10,20]), np.array([11,22]))"},
    {"assert":"np.allclose(trans_afin(np.array([1,0]),np.pi/2,[1,1],[5,5]), np.array([5,6]), atol=1e-5)"}
  ],
  "disponible":{"desde":fecha}
}

def norma(fecha):
  return {
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
    {"assert":"np.allclose(norma(np.array([0,0,0,0]),1),0)"},
    {"assert":"np.allclose(norma(np.array([4,3,-100,-41,0]),'inf'),100)"},
    {"assert":"np.allclose(norma(np.array([1,1]),2),np.sqrt(2))"},
    {"assert":"np.allclose(norma(np.array([1]*10),2),np.sqrt(10))"},
    {"assert":"norma(np.random.rand(10),2)<=np.sqrt(10)"},
    {"assert":"norma(np.random.rand(10),2)>=0"},
    {"assert":"np.isclose(norma(np.array([3,-4]),1),7.0)"},
    {"assert":"np.isclose(norma(np.array([3,4]),2),5.0)"},
    {"assert":"np.isclose(norma(np.array([1,-5,3]),'inf'),5.0)"},
    {"post":"vals = []\nfor i in range(4):\n    e = np.zeros(4)\n    e[i] = 1.0\n    vals.append(np.isclose(norma(e,2),1.0))","assert":"all(vals)"},
    {"assert":"np.isclose(norma(np.array([-2.0,-2.0,-2.0]),5),(3*(2.0**5))**(1/5))"}
  ],
  "timeout":60,
  "disponible":{"desde":fecha}
}

def normaliza(fecha):
  return {
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
  "post":"\n\n\
def norma(x,p):\n\
  if p == 'inf':\n\
    return np.max(np.abs(x))\n\
  return np.power(sum(np.power(np.abs(x),p)),1/p)\n\n",
  "run_data":[
    {"assert":"all([np.allclose(norma(x,2),1) for x in normaliza([np.array([1]*k) for k in range(1,11)],2)])"},
    {"assert":"all([not np.allclose(norma(x,2),1) for x in normaliza([np.array([1]*k) for k in range(2,11)],1)])"},
    {"assert":"all([np.allclose(norma(x,'inf'),1) for x in normaliza([np.random.rand(k) for k in range(1,11)],'inf')])"},
    {"post":"X = np.array([[3.0,4.0],[1.0,2.0],[5.0,0.0]])\nXn = normaliza(X,2)\nvals = [np.isclose(norma(fila,2),1.0) for fila in Xn]","assert":"all(vals)"},
    {"post":"X = np.array([[1.0,2.0],[3.0,4.0]])\nXn = normaliza(X,2)\nfila0_esperada = np.array([1,2])/np.sqrt(5)\nfila1_esperada = np.array([3,4])/5.0","assert":"np.allclose(Xn[0],fila0_esperada) and np.allclose(Xn[1],fila1_esperada)"},
    {"post":"X = np.array([[3.0,4.0],[6.0,8.0]])\nX_copia = X.copy()\n_ = normaliza(X,2)","assert":"np.allclose(X,X_copia)"},
    {"post":"np.random.seed(2025)\nX = np.random.randn(100,50)\nXn = normaliza(X,2)\nvals = [np.isclose(norma(fila,2),1.0) for fila in Xn]","assert":"all(vals)"}
  ],
  "timeout":60,
  "disponible":{"desde":fecha}
}

def normaMatMC(fecha):
  return {
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
    {"assert":"np.allclose(nMC3[0],normaExacta(A)[1],rtol=1e-1)"},
    {"post":"norma_mc, v = normaMatMC(np.eye(3),2,2,5000)","assert":"np.isclose(norma_mc,1.0,atol=1e-2)"},
    {"post":"A = np.diag([3.0,1.0,2.0])\nnorma_mc, v = normaMatMC(A,2,2,10000)","assert":"np.isclose(norma_mc,3.0,atol=1e-2)"},
    {"post":"A = np.array([[3.0,0.0],[0.0,2.0],[0.0,0.0]])\nnorma_mc, v = normaMatMC(A,2,2,5000)","assert":"np.isclose(norma_mc,3.0,atol=1e-2) and v.shape[0] == A.shape[1]"},
    {"post":"A = np.array([[1.0,2.0],[3.0,4.0]])\nA_copia = A.copy()\n_ = normaMatMC(A,2,2,1000)","assert":"np.allclose(A,A_copia)"},
    {"post":"A = np.array([[1.0,-1.0],[-1.0,1.0]])\nnorma_mc, v = normaMatMC(A,2,2,100000)","assert":"norma_mc > 1.8"},
    {"post":"A = np.array([[1.0,3.0],[-2.0,4.0]])\nnorma_mc, v = normaMatMC(A,q='inf',p=1,Np=10000)","assert":"np.isclose(norma_mc,4.0,atol=0.3)"},
    {"post":"np.random.seed(2026)\nQ, _ = np.linalg.qr(np.random.randn(3,3))\nD = np.diag([100.0,1.0,3.0])\nA = Q @ D @ Q.T\nautovector_esperado = Q[:,0]\nnorma_mc, v = normaMatMC(A,2,2,50000)","assert":"np.isclose(norma_mc,100.0,atol=1e-3) and (np.allclose(v,autovector_esperado,atol=1e-2) or np.allclose(v,-autovector_esperado,atol=1e-2))"}
  ],
  "timeout":60,
  "disponible":{"desde":fecha}
}

def normaExacta(fecha):
  return {
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
    {"assert":"np.allclose(normaExacta(np.array([[1,-1],[-1,-1]]))[0],2)"},
    {"assert":"np.allclose(normaExacta(np.array([[1,-1],[-1,-1]]))[1],2)"},
    {"assert":"np.allclose(normaExacta(np.array([[1,-2],[-3,-4]]))[0],6)"},
    {"assert":"np.allclose(normaExacta(np.array([[1,-2],[-3,-4]]))[1],7)"},
    {"assert":"normaExacta(np.array([[1,-2],[-3,-4]]),2) is None"},
    {"assert":"normaExacta(np.random.random((10,10)))[0]<=10"},
    {"assert":"normaExacta(np.random.random((4,4)))[1]<=4"}
  ],
  "timeout":60,
  "disponible":{"desde":fecha}
}

def condMC(fecha):
  return {
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
  "post":"\
def normaMatMC(A,q,p,Np):\n\
    R = np.random.randn(A.shape[0], Np)\n\
    R = R / np.linalg.norm(R, axis=0, ord=p)\n\
    normas = A @ R\n\
    normas_q = np.linalg.norm(normas, axis=0, ord=q)\n\
    res = np.max(normas_q)\n\
    max_vector_idx = np.argmax(normas_q)\n\
    max_vector = R[:, max_vector_idx]\n\
    return res, max_vector\n\n",
  "run_data":[
    {"post":"\
A = np.array([[1,1],[0,1]])\n\
A_ = np.linalg.solve(A,np.eye(A.shape[0]))\n\
normaA = normaMatMC(A,2,2,10000)\n\
normaA_ = normaMatMC(A_,2,2,10000)\n\
condA = condMC(A,2)\n\
","assert":"np.allclose(normaA[0]*normaA_[0],condA,atol=1e-2)"},
    {"post":"\
A = np.array([[3,2],[4,1]])\n\
A_ = np.linalg.solve(A,np.eye(A.shape[0]))\n\
normaA = normaMatMC(A,2,2,10000)\n\
normaA_ = normaMatMC(A_,2,2,10000)\n\
condA = condMC(A,2)\n\
","assert":"np.allclose(normaA[0]*normaA_[0],condA,atol=1e-2)"},
    {"post":"I = np.eye(3)\ncond = condMC(I,2)","assert":"np.isclose(cond,1.0,atol=1e-3)"},
    {"post":"A = np.diag([4.0,2.0])\ncond = condMC(A,2)","assert":"np.isclose(cond,2.0,atol=1e-3)"},
    {"post":"A = np.array([[2.0,1.0],[0.0,3.0]])\nA_copia = A.copy()\n_ = condMC(A,2)","assert":"np.allclose(A,A_copia)"},
    {"post":"n = 4\nH = np.array([[1.0/(i+j+1) for j in range(n)] for i in range(n)])\ncond = condMC(H,2)","assert":"cond > 13000"},
    {"post":"np.random.seed(123)\nerrores = []\nfor _ in range(20):\n    n = np.random.randint(2,5)\n    A = np.random.randn(n,n)\n    cond_np = np.linalg.cond(A,2)\n    cond_mc = condMC(A,2)\n    errores.append(abs(cond_mc-cond_np)/cond_np)","assert":"all([e < 0.03 for e in errores])"}
  ],
  "disponible":{"desde":fecha}
}

def condExacto(fecha):
  return {
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
  "post":"\
def normaExacta(A,p=[1, 'inf']):\n\
    norma_1 = np.linalg.norm(A, ord=1)\n\
    norma_inf = np.linalg.norm(A, ord=np.inf)\n\
    if p == 1:\n\
        return norma_1\n\
    if p == 'inf':\n\
        return norma_inf\n\
    return [norma_1, norma_inf]\n\n",
  "run_data":[
    {"post":"\
A = np.random.rand(10,10)\n\
A_ = np.linalg.solve(A,np.eye(A.shape[0]))\n\
normaA = normaExacta(A,1)\n\
normaA_ = normaExacta(A_,1)\n\
condA = condExacto(A,1)\
","assert":"np.allclose(normaA*normaA_,condA)"},
    {"post":"\
A = np.random.rand(10,10)\n\
A_ = np.linalg.solve(A,np.eye(A.shape[0]))\n\
normaA = normaExacta(A,'inf')\n\
normaA_ = normaExacta(A_,'inf')\n\
condA = condExacto(A,'inf')\
","assert":"np.allclose(normaA*normaA_,condA)"},
    {"post":"A = np.eye(3)","assert":"np.isclose(condExacto(A,1),1.0)"},
    {"post":"A = np.eye(3)","assert":"np.isclose(condExacto(A,'inf'),1.0)"},
    {"post":"A = np.diag([5.0,2.0])","assert":"np.isclose(condExacto(A,1),2.5)"},
    {"post":"A = np.array([[1.0,2.0],[3.0,4.0]])","assert":"np.isclose(condExacto(A,1),np.linalg.cond(A,1),rtol=1e-6) and np.isclose(condExacto(A,'inf'),np.linalg.cond(A,np.inf),rtol=1e-6)"},
    {"post":"A = np.array([[2.0,1.0],[1.0,3.0]])\nA_copia = A.copy()\n_ = condExacto(A,1)\n_ = condExacto(A,'inf')","assert":"np.allclose(A,A_copia)"},
    {"post":"np.random.seed(456)\nchecks = []\nfor _ in range(20):\n    n = np.random.randint(2,6)\n    A = np.random.randn(n,n)\n    if abs(np.linalg.det(A)) < 1e-6:\n        continue\n    for p, p_np in [(1,1), ('inf', np.inf)]:\n        checks.append(np.isclose(condExacto(A,p), np.linalg.cond(A,p_np), rtol=1e-5))","assert":"all(checks)"}
  ],
  "disponible":{"desde":fecha}
}

def calculaLU(fecha):
  return {
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
    {"assert":"nops2 == 19"},
    {"assert":"L3 is None"},
    {"assert":"U3 is None"},
    {"assert":"nops3 == 14"},
    {"assert":"calculaLU(None) == (None, None, 0)"},
    {"assert":"calculaLU(np.array([[1,2,3],[4,5,6]])) == (None, None, 0)"},
    {"post":"A = np.array([[1.0,2.0],[3.0,4.0]])\nA_copy = A.copy()\nL,U,ops = calculaLU(A)","assert":"np.allclose(A,A_copy)"},
    {"post":"A = np.array([[1.0,0.0],[0.0,1.0]])\nL,U,ops = calculaLU(A)","assert":"L is not None and U is not None and np.allclose(L,np.eye(2)) and np.allclose(U,np.eye(2)) and np.allclose(L@U,A)"},
    {"post":"A = np.array([[4.0,3.0,2.0],[6.0,3.0,4.0],[2.0,1.0,5.0]])\nL,U,ops = calculaLU(A)\ndiagL = [np.isclose(L[i,i],1.0) for i in range(3)]\ntriang = [np.isclose(U[i,j],0.0) and np.isclose(L[j,i],0.0) for i in range(3) for j in range(i)]","assert":"L is not None and U is not None and all(diagL) and all(triang) and np.allclose(L@U,A)"},
    {"post":"np.random.seed(42)\nA = np.random.rand(7,7)\nL,U,ops = calculaLU(A)\ndiagL = [np.isclose(L[i,i],1.0) for i in range(7)]\ntriang = [np.isclose(U[i,j],0.0) and np.isclose(L[j,i],0.0) for i in range(7) for j in range(i)]","assert":"L is not None and U is not None and all(diagL) and all(triang) and np.allclose(L@U,A)"},
    {"post":"A = np.array([[2.0,4.0,1.0],[4.0,8.0,2.0],[1.0,2.5,7.5]])\nL,U,ops = calculaLU(A)","assert":"L is None and U is None"},
    {"post":"A = np.zeros((3,3))\nL,U,ops = calculaLU(A)","assert":"L is None and U is None"},
    {"post":"A = np.array([[0.0,1.0,2.0],[3.0,4.0,5.0],[6.0,7.0,8.0]])\nL,U,ops = calculaLU(A)","assert":"L is None and U is None"},
    {"post":"A = np.array([[1.0,2.0,3.0],[4.0,8.0,6.0],[0.0,0.0,0.0]])\nL,U,ops = calculaLU(A)","assert":"L is None and U is None"},
    {"post":"A = np.array([[-100,1.0,2.0],[3.0,4.0,5.0],[6.0,7.0,8.0]])\nL,U,ops = calculaLU(A)","assert":"L is not None and U is not None"},
    {"post":"A = np.array([[1.0,2.0,3.0],[4.0,-5.0,6.0],[0.0,0.0,0.0]])\nL,U,ops = calculaLU(A)\ndiagL = [np.isclose(L[i,i],1.0) for i in range(3)] if L is not None else []\ntriang = [np.isclose(U[i,j],0.0) and np.isclose(L[j,i],0.0) for i in range(3) for j in range(i)] if L is not None else []","assert":"L is not None and U is not None and all(diagL) and all(triang) and np.allclose(L@U,A)"},
    {"post":"np.random.seed(42)\nn = 100\nA1 = np.random.rand(n,n)\nA2 = np.random.rand(2*n,2*n)\n_, _, ops1 = calculaLU(A1)\n_, _, ops2 = calculaLU(A2)\nratio_empirico = ops2/ops1","assert":"ratio_empirico > 7.8 and ratio_empirico < 8.2"}
  ],
  "disponible":{"desde":fecha}
}

def res_tri(fecha):
  return {
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
    { "post":"b = np.array([1,1,1])",
      "assert":"np.allclose(res_tri(A1,b),np.array([1,0,0]))"
    },
    { "post":"b = np.array([0,1,0])",
      "assert":"np.allclose(res_tri(A1,b),np.array([0,1,-1]))"
    },
    { "post":"b = np.array([-1,1,-1])",
      "assert":"np.allclose(res_tri(A1,b),np.array([-1,2,-2]))"
    },
    { "post":"b = np.array([-1,1,-1])",
      "assert":"np.allclose(res_tri(A1,b,inferior=False),np.array([-1,1,-1]))"
    },
    { "post":"b = np.array([3,2,1])",
      "assert":"np.allclose(res_tri(A2,b,inferior=False),np.array([1/3,1/2,1]))"
    },
    { "post":"b = np.array([1,0,1])",
      "assert":"np.allclose(res_tri(A3,b,inferior=False),np.array([1,1,1]))"
    },
    {"post":"L = np.array([[1.0,0.0],[2.0,1.0]])\nb = np.array([1.0,2.0])\nx = res_tri(L,b,inferior=True)","assert":"np.allclose(L@x,b)"},
    {"post":"U = np.array([[2.0,3.0],[0.0,1.0]])\nb = np.array([5.0,1.0])\nx = res_tri(U,b,inferior=False)","assert":"np.allclose(U@x,b)"},
    {"post":"L = np.array([[0.0,0.0],[2.0,1.0]])\nb = np.array([1.0,2.0])\nx = res_tri(L,b,inferior=True)","assert":"x is None"},
    {"post":"np.random.seed(2025)\nchecks = []\nfor _ in range(10):\n    n = 10\n    L = np.tril(np.random.randn(n,n))\n    b = np.random.rand(n)\n    i = np.random.randint(0,n)\n    L[i,i] = 0.0\n    checks.append(res_tri(L,b,inferior=True) is None)\n    U = np.triu(np.random.randn(n,n))\n    b = np.random.rand(n)\n    i = np.random.randint(0,n)\n    U[i,i] = 0.0\n    checks.append(res_tri(U,b,inferior=False) is None)","assert":"all(checks)"}
  ],
  "disponible":{"desde":fecha}
}

def inversa(fecha):
  return {
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
    {"post":"\
def esSingular(A):\n\
    try:\n\
        np.linalg.inv(A)\n\
        return False\n\
    except:\n\
        return True\n\
\n\
asserts = []\n\
ntest = 10\n\
for i in range(ntest):\n\
    A = np.random.random((4,4))\n\
    A_ = inversa(A)\n\
    if not esSingular(A):\n\
        asserts.append(A_ is not None and np.allclose(np.linalg.inv(A),A_))\n\
    else:\n\
        asserts.append(A_ is None)\
    ","assert":"all(asserts)"},
    { "post":"A = np.array([[1,2,3],[4,5,6],[7,8,9]])",
      "assert":"inversa(A) is None"
    },
    {"post":"A = np.array([[1.0,2.0,3.0],[0.0,1.0,4.0],[5.0,6.0,0.0]])\nAinv = inversa(A)","assert":"Ainv is not None and np.allclose(A@Ainv,np.eye(3))"},
    {"post":"A = np.array([[1.0,2.0],[2.0,4.0]])\nAinv = inversa(A)","assert":"Ainv is None"},
    {"post":"A = np.eye(4)\nAinv = inversa(A)","assert":"Ainv is not None and np.allclose(Ainv,np.eye(4))"},
    {"post":"np.random.seed(2026)\nchecks = []\nfor k in range(10):\n    A = np.random.randn(20,20)\n    Ainv = inversa(A)\n    checks.append(Ainv is not None and np.allclose(A@Ainv,np.eye(20),atol=1e-5))","assert":"all(checks)"},
    {"post":"A = np.array([[1.0,2.0],[3.0,4.0]])\nA_copy = A.copy()\nAinv = inversa(A)","assert":"np.allclose(A,A_copy)"}
  ],
  "disponible":{"desde":fecha}
}

def calculaLDV(fecha):
  return {
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
L1,D1,V1 = calculaLDV(A1)\n\
L02 = np.array([[1,0,0],[1,1.001,0],[1,1,1]])\n\
D02 = np.diag([3,2,1])\n\
V02 = np.array([[1,1,1],[0,1,1],[0,0,1.001]])\n\
A2 =  L02 @ D02  @ V02\n\
L2,D2,V2 = calculaLDV(A2)\
  ",
  "run_data":[
    {"assert":"np.allclose(L1,L01)"},
    {"assert":"np.allclose(D1,D01)"},
    {"assert":"np.allclose(V1,V01)"},
    {"assert":"np.allclose(L2,L02,1e-3)"},
    {"assert":"np.allclose(D2,D02,1e-3)"},
    {"assert":"np.allclose(V2,V02,1e-3)"},
    {"post":"A = np.array([[4.0,2.0],[2.0,3.0]])\nA_copy = A.copy()\nL,D,V = calculaLDV(A)","assert":"np.allclose(A,A_copy)"},
    {"post":"A = np.eye(2)\nL,D,V = calculaLDV(A)","assert":"L is not None and D is not None and V is not None and np.allclose(L,np.eye(2)) and np.allclose(D,np.eye(2)) and np.allclose(V,np.eye(2)) and np.allclose(L@D@V,A)"},
    {"post":"A = np.array([[4.0,2.0,1.0],[2.0,5.0,3.0],[1.0,3.0,6.0]])\nL,D,V = calculaLDV(A)\ndiagL = [np.isclose(L[i,i],1.0) for i in range(3)]\nupperL = [np.isclose(L[i,j],0.0) for i in range(3) for j in range(i+1,3)]\noffD = [np.isclose(D[i,j],0.0) for i in range(3) for j in range(3) if i != j]","assert":"L is not None and D is not None and V is not None and all(diagL) and all(upperL) and all(offD) and np.allclose(V,L.T) and np.allclose(L@D@V,A)"},
    {"post":"A = np.diag([3.0,5.0,7.0])\nL,D,V = calculaLDV(A)","assert":"L is not None and D is not None and V is not None and np.allclose(L,np.eye(3)) and np.allclose(D,A) and np.allclose(V,np.eye(3)) and np.allclose(L@D@V,A)"},
    {"post":"np.random.seed(2026)\nchecks = []\nfor _ in range(10):\n    B = np.random.randn(10,10)\n    A = B@B.T + np.eye(10)*0.1\n    L,D,V = calculaLDV(A)\n    ok = L is not None and D is not None and V is not None\n    if ok:\n        ok = all(np.isclose(L[i,i],1.0) for i in range(10)) and np.allclose(D,np.diag(np.diag(D))) and np.allclose(V,L.T) and np.allclose(L@D@V,A,atol=1e-5)\n    checks.append(ok)","assert":"all(checks)"}
  ],
  "disponible":{"desde":fecha}
}

def esSDP(fecha):
  return {
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
    {"post":"\
L0 = np.array([[1,0,0],[1,1,0],[1,1,1]])\n\
D0 = np.diag([1,1,1])\n\
A = L0 @ D0 @ L0.T\
    ","assert":"esSDP(A)"},
    {"post":"\
D0 = np.diag([1,-1,1])\n\
A = L0 @ D0 @ L0.T\
    ","assert":"not esSDP(A)"},
    {"post":"\
D0 = np.diag([1,1,1e-16])\n\
A = L0 @ D0 @ L0.T\
    ","assert":"not esSDP(A)"},
    {"post":"\
L0 = np.array([[1,0,0],[1,1,0],[1,1,1]])\n\
D0 = np.diag([1,1,1])\n\
V0 = np.array([[1,0,0],[1,1,0],[1,1+1e-3,1]]).T\n\
A = L0 @ D0 @ V0\
    ","assert":"esSDP(A,1e-3)"},
    {"post":"A = np.array([[4.0,2.0],[2.0,3.0]])","assert":"esSDP(A) == True"},
    {"post":"v = np.array([1.0,-1.0,12.0])\nv = v/np.linalg.norm(v)\nH = np.eye(3) - 2*np.outer(v,v)\nA = H @ np.diag([1.0,-2.0,3.0]) @ H.T","assert":"esSDP(A) == False"},
    {"post":"A = np.array([[1.0,2.0],[3.0,4.0]])","assert":"esSDP(A) == False"},
    {"post":"A = np.eye(3)","assert":"esSDP(A) == True"},
    {"post":"A = np.diag([2.0,3.0,4.0])","assert":"esSDP(A) == True"},
    {"post":"A = np.diag([2.0,-3.0,4.0])","assert":"esSDP(A) == False"},
    {"post":"A = np.zeros((2,2))","assert":"esSDP(A) == False"},
    {"post":"np.random.seed(2026)\nchecks = []\nfor _ in range(10):\n    B = np.random.randn(10,10)\n    A = B@B.T + np.eye(10)*0.1\n    checks.append(esSDP(A) == True and esSDP(-A) == False)","assert":"all(checks)"},
    {"post":"A = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])","assert":"esSDP(A) == False"},
    {"post":"A = np.array([[1.0,2.0],[3.0,4.0],[5.0,6.0]])","assert":"esSDP(A) == False"}
  ],
  "disponible":{"desde":fecha}
}

def calculaCholesky(fecha):
  return {
  "tipo":"CODIGO",
  "id":"calculaCholesky",
  "nombre":"Cholesky",
  "enunciado":"En los casos en que <i>A</i> es SDP, se puede factorizar en la forma <i>RR<sup>t</sup></i>, donde <i>R</i> es una matriz triangular inferior tal que <i>R = LD<sup>1/2</sup></i>, con <i>D<sup>1/2</sup></i> la matriz diagonal con las raices de los elementos de la diagonal de <i>D</i>, y <i>L</i> y <i>D</i> resultan de la factorizacion LDV de <i>A</i>. Implementar la función <code>calculaCholesky(A,atol=1e-10)</code> que verifique si la matriz es SDP y en caso afirmativo devuelva la matriz <i>R</i> asociada a <i>A</i>.",
  "base":"\
def calculaCholesky(A,atol=1e-10):\n\
  \"\"\"\n\
  Verifica si la matriz A es SDP y en caso afirmativo devuelve la matriz R asociada a A, tal que A = R @ R.T.\n\
  \"\"\"\n",
  "aridad":{"calculaCholesky":2},
  "pre":"import numpy as np",
  "run_data":[
    {"post":"A = np.array([[4.0,2.0],[2.0,3.0]])\nA_copy = A.copy()\nL = calculaCholesky(A)","assert":"np.allclose(A,A_copy)"},
    {"post":"A = np.array([[4.0,2.0],[2.0,3.0]])\nL = calculaCholesky(A)\ntriang = [np.isclose(L[i,j],0.0) for i in range(2) for j in range(i+1,2)] if L is not None else []","assert":"L is not None and all(triang) and np.allclose(L@L.T,A,atol=1e-4)"},
    {"post":"A = np.array([[4.0,2.0,1.0],[2.0,3.0,0.5],[1.0,0.5,2.0]])\nL = calculaCholesky(A)","assert":"L is not None and np.allclose(L@L.T,A,atol=1e-4)"},
    {"post":"A = np.eye(3)\nL = calculaCholesky(A)","assert":"L is not None and np.allclose(L,np.eye(3),atol=1e-10)"},
    {"post":"A = np.array([[9.0,0.0,0.0],[0.0,4.0,0.0],[0.0,0.0,1.0]])\nL = calculaCholesky(A)\ndiagOk = [np.isclose(L[i,i],np.sqrt(A[i,i]),atol=1e-4) for i in range(3)] if L is not None else []","assert":"L is not None and all(diagOk) and np.allclose(L@L.T,A,atol=1e-4)"},
    {"post":"A = np.array([[1.0,2.0],[2.0,1.0]])\nL = calculaCholesky(A)","assert":"L is None"},
    {"post":"np.random.seed(2026)\nchecks = []\nfor _ in range(10):\n    B = np.random.randn(10,10)\n    A = B@B.T + np.eye(10)*0.1\n    L = calculaCholesky(A)\n    checks.append(L is not None and np.allclose(L@L.T,A,atol=1e-4))","assert":"all(checks)"},
    {"post":"A = np.array([[4.0,2.0],[2.0,1.0]])\nL = calculaCholesky(A)","assert":"L is None"},
    {"post":"np.random.seed(2026)\nchecks = []\nfor _ in range(10):\n    B = np.random.randn(10,10)\n    A = -(B@B.T + np.eye(10)*0.1)\n    checks.append(calculaCholesky(A) is None)","assert":"all(checks)"}
  ],
  "disponible":{"desde":fecha}
}

fechas = {
  "0":"11/8/2026-8:30", 
  "1":"18/8/2026-8:30",
  "2":"25/8/2026-8:30",
  "3":"1/9/2026-8:30",
  "4":"8/9/2026-8:30",
  "5":"15/9/2026-8:30",
  "6":"22/9/2026-8:30",
  "7":"6/10/2026-8:30",
  "8":"13/10/2026-8:30",
  "9":"27/10/2026-8:30"
}

# def etiqueta(id, texto):
#   return {
#     "tipo":"SECCION",
#     "id":id,
#     "nombre":texto
#   }

def labo(id, texto, actividades, fecha):
  return {
    "tipo":"SECCION",
    "id":id,
    "nombre":texto,
    "disponible":{"desde":fecha},
    "actividades":actividades
  }

CURSOS = {
  # "alc_prueba":{
  #   "nombre":"Álgebra Lineal Computacional - FCEN-UBA (PRUEBA)",
  #   "anio":"2025",
  #   "edicion":"Prueba",
  #   "descripcion":"Curso correspondiente a la materia Álgebra Lineal Computacional de la Facultad de Ciencias Exactas y Naturales (FCEyN), UBA",
  #   "responsable":{
  #     "nombre":"Equipo de ALC",
  #     "contacto":"? (AT) ?"
  #   },
  #   "institucion":"Facultad de Ciencias Exactas y Naturales (FCEyN) - UBA",
  #   "lenguaje":"Python",
  #   "lenguaje_display":"none",
  #   # "analisisCodigo":[
  #   #   {"key":"CMD_X_LINE"},
  #   #   {"key":"INDENT_NEST"},
  #   #   {"key":"NEST_CMD","max":1}
  #   # ],
  #   "actividades":[
  #     # traza,
  #     # traspuesta,
  #     # producto,
  #     # esDiagonalDominante,
  #     # etiqueta("labo1","Labo 01 (" + fechas["1"] + ")"),
  #     etiqueta("labo1","Labo 01"),
  #       # error,
  #       error_relativo(fechas["1"]),
  #       matricesIguales(fechas["1"]),
  #     # etiqueta("labo2","Labo 02 (" + fechas["2"] + ")"),
  #     etiqueta("labo2","Labo 02"),
  #       rota(fechas["2"]),
  #       escala(fechas["2"]),
  #       rota_y_escala(fechas["2"]),
  #       afin(fechas["2"]),
  #       trans_afin(fechas["2"]),
  #     # etiqueta("labo3","Labo 03 (" + fechas["3"] + ")"),
  #     etiqueta("labo3","Labo 03"),
  #       norma(fechas["3"]),
  #       normaliza(fechas["3"]),
  #       normaMatMC(fechas["3"]),
  #       normaExacta(fechas["3"]),
  #       condMC(fechas["3"]),
  #       condExacto(fechas["3"]),
  #     # etiqueta("labo4","Labo 04 (" + fechas["4"] + ")"),
  #     etiqueta("labo4","Labo 04"),
  #       calculaLU(fechas["4"]),
  #       res_tri(fechas["4"]),
  #       inversa(fechas["4"]),
  #       calculaLDV(fechas["4"]),
  #       esSDP(fechas["4"])
  #   ],
  #   "planilla":{
  #     "url":"1FAIpQLSfijJIbAFHK5BNEJhi31q1kXa3Z_LuLdiZjz7_O9N4SGu58WA",
  #     "campos":{
  #       "usuario":"9867257",
  #       "actividad":"1165966175",
  #       "respuesta":"1778184894",
  #       "resultado":"1496208069",
  #       "duracion":"1460244707"
  #     }
  #   }
  # },
  # "alc_2025_c2":{
  #   "nombre":"Álgebra Lineal Computacional - FCEN-UBA (2025 - 2C)",
  #   "anio":"2025",
  #   "edicion":"Segundo Cuatrimestre",
  #   "descripcion":"Curso correspondiente a la materia Álgebra Lineal Computacional de la Facultad de Ciencias Exactas y Naturales (FCEyN), UBA",
  #   "responsable":{
  #     "nombre":"Equipo de ALC",
  #     "contacto":"? (AT) ?"
  #   },
  #   "institucion":"Facultad de Ciencias Exactas y Naturales (FCEyN) - UBA",
  #   "lenguaje":"Python",
  #   "lenguaje_display":"none",
  #   # "analisisCodigo":[
  #   #   {"key":"CMD_X_LINE"},
  #   #   {"key":"INDENT_NEST"},
  #   #   {"key":"NEST_CMD","max":1}
  #   # ],
  #   "actividades":[
  #     # traza,
  #     # traspuesta,
  #     # producto,
  #     # esDiagonalDominante,
  #     # etiqueta("labo1","Labo 01 (" + fechas["1"] + ")"),
  #     etiqueta("labo1","Labo 01"),
  #       # error,
  #       error_relativo,
  #       matricesIguales,
  #     # etiqueta("labo2","Labo 02 (" + fechas["2"] + ")"),
  #     etiqueta("labo2","Labo 02"),
  #       rota,
  #       escala,
  #       rota_y_escala,
  #       afin,
  #       trans_afin,
  #     # etiqueta("labo3","Labo 03 (" + fechas["3"] + ")"),
  #     etiqueta("labo3","Labo 03"),
  #       norma,
  #       normaliza,
  #       normaMatMC,
  #       normaExacta,
  #       condMC,
  #       condExacto,
  #     # etiqueta("labo4","Labo 04 (" + fechas["4"] + ")"),
  #     etiqueta("labo4","Labo 04"),
  #       calculaLU,
  #       res_tri,
  #       inversa,
  #       calculaLDV,
  #       esSDP
  #   ],
  #   "planilla":{
  #     "url":"1FAIpQLSfijJIbAFHK5BNEJhi31q1kXa3Z_LuLdiZjz7_O9N4SGu58WA",
  #     "campos":{
  #       "usuario":"9867257",
  #       "actividad":"1165966175",
  #       "respuesta":"1778184894",
  #       "resultado":"1496208069",
  #       "duracion":"1460244707"
  #     }
  #   }
  # },
  "alc_2026_c2":{
    "nombre":"Álgebra Lineal Computacional - FCEN-UBA (2026 - 2C)",
    "anio":"2026",
    "edicion":"Segundo Cuatrimestre",
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
    #   {"key":"INDENT_NEST"},
    #   {"key":"NEST_CMD","max":1}
    # ],
    "actividades":[
      labo("labo00","Labo 00", [
          esCuadrada(fechas["0"]),
          triangSup(fechas["0"]),
          triangInf(fechas["0"]),
          diagonal(fechas["0"]),
          traza(fechas["0"]),
          traspuesta(fechas["0"]),
          esSimetrica(fechas["0"]),
          producto(fechas["0"]),
          intercambiarFilas(fechas["0"]),
          sumar_fila_multiplo(fechas["0"]),
          esDiagonalDominante(fechas["0"]),
          matrizCirculante(fechas["0"]),
          matrizVandermonde(fechas["0"]),
          numeroAureo(fechas["0"]),
          matrizFiboncacci(fechas["0"]),
          matrizHilbert(fechas["0"]),
          ], fechas["0"]),
      labo("labo1","Labo 01", [
        error(fechas["1"]),
        error_relativo(fechas["1"]),
        matricesIguales(fechas["1"])
      ], fechas["1"]),
      labo("labo2","Labo 02", [
        rota(fechas["2"]),
        escala(fechas["2"]),
        rota_y_escala(fechas["2"]),
        afin(fechas["2"]),
        trans_afin(fechas["2"])
      ], fechas["2"]),
      labo("labo3","Labo 03", [
        norma(fechas["3"]),
        normaliza(fechas["3"]),
        normaMatMC(fechas["3"]),
        normaExacta(fechas["3"]),
        condMC(fechas["3"]),
        condExacto(fechas["3"])
      ], fechas["3"]),
      labo("labo4","Labo 04", [
        calculaLU(fechas["4"]),
        res_tri(fechas["4"]),
        inversa(fechas["4"]),
        calculaLDV(fechas["4"]),
        esSDP(fechas["4"]),
        calculaCholesky(fechas["4"])
      ], fechas["4"])
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
