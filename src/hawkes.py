import numpy as np


# --------------------------------------------------------------
# Hawkes intensity
#
# lambda(t) = mu + sum(alpha * exp(-beta*(t-ti)))
# --------------------------------------------------------------

def intensity(t, history, mu, alpha, beta):

    if len(history) == 0:
        return mu

    return (
        mu
        +
        np.sum(
            alpha * np.exp(
                -beta * (t - history)
            )
        )
    )


# --------------------------------------------------------------
# Hawkes log-likelihood
#
# log L =
#
# sum(log(lambda(t_i)))
# -
# integral(lambda(t))dt
# --------------------------------------------------------------

def hawkes_log_likelihood(params, times):

    mu, alpha, beta = params

    # Parameters constraints
    if mu <= 0 or alpha < 0 or beta <= 0:
        return -np.inf


    # Event contribution

    log_sum = 0

    for i, t in enumerate(times):

        history = times[:i]

        lam = intensity(
            t,
            history,
            mu,
            alpha,
            beta
        )

        log_sum += np.log(lam)


    # Integral contribution

    T = times[-1]

    integral = (
        mu * T
        +
        np.sum(
            alpha / beta
            *
            (
                1
                -
                np.exp(
                    -beta * (T-times)
                )
            )
        )
    )


    return log_sum - integral



# --------------------------------------------------------------
# Hawkes simulation (Ogata thinning)
# --------------------------------------------------------------

def simulate_hawkes(mu, alpha, beta, T):

    events = []

    t = 0

    while t < T:

        if len(events) == 0:
            lam = mu

        else:
            lam = (
                mu
                +
                np.sum(
                    alpha
                    *
                    np.exp(
                        -beta *
                        (t - np.array(events))
                    )
                )
            )


        # propose next event

        t += np.random.exponential(
            1 / lam
        )


        if t >= T:
            break


        # calculate real intensity

        if len(events) == 0:
            new_lam = mu

        else:
            new_lam = (
                mu
                +
                np.sum(
                    alpha
                    *
                    np.exp(
                        -beta *
                        (t - np.array(events))
                    )
                )
            )


        # thinning acceptance

        if np.random.rand() < new_lam / lam:
            events.append(t)


    return np.array(events)