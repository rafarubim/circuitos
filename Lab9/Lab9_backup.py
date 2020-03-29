
# coding: utf-8

# # Lab de Circuitos - Preparatório 9
# ## Rafael Rubim Cabral - 1511068

# ### 1)
# &emsp;Cálculo da função de transferência $H_{Z}(s)$:
# 
# $Z_{1}(s) = \dfrac{1}{sC} // (Ls+Z) = \dfrac{1}{\dfrac{1}{Ls+Z}+sC} = \dfrac{Ls+Z}{1+LCs^2+ZCs}$
# 
# $V_{2}(s) = V(s) \dfrac{Z_{1}(s)}{R+Z_{1}(s)}$
# 
# $V_{Z}(s) = V_{2}(s)\dfrac{Z}{Ls+Z}$
# 
# $H_{Z}(s) = \dfrac{V_{Z}(s)}{V(s)} = \dfrac{Z_{1}(s)}{R+Z_{1}(s)}\dfrac{Z}{Ls+Z} = \dfrac{Z_{1}Z}{RLs+ZR+Z_{1}Ls+Z_{1}Z} = \dfrac{Z}{\dfrac{RLs}{Z_1}+\dfrac{ZR}{Z_1}+Ls+Z}$
# 
# $H_{Z}(s) = \dfrac{Z}{\dfrac{RLs + RL^2Cs^3 + RLZCs^2}{Ls+Z}+\dfrac{ZR + ZRLCs^2 + Z^2RCs}{Ls+Z}+Ls+Z}$
# 
# $H_{Z}(s) = \dfrac{ZLs + Z^2}{RLs + RL^2Cs^3 + RLZCs^2 + ZR + ZRLCs^2 + Z^2RCs+(Ls+Z)^2}$
# 
# $H_{Z}(s) = \dfrac{ZLs + Z^2}{RL^2Cs^3 + RLZCs^2 + ZRLCs^2 + L^2s^2 + RLs + Z^2RCs + 2LZs + ZR + Z^2}$
# 
# $H_{Z}(s) = \dfrac{ZLs + Z^2}{RL^2Cs^3 + (2RLZC + L^2)s^2 + (RL + Z^2RC + 2LZ)s + (ZR + Z^2)}$
# 
# &emsp;Vamos considerar a fase da fonte $\phi = 0$. Logo temos o fasor $\dot V = Ae^{j.0}$. O fasor da saída $\dot V_{Z}$ será:
# 
# $\dot V_{Z} = H_{Z}(j\omega_{0}) \dot V$
# 
# $H_{Z}(j\omega_{0}) = \dfrac{jZL\omega_0 + Z^2}{-jRL^2C\omega_0^3 - (2RLZC + L^2)\omega_0^2 + (RL + Z^2RC + 2LZ)j\omega_0 + (ZR + Z^2)}$
# 
# $H_{Z}(j\omega_{0}) = \dfrac{Z^2+jZL\omega_0}{[ZR + Z^2 - (2RLZC + L^2)\omega_0^2] + j[(RL + Z^2RC + 2LZ)\omega_0-RL^2C\omega_0^3]}$
# 
# ### a)
# 
# &emsp;$Z = Z_0e^{j\phi}$ puramente resistivo: $Z = R + j.0 \rightarrow \phi = 0 \rightarrow Z = Z_0$
# 
# $H_{Z}(j\omega_{0}) = \dfrac{Z_0^2+jZ_0L\omega_0}{[Z_0R + Z_0^2 - (2RLZ_0C + L^2)\omega_0^2] + j[(RL + Z_0^2RC + 2LZ_0)\omega_0-RL^2C\omega_0^3]}$
# 
# &emsp;Logo $\dot V_{Z} = H_{Z}(j\omega_{0}) \dot V = H_{Z}(j\omega_{0}) A$ e então $V_{Z}(t) = H_{Z}(j\omega_0) A e^{j\omega_0t}$
# 
# $V_{Z}(t) = \dfrac{(Z_0^2+jZ_0L\omega_0) A e^{j\omega_0t}}{[Z_0R + Z_0^2 - (2RLZ_0C + L^2)\omega_0^2] + j[(RL + Z_0^2RC + 2LZ_0)\omega_0-RL^2C\omega_0^3]}$
# 
# $H_{Z}(j\omega_{0}) = \dfrac{\sqrt{Z_0^4+Z_0^2L^2\omega_0^2}e^{j.tan^{-1}\left(\dfrac{L\omega_0}{Z_0}\right)}}
# {\sqrt{[Z_0^2R^2+2Z_0^3R-4R^2LZ_0^2C\omega_0^2-2RZ_0L^2\omega_0^2+Z_0^4-4RLZ_0^3C\omega_0^2-2Z_0^2L^2\omega_0^2+4R^2L^2Z_0^2C^2\omega_0^4+4RL^3Z_0C\omega_0^4+L^4\omega_0^4+R^2L^2\omega_0^2+2R^2LZ_0^2C\omega_0^2+4RL^2Z_0\omega_0^2-2R^2L^3C\omega_0^4+Z_0^4R^2C^2\omega_0^2+4LZ_0^3RC\omega_0^2-2R^2Z_0^2L^2C^2\omega^4+4L^2Z_0^2\omega_0^2-4RL^3Z_0C\omega_0^4+R^2L^4C^2\omega_0^6]}
# e^{j.tan^{-1}\left(\dfrac{[(RL + Z_0^2RC + 2LZ_0)\omega_0-RL^2C\omega_0^3]}{[Z_0R + Z_0^2 - (2RLZ_0C + L^2)\omega_0^2]}\right)}}$

# In[ ]:




