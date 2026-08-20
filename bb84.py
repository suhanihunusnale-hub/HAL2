import random


def generate_quantum_key(length=16):

    # Alice generates random bits
    alice_bits = [
        random.randint(0,1)
        for _ in range(length)
    ]


    # Alice chooses bases
    alice_bases = [
        random.choice(["+","x"])
        for _ in range(length)
    ]


    # Bob chooses measurement bases
    bob_bases = [
        random.choice(["+","x"])
        for _ in range(length)
    ]


    shared_key = []


    # Compare bases
    for i in range(length):

        if alice_bases[i] == bob_bases[i]:

            shared_key.append(
                str(alice_bits[i])
            )


    quantum_key = "".join(shared_key)


    if len(quantum_key) < 8:

        return generate_quantum_key(length)


    return quantum_key[:16]



def detect_eavesdropping():

    attack = random.choice(
        [
            True,
            False,
            False,
            False
        ]
    )

    return attack
    