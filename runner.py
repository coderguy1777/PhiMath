import phimath.linear_alg.translate_vector as vc

a = vc.Vec(0.5, 0.5)
for i in range(0, 100):
    a.trans_x()
    print(str(a.get_x()))