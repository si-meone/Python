import os
def freespace(p):
    """
    Returns the number of free bytes on the drive that ``p`` is on
    """
    s = os.statvfs(p)
    return (s.f_bsize * s.f_bavail) /1024

def main():
    print(freespace('/'))

if __name__ == "__main__":
    main()
