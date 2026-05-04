import psutil
import platform
from datetime import datetime

class SystemControl:
    """Handles system monitoring and control"""
    
    @staticmethod
    def get_cpu_usage():
        """Get current CPU usage percentage"""
        usage = psutil.cpu_percent(interval=1)
        return f"CPU usage is {usage}%"
    
    @staticmethod
    def get_memory_usage():
        """Get current memory usage"""
        memory = psutil.virtual_memory()
        return f"Memory usage is {memory.percent}%. {memory.available // (1024**3)} GB available."
    
    @staticmethod
    def get_disk_usage():
        """Get disk usage for all partitions"""
        disk_info = []
        for partition in psutil.disk_partitions():
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append(
                f"{partition.device}: {usage.percent}% used ({usage.used // (1024**3)} GB used)"
            )
        return "\n".join(disk_info) if disk_info else "Could not retrieve disk info"
    
    @staticmethod
    def get_battery_status():
        """Get battery status (if available)"""
        try:
            battery = psutil.sensors_battery()
            if battery:
                return f"Battery level: {battery.percent}%. Plugged in: {battery.power_plugged}"
            return "Battery information not available"
        except:
            return "Battery information not available"
    
    @staticmethod
    def get_system_info():
        """Get comprehensive system information"""
        info = {
            'OS': platform.system() + " " + platform.release(),
            'Processor': platform.processor(),
            'Architecture': platform.architecture()[0],
            'Hostname': platform.node(),
            'Python Version': platform.python_version(),
            'CPU Cores': psutil.cpu_count(),
            'Total Memory': f"{psutil.virtual_memory().total // (1024**3)} GB",
            'Current Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return info
    
    @staticmethod
    def format_system_info(info_dict):
        """Format system info dictionary into readable string"""
        return "\n".join([f"{k}: {v}" for k, v in info_dict.items()])
    
    @staticmethod
    def open_application(app_name):
        """Open an application (platform specific)"""
        import subprocess
        import os
        
        try:
            if platform.system() == 'Windows':
                os.startfile(app_name)
            elif platform.system() == 'Darwin':  # macOS
                subprocess.run(['open', '-a', app_name])
            elif platform.system() == 'Linux':
                subprocess.Popen([app_name])
            return f"Opening {app_name}"
        except Exception as e:
            return f"Could not open {app_name}: {e}"
