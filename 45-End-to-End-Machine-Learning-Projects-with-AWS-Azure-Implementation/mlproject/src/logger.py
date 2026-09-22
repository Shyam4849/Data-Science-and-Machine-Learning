import logging
import os
from datetime import datetime

# 1. Timestamp aur clean file name configure karein
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. 'src/logs' ke andar timestamp folder ka path set karein
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
logs_path = os.path.join(SRC_DIR, "logs", LOG_FILE.replace(".log", ""))

# CORRECTION: Sirf folder banayein, file name ke saath nahi
os.makedirs(logs_path, exist_ok=True)

# 3. Final single log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
