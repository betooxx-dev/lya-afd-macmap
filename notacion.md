# Q: Conjunto de estados

Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43, q44}

# Σ: Alfabeto de entrada

Σ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, a, b, c, d, e, f, :, -, espacio}

# δ: Función de transición

δ: Q × Σ → Q

La función de transición se define como sigue:

δ(q0, espacio) = q0
δ(q0, hex) = q1, donde hex ∈ {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, a, b, c, d, e, f}
δ(q1, hex) = q2
δ(q2, :) = q3
δ(q2, -) = q4
δ(q2, espacio) = q5
δ(q3, hex) = q6
δ(q4, hex) = q7
δ(q5, hex) = q8
δ(q6, hex) = q9
δ(q7, hex) = q10
δ(q8, hex) = q11
δ(q9, :) = q12
δ(q10, -) = q13
δ(q11, espacio) = q14
δ(q12, hex) = q15
δ(q13, hex) = q16
δ(q14, hex) = q17
δ(q15, hex) = q18
δ(q16, hex) = q19
δ(q17, hex) = q20
δ(q18, :) = q21
δ(q19, -) = q22
δ(q20, espacio) = q23
δ(q21, hex) = q24
δ(q22, hex) = q25
δ(q23, hex) = q26
δ(q24, hex) = q27
δ(q25, hex) = q28
δ(q26, hex) = q29
δ(q27, :) = q30
δ(q28, -) = q31
δ(q29, espacio) = q32
δ(q30, hex) = q33
δ(q31, hex) = q34
δ(q32, hex) = q35
δ(q33, hex) = q36
δ(q34, hex) = q37
δ(q35, hex) = q38
δ(q36, :) = q39
δ(q37, -) = q40
δ(q38, espacio) = q41
δ(q39, hex) = q42
δ(q40, hex) = q42
δ(q41, hex) = q42
δ(q42, hex) = q43
δ(q43, espacio) = q44
δ(q43, λ) = q44

Para cualquier otro par (q, a) no listado arriba, δ(q, a) = q0

# q0: Estado inicial

q0 = q0

# F: Conjunto de estados de aceptación

F = {q44}