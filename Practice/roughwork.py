import psutil as psu
io_counter = psu.disk_usage("/")
print(io_counter)