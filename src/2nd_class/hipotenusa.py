import math

cat_a = int(input("Qual o primeiro cateto? "))
cat_a_sq = pow(cat_a, 2)
cat_b = int(input("Qual o segundo cateto? "))
cat_b_sq = pow(cat_b, 2)
hip_pow = cat_a_sq + cat_b_sq
hip = int(math.sqrt(cat_a_sq + cat_b_sq))

print("A hipotenusa é", hip)