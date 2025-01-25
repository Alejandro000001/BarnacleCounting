def move_disk(n, from_peg, to_peg):
    print(f"Move disk {n} from peg {from_peg} to peg {to_peg}")

def hanoi(n, start=0):
    if n > 0:
        long(n - 1, start)
        # Moving from start to (start + 1) % 3
        move_disk(n, start, (start + 1) % 3)
        long(n - 1, start)

def long(n, start):
    if n > 0:
        long(n - 1, start)
        # Moving from start to (start + 1) % 3
        move_disk(n, start, (start + 1) % 3)
        long(n - 1, start)
        # Moving from (start + 1) % 3 to (start + 2) % 3
        move_disk(n, (start + 1) % 3, (start + 2) % 3)
        long(n - 1, start)

# Start the process to move disks from peg 0 to peg 1, with 3 disks initially.
hanoi(3)