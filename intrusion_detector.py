import random
from collections import defaultdict, deque
from datetime import datetime

class IntrusionDetector:
    def __init__(self, threshold=5, window=60):
        self.threshold = threshold
        self.window = window
        self.attempts = defaultdict(deque)
        self.blocked = set()
        
    def analyze(self, ip, success=False):
        now = datetime.now().timestamp()
        if ip in self.blocked:
            return "BLOCKED"
        history = self.attempts[ip]
        while history and now - history[0] > self.window:
            history.popleft()
        if success:
            history.clear()
            return "AUTHENTICATED"
        history.append(now)
        if len(history) >= self.threshold:
            self.blocked.add(ip)
            return "INTRUSION DETECTED"
        return "MONITORING"
    
    def report(self):
        print("\n--- SECURITY REPORT ---")
        print("Blocked IPs:", len(self.blocked))
        for ip in sorted(self.blocked):
            print(f"[ALERT] {ip}")
            
if __name__ == "__main__":
    firewall = IntrusionDetector()
    ips = ["192.168.1.10", "10.0.0.5", "172.16.0.8"]
    for _ in range(30):
        ip = random.choice(ips)