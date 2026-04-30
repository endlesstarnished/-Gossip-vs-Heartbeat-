# bandwidth_calculator.py

def calculate_gossip_bandwidth(nodes, fanout, interval_sec, packet_bytes=100):
    """
    Расчет пропускной способности для Gossip протокола
    """
    messages_per_second = (nodes * fanout) / interval_sec
    bandwidth_bytes_per_sec = messages_per_second * packet_bytes
    bandwidth_mbps = (bandwidth_bytes_per_sec * 8) / 1_000_000
    
    return {
        'messages_per_sec': messages_per_second,
        'bandwidth_mbps': bandwidth_mbps
    }

def calculate_heartbeat_bandwidth(nodes, interval_sec, packet_bytes=100):
    """
    Расчет пропускной способности для Heartbeat протокола
    """
    messages_per_second = nodes / interval_sec
    bandwidth_bytes_per_sec = messages_per_second * packet_bytes
    bandwidth_mbps = (bandwidth_bytes_per_sec * 8) / 1_000_000
    
    return {
        'messages_per_sec': messages_per_second,
        'bandwidth_mbps': bandwidth_mbps
    }

# Расчет для задания (50 узлов)
print("=== Результаты для 50 узлов ===")
gossip = calculate_gossip_bandwidth(50, 3, 0.2)
print(f"Gossip: {gossip['messages_per_sec']:.0f} сообщений/с, {gossip['bandwidth_mbps']:.2f} Мбит/с")

heartbeat = calculate_heartbeat_bandwidth(50, 0.2)
print(f"Heartbeat: {heartbeat['messages_per_sec']:.0f} сообщений/с, {heartbeat['bandwidth_mbps']:.2f} Мбит/с")

print("\n=== Для 100 узлов ===")
gossip_100 = calculate_gossip_bandwidth(100, 3, 0.2)
print(f"Gossip: {gossip_100['messages_per_sec']:.0f} сообщений/с, {gossip_100['bandwidth_mbps']:.2f} Мбит/с")

heartbeat_100 = calculate_heartbeat_bandwidth(100, 0.2)
print(f"Heartbeat: {heartbeat_100['messages_per_sec']:.0f} сообщений/с, {heartbeat_100['bandwidth_mbps']:.2f} Мбит/с")