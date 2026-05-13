current_session = "default"

did_database = {
    "F190": "WV123456789ABCDEF"
}


# ====================================
# Core UDS Communication
# ====================================

def send_request(request):

    global current_session

    print(f"Sending Request: {request}")

    parts = request.split()

    sid = parts[0]

    # =========================
    # Session Control
    # =========================

    if request == "10 01":

        current_session = "default"

        return bytes([0x50, 0x01])

    # =========================
    # Read DID
    # =========================

    elif sid == "22":

        did = parts[1] + parts[2]

        if did not in did_database:

            return bytes([0x7F, 0x22, 0x31])

        value = did_database[did]

        response = bytes([
            0x62,
            int(parts[1], 16),
            int(parts[2], 16)
        ]) + value.encode("ascii")

        return response

    return bytes([0x7F, 0x22, 0x13])


# ====================================
# Robot Keywords
# ====================================

def enter_default_session():

    response = send_request("10 01")

    if response[0] != 0x50:
        raise Exception("Failed Session Control")


def read_vin():

    response = send_request("22 F1 90")

    if response[0] != 0x62:
        raise Exception("Negative Response")

    vin = response[3:].decode("ascii")

    return vin


def read_invalid_did():

    response = send_request("22 F1 99")

    if response[0] != 0x7F:
        raise Exception("Expected Negative Response")

    if response[2] != 0x31:
        raise Exception("Expected NRC 0x31")

    return response
