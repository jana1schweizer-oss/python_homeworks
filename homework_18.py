def analyze_heartbeat_log():
    key = "Key TSTFEED0300|7E3E|0400"
    filtered_lines = []

    # Читаємо файл построково
    with open("hblog.txt", "r") as file:
        for line in file:
            if key in line:
                filtered_lines.append(line)

    # Тут далі будемо аналізувати час
    # Поки залишаємо порожньо
    print(f"Відібрано {len(filtered_lines)} рядків з ключем.")
from datetime import datetime

def analyze_heartbeat_log():
    key = "Key TSTFEED0300|7E3E|0400"
    filtered_lines = []

    # Читаємо файл построково
    with open("hblog.txt", "r") as file:
        for line in file:
            if key in line:
                filtered_lines.append(line)

    print(f"Відібрано {len(filtered_lines)} рядків з ключем.")

    # Витягуємо часи
    timestamps = []
    for line in filtered_lines:
        pos = line.find("Timestamp ")
        if pos != -1:
            time_str = line[pos + 10 : pos + 18]   # беремо 8 символів після "Timestamp "
            time_obj = datetime.strptime(time_str, "%H:%M:%S")
            timestamps.append(time_obj)

    print("Знайдені часи:")
    for t in timestamps:
        print(t)
    # Аналіз heartbeat
    with open("hb_test.log", "w") as out:
        for i in range(len(timestamps) - 1):
            current = timestamps[i]
            next_time = timestamps[i + 1]

            diff = (current - next_time).total_seconds()
            diff = abs(diff)  # на випадок, якщо порядок у логах інший

            if 31 < diff < 33:
                out.write(f"WARNING: heartbeat {diff} sec at {current.time()}\n")
            elif diff >= 33:
                out.write(f"ERROR: heartbeat {diff} sec at {current.time()}\n")
if __name__ == "__main__":
    analyze_heartbeat_log()
