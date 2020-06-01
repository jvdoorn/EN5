import math


def px_to_m(d_px, d_px_err, r_px, r_px_err, r_m, r_m_err):
    return d_px / r_px * r_m, math.sqrt(
        (d_px * r_m_err / r_px) ** 2 + (r_m * d_px_err / r_px) ** 2 + (d_px * r_m * r_px_err / r_px ** 2) ** 2)


def calc_wavelength(d, d_err, delta_y, delta_y_err, R, R_err):
    return (d * delta_y) / R, math.sqrt(
        (delta_y * d_err / R) ** 2 + (d * delta_y_err / R) ** 2 + (delta_y * d * R_err / R ** 2) ** 2)


def calc_slit_width(lamb, lamb_err, R, R_err, y, y_err):
    return (lamb * R) / y, math.sqrt(
        (R * lamb_err / y) ** 2 + (lamb * R_err / y) ** 2 + (R * lamb * y_err / y ** 2) ** 2)
