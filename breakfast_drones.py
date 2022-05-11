"""
Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.
The IDs are not guaranteed to be sorted or sequential.
Orders aren't always fulfilled in the order they were received, and some deliveries get cancelled before takeoff.

"""


def find_unique_integer(delivery_id_confirmations):
    # brute force
    seen = {}
    for id in delivery_id_confirmations:
        if id in seen.keys():
            seen.pop(id)
        else:
            seen[id] = 1

    if len(seen.keys()) > 1:
        raise ValueError("more than 1 drone is missing")

    return list(seen.keys())[0]


def find_unique_with_xor(delivery_id_confirmations):
    """
    When we XOR with a new ID, it will change the bits. XOR with the same ID will cancel out the earlier change
    """
    unique_delivery_id = 0
    for delivery_id in delivery_id_confirmations:
        unique_delivery_id ^= delivery_id
    return unique_delivery_id
