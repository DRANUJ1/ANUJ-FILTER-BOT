# 1. Base Image
FROM python:3.11-slim

# 2. Working Directory (yahan saari files rahengi)
WORKDIR /app

# 3. System dependencies install karein (agar zaroori ho)
# apt update aur git install ko ek saath karna behtar hai
RUN apt-get update && apt-get install -y --no-install-recommends git

# 4. Python dependencies install karein
# Pehle sirf requirements file copy karein
COPY requirements.txt .
# Phir packages install karein
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -r requirements.txt

# 5. Apna saara code (bot.py, start.sh, etc.) copy karein
# Yeh command aapke project ki sabhi files ko /app/ folder mein daal dega
COPY . .

# 6. start.sh ko execute karne ki permission dein
RUN chmod +x /app/start.sh

# 7. Container shuru hone par start.sh ko chalayein
CMD ["/bin/bash", "/app/start.sh"]

