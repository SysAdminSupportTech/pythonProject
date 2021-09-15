import wmi
conn = wmi.WMI()
method = wmi.WMI().Win32_Process.methods.keys()
print(method)

prop = wmi.WMI().Win32_Process.properties.keys()
print("properties found below...............")

print(prop)

#https://adamtheautomator.com/powershell-vs-python/