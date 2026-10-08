def pad_always(msg, size):
    n = size - len(msg) % size
    return msg + b"\x80" + b"\x00" * (n - 1)


def pad_if_needed(msg, size):
    return msg if len(msg) % size == 0 else pad_always(msg, size)


def unpad(msg):
    stripped = msg.rstrip(b"\x00")
    return stripped[:-1] if stripped.endswith(b"\x80") else msg


message = input("Enter the message: ").encode()
size = int(input("Enter the block size in bytes: "))
print("Message length:", len(message), "bytes   Block size:", size, "bytes")
padded = pad_always(message, size)
print("1. Always pad  :", padded.hex(), "(%d blocks)" % (len(padded) // size))
print("   After removing padding:", unpad(padded))
full = message if len(message) % size == 0 else b"\x00" * size
print("2. A message that already fills whole blocks (%d bytes):" % len(full))
print("   Pad only if needed -> %d blocks, always pad -> %d blocks"
      % (len(pad_if_needed(full, size)) // size,
         len(pad_always(full, size)) // size))
tricky = pad_always(message, size)
print("3. Message whose last bytes look like padding:", tricky.hex())
sent = pad_if_needed(tricky, size)
print("   Pad only if needed : sent unchanged, receiver recovers", unpad(sent))
print("                        original recovered correctly:",
      unpad(sent) == tricky)
sent = pad_always(tricky, size)
print("   Always pad         : receiver recovers", unpad(sent).hex())
print("                        original recovered correctly:",
      unpad(sent) == tricky)
print("Motivation: a padding block makes the padding unambiguous, so the")
print("receiver can always remove exactly the padding that was added.")
