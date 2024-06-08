import numpy as np
import time

def func(x):
    return 4 / (1 + x**2)

#Integrasi Simpson 1/3
def simpsons_one_third(a, b, N):
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    y = func(x)
    integral = h/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return integral

def estimasi_pi(N):
    a = 0
    b = 1
    integral = simpsons_one_third(a, b, N)
    pi_est = integral
    return pi_est

#Mencari galat RMS
def galat_RMS(pi_est, decimal_places=10):
    true_pi = 3.14159265358979323846
    error = np.abs(pi_est - true_pi)
    error_rms = np.sqrt(np.mean(error**2))
    error_str = "{:.{}f}".format(error_rms, decimal_places)
    return error_str

#Variasi nilai N
N_values = [10, 100, 1000, 10000]

#Jumlah desimal
decimal_places = 20

for N in N_values:
    start_time = time.time()
    pi_est = estimasi_pi(N)
    end_time = time.time()
    execution_time = end_time - start_time
    error = galat_RMS(pi_est, decimal_places)
    print(f"For N = {N}:")
    print(f"Estimasi Nilai pi: {pi_est:.{decimal_places}f}")
    print(f"Galat RMS: {error}")
    print(f"Waktu Eksekusi: {execution_time:.4f} seconds\n")
