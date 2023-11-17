import ctypes

# Загрузка библиотеки C++
lib = ctypes.CDLL('./spherical_harmonic.dll') # Путь к скомпилированной shared-библиотеке .so/.dll

# Обётка функции на с++ для spherical_harmonic_real
spherical_harmonic_real_c = lib.spherical_harmonic_real
spherical_harmonic_real_c.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
spherical_harmonic_real_c.restype = ctypes.c_double

# Обёртка для python
def sphh_harm_r(theta, phi, l, m):
    return spherical_harmonic_real_c(ctypes.c_double(theta), ctypes.c_double(phi), ctypes.c_int(l), ctypes.c_int(m))

# Обётка функции на с++ для spherical_harmonic_imag
spherical_harmonic_imag_c = lib.spherical_harmonic_imag
spherical_harmonic_imag_c.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
spherical_harmonic_imag_c.restype = ctypes.c_double

# Обёртка для python
def sphh_harm_im(theta, phi, l, m):
    return spherical_harmonic_imag_c(ctypes.c_double(theta), ctypes.c_double(phi), ctypes.c_int(l), ctypes.c_int(m))



