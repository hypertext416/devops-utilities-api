#create a function that can be reused and it shows the system info
import psutil

def get_system_info(): #now this function has been created which we can reuse in another code entirely
    cpu = psutil.cpu_percent(interval=1)
    memory= psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    
    system_info={
        "cpu":cpu,
        "memory":memory,
        "disk":disk    
        }
    return system_info


