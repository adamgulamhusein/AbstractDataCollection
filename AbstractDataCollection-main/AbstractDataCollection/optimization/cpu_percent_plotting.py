import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from psutil import cpu_percent, swap_memory, virtual_memory
import time

def main():
    frame_len = 20
    y = []

    def animate(i):
        y.append(cpu_percent())

        if len(y) <= frame_len:
            plt.cla()
            plt.plot(y, 'r', label = 'Real-Time CPU Uses')
            plt.title("Real-Time CPU Usage")
        
        plt.tight_layout()

        plt.xlabel('Time (s)')
        plt.ylabel('CPU Uses (%)')
        plt.legend(loc = 'upper right')

    ani = FuncAnimation(plt.gcf(), animate, interval=1000)
    plt.show()

def data_gathering():
    y_list = []
    while True:

       y = cpu_percent()
       y_list.append(y)
       time.sleep(0.3)
       
       if len(y_list) >= 45:
            with open('Algo_CPU_data_device.txt', 'w') as f:
                for point in y_list:
                    f.write(f"{point}\n")
            break

def swap_memory_data_gathering():
    y_list = []
    while True:

       y = virtual_memory().percent
       y_list.append(y)
       time.sleep(0.3)
       
       if len(y_list) >= 10:
            with open('LDA_VM_data_device.txt', 'w') as f:
                for point in y_list:
                    f.write(f"{point}\n")
            break
