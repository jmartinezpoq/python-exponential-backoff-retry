import random
import time


def retry_with_backoff(retries=5, backoff_in_seconds=1):
    retry_counter = 0
    counter = 0
    while True:
        try:
            counter += count_numbers()
            print(counter)
        except Exception:
            if retry_counter == retries:
                print("Time is up!")
                raise
            else:
                sleep = backoff_in_seconds * 2 ** retry_counter
                print("  Sleep :", str(sleep) + "s")
                time.sleep(sleep)
                retry_counter += 1


def count_numbers():
    action = random.choices([True, False], [1, 2])[0]
    if action:
        return 1
    else:
        raise Exception


if __name__ == "__main__":
    retry_with_backoff()
