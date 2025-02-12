import time

# # Without flush
# print("Start 1")
# time.sleep(2)
# print("End", end=". ",flush=True)
# time.sleep(3)
# print("After 3sec delay.")
# # With flush
# # print("Start 2", end="...", flush=True)
# # time.sleep(2)
# # print("End")


for i in range(0, 10000):
    print(i, "Hello", sep=' ', end='. ')
    time.sleep(1)