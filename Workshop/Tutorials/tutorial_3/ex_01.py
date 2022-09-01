import numpy as np

def skew(w):
    w_skew = np.array([
        [0,    -w[2],  w[1]],
        [w[2],     0, -w[0]],
        [-w[1], w[0],     0]
    ])
    return w_skew

def exp3(w_hat, theta):
    w_skew_hat = skew(w_hat)
    return np.eye(3) + np.sin(theta) * w_skew_hat \
            + (1 - np.cos(theta)) * (w_skew_hat @ w_skew_hat)

def G(w_hat, theta):
    w_skew_hat = skew(w_hat)
    return np.eye(3) * theta + (1 - np.cos(theta)) * w_skew_hat \
            + (theta - np.sin(theta)) * (w_skew_hat @ w_skew_hat)

def exp6(S, theta):
    w_hat = S[:3]
    v_hat = S[3:]
    R = exp3(w_hat, theta)
    p = G(w_hat, theta) @ v_hat
    T = np.vstack((
        np.hstack((R, np.expand_dims(p, 1))),
        np.array([[0.0, 0.0, 0.0, 1.0]], dtype=np.float64)
    ))
    return T

if __name__ == "__main__":
    l0 = 1
    l1 = 1
    l2 = 1
    theta1 = 0
    theta2 = np.pi / 2
    theta3 = -np.pi / 2
    theta4 = 1
    M = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, l1 + l2],
        [0, 0, 1, l0],
        [0, 0, 0, 1]
    ])
    S1 = np.array([0, 0, 1, 0, 0, 0])
    S2 = np.array([0, 0, 1, l1, 0, 0])
    S3 = np.array([0, 0, 1, l1 + l2, 0, 0])
    S4 = np.array([0, 0, 0, 0, 0, 1])
    T1 = exp6(S1, theta1)
    T2 = exp6(S2, theta2)
    T3 = exp6(S3, theta3)
    T4 = exp6(S4, theta4)
    T = T1 @ T2 @ T3 @ T4 @ M
    print(T)