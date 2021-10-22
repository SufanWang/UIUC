import tensorflow as tf

Spot = 36   # stock price
σ = 0.2     # stock volatility
K = 40      # strike price
r = 0.06    # risk free rate
n = 100000  # Number of simualted paths
m = 50      # number of exercise dates
T = 1       # maturity
order = 6   # Polynmial order
Δt = T / m  # interval between two exercise dates


# In TensorFlow you can use tf.one_hot, so you dont need to convert that
# def one_hot(array, depth):
#     return np.eye(depth)[array]

# Construct polynomial features of order up to k using the
# recursive formulation
def chebyshev_basis(x, k):
    B = [tf.ones(len(x)), x]
    for n in range(2, k):
        Bn = 2 * x * B[n - 1] - B[n - 2]
        B.append(Bn)

    return tf.stack(B,axis=1)

# scales x to be in the interval(-1, 1)
def scale(x):
    xmin = tf.reduce_min(x)
    xmax = tf.reduce_max(x)
    a = 2 / (xmax - xmin)
    b = 1 - a * xmax
    return a * x + b

# simulates the stock price evolution
def advance(S, r, σ, Δt, n):
    dB = tf.sqrt(Δt) * tf.random.normal([len(S)])
    out = S + r * S * Δt + σ * S * dB
    return out

# LSMC algorithm
def compute_price(order, Spot, σ, K, r):
    tf.random.set_seed(0)
    S0 = Spot * tf.ones(n)
    S = {0: S0}

    for t in range(m):
        S[t + 1] = advance(S[t], r, σ, Δt, n)

    discount = tf.exp(-r * Δt)
    CFL = {t: tf.maximum(0., K - S[t]) for t in S.keys()}
    value_tp1 = CFL[m] * discount
    CV = {m: tf.zeros_like(S0)}

    for t in range(m - 1, 0, -1):
        X = chebyshev_basis(scale(S[t]), order)
        Y = tf.constant(value_tp1, shape=(n, 1))

        # regression to estimate the continuation value
        Θ = tf.linalg.solve(tf.transpose(X) @ X, tf.transpose(X) @ Y)
        CV[t] = X @ Θ
        CFL[t] = tf.reshape(CFL[t], [n, 1])
        value_tp1 = tf.reshape(value_tp1, [n, 1])

        exercise = CFL[t] > CV[t]
        value_t = tf.where(exercise, CFL[t], value_tp1)
        value_tp1 = discount * value_t

    POF = {t: tf.where(CV[t] < CFL[t], CFL[t], 0) for t in range(1, m + 1)}

    for t in [49, 50]:
        POF[t] = tf.reshape(POF[t], [n, 1])

    POF = tf.transpose(tf.concat(list(POF.values()), axis=1))
    idx_payoffs = tf.argmax(POF > 0, axis=0)
    FPOF = tf.transpose(tf.one_hot(idx_payoffs, m)) * POF
    m_range = tf.reshape(tf.constant(range(0, m),dtype=tf.float32), [-1, 1])
    dFPOF = FPOF * tf.exp(-r * m_range * Δt)
    PRICE = tf.reduce_sum(dFPOF) / n
    return PRICE


print(compute_price(order, Spot, σ, K, r))
test = compute_price(order, Spot, σ, K, r)
