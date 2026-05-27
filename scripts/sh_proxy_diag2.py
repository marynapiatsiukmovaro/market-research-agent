#!/usr/bin/env python3
# Decisive proxy diagnostic via curl + raw TCP (clearer errors than Playwright).
# Pinpoints WHERE it fails: VPS direct internet? TCP to proxy host:port? proxy CONNECT/auth? routing?
import socket, subprocess
creds = {}
for line in open('/opt/market-research-agent/cookies/proxy.creds'):
    if '=' in line:
        k, v = line.strip().split('=', 1); creds[k] = v
H, P = creds['PROXY_HOST'], creds['PROXY_PORT']
U, PW = creds['PROXY_USER'], creds['PROXY_PASS']
mask = lambda s: s.replace(PW, '****').replace(U, 'USER')

def run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=40)
        return 'exit=%d\nOUT:%s\nERR:%s' % (r.returncode, mask(r.stdout[:400]), mask(r.stderr[:600]))
    except subprocess.TimeoutExpired:
        return 'exit=TIMEOUT(40s)'

print('PROXY target: %s:%s  user=%s  pass_len=%d' % (H, P, U[:14] + ('...' if len(U) > 14 else ''), len(PW)))
print()
print('=== [1] VPS DIRECT internet (no proxy) -> ipify ===')
print(run(['curl', '-sS', '-m', '15', 'https://api.ipify.org?format=json']))
print()
print('=== [2] Raw TCP connect to proxy %s:%s ===' % (H, P))
try:
    s = socket.create_connection((H, int(P)), timeout=10); s.close(); print('TCP_OPEN (handshake ok)')
except Exception as e:
    print('TCP_FAIL', type(e).__name__, str(e)[:80])
print()
print('=== [3] curl THROUGH proxy -> ipify (verbose, pass masked) ===')
print(run(['curl', '-sS', '-v', '-m', '25', '-x', 'http://%s:%s@%s:%s' % (U, PW, H, P), 'https://api.ipify.org?format=json']))
print()
print('=== [4] curl THROUGH proxy -> Shopify products.json ===')
print(run(['curl', '-sS', '-m', '25', '-x', 'http://%s:%s@%s:%s' % (U, PW, H, P), 'https://uahpet.com/products.json?limit=2']))
print('=== DIAG2 DONE ===')
