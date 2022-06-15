"""
Создать тест в отдельном файле и проверить несколько телефонных номеров.
"""

import re
from classwork_01 import is_mobile_phone
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    for item in ("+375 (29) 299-29-29", "+375 (29) 605-00-33"):
        assert is_mobile_phone(item) is not None

    for item in ("+375 (29) 2992929", "+375296050033"):
        assert is_mobile_phone(item) is None

    logger.debug("All test are OK")