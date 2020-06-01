import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    # [R, R_err, y, y_err, dy, dy_err]
    [6, 0.05, 0.028402777777777777, 0.0142045899281194900, 0.0042476851851851850, 0.0021243597075690810],
    [5, 0.05, 0.023544303797468358, 0.0117775182132870780, 0.0035097813578826233, 0.0017557744450249194],
    [4, 0.05, 0.017607655502392346, 0.0088075196624038280, 0.0028771929824561400, 0.0014392134676547670],
    [3, 0.05, 0.014455611390284758, 0.0072307600200240815, 0.0021161362367392520, 0.0010585847297524580],
    [2, 0.05, 0.009706103993971364, 0.0048559426373586180, 0.0013514192413966340, 0.0006762530486505836],
    [1, 0.05, 0.004875690607734807, 0.0024419871178887713, 0.0006813996316758749, 0.0003415090647735728]
])

d = 0.0008

if __name__ == '__main__':
    x = data[:, 0]
    y = data[:, 4]
    x_err = data[:, 1]
    y_err = data[:, 5]

    m, err = np.polyfit(x, y, 1)

    plt.title(f'Fit of wavelength (lambda)')
    plt.xlabel('Distance (R) [m]')
    plt.ylabel('Periodicity of peaks (delta y) [m]')
    plt.errorbar(x, y, x_err, y_err, fmt='o', label='data')
    plt.plot(x, m * x, label=f'fit (lambda={m * d:.2e}m)')
    plt.legend()
    plt.savefig('wavelength.png')
    plt.show()

    y = data[:, 2]
    y_err = data[:, 3]

    m2, err2 = np.polyfit(x, y, 1)

    plt.title(f'Fit for slit width (a)')
    plt.xlabel('Distance (R) [m]')
    plt.ylabel('Width of the central peak (y) [m]')
    plt.errorbar(x, y, x_err, y_err, fmt='o', label='data')
    plt.plot(x, m2 * x, label=f'fit (a={m2 / m * d:.2e}m)')
    plt.legend()
    plt.savefig('a.png')
    plt.show()
