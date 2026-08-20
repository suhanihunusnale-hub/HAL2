import random


def check_threat():


    attacks = [

        (
            "Quantum Interception",
            "HIGH",
            "Quantum key mismatch detected. Possible eavesdropping attempt on secure communication channel."
        ),


        (
            "Unauthorized Login",
            "MEDIUM",
            "Multiple failed authentication attempts detected from unknown user."
        ),


        (
            "Message Tampering",
            "HIGH",
            "Message integrity verification failed. Encrypted data may have been modified."
        ),


        (
            "Suspicious Communication",
            "MEDIUM",
            "Unusual communication pattern detected between network users."
        )

    ]


    detected = random.choice(
        [True,False,False]
    )


    if detected:

        return random.choice(attacks)


    return None