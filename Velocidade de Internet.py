import speedtest

st = speedtest.Speedtest()

down_speed = st.download()
up_speed = st.upload()
ping = st.results.ping

# convesão dos dados obtidos para Mbps

down_speed_mbps = down_speed / 1_000_000
up_speed_mbps = up_speed / 1_000_000

# Exibindo os resultados

print(f"Velocidade de Download: {down_speed_mbps:.2f} Mbps")
print(f"Velocidade de Upload: {up_speed_mbps:.2f} Mbps")
print(f"Ping: {ping:.2f} ms")